import tkinter as tk
from tkinter import messagebox

def initialize_board():
    global board, current_player
    board = [['+' for _ in range(30)] for _ in range(30)]
    current_player = '흑돌'

initialize_board()

def print_board():
    for row in board:
        print(" ".join(row))

def check_winner(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for dr, dc in directions:
        count = 1
        for i in range(1, 5):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == current_player:
                count += 1
            else:
                break

        for i in range(1, 5):
            r, c = row - dr * i, col - dc * i
            if 0 <= r < 15 and 0 <= c < 15 and board[r][c] == current_player:
                count += 1
            else:
                break

        if count >= 5:
            return True

    return False

def place_piece(event):
    col = round(event.x / 30)
    row = round(event.y / 30)

    if board[row][col] == '+':
        board[row][col] = current_player
        color = 'black' if current_player == '흑돌' else 'white'
        canvas.create_oval(col * 30 - 10, row * 30 - 10, col * 30 + 10, row * 30 + 10, fill=color)
        if check_winner(row, col):
            print_board()
            print(f"{current_player}")
            if messagebox.askyesno("족발마싯당", f"{current_player} 승리! 다시 대결해보세요."):
                initialize_board()
                canvas.delete("all")
                draw_lines()
        else:
            change_player()

def change_player():
    global current_player
    if current_player == '흑돌':
        current_player = '백돌'
    else:
        current_player = '흑돌'

def draw_lines():
    for i in range(15):
        canvas.create_line(0, i * 30, 450, i * 30)
        canvas.create_line(i * 30, 0, i * 30, 450)

root = tk.Tk()
root.title("오목 게임")

canvas = tk.Canvas(root, width=450, height=450)
canvas.pack()

draw_lines()
canvas.bind("<Button-1>", place_piece)

try:
    import Tkinter as tk
except:
    import tkinter as tk

root.minsize(width=900, height=900)
root.maxsize(width=900, height=900)

root.mainloop()
