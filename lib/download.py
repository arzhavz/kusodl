import os, requests
from pathlib import Path
from urllib.parse import unquote
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from lib.scraper import Kusonime


def Download(url: str) -> None:
	response = requests.get(url)
	html = bs(response.text, "html.parser")
	form_url = unquote(html.find("form").get("action"))
	token = html.find("input").get("value")
	response = requests.post(form_url, data={"value": token}, stream=True)
	file_size = int(response.headers.get('Content-Length', 0))
	file_name = html.find("span", {"class": "uc-name-size"}).find("a").text
	
	os.chdir(Path(Path(__file__).parent.parent, "tmp"))
	os.system("clear")
	
	print(f"Mengunduh {file_name}\n")
	
	with open(file_name, 'wb') as file:
		with tqdm(total=file_size, desc=f'Processing file', leave=True, file=None, mininterval=0.1, miniters=1, dynamic_ncols=True,
				  smoothing=True, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}~{remaining}, {rate_fmt}]',
				  initial=0, position=None, ascii=None, unit='B', unit_scale=True, unit_divisor=1024,
				  ncols=100, colour="magenta") as progress_bar:
			for data in response.iter_content(chunk_size=1024):
				file.write(data)
				progress_bar.update(len(data))
		
		with open(file_name, 'rb') as file:
			with tqdm(total=file_size, desc=f'Saving file', leave=True, file=None, mininterval=0.1, miniters=1, dynamic_ncols=True,
					  smoothing=True, bar_format='{l_bar}{bar}| [{elapsed}~{remaining}]',
					  initial=0, position=None, ascii=None, unit='B', unit_scale=True, unit_divisor=1024,
					  ncols=200, colour="green") as progress_bar:
				while True:
					data = file.read(1024)
					if not data:
						break
					progress_bar.update(len(data))

	print(f"\nSuccess download {file_name}!")