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

    def displaySeats():
        print("\n========== CINEMA SEATS ==========")
        print("SCREEN".center(6 +seats_per_row * 5) + "\n")

        print(" " * 6, end="")
        for seat_num in range(1, seats_per_row + 1):
            print(f"{seat_num:^5}", end="")
        print("\n")

        for row in range(rows):
            row_letter = chr(65 + row)
            print(f"Row {row_letter} ", end="")

            for seat_num in range(1, seats_per_row + 1):
                seat = row_letter + str(seat_num)

                if seat in booked_seats:
                    symbol = "[X]"
                elif seat in selected_seats :
                    symbol = "[S]"
                else:
                    symbol = "[ ]"

                print(f"{symbol:^5}", end="")

            if row < 3 :
                print(" Premium")
            else :
                print(" Basic")

        print("\n[X] = Booked")
        print("[S] = Your Selection")
        print("[ ] = Available")
        print(f"Premium (Rows A-C) : RM {premium_price:.2f}")
        print(f"Basic (Rows D-E) : RM {basic_price:.2f}")

    available_count = len(all_seats) - len(booked_seats)

    while True :
        try :
            num_seats = int(input("\nNumber of seats to book (1-5) : "))

            if num_seats <= 0 or num_seats > 5:
                print("Please select between 1 and 5 seats.")
            elif num_seats > available_count :
                print(f"Only {available_count} seats are available. Please enter again.")
            else:
                break

        except ValueError :
            print("Please enter a valid number.")

    while len(selected_seats) < num_seats :
        displaySeats()
        seat_choice = input(f"\nSelect seat {len(selected_seats) + 1} (e.g., A1, B3) : ").upper()

        if seat_choice in booked_seats :
            print("Sorry, that seat is already booked. Please choose another seat.")
        elif seat_choice not in all_seats :
            print("Invalid seat selection. Please choose a valid seat.")
        elif seat_choice in selected_seats :
            print("You have already selected that seat. Please choose another seat.")
        else :
            selected_seats.append(seat_choice)
            print(f"Seat {seat_choice} has been added to your selection.")

    total_price = 0

    for seat in selected_seats :
        row_letter = seat[0]

        if row_letter in ["A", "B", "C"] :
            price = premium_price
            seat_type = "Premium"
        else : 
            price = basic_price
            seat_type = "Basic"

        total_price += price

    booked_seats.extend(selected_seats)

    return selected_seats, total_price


def selectBeverages():
    while True:
        answer = input("Would you like to purchase beverages? (yes/no): ").strip().lower()

        if answer == "yes" :
            break
        elif answer == "no" :
            return "No beverage", 0.00
        else :
            print("Invalid choice. Please enter yes or no.")

    beverages = {
        "1": ("Coca-Cola", 5.00),
        "2": ("Pepsi", 5.00),
        "3": ("Mineral Water", 3.00)
    }

    print("\n========== BEVERAGES ==========")
    print("1. Coca-Cola      - RM5.00")
    print("2. Pepsi          - RM5.00")
    print("3. Mineral Water  - RM3.00")

    while True :
        choice = input("Choose your beverage (1-3) : ")

        if choice in beverages :
            beverage_name, beverage_price = beverages[choice]
            return beverage_name, beverage_price
        else:
            print("Invalid choice. Please select a valid beverage option.")