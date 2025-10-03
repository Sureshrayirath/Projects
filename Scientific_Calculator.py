import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Style
        self.style = ttk.Style()
        self.style.configure('TButton', padding=5, font=('Arial', 10))
        
        # Display
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(
            root, 
            textvariable=self.display_var, 
            font=('Arial', 20), 
            justify='right'
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
        
        # Button layout
        self.create_buttons()
        
        # Configure grid
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        # Button definitions: (text, row, column, command)
        buttons = [
            ('C', 1, 0, self.clear),
            ('⌫', 1, 1, self.backspace),
            ('±', 1, 2, self.negate),
            ('/', 1, 3, lambda: self.add_operator('/')),
            
            ('7', 2, 0, lambda: self.add_number('7')),
            ('8', 2, 1, lambda: self.add_number('8')),
            ('9', 2, 2, lambda: self.add_number('9')),
            ('*', 2, 3, lambda: self.add_operator('*')),
            
            ('4', 3, 0, lambda: self.add_number('4')),
            ('5', 3, 1, lambda: self.add_number('5')),
            ('6', 3, 2, lambda: self.add_number('6')),
            ('-', 3, 3, lambda: self.add_operator('-')),
            
            ('1', 4, 0, lambda: self.add_number('1')),
            ('2', 4, 1, lambda: self.add_number('2')),
            ('3', 4, 2, lambda: self.add_number('3')),
            ('+', 4, 3, lambda: self.add_operator('+')),
            
            ('0', 5, 0, lambda: self.add_number('0')),
            ('.', 5, 1, lambda: self.add_number('.')),
            ('=', 5, 2, self.calculate),
            ('√', 5, 3, self.square_root),
            
            ('sin', 6, 0, lambda: self.trig_function('sin')),
            ('cos', 6, 1, lambda: self.trig_function('cos')),
            ('tan', 6, 2, lambda: self.trig_function('tan')),
            ('^', 6, 3, lambda: self.add_operator('^')),
            
            ('(', 7, 0, lambda: self.add_number('(')),
            (')', 7, 1, lambda: self.add_number(')')),
            ('π', 7, 2, lambda: self.add_number(str(math.pi))),
            ('e', 7, 3, lambda: self.add_number(str(math.e))),
        ]
        
        for (text, row, col, command) in buttons:
            ttk.Button(
                self.root,
                text=text,
                command=command
            ).grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

    def add_number(self, number):
        current = self.display_var.get()
        self.display_var.set(current + number)

    def add_operator(self, operator):
        current = self.display_var.get()
        if current and current[-1] not in '+-*/^':
            self.display_var.set(current + operator)

    def clear(self):
        self.display_var.set('')

    def backspace(self):
        current = self.display_var.get()
        self.display_var.set(current[:-1])

    def negate(self):
        try:
            current = float(self.display_var.get())
            self.display_var.set(str(-current))
        except ValueError:
            pass

    def square_root(self):
        try:
            current = float(self.display_var.get())
            if current >= 0:
                self.display_var.set(str(math.sqrt(current)))
            else:
                self.display_var.set('Error')
        except ValueError:
            self.display_var.set('Error')

    def trig_function(self, func):
        try:
            current = float(self.display_var.get())
            if func == 'sin':
                result = math.sin(math.radians(current))
            elif func == 'cos':
                result = math.cos(math.radians(current))
            else:  # tan
                result = math.tan(math.radians(current))
            self.display_var.set(str(round(result, 10)))
        except ValueError:
            self.display_var.set('Error')

    def calculate(self):
        try:
            expression = self.display_var.get().replace('^', '**')
            result = eval(expression)
            self.display_var.set(str(result))
        except:
            self.display_var.set('Error')

if __name__ == '__main__':
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()