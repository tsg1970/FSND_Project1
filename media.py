import webbrowser


class Movie():
    """Creates space for each instance of movies."""
    def __init__(self, movie_title, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
