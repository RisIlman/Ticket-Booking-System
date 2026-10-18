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


def selectShowtime() :
    print ("=== Available Showtimes ===")
    print ("1. 10:00 AM")
    print ("2. 1:00 PM")
    print ("3. 4:00 PM")
    print ("4. 8:00 PM")

    showtimes = {
        1: "10:00 AM",
        2: "1:00 PM",
        3: "4:00 PM",
        4: "8:00 PM"
    }

    while True:
        try:
            choice = int(input("Please select a showtime (1-4) :"))

            if choice in showtimes:
                print(f"You have selected the {showtimes[choice]} showtime.")
                return showtimes[choice]
            else :
                print("Invalid selection. Please try again.")

        except ValueError:
            print("Please enter a number.")


def selectSeats() :
    print ("=== Seat Selection ===")

    rows = 5
    seats_per_row = 6

    basic_price = 15.00
    premium_price = 20.00

    booked_seats = ["A3", "B5", "C3", "D1", "E6"]
    selected_seats = []
    all_seats = []

    for row in range(rows):
        row_letter = chr(65 + row)

        for seat_num in range(1, seats_per_row + 1):
            seat = row_letter + str(seat_num)
            all_seats.append(seat)