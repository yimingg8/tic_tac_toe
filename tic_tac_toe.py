def print_board(board):
  for row in board:
      for cell in row:
          print(cell, end=" | ")
      print("\n" + "-" * 9)

def check_winner(board, player):
  # Check rows
  for row in board:
      if row[0] == row[1] == row[2] == player:
          return True

  # Check columns
  for col in range(3):
      if board[0][col] == board[1][col] == board[2][col] == player:
          return True

  # Check diagonals
  if (board[0][0] == board[1][1] == board[2][2] == player) or \
     (board[0][2] == board[1][1] == board[2][0] == player):
      return True

  return False

def is_board_full(board):
  for row in board:
      for cell in row:
          if cell == " ":
              return False
  return True

def main():
  board = [[" " for _ in range(3)] for _ in range(3)]
  player = "X"

  print("Welcome to Tic Tac Toe!")
  print_board(board)

  while True:
      row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
      col = int(input(f"Player {player}, enter the column (0, 1, 2): "))

      if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
          print("Invalid move. Try again.")
      else:
          board[row][col] = player
          print_board(board)

          if check_winner(board, player):
              print(f"Player {player} wins!")
              break

          if is_board_full(board):
              print("It's a tie!")
              break

          player = "O" if player == "X" else "X"

if __name__ == "__main__":
  main()
1
