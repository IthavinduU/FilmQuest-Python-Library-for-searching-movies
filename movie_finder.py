# movie_finder.py
import csv
import random

# Constants
DATA_FILE = "movies.csv"
OUTPUT_FILE = "filtered_movies.csv"
CATEGORIES = ["Action", "Crime", "Romance", "Drama", "Comedy"]


class Movie:
    def __init__(self, title, year, rating, box_office, category):
        self.title = title
        self.year = year
        self.rating = rating
        self.box_office = box_office
        self.category = category


class MovieFinder:
    CATEGORIES = CATEGORIES

    def __init__(self, data_file):
        self.data_file = data_file
        self.movies = []

    def load_data(self):
        """Load data from CSV file into the movies list."""
        with open(self.data_file, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                title, year, rating, box_office, category = row
                self.movies.append(
                    Movie(title, int(year), float(rating), float(box_office), category)
                )

    def filter_movies(self, year_range=None, category=None, min_rating=None):
        """Filter movies based on year range, category, and minimum rating."""
        filtered = self.movies

        if year_range:
            start_year, end_year = year_range
            filtered = [
                movie for movie in filtered if start_year <= movie.year <= end_year
            ]

        if category:
            filtered = [movie for movie in filtered if movie.category == category]

        if min_rating:
            filtered = [movie for movie in filtered if movie.rating >= min_rating]

        return filtered

    def sort_movies_by_rating(self, movies):
        """Sort movies by rating in descending order."""
        return sorted(movies, key=lambda movie: movie.rating, reverse=True)

    def save_filtered_movies(self, filtered_movies):
        """Save filtered movies to an output CSV file."""
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Year", "Rating", "Box Office", "Category"])
            for movie in filtered_movies:
                writer.writerow(
                    [
                        movie.title,
                        movie.year,
                        movie.rating,
                        movie.box_office,
                        movie.category,
                    ]
                )
