import re
from prompt_toolkit.shortcuts import (
	yes_no_dialog,
	message_dialog,
	input_dialog,
	radiolist_dialog
)

from config.metadata import Styles
from lib.scraper import Kusonime
from lib.download import Download

def create_key_list2(data):
	keys = data.keys()
	result = []
	for key in keys:
		if isinstance(data[key], dict):
			for sub_key in data[key]:
				alias = sub_key.upper()
				result.append((sub_key, alias))
		else:
			result.append((key, key.upper()))
	return result

def create_key_list(data):
	result = []
	for key in data:
		result.append((key, key.upper()))
	return result

def isURL(url):
	pattern = re.compile(
		r'^https?://' 
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
		r'kusonime|'  
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
		r'(?::\d+)?'  
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)  
	return bool(pattern.match(url))

def cancel(kata: str = "Sayonara!"):
	message_dialog(
		title="KusoDL V.0.1",
		text=f"{kata}\n\nTerimakasih sudah menggunakan!\nSilahkan kunjungi profile author di URL dibawah\nhttps://arzxh.netlify.app",
		style=Styles.Retro
	).run()

def ddl(data, tup: tuple):
	result = radiolist_dialog(
	title="KusoDL V.0.1",
	text="Pilih file hosting dari file yang ingin diunduh.\nDisarankan menggunakan Google Drive.",
	values=tup,
	style=Styles.Retro
	).run()
	if result:
		try:
			data = data[result]
			Download(data)
			cancel("Success mengunduh file!\nSilahkan periksa folder /tmp untuk mengekstrak file.")
		except Exception as e:
			cancel(f"Maaf, terjadi kesalahan!\nSebagai alternatif lain, silahkan buka url berikut\n\n{data[result]}")
	else:
		cancel("Operasi dibatalkan oleh user!")
	
def get_res(data, tup: tuple):
	result = radiolist_dialog(
	title="KusoDL V.0.1",
	text="Pilih resolusi video yang ingin kamu unduh.",
	values=tup,
	style=Styles.Retro
	).run()
	if result:
		try:
			data = data.get_url(result)
			hosts = create_key_list2(data)
			ddl(data, hosts)
		except Exception as e:
			cancel("Maaf, terjadi kesalahan.")
	else:
		cancel("Operasi dibatalkan oleh user!")
	
def start():
	url = input_dialog(
		title="KusoDL V.0.1",
		text="Masukkan URL anime dari website Kusonime\nhttps://kusonime.com",
		style=Styles.Retro
	).run()
	if isURL(url):
		try:
			data = Kusonime(url.strip())
			keys = create_key_list(data.all_res)
			get_res(data, keys)
		except Exception as e:
			cancel("Maaf, Anime tidak bisa diunduh!")
	else:
		cancel("Maaf, URL yang kamu masukkan tidak valid!")

def main():
	result = yes_no_dialog(
		title="KusoDL V.0.1",
		text="Selamat datang di Kusonime Downloader!\nSilahkan pilih 'Yes' untuk melanjutkan.",
		style=Styles.Retro
	).run()
	if result:
		start()
	else:
		cancel("Operasi dibatalkan oleh user!")

if __name__ == "__main__":
	main()
