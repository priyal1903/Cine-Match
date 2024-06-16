class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

class MovieRecommendationSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, rating):
        new_movie = Movie(title, genre, rating)
        self.movies.append(new_movie)
        print(f"Movie '{title}' added successfully.")

    def search_movie(self, title=None, genre=None):
        results = []
        for movie in self.movies:
            if (title and title.lower() in movie.title.lower()) or (genre and genre.lower() in movie.genre.lower()):
                results.append(movie)
        return results

    def delete_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                self.movies.remove(movie)
                print(f"Movie '{title}' deleted successfully.")
                return
        print(f"Movie '{title}' not found.")

    def recommend_top_movies(self, n):
        sorted_movies = sorted(self.movies, key=lambda x: x.rating, reverse=True)
        return sorted_movies[:n]

    def display_movies(self, movies):
        for movie in movies:
            print(f"Title: {movie.title}, Genre: {movie.genre}, Rating: {movie.rating}")

# Usage
if __name__ == "__main__":
    system = MovieRecommendationSystem()
    
    # Add movies
    system.add_movie("Inception", "Sci-Fi", 9.0)
    system.add_movie("The Matrix", "Sci-Fi", 8.7)
    system.add_movie("Interstellar", "Sci-Fi", 8.6)
    system.add_movie("The Godfather", "Crime", 9.2)
    system.add_movie("The Dark Knight", "Action", 9.0)
    
    # Search movies
    print("\nSearch Results:")
    search_results = system.search_movie(title="The")
    system.display_movies(search_results)
    
    # Recommend top N movies
    print("\nTop 3 Movies:")
    top_movies = system.recommend_top_movies(3)
    system.display_movies(top_movies)
    
    # Delete a movie
    system.delete_movie("Inception")
    
    # Display all movies
    print("\nAll Movies:")
    system.display_movies(system.movies)
