#ex1
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
# movie1 = input("Enter a movie name: ")

# def is_high_score(movie):
#     return movie["name"] == movie1 and movie["imdb"] > 5.5

# for movie in movies:
#     if movie["name"] == movie1:
#         result = is_high_score(movie)
#         print(result)

#ex2
# list=[]
# def is_high_score(movie):
#     return  movie["imdb"] > 5.5
# for movie in movies:
#     result = is_high_score(movie)
#     if(result==True):
#         list.append(movie)
# print(list)

#ex3
# def get_movies_by_category(category, movie_list):
#     return [movie for movie in movie_list if movie["category"] == category]
# category_name = input("Enter a category name: ")
# movies_in_category = get_movies_by_category(category_name, movies)
# if movies_in_category:
#     print(f"Movies in the category '{category_name}':")
#     for movie in movies_in_category:
#         print(f"- {movie['name']} (IMDB: {movie['imdb']})")
# else:
#     print(f"No movies found in the category '{category_name}'.")

# ex4
# sum=0
# for i in movies:
#     sum+=i['imdb']
# print(sum/len(movies))

# ex5
# def get_movies_by_category(category, movie_list):
#     return [movie for movie in movie_list if movie["category"] == category]
# category_name = input("Enter a category name: ")
# movies_in_category = get_movies_by_category(category_name, movies)
# sum=0
# for i in movies_in_category:
#     sum+=i['imdb']
# print(sum/len(movies_in_category))