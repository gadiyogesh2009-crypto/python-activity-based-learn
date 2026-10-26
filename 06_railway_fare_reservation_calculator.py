# Assignment 6: Railway Fare and Reservation Calculator

distance = float(input("Enter journey distance in km: "))
if distance <= 0:
    print("Error: Distance must be greater than zero.")
else:
    coach = input("Enter coach type (Sleeper/AC): ").strip().lower()
    passengers = int(input("Enter number of passengers: "))

    rates = {"sleeper": 1.2, "ac": 2.5}
    if coach not in rates or passengers <= 0:
        print("Error: Select Sleeper or AC and enter at least one passenger.")
    else:
        base_fare = distance * rates[coach]
        distance_discount = 0.10 * base_fare if distance > 500 else 0
        total = 0

        for i in range(1, passengers + 1):
            age = int(input(f"Enter age of passenger {i}: "))
            if age < 0:
                print("Invalid age. This passenger's fare will be zero.")
                passenger_fare = 0
            elif age < 5:
                passenger_fare = 0
            else:
                passenger_fare = base_fare - distance_discount
                if age >= 60:
                    passenger_fare -= 0.20 * base_fare
                passenger_fare = max(0, passenger_fare) + 40

            cancel = input(f"Cancel reservation for passenger {i}? (yes/no): ").strip().lower()
            if cancel == "yes":
                passenger_fare = 0.10 * base_fare

            print(f"Passenger {i} fare: Rs. {passenger_fare:.2f}")
            total += passenger_fare

        print(f"\nTotal fare: Rs. {total:.2f}")
