import sqlite3

# Function to create the database and table if they don't exist
def create_database_and_table():
    conn = sqlite3.connect("stephen_king_adaptations.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
                    movieID text,
                    movieName text,
                    movieYear INTEGER,
                    imdbRating REAL
                    )''')
    conn.commit()
    conn.close()

# Function to read the file and return its content as a list
def read_file_to_list(filename):
    with open(filename, "r") as file:
        return file.readlines()

# Function to insert data from the list into the database
def insert_data_into_database(data_list):
    conn = sqlite3.connect("stephen_king_adaptations.db")
    cursor = conn.cursor()

    for line in data_list:
        movie_data = line.strip().split(',')
        print(movie_data)
        if len(movie_data) == 4:
            # print()
            cursor.execute("INSERT INTO stephen_king_adaptations_table (movieID ,movieName, movieYear, imdbRating) VALUES (?, ?, ?, ?)",
                           (movie_data[0],movie_data[1], int(movie_data[2]), float(movie_data[3])))       
    conn.commit()
    conn.close()

# Function to search for movies in the database based on user input
def search_movies():
    conn = sqlite3.connect("stephen_king_adaptations.db")
    cursor = conn.cursor()

    while True:
        print("\nOptions:")
        print("1. Search by Movie Name")
        print("2. Search by Movie Year")
        print("3. Search by Movie Rating")
        print("4. STOP")
        choice = input("Enter your choice: ")

        if choice == "1":
            movie_name = input("Enter the name of the movie: ")
            cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(f"Movie Name: {row[1]}, Year: {row[2]}, IMDb Rating: {row[3]}")
            else:
                print("No such movie exists in our database.")
        elif choice == "2":
            movie_year = input("Enter the year: ")
            cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (movie_year,))
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(f"Movie Name: {row[1]}, Year: {row[2]}, IMDb Rating: {row[3]}")
            else:
                print("No movies were found for that year in our database.")
        elif choice == "3":
            min_rating = float(input("Enter the minimum rating: "))
            cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (min_rating,))
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(f"Movie Name: {row[1]}, Year: {row[2]}, IMDb Rating: {row[3]}")
            else:
                print("No movies at or above that rating were found in the database.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    create_database_and_table()
    data_list = read_file_to_list("stephen_king_adaptations.txt")
    print("1")
    #print(data_list)
    insert_data_into_database(data_list)
    search_movies()