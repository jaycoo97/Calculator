# Calling the graphical interface module
import tkinter as tk

# Determine graphic elements in the program
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("480x620")
        self.result = tk.Entry(self, font=("Arial", 36))
        self.result.grid(row=0, column=0, columnspan=4, padx=10,
                         pady=10, ipadx=40, ipady=20, sticky=tk.W+tk.E)
        self.result.config(justify=tk.LEFT)
        self.grid_columnconfigure(0, weight=1)

        button_frame = tk.Frame(self)
        button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.create_button("1", button_frame, 0, 0, lambda: self.add_number(1))
        self.create_button("2", button_frame, 0, 1, lambda: self.add_number(2))
        self.create_button("3", button_frame, 0, 2, lambda: self.add_number(3))
        self.create_button("4", button_frame, 1, 0, lambda: self.add_number(4))
        self.create_button("5", button_frame, 1, 1, lambda: self.add_number(5))
        self.create_button("6", button_frame, 1, 2, lambda: self.add_number(6))
        self.create_button("7", button_frame, 2, 0, lambda: self.add_number(7))
        self.create_button("8", button_frame, 2, 1, lambda: self.add_number(8))
        self.create_button("9", button_frame, 2, 2, lambda: self.add_number(9))
        self.create_button("0", button_frame, 3, 1, lambda: self.add_number(0))
        self.create_button("+", button_frame, 0, 3,
                           lambda: self.add_operation("+"), "#D687F8")
        self.create_button("-", button_frame, 1, 3,
                           lambda:self.add_operation("-"), "#D687F8")
        self.create_button("*", button_frame, 2, 3,
                           lambda: self.add_operation("*"), "#D687F8")
        self.create_button("/", button_frame, 3, 3,
                           lambda: self.add_operation("/"), "#D687F8")
        self.create_button("=", button_frame, 3, 2,self.calculate, "#77C9DA")
        self.create_button("C", button_frame, 3, 0,self.clear, "#F17667")

# Determine program key values
    def create_button(self, text, frame, row, column, command, bg="#ABB7F7"):
        button = tk.Button(frame, text=text, command=command,
                           font=("Arial", 18), width=5, height=3)
        button.config(bg=bg)
        button.grid(row=row, column=column, padx=10, pady=10)

# Add numbers to the input
    def add_number(self, number):
        current = self.result.get()
        current += str(number)
        self.result.delete(0, tk.END)
        self.result.insert(0, current)

# Add Arithmetic operators
    def add_operation(self, operator):
        current = self.result.get()
        current += operator
        self.result.delete(0, tk.END)
        self.result.insert(0, current)

# It reads and stores everything that comes from the input
    def calculate(self):
        current = self.result.get()
        self.result.delete(0, tk.END)
        self.result.insert(0, eval(current))

# Clear displayable values
    def clear(self):
        self.result.delete(0, tk.END)

# Final approval of the program execution, which is the main script
if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()



