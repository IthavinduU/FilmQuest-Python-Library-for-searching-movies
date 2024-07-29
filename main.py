# main.py
from movie_finder import MovieFinder, DATA_FILE

OUTPUT_FILE = 'filtered_movies.csv'  # Define the output file name


def get_user_input():
    year_range = None
    category = None
    min_rating = None

    # Get year range from user
    year_input = input(
        "Enter the year range (e.g., 1990-2000) or leave blank to skip: "
    )
    if year_input:
        start_year, end_year = map(int, year_input.split("-"))
        year_range = (start_year, end_year)

    # Get category from user
    category_input = input(
        f"Enter the category ({', '.join(MovieFinder.CATEGORIES)}) or leave blank to skip: "
    )
    if category_input:
        category = category_input

    # Get minimum rating from user
    min_rating_input = input(
        "Enter the minimum rating (e.g., 7.5) or leave blank to skip: "
    )
    if min_rating_input:
        min_rating = float(min_rating_input)

    return year_range, category, min_rating


def main():
    edson = MovieFinder(DATA_FILE)

    # Load data
    edson.load_data()

    # Get user input for filtering criteria
    year_range, category, min_rating = get_user_input()

    # Filter movies based on user criteria
    filtered_movies = edson.filter_movies(year_range, category, min_rating)

    # Sort filtered movies by rating
    sorted_movies = edson.sort_movies_by_rating(filtered_movies)

    # Save the filtered and sorted movies to an output file
    edson.save_filtered_movies(sorted_movies)

    print(f"Filtered and sorted movies saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
