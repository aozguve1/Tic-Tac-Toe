import tkinter as tk
from tkinter import messagebox

def check_winner():
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != "-":
            return board[i]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != "-":
            return board[i]
    if board[0] == board[4] == board[8] != "-":
        return board[0]
    if board[2] == board[4] == board[6] != "-":
        return board[2]
    if "-" not in board:
        return "Tie"
    return None

def on_click(i):
    global currentPlayer
    if board[i] == "-" and winner is None:
        board[i] = currentPlayer
        buttons[i].config(text=currentPlayer)
        switch_player()
        check_game_over()

def switch_player():
    global currentPlayer
    currentPlayer = "X" if currentPlayer == "O" else "O"
    label.config(text=f"It's {currentPlayer}'s Turn")

def check_game_over():
    global winner
    winner = check_winner()
    if winner is not None:
        if winner == "Tie":
            messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        else:
            messagebox.showinfo("Tic Tac Toe", f"Congratulations {winner} Won the Game!")
        root.destroy()

def reset_game():
    global board, winner, currentPlayer
    board = ["-"] * 9
    winner = None
    currentPlayer = "X"
    for button in buttons:
        button.config(text="")
    label.config(text=f"It's {currentPlayer}'s Turn")

root = tk.Tk()
root.title("Tic Tac Toe")

currentPlayer = "X"
winner = None
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("normal", 40), height=1, width=2, command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

label = tk.Label(root, text=f"It's {currentPlayer}'s Turn", font=("normal", 20))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
