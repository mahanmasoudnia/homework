while True:
    try:
        birth_year = int(input("Enter your birth year: \n"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid year.")

current_year = 2025
age = current_year - birth_year
print(f"You are {age} years old.")
