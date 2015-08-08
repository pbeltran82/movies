# author: Pedro Beltran

import webbrowser

class Movie():
    """
    This class will create movie instances so that we can append them to our
    web page.

    Attributes:
        title: title of the movie
        storyline: a quick story line of the line
        poster_image_url: the url for the poster image of the movie
        trailer_youtube_url: the url of the trailer of the movie on youtube
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Constructor initializes all the instance variable to create movie
        object.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens up the youtube video of the specified movie """
        webbrowser.open(self.trailer_youtube_url)
