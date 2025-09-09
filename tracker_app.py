from database import init_db, add_bus, get_all_buses
from utils import print_bus_schedule

def main():
    init_db()
    
    while True:
        print("\n--- Public Transport Tracker ---")
        print("1. Add Bus Schedule")
        print("2. View All Buses")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            bus_number = input("Enter bus number: ")
            stop = input("Enter stop name: ")
            arrival_time = input("Enter estimated arrival time (HH:MM): ")
            add_bus(bus_number, stop, arrival_time)
            print(f"Bus {bus_number} schedule added successfully.")
        elif choice == '2':
            buses = get_all_buses()
            print_bus_schedule(buses)
        elif choice == '3':
            print("Exiting Public Transport Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
