class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def __init__(self):
        super().__init__()
    
    def add_movie(self, comedy):
        super().add_movie(comedy)
        return f"Comedy: {self.movies}"
    

class Drama(Movies):
    def __init__(self):
        super().__init__()
        
    def add_movie(self, drama):
        super().add_movie(drama)
        return f"Drama: {self.movies}"
    
    

comedy = Comedy()
comedy.add_movie("The Hangover")
print(comedy.add_movie("Superbad"))

drama = Drama()
drama.add_movie("The Shawshank Redemption")
drama.add_movie("The Godfather")
print(drama.add_movie("The Dark Knight"))