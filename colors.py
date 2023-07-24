class Colors:
	dark_grey = (30, 35, 50)
	green = (55, 220, 35)
	red = (240, 30, 30)
	orange = (240, 120, 20)
	yellow = (245, 240, 15)
	purple = (180, 10, 250)
	cyan = (20, 210, 220)
	blue = (20, 80, 230)
	white = (250, 250, 250)
	dark_blue = (20, 70, 125)
	light_blue = (130, 180, 220)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
