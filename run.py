

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


