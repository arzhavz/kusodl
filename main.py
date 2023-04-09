import re
from prompt_toolkit import HTML
from prompt_toolkit.shortcuts import (
	yes_no_dialog,
	message_dialog,
	input_dialog,
	radiolist_dialog
)

from config.metadata import Messages, Styles, Configs
from lib.scraper import Kusonime
from lib.download import GDDownload
from lib.utils import KeyListCreator, Validation, Browser


class KusoDL:
	def __init__(self):
		self.theme = Styles.default
		self.platform = "l"
		
	def _display_goodbye_message(self, message="Sayonara!"):
			message_dialog(
			title=Messages.title,
			text=HTML(f"{message}"),
			style=self.theme
		).run()
	
	def _download_episode(self, data, hosts):
		selected_host = radiolist_dialog(
			title=Messages.title,
			text=Messages.host_text,
			values=hosts,
			style=self.theme
		).run()

		if selected_host:
			try:
				host_data = data[selected_host]
				result = GDDownload(host_data)
				if result == True:
					self._display_goodbye_message(Messages.success_text)
				elif result == False:
						self._display_goodbye_message(Messages.canceled)
			except Exception as e:
				self._display_goodbye_message(
					Messages.cant_download.format(data[selected_host])
				)
				print(f"\033[32mOpening \033[0m\033[35m{data[selected_host]}\033[0m \033[32min your local browser.\033[0m")
				Browser(data[selected_host]).open(self.platform)
		else:
			self._display_goodbye_message(Messages.canceled)


	def _get_episode_resolution(self, data, resolutions):
		selected_resolution = radiolist_dialog(
			title=Messages.title,
			text=Messages.res_text,
			values=resolutions,
			style=self.theme
		).run()

		if selected_resolution:
			try:
				resolution_data = data.get_url(selected_resolution)
				hosts = KeyListCreator(resolution_data).create_sub_key_list()
				self._download_episode(resolution_data, hosts)
			except Exception as e:
				self._display_goodbye_message(Messages.error.format(str(e)))
		else:
			self._display_goodbye_message(Messages.canceled)


	def _start_downloading(self):
		try:
			url = input_dialog(
				title=Messages.title,
				text=Messages.input_text,
				style=self.theme
			).run()

			if Validation(Configs.kuso_regex).URL(url):
				try:
					kusonime_data = Kusonime(url.strip())
					resolutions = KeyListCreator(kusonime_data.all_res).create_key_list()
					self._get_episode_resolution(kusonime_data, resolutions)
				except Exception as e:
					self._display_goodbye_message(Messages.error.format(str(e)))
			else:
				self._display_goodbye_message(Messages.invalid_url)
				self._start_downloading()
		except Exception as e:
			self._display_goodbye_message(Messages.canceled)


	def _select_theme(self):
		theme = radiolist_dialog(
			title=Messages.title,
			text=Messages.theme_text,
			values=Configs.themes,
			style=self.theme
		).run()

		if theme:
			self.theme = theme
			Styles.default = self.theme
			self._start_downloading()
		else:
			self._run_program()
	

	def run_program(self):
		result = radiolist_dialog(
			title=Messages.title,
			text=Messages.intro_text,
			values=[("l", "Linux"), ("w", "Windows")],
			style=self.theme
		).run()

		if result:
			self.platform = result
			self._select_theme()
		else:
			self._display_goodbye_message(Messages.canceled)


if __name__ == "__main__":
	KusoDL().run_program()
