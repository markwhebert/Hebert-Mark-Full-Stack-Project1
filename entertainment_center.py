import media
import fresh_tomatoes

"""Defines the Title, Description, Image Link and Trailer Link for respective movies"""
toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life", 
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.khabinh.vn/images/files/avatar-oridginal.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

rush = media.Movie("Rush",
                   "A biography of Formula 1 champion driver Niki Lauda and the 1976 crash that almost claimed his life. Mere weeks after the accident, he got behind the wheel to challenge his rival, James Hunt.",
                   "http://ia.media-imdb.com/images/M/MV5BMTQyMDE0MTY0OV5BMl5BanBnXkFtZTcwMjI2OTI0OQ@@._V1_SX214_AL_.jpg",
                   "https://www.youtube.com/watch?v=aphGbb07xk8")

movies = [toy_story, avatar, rush]

fresh_tomatoes.open_movies_page(movies)
