from datetime import datetime

# First feature - record baby activities

def record_baby_activities():
    while True:
        baby_name = input("Enter baby name (or 'q' to quit): ")
        if baby_name.lower() == 'q':
            break

        baby_name = baby_name.lower()  # Convert baby name to lowercase

        nappies = get_valid_int("Enter number of nappies changed: ")
        if nappies is None:
            continue

        bottles = get_valid_int("Enter number of 100ml bottles fed: ")
        if bottles is None:
            continue

        weight = get_valid_float("Enter baby's weight (in kg): ")
        if weight is None:
            continue

        length = get_valid_float("Enter baby's length (in cm): ")
        if length is None:
            continue

        date = get_valid_date("Enter the date (YYYY-MM-DD): ")
        if date is None:
            continue

        with open('baby_data.txt', 'a') as file:
            file.write(f"{baby_name},{nappies},{bottles},{weight},{length},{date}\n")

        print("Data has been recorded successfully!")



# Second feature - remove baby entry

def remove_baby_entry():
    baby_name = input("Enter baby name to select activities for removal: ").lower()  # Convert baby name to lowercase
    try:
        with open('baby_data.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No data found.")
        return

    entries_to_remove = []
    for line in lines:
        record = line.strip().split(',')
        if record[0].lower() == baby_name:  # Check for case-insensitive baby name match
            entries_to_remove.append(record)

    if not entries_to_remove:
        print("No entry found for the specified baby name.")
        return

    print(f"Entries for {baby_name}:")
    for idx, entry in enumerate(entries_to_remove, start=1):
        print(f"{idx}. Date: {entry[5]}")
        print("   Nappies:", entry[1])
        print("   100ml Bottles:", entry[2]) 
        print("   Weight:", entry[3], "kg")
        print("   Length:", entry[4], "cm")
        print("-" * 30)

    while True:
        selection = input("Enter the number of the entry to remove (or 'q' to cancel): ")
        if selection.lower() == 'q':
            return

        if not selection.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        selection = int(selection)
        if 1 <= selection <= len(entries_to_remove):
            selected_entry = entries_to_remove[selection - 1]
            with open('baby_data.txt', 'w') as file:
                for line in lines:
                    if line.strip() != ','.join(selected_entry):
                        file.write(line)
            print("Entry has been removed successfully.")
            break
        else:
            print("Invalid selection. Please enter a valid number.")


# Third feature - total per week (nappies and bottles)
def get_week_number(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    week_number = date.strftime('%U')  # Get the week number (0-53)
    return int(week_number)

def totalize_data_per_week():
    try:
        with open('baby_data.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No data found.")
        return

    weekly_totals = {}
    for line in lines:
        record = line.strip().split(',')
        baby_name = record[0].lower()
        nappies = int(record[1])
        bottles = int(record[2])
        date = record[5]

        week_number = get_week_number(date)

        if baby_name not in weekly_totals:
            weekly_totals[baby_name] = {}

        if week_number not in weekly_totals[baby_name]:
            weekly_totals[baby_name][week_number] = {
                'nappies': 0,
                'bottles': 0,
            }

        weekly_totals[baby_name][week_number]['nappies'] += nappies
        weekly_totals[baby_name][week_number]['bottles'] += bottles

    print("\nWeekly Totals (Nappies and Bottles):")
    for baby_name, weekly_data in weekly_totals.items():
        print(f"\nBaby: {baby_name}")
        for week_number, data in weekly_data.items():
            print(f"Week {week_number} - Nappies: {data['nappies']}, Bottles: {data['bottles']}")

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


# Entry app - Menu
if __name__ == "__main__":
    print("Welcome to the Terminal Baby Tracker Application!")
    while True:
        print("\nMenu:")
        print("1. Record Baby Activities")
        print("2. Remove entry")
        print("3. Total Data per Week")
        print("4. Exit")
        choice = get_valid_int("Enter your choice: ")

        if choice == 1:
            record_baby_activities()


        elif choice == 2:
            remove_baby_entry()

        elif choice == 3:
            totalize_data_per_week()

        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")



