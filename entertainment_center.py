import fresh_tomatoes
import media


# List of my 6 favorite movies as instances of the class Movie
unforgiven = media.Movie("Unforgiven",
                         "https://upload.wikimedia.org/wikipedia/en/4/4e/Unforgiven_2.jpg",
                         "https://www.youtube.com/watch?v=XDAXGILEdro")
pans_labyrinth = media.Movie("Pan's Labyrinth",
                             "https://upload.wikimedia.org/wikipedia/en/7/7c/Pan'slabyrinthsndtrk.jpg",
                             "https://www.youtube.com/watch?v=EqYiSlkvRuw")
last_of_the_mohicans = media.Movie("The Last of the Mohicans",
                                   "https://upload.wikimedia.org/wikipedia/en/d/dd/Mohicansposter.jpg",
                                   "https://www.youtube.com/watch?v=dn7UHJLcPp4")
gladiator = media.Movie("Gladiator",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=AxQajgTyLcM")
train_a_dragon = media.Movie("How To Train Your Dragon",
                             "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                             "https://www.youtube.com/watch?v=oKiYuIsPxYk")
braveheart = media.Movie("Braveheart",
                         "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                         "https://www.youtube.com/watch?v=j53_WxqPZ7c")

#Place each movie in a list called movies and call function to start webpage
movies = [unforgiven,pans_labyrinth,last_of_the_mohicans,gladiator,train_a_dragon,braveheart]
fresh_tomatoes.open_movies_page(movies)

