import csv
import random

# Constants
OUTPUT_FILE = "movies.csv"
NUM_RECORDS = 10000
TITLES = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]
YEARS = list(range(1980, 2024))
CATEGORIES = ["Action", "Crime", "Romance", "Drama", "Comedy"]
RATINGS = [round(random.uniform(1.0, 10.0), 1) for _ in range(NUM_RECORDS)]
BOX_OFFICE = [
    round(random.uniform(1_000_000, 1_000_000_000), 2) for _ in range(NUM_RECORDS)
]


def generate_movie_data(num_records):
    """Generate a list of movie data records."""
    data = []
    for _ in range(num_records):
        title = random.choice(TITLES)
        year = random.choice(YEARS)
        rating = random.choice(RATINGS)
        box_office = random.choice(BOX_OFFICE)
        category = random.choice(CATEGORIES)
        data.append([title, year, rating, box_office, category])
    return data


def save_to_csv(data, filename):
    """Save data to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["Title", "Year", "Rating", "Box Office", "Category"]
        )  # Write header
        writer.writerows(data)


def main():
    # Generate movie data
    movie_data = generate_movie_data(NUM_RECORDS)

    # Save movie data to CSV
    save_to_csv(movie_data, OUTPUT_FILE)

    print(f"Generated {NUM_RECORDS} records and saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
