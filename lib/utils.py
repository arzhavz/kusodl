import re
import os 
import time


class KeyListCreator:
	def __init__(self, data):
		self.data = data

	def create_sub_key_list(self):
		sub_keys = []
		for key, value in self.data.items():
			if isinstance(value, dict):
				sub_keys.extend([(sub_key, sub_key.upper()) for sub_key in value])
			else:
				sub_keys.append((key, key.upper()))
		return sub_keys

	def create_key_list(self):
		return [(key, key.upper()) for key in self.data]

	
class Validation:
	def __init__(self, regex):
		self.regex = regex
		
	def URL(self, url):
		pattern = self.regex
		return bool(pattern.match(url))
	

class Browser:
	def __init__(self, url):
		self.url = url
		
	def open(self, platform, delay=3):
		try:
			if platform.lower().strip() == "l":
				time.sleep(delay)
				os.system(f"xdg-open {self.url}")
			elif platform.lower().strip() == "w":
				time.sleep(delay)
				os.system(f"start {self.url}")
			return
		except:
			print("Error: Could not open browser")