from datetime import datetime

# First feature - record baby activities

def record_baby_activities():
    while True:
        baby_name = input("Enter baby name (or 'q' to quit): ")
        if baby_name.lower() == 'q':
            break

        baby_name = baby_name.lower()  # Convert baby name to lowercase
        
        nappies = get_valid_int("Enter number of nappies changed: ")
        if nappies is None:  # Check if user entered 'q'
            continue

        bottles = get_valid_int("Enter number of 100ml bottles fed: ")
        if bottles is None:  # Check if user entered 'q'
            continue

        weight = get_valid_float("Enter baby's weight (in kg): ")
        if weight is None:  # Check if user entered 'q'
            continue

        length = get_valid_float("Enter baby's length (in cm): ")
        if length is None:  # Check if user entered 'q'
            continue

        date = get_valid_date("Enter the date (YYYY-MM-DD): ")
        if date is None:  # Check if user entered 'q'
            continue

        with open('baby_data.txt', 'a') as file:
            file.write(f"{baby_name},{nappies},{bottles},{weight},{length},{date}\n")

        print("Data has been recorded successfully!")

# Helpers
def get_valid_int(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'q':
                return None
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_float(prompt):
    while True:
        try:
            value = input(prompt)
            if value.lower() == 'q':
                return None
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number.")

def get_valid_date(prompt):
    while True:
        date = input(prompt)
        if date.lower() == 'q':
            return None
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
# Menu
if __name__ == "__main__":
    print("Welcome to the Terminal Baby Tracker Application!")
    while True:
        print("\nMenu:")
        print("1. Record Baby Activities")
        print("2. Exit")
        choice = get_valid_int("Enter your choice: ")

        if choice == 1:
            record_baby_activities()
        elif choice == 2:
            break

        else:
            print("Invalid choice. Please try again.")