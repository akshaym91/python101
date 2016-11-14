import webbrowser

class Video(object):
	"""docstring for Video"""
	def __init__(self, title, duration, poster_image):
		super(Video, self).__init__()
		self.title = title
		self.duration = duration
		self.poster_image = poster_image


# Movie: Blueprint for any movie
class Movie(Video):
	Video.__init__(self, title, duration)
	"""Class which provides the blueprint to make a new movie."""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	# self is the object that is being created
	def __init__(self, movie_storyline,, trailer_youtube):
		self.storyline = movie_storyline
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
	Video.__init__(self, title, duration)
	"""docstring for TvShow"""
	def __init__(self, season, episode, tvstation):
		super(TvShow, self).__init__()
		self.season = season
		self.episode = episode
		self.tvstation = tvstation
		
	def get_local_listing(self):
		pass