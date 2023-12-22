import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root, data):
        self.root = root
        self.root.title("Sudoku")
        # Create a 9x9 grid to hold the Sudoku numbers
        self.grid = self.initialize_grid(data)
        self.create_grid() # Create the GUI elements

    def initialize_grid(self, data):
        grid = []
        for i in range(9):
            grid.append([])
            for j in range(9):
                grid[i].append(tk.StringVar(value=data[i*9+j]))
        return grid

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j].get() == '0': # if empty, allows to enter number
                    entry = tk.Entry(self.root, width=4, font=('Arial', 14))
                    entry.grid(row=i, column=j)
                    # Add validation to ensure only single digits are entered
                    validate_digit_cmd = (self.root.register(self.validate_digit),
                                          '%P', '%V', i, j)
                    entry.config(validate='key',
                                 validatecommand=validate_digit_cmd)
                else:
                    label = ttk.Label(self.root, text=self.grid[int(i)][int(j)].get())
                    label.grid(row=i, column=j)

        if self.check_win():
            messagebox.showinfo("Information", "You win!")

        quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        quit_button.grid(row=11, column=3, columnspan=3)

    def validate_digit(self, new_value, event, i, j):
        test1 = new_value.isdigit() and int(new_value) > 0 and int(new_value) < 10
        test2 = self.check_row(new_value, i)
        test3 = self.check_column(new_value, j)
        test4 = self.check_square(new_value, i, j)
        if test1 and test2 and test3 and test4:
            # Update the existing StringVar associated with the Entry widget
            self.grid[int(i)][int(j)].set(new_value)
            return True
        else:
            if test1 is False:
                messagebox.showerror("Invalid Input", "Please enter digit between 1 and 9.")
            if test2 is False:
                messagebox.showerror("Invalid Input", f"{new_value} is already in the row.")
            if test3 is False:
                messagebox.showerror("Invalid Input", f"{new_value} is already in the column.")
            if test4 is False:
                messagebox.showerror("Invalid Input", f"{new_value} is already in the square.")
            return False

    def check_row(self, new_value, i):
        for j in range(9):
            if j != int(i) and self.grid[int(i)][int(j)].get() == new_value:
                return False
        return True

    def check_column(self, new_value, j):
        for i in range(9):
            if i != int(j) and self.grid[int(i)][int(j)].get() == new_value:
                return False
        return True

    def check_square(self, new_value, i, j):
        for a in range(int(i) // 3, int(i) // 3 + 3):
            for b in range(int(j) // 3, int(j) // 3 + 3):
                if self.grid[a][b].get() == new_value:
                    return False
        return True

    def check_win(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j].get() == '0':
                    return False
        return True

def main():
    root = tk.Tk()
    data = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
    sudoku_gui = SudokuGUI(root, data)
    root.mainloop()

if __name__ == "__main__":
    main()
