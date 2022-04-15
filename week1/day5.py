# #
# # TIC TAC TOE
# #
# # display_board() – To display the Tic Tac Toe board (GUI).
# # player_input(player) – To get the position from the player.
# # check_win() – To check whether there is a winner or not.
# # play() – The main function, which calls all the functions created above.
#
# from itertools import groupby
#
#
# class UsedNum(Exception):
#     """Raised when the input value is already taken"""
#     pass
#
#
# global player
# player = 'X'
# matrix = [
#     [' ', ' ', ' '],
#     [' ', ' ', ' '],
#     [' ', ' ', ' '],
# ]
#
#
# def display_board():
#     print(f'''
#     {matrix[0][0]}|{matrix[0][1]}|{matrix[0][2]}
#     ------
#     {matrix[1][0]}|{matrix[1][1]}|{matrix[1][2]}
#     ------
#     {matrix[2][0]}|{matrix[2][1]}|{matrix[2][2]}
#     ''')
#
#
# def board_not_full():
#     for j in range(len(matrix)):
#         for i in range(len(matrix[j])):
#             if matrix[j][i] == ' ':
#                 return True
#     return False
#
#
# def player_input():
#     global player
#     player = 'X' if player == 'O' else 'X'
#     while True:
#         try:
#             x = int(input('what row would you like? (0,1,2) '))
#             y = int(input('what column would you like? (0,1,2) '))
#             if x not in [0, 1, 2] or y not in [0, 1, 2]:
#                 raise TypeError
#             if matrix[x][y] != ' ':
#                 raise UsedNum
#             break
#         except (ValueError, TypeError):
#             print('Please insert 0 or 1 or 2')
#         except UsedNum:
#             print('Please insert a spot that hasent been taken')
#     matrix[x][y] = player
#
#
# def check_win(board=matrix):
#     mark = player
#     i = 0
#     j = 0
#     return ((all(char == mark for char in [board[i][j], board[i][j + 1], board[i][j + 2]])) or
#             (all(char == mark for char in {board[i + 1][j], board[i + 1][i + 1], board[i + 1][j + 2]})) or
#             (all(char == mark for char in {board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]})) or
#             (all(char == mark for char in {board[i][j], board[i + 1][j], board[i + 2][j]})) or
#             (all(char == mark for char in {board[i][j + 1], board[i + 1][j + 1], board[i + 2][j + 1]})) or
#             (all(char == mark for char in {board[i][j + 2], board[i + 1][j + 2], board[i + 2][j + 2]})) or
#             (all(char == mark for char in {board[i][j], board[i + 1][j + 1], board[i + 2][j + 2]})) or
#             (all(char == mark for char in {board[i + 2][j], board[i + 1][j + 1], board[i][j + 2]})))
#
#
# def play():
#     while board_not_full():
#         player_input()
#         display_board()
#         if check_win():
#             print(f'{player} Won the Game')
#             break
#     else:
#         print('Game is tied')
#
#
# play()



#sorting
x = 'without,hello,bag,world'

t = x.split(',')
t.sort()
print(','.join(t))
