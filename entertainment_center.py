import fresh_tomatoes
import media

wiki_url = "https://upload.wikimedia.org/wikipedia/en/"
youtube_url = "https://www.youtube.com/watch?v="

# List of my 6 favorite movies as instances of the class Movie
unforgiven = media.Movie("Unforgiven",
                         wiki_url+"4/4e/Unforgiven_2.jpg",
                         youtube_url+"XDAXGILEdro")
pans_labyrinth = media.Movie("Pan's Labyrinth",
                             wiki_url+"7/7c/Pan'slabyrinthsndtrk.jpg",
                             youtube_url+"EqYiSlkvRuw")
last_of_the_mohicans = media.Movie("The Last of the Mohicans",
                                   wiki_url+"d/dd/Mohicansposter.jpg",
                                   youtube_url+"dn7UHJLcPp4")
gladiator = media.Movie("Gladiator",
                        wiki_url+"8/8d/Gladiator_ver1.jpg",
                        youtube_url+"AxQajgTyLcM")
train_a_dragon = media.Movie("How To Train Your Dragon",
                             wiki_url+"9/99/How_to_Train_Your_"
                             "Dragon_Poster.jpg",
                             youtube_url+"oKiYuIsPxYk")
braveheart = media.Movie("Braveheart",
                         wiki_url+"5/55/Braveheart_imp.jpg",
                         youtube_url+"j53_WxqPZ7c")

# Place each movie in a list called movies and call function to start webpage
movies = [unforgiven, pans_labyrinth, last_of_the_mohicans, gladiator,
          train_a_dragon, braveheart]
fresh_tomatoes.open_movies_page(movies)


