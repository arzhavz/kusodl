import re
from prompt_toolkit import HTML
from prompt_toolkit.shortcuts import (
	yes_no_dialog,
	message_dialog,
	input_dialog,
	radiolist_dialog
)

from config.metadata import Styles, Messages
from lib.scraper import Kusonime
from lib.download import Download


def create_sub_key_list(data):
	sub_keys = []
	for key, value in data.items():
		if isinstance(value, dict):
			sub_keys.extend([(sub_key, sub_key.upper()) for sub_key in value])
		else:
			sub_keys.append((key, key.upper()))
	return sub_keys


def create_key_list(data):
	return [(key, key.upper()) for key in data]


def is_valid_url(url):
	pattern = re.compile(
		r'^https?://'
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
		r'kusonime|'
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
		r'(?::\d+)?'
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	return bool(pattern.match(url))


def display_goodbye_message(message="Sayonara!"):
	message_dialog(
		title=Messages.title,
		text=HTML(f"{message}\n\n{Messages.bye_text}"),
		style=Styles.Retro
	).run()


def download_episode(data, hosts):
	selected_host = radiolist_dialog(
		title=Messages.title,
		text=Messages.host_text,
		values=hosts,
		style=Styles.Retro
	).run()

	if selected_host:
		try:
			host_data = data[selected_host]
			result = Download(host_data)
			if result == True:
				display_goodbye_message("Berhasil mengunduh file!\nFile akan tersimpan di folder tmp")
			elif result == False:
				display_goodbye_message("Operasi dibatalkan oleh User.")
		except Exception as e:
			display_goodbye_message(f"Terjadi kesalahan saat mengunduh file!\n<ansired>{str(e)}</ansired>\nSilahkan copy URL dibawah untuk mengunduhnya secara manual di browser.\n<ansigreen>{data[selected_host]}</ansigreen>")
	else:
		display_goodbye_message("Operasi dibatalkan oleh User.")


def get_episode_resolution(data, resolutions):
	selected_resolution = radiolist_dialog(
		title=Messages.title,
		text=Messages.res_text,
		values=resolutions,
		style=Styles.Retro
	).run()

	if selected_resolution:
		try:
			resolution_data = data.get_url(selected_resolution)
			hosts = create_sub_key_list(resolution_data)
			download_episode(resolution_data, hosts)
		except Exception as e:
			display_goodbye_message("Terjadi kesalahan.\n<ansired>{str(e)}</ansired>")
	else:
		display_goodbye_message("Operasi dibatalkan oleh User.")


def start_downloading():
	url = input_dialog(
		title=Messages.title,
		text=Messages.input_text,
		style=Styles.Retro
	).run()

	if is_valid_url(url):
		try:
			kusonime_data = Kusonime(url.strip())
			resolutions = create_key_list(kusonime_data.all_res)
			get_episode_resolution(kusonime_data, resolutions)
		except Exception as e:
			display_goodbye_message("Terjadi kesalahan saat mengambil informasi dari URL yang diberikan.\n<ansired>{str(e)}</ansired>")
	else:
		display_goodbye_message("Tautan yang kamu berikan tidak valid, coba periksa kembali tautan kamu.")


def run_program():
	result = yes_no_dialog(
		title=Messages.title,
		text=Messages.intro_text,
		style=Styles.Retro
	).run()

	if result:
		start_downloading()
	else:
		display_goodbye_message("Operasi dibatalkan oleh User.")


if __name__ == "__main__":
	run_program()
