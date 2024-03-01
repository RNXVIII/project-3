

def get_grid_size():
    """Prompt the user to input the grid size."""
    while True:
        try:
            grid_size = int(input("Enter grid size (e.g., 3 for a 3x3 grid): "))
            if grid_size <= 0:
                raise ValueError("Grid size must be a positive integer.")
            return grid_size
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid grid size.")

get_grid_size()

def get_num_ships():
    """Prompt the user to input the number of ships."""
    while True:
        try:
            num_ships = int(input("Enter number of ships: "))
            if num_ships <= 0:
                raise ValueError("Number of ships must be a positive integer.")
            return num_ships
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number of ships.")

get_num_ships()


def get_ship_sizes(num_ships, grid_size):
    """Prompt the user to input the size of each ship."""
    ship_sizes = []
    while True:
        try:
            print(f"Enter the size of each ship (1-{grid_size}):")
            for i in range(1, num_ships + 1):
                ship_size = int(input(f"Size of ship {i}: "))
                if ship_size < 1 or ship_size > grid_size:
                    raise ValueError(f"Ship size must be between 1 and {grid_size}.")
                ship_sizes.append(ship_size)
            return ship_sizes
        except ValueError as e:
            print(f"Error: {e}. Please enter valid ship sizes.")


#if statment to check that all fucntions work
if __name__ == "__main__":
    # Define sample values for testing
    num_ships = 3
    grid_size = 5

    # Call the get_ship_sizes function with sample values
    ship_sizes = get_ship_sizes(num_ships, grid_size)

    # Print the resulting ship sizes
    print("Ship Sizes:", ship_sizes)
