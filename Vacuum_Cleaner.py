def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum (A or B): ").upper()
    status_input = input(f"Enter status of Room {location_input} (0 for Clean, 1 for Dirty): ")
    status_input_complement = input("Enter status of other room (0 for Clean, 1 for Dirty): ")

    print("\nInitial State:")
    print(f"Vacuum Location: {location_input}")
    print(f"Room A Status: {status_input if location_input == 'A' else status_input_complement}")
    print(f"Room B Status: {status_input if location_input == 'B' else status_input_complement}")
    print("-" * 40)

    if location_input == 'A':
        print("Vacuum is placed in Location A")

        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'
            cost += 1
            print("Location A has been cleaned.")
            print(f"Cost: {cost}")

        if status_input_complement == '1':
            print("Location B is Dirty.")
            print("Moving right to Location B.")
            cost += 1
            print(f"Cost: {cost}")

            goal_state['B'] = '0'
            cost += 1
            print("Location B has been cleaned.")
            print(f"Cost: {cost}")

    elif location_input == 'B': 
        print("Vacuum is placed in Location B")

        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'
            cost += 1
            print("Location B has been cleaned.")
            print(f"Cost: {cost}")

        if status_input_complement == '1':
            print("Location A is Dirty.")
            print("Moving left to Location A.")
            cost += 1
            print(f"Cost: {cost}")

            goal_state['A'] = '0'
            cost += 1
            print("Location A has been cleaned.")
            print(f"Cost: {cost}")

    print("-" * 40)
    print("Goal State Reached:")
    print(goal_state)
    print("Total Cost:", cost)


vacuum_world()