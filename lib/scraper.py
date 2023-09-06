import requests, re
from bs4 import BeautifulSoup as soup
from urllib.parse import unquote


class Kusonime:
	def __init__(self, url: str = None) -> None:
		self.url = url
		self.info = self.get_info
		self.title = self.get_info["title"]
		self.all_res = self.get_info["available_res"]

	@property
	def get_info(self) -> dict:
		try:
			data = requests.get(self.url)
			html = soup(data.text, "html.parser")
			title = html.find("title").text
			views = (
				html.find("span", {"class": "viewoy"}).text.split("Views")[0].strip()
			)
			info = html.find("div", {"class": "info"})
			japanese = (
				info.find("b", string=re.compile("Japanese"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			genres = (
				info.find("b", string=re.compile("Genre"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			seasons = (
				info.find("b", string=re.compile("Seasons"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			producers = (
				info.find("b", string=re.compile("Producers"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			tipe = (
				info.find("b", string=re.compile("Type"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			status = (
				info.find("b", string=re.compile("Status"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			total_episode = (
				info.find("b", string=re.compile("Total Episode"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			score = (
				info.find("b", string=re.compile("Score"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			duration = (
				info.find("b", string=re.compile("Duration"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			released_on = (
				info.find("b", string=re.compile("Released on"))
				.find_parent()
				.text.split(":")[1]
				.strip()
			)
			ddl = html.find("div", {"class": "smokeddlrh"})
			smokeurl = ddl.find_all("div", {"class": "smokeurlrh"})
			Key1 = {}
			Resolutions = []
			for url in smokeurl:
				Key2 = {}
				reso = url.find("strong").text.strip().lower()
				links = url.find_all("a")
				for link in links:
					key = (
						link.text.strip().lower().replace(" ", "_")
						if " " in link.text.strip().lower()
						else link.text.strip().lower()
					)
					item = unquote(link.get("href"))
					Key2.update({key: item})
				Resolutions.append(reso)
				Key1.update({reso: Key2})
			results = {
				"title": title,
				"info": {
					"japanese": japanese,
					"views": int(views),
					"genres": genres,
					"seasons": seasons,
					"producers": producers,
					"type": tipe,
					"status": status,
					"episodes": total_episode,
					"scores": score,
					"duration": duration,
					"release": released_on,
				},
				"download": Key1,
				"available_res": Resolutions
			}
			return results
		except Exception as e:
			raise e

	def get_url(self, res: str = None, **kwargs) -> dict:
		try:
			urls = self.info["download"]
			if res == None:
				return urls
			if res in urls:
				if "host" in kwargs:
					return urls[res][kwargs.get("host")]
				else:
					return urls[res]
			else:
				return {"message": "Invalid resolution"}
		except Exception as e:
			raise e
