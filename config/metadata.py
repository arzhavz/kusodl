from prompt_toolkit.styles import Style


class Styles:
	Retro = Style.from_dict(
		{
			# Warna latar belakang utama
			"window": "bg:#1d1f21 #ffffff",
			# Dialog dan kotak pesan
			"dialog": "bg:#1d1f21",
			"dialog.border": "bg:#c5c8c6",
			"dialog.body": "bg:#1d1f21 #ffffff",
			"dialog.title": "bg:#1d1f21 #c5c8c6",
			"dialog.shadow": "bg:#1d1f21",
			# Tombol
			"button": "bg:#373b41 #ffffff",
			"button.border": "bg:#c5c8c6",
			"button.focus": "bg:#1d1f21 #c5c8c6",
			"button.selected": "bg:#373b41 #ffffff",
			"button.selected.border": "bg:#c5c8c6",
			"button.disabled": "bg:#373b41 #999999",
			# Label dan bingkai
			"frame.label": "bg:#1d1f21 #c5c8c6",
			"frame.border": "bg:#1d1f21 #c5c8c6",
			# Menu dan bilah menu
			"menu-bar": "bg:#1d1f21 #c5c8c6",
			"menu": "bg:#1d1f21 #ffffff",
			"menu.border": "bg:#1d1f21 #c5c8c6",
			"menu.shadow": "bg:#1d1f21",
			"selected-menu-item": "bg:#373b41 #ffffff",
			"separator": "bg:#c5c8c6",
			# Pilihan kotak centang dan lingkaran radio
			"checkbox": "bg:#1d1f21 #c5c8c6",
			"checkbox.border": "bg:#c5c8c6",
			"checkbox.focus": "bg:#1d1f21 #c5c8c6",
			"checkbox.selected": "bg:#373b41 #c5c8c6",
			"checkbox.selected.border": "bg:#c5c8c6",
			"checkbox.disabled": "bg:#1d1f21 #999999",
			"radio": "bg:#1d1f21 #c5c8c6",
			"radio.border": "bg:#c5c8c6",
			"radio.focus": "bg:#1d1f21 #c5c8c6",
			"radio.selected": "bg:#373b41 #c5c8c6",
			"radio.selected.border": "bg:#c5c8c6",
			"radio.disabled": "bg:#1d1f21 #999999",
			# Progress bar
			"progressbar.background": "bg:#373b41",
			"progressbar.border": "bg:#1d1f21 #c5c8c6",
			"progressbar.bar": "bg:#b8bb26",
			"progressbar.pulse": "bg:#b8bb26",
			"progressbar.percentage": "bg:#b8bb26",
			"progressbar.label": "bg:#1d1f21 #c5c8c6",
			# Input
			"text-area": "bg:#1d1f21 #c5c8c6",
			"text-area.border": "bg:#c5c8c6",
			"text-area.focus": "bg:#1d1f21 #c5c8c6",
			"text-area cursor": "fg:#c5c8c6 bg:#c5c8c6",
			"text-area.selection": "bg:#373b41 #c5c8c6",
			"text-area.line": "bg:#1d1f21",
			"text-area prompt": "fg:#c5c8c6",
			"text-area.status-bar": "bg:#1d1f21 #c5c8c6",
			"text-area.status-bar.current-position": "bg:#373b41 #c5c8c6",
			"text-area.status-bar.mode": "bg:#1d1f21 #c5c8c6 fg:#c5c8c6",
		}
	)