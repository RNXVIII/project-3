

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


