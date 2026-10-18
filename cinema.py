def displayMovies() :
    print ("=== Available Movies ===")
    print ("1. The Batman ")
    print ("2. Spider-Man: No Way Home")
    print ("3. Dune")
    print ("4. Top Gun: Maverick")

    movies = {
        1: "The Batman",
        2: "Spider-Man: No Way Home",
        3: "Dune",
        4: "Top Gun: Maverick"
    }

    while True:
        try:
            choice = int(input("Please select a movie (1-4) : "))

            if choice in movies:
                print(f"You have selected '{movies[choice]}'.")
                return movies[choice]
            else :
                print("Invalid selection. Please try again.")

        except ValueError:
            print("Please enter a number.")
