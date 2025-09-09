def print_bus_schedule(buses):
    if not buses:
        print("No bus schedule available.")
        return
    print("\nBus Schedule:")
    for i, (bus_number, stop, arrival_time) in enumerate(buses, 1):
        print(f"{i}. Bus {bus_number} - Stop: {stop} - Arrival: {arrival_time}")
