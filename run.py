# We use random to randomly place the ships on the grid
import random


# This gets the grid size while also handling inputs
def get_grid_size():
    """Prompt the user to input the grid size."""
    while True:
        try:
            grid_size = int(input("Enter grid size (e.g., 3 for a "
                                  "3x3 grid): "))
            if grid_size <= 0:
                raise ValueError("Grid size must be a positive integer.")
            return grid_size
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid grid size.")


# Gets number of ships and has an error catcher
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


# Note: the ships only enlarge horizontally
def get_ship_sizes(num_ships, grid_size):
    """Prompt the user to input the size of each ship."""
    ship_sizes = []
    while True:
        try:
            print(f"Enter the size of each ship (1-{grid_size}):")
            for i in range(1, num_ships + 1):
                ship_size = int(input(f"Size of ship {i}: "))
                if ship_size < 1 or ship_size > grid_size:
                    raise ValueError(f"Ship size must be between 1 and "
                                     f"{grid_size}.")
                ship_sizes.append(ship_size)
            return ship_sizes
        except ValueError as e:
            print(f"Error: {e}. Please enter valid ship sizes.")


def initialize_board(grid_size):
    """Create and initialize the game board."""
    return [['O' for _ in range(grid_size)] for _ in range(grid_size)]


# The place_ships function also places the ships randomly for the computer
def place_ships(board, ships):
    """Randomly place ships on the game board."""
    for ship_size in ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        direction = random.choice(['horizontal', 'vertical'])

        if direction == 'horizontal' and col + ship_size <= len(board[0]):
            for i in range(ship_size):
                board[row][col + i] = 'S'
        elif direction == 'vertical' and row + ship_size <= len(board):
            for i in range(ship_size):
                board[row + i][col] = 'S'
        else:
            place_ships(board, [ship_size])


# How the User can see the grid AND ships
def display_board(board):
    """Display the game board."""
    for row in board:
        print(' '.join(row))


# This function is the users guess, it uses two inputs
def get_guess(grid_size):
    while True:
        try:
            row = int(input(f"Enter row (1-{grid_size}): ")) - 1
            col = int(input(f"Enter column (1-{grid_size}): ")) - 1
            if not (0 <= row < grid_size and 0 <= col < grid_size):
                raise ValueError("Guess is off the grid.")
            return row, col
        except ValueError as e:
            print(f"Error: {e}. Please enter valid row and column numbers.")


def computer_move(board, grid_size):
    """Generate a random move for the computer."""
    while True:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        if board[row][col] == 'O':
            return row, col


def play_game():
    """Main game loop."""
    while True:
        try:
            grid_size = get_grid_size()
            num_ships = get_num_ships()
            ship_sizes = get_ship_sizes(num_ships, grid_size)
            board = initialize_board(grid_size)
            place_ships(board, ship_sizes)

            while True:
                display_board(board)
                row, col = get_guess(grid_size)

                # This is how the game figures out whether or not it is a ship
                if board[row][col] == 'S':
                    print("Hit!")
                    board[row][col] = 'X'
                else:
                    print("Miss!")

                # Print computer's move
                computer_row, computer_col = computer_move(board, grid_size)
                if board[computer_row][computer_col] == 'S':
                    print(f"Computer's Move: Hit at "
                          f"({computer_row + 1}, {computer_col + 1})!")
                    board[computer_row][computer_col] = 'X'
                else:
                    print(f"Computer's Move: Miss at "
                          f"({computer_row + 1}, {computer_col + 1})!")

                if all('S' not in row for row in board):
                    print("Congratulations! You sunk all the ships!")
                    break

                restart = input("Do you want to play again? (yes/no): "
                                ).lower()
                if restart != 'yes':
                    break
        except KeyboardInterrupt:
            print("\nGame terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}. Restarting the game.")


play_game()

# end of program
