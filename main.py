import sqlite3


file_path = r"stephen_king_adaptations.txt"
king_list = []

with open(file_path, "r") as file:
    for line in file:
        movie_info = line.strip().split(",")
        king_list.append(movie_info)


conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS movie_table (MovieID TEXT, MovieName TEXT, Year INTEGER, Rating REAL)")


for movie in king_list:
    cursor.execute("INSERT INTO movie_table (MovieID, MovieName, Year, Rating) VALUES (?, ?, ?, ?)", movie)

conn.commit()

while True:
    print("Please select a search method:")
    print("1. Movie name")
    print("2. Movie year")
    print("3. Movie rating")
    print("4. STOP")
    choice = input("Please enter an option: ")

    if choice == "1":
        movie_name = input("Please enter the movie name you want to search for: ")
        cursor.execute("SELECT * FROM movie_table WHERE MovieName=?", (movie_name,))
        result = cursor.fetchall()
        if result:
            for movie in result:
                print("Movie name:", movie[1])
                print("Movie year:", movie[2])
                print("Movie rating:", movie[3])
        else:
            print("Sorry, no results found.")

    elif choice == "2":
        movie_year = input("Please enter the movie year you want to search for: ")
        cursor.execute("SELECT * FROM movie_table WHERE Year=?", (movie_year,))
        result = cursor.fetchall()
        if result:
            for movie in result:
                print("Movie name:", movie[1])
                print("Movie year:", movie[2])
                print("Movie rating:", movie[3])
        else:
            print("Sorry, no results found.")

    elif choice == "3":
        movie_rating = float(input("Please enter the movie rating you want to search for: "))
        cursor.execute("SELECT * FROM movie_table WHERE Rating>=?", (movie_rating,))
        result = cursor.fetchall()
        if result:
            for movie in result:
                print("Movie name:", movie[1])
                print("Movie year:", movie[2])
                print("Movie rating:", movie[3])
        else:
            print("Sorry, no results found.")

    elif choice == "4":
        break
    else:
        print("Invalid option. Please try again.")