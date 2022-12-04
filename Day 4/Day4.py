from copy import copy, deepcopy

def read_file(filename):
    # Create empty lists to store the numbers and the arrays
    numbers = []
    sub_array = []
    arrays = []
    
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the first line and split it by the comma to get the numbers
        numbers = [int(n) for n in file.readline().split(",")]
        counter = 0
        
        # Iterate over the remaining lines in the file
        for line in file:
            temp = line.strip('\n').replace('  ', ' ')
            if len(temp) > 0 and temp[0] == ' ':
                temp.replace(' ', '', 1)
            
            # Split the line by the space to get the numbers in the array
            array = [int(n) for n in temp.split()]
            if (len(array) == 0):
                continue

            # Add the array to the list of arrays
            sub_array.append(copy(array))
            counter += 1
            if counter == 5:
                arrays.append(copy(sub_array))
                counter = 0
                sub_array = []
            
    # Return the numbers and arrays as a tuple
    return numbers, arrays

def bingo_winner(called_numbers, game_boards):
  # Keep track of the number of numbers called for each game board
  called_counts = 0
  
  # Keep track of whether each game board has won yet
  game_won = [False] * len(game_boards)
  
  # For each number called
  for number in called_numbers:
    # For each game board
    for i, game_board in enumerate(game_boards):
      # If this game board has already won, skip it
      if game_won[i]:
        # Return the winning game board and the number of numbers called to win
        winning_board_index = game_won.index(True)
        return game_board, called_numbers[called_counts-1], winning_board_index
      
      # Check if this number completes a row, column, or diagonal on this game board
      game_board = copy(game_board)
      for j, row in enumerate(game_board):
        if row.count(number) > 0:
          row[row.index(number)] = 'X'
      for j, row in enumerate(game_board):
        if row.count('X') == 5:
          game_won[i] = True
      for j in range(5):
        column = [game_board[k][j] for k in range(5)]
        if column.count('X') == 5:
          game_won[i] = True

    called_counts += 1
      

  # Find the index of the first game board that has won
  winning_board_index = game_won.index(True)
  
  # Return the winning game board and the number of numbers called to win
  return game_boards[winning_board_index], called_numbers[called_counts-1], winning_board_index
  
  
def bingo_winner_last(called_numbers, game_boards):
  # Keep track of the number of numbers called for each game board
  called_counts = 0
  
  won_boards_indexes = []
  won_nums = []
  final_boards = []
  # Keep track of whether each game board has won yet
  game_won = [False] * len(game_boards)
  
  # For each number called
  for number in called_numbers:
    # For each game board
    for i, game_board in enumerate(game_boards):
      # If this game board has already won, skip it
      if game_won[i]:
        if i not in won_boards_indexes:
            won_boards_indexes.append(i)
            won_nums.append(called_counts)
            
            final_boards.append(copy(game_board))
        continue
        
      # Check if this number completes a row, column, or diagonal on this game board
      game_board = copy(game_board)
      for j, row in enumerate(game_board):
        if row.count(number) > 0:
          row[row.index(number)] = 'X'
      for j, row in enumerate(game_board):
        if row.count('X') == 5:
          game_won[i] = True
      for j in range(5):
        column = [game_board[k][j] for k in range(5)]
        if column.count('X') == 5:
          game_won[i] = True

    called_counts += 1
      

  # Find the index of the first game board that has won
  winning_board_index = game_won.index(True)
  
  # Return the winning game board and the number of numbers called to win
  last_won = won_boards_indexes.pop()
  last_num = called_numbers[won_nums.pop()-1]
  
  return game_boards[last_won], last_num, last_won

def calc_score(board, num):
    sum = 0
    for row in board:
        for n in row:
            if(n != 'X'):
                sum += n
    return sum * num


# Sample called numbers
called_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

# Sample game boards
game_boards = [
  [[22, 13, 17, 11,  0],
 [8,  2, 23,  4, 24],
[21,  9, 14, 16,  7],
 [6, 10,  3, 18,  5],
 [1, 12, 20, 15, 19]],
 
  [ [3, 15,  0,  2, 22],
 [9, 18, 13, 17,  5],
[19,  8,  7, 25, 23],
[20, 11, 10, 24,  4],
[14, 21, 16, 12,  6]],

  [[14, 21, 17, 24,  4],
[10, 16, 15,  9, 19],
[18,  8, 23, 26, 20],
[22, 11, 13,  6,  5],
 [2,  0, 12,  3,  7]]
]

called_numbers, boards = read_file('day4Data.txt')

# Calculate the bingo winner
winning_board, num, winning_index = bingo_winner(called_numbers, boards)

# Print the bingo winner
print(f'Bingo winner: Board#', winning_index + 1)
print(f'Final Score:', calc_score(winning_board, num))

# Print the last bingo winner
winning_board, num, winning_index = bingo_winner_last(called_numbers, boards)
print(f'Last Bingo winner: Board#', winning_index + 1)
print(f'Final Score:', calc_score(winning_board, num))
