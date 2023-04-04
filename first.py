class Movie:  
    def __init__(self,actor):
        self.actor=actor

movie1 = Movie("George Clooney")
movie2 = movie1

print(id(movie1))
print(id(movie2))