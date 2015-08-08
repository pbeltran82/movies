# author: Pedro Beltran
# description: A program that creates movies to be added to a web page with
# title, poster image, and youtube movie trailer

import media
import fresh_tomatoes

# Creating six instances of my favorite movies
# Includes title, story line, poster image url, and movie trailer url
san_andreas = media.Movie(
    "San Andreas",
    "A big earthquake hits hard in California, and the after math is devasting.",
    "http://i1.wp.com/2.bp.blogspot.com/-1dnTvqfCj1Y/VMiBivwRQKI/AAAAAAAAAD0/fUsh7rfAmTE/s1600/San%2Bandreas%2BPoster.jpg",
    "https://youtu.be/yftHosO0eUo")

pain_gain = media.Movie(
    "Pain and Gain",
    "A group of muscle heads do everything to achieve the American dream at all costs.",
    "http://thesecondtake.com/wp-content/uploads/2013/04/Pain-and-Gain-New-Poster-4-4.jpg",
    "https://youtu.be/SEQ8jyvmYtw")

sum_of_all_fears = media.Movie(
    "Sum of all Fears",
    "CIA analyst must prevent a terrorist bomb attack that would cause a nuclear war between USA and Russia.",
    "http://ilarge.lisimg.com/image/4757/968full-the-sum-of-all-fears-poster.jpg",
    "https://youtu.be/p4Y-0Pun2Eg")

flight = media.Movie(
    "Flight",
    "A pilot under the influence manages to land a faulty commercial airline plane but comes under a lot of investigation.",
    "http://ia.media-imdb.com/images/M/MV5BMTUxMjI1OTMxNl5BMl5BanBnXkFtZTcwNjc3NTY1OA@@._V1_SX640_SY720_.jpg",
    "https://youtu.be/Aqn2L6kQQt8")

borat = media.Movie(
    "Borat",
    "A Kazakhstan journalist comes to the USA to learn American customs and film a video to take back to his country.",
    "http://ia.media-imdb.com/images/M/MV5BMTk0MTQ3NDQ4Ml5BMl5BanBnXkFtZTcwOTQ3OTQzMw@@._V1_SX640_SY720_.jpg",
    "https://youtu.be/4_I3tIjztj8")

american_sniper = media.Movie(
    "American Sniper",
    "Navy SEAL sniper Chris Kyle's pinpoint accuracy saves countless lives on the battlefield.",
    "http://www.joblo.com/newsimages1/American-Sniper-Poster1.jpg",
    "https://youtu.be/99k3u9ay1gs")

# Creating a movies list with all the movie objects
movies = [san_andreas, pain_gain, sum_of_all_fears, flight, borat, american_sniper]

#Calling open_movies method to add the movies to an html file with CSS
fresh_tomatoes.open_movies_page(movies)
