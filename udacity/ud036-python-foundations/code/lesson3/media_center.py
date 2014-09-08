import media, fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
                             "Jack Black is not a good actor",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

hunger_games = media.Movie("Hunger Games",
                           "Children participate in death match",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=keT5CRhhy84")

movies = [toy_story, avatar, school_of_rock, hunger_games]
fresh_tomatoes.open_movies_page(movies)

print toy_story.ratings
print media.Movie.__doc__