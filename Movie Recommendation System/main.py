from imdb import IMDb
mov=IMDb()

'''Same function just different names, basically the same thing, and just name is updated, rest works the same'''
#from imdb import Cinemagoer  
#movie=Cinemagoer()

#m=movie.search_movie("baby")
#n=movie.get_keyword('thriller drama')

  
# get a movie  
def movie_info(id):
    movie = mov.get_movie(id)  
    
    print('------------------------------------Movie Name----------------------------------------: ')  
    print(movie['title'])  
    try:
        full_cast = movie['cast']  
        print('------------------------------------Movie Cast-----------------------------------------:')  
        for person in full_cast:  
            print(person['name']) 
    except Exception as e:
        print(" ")

    try:    
        print('--------------------------------------Directors----------------------------------------:')  
        for director in movie['directors']:  
            print(director['name'])  
    except Exception as e:
        print(" ")

    try:    
        print('---------------------------------------Genres------------------------------------------:')  
        for genre in movie['genres']:  
            print(genre)  
    except Exception as e:
        print(" ")

k=mov.search_movie('Wednesday')
for i in k[:1]:    
    print(i['title'])
    a=i.movieID
print(a)

movie_info(a)
