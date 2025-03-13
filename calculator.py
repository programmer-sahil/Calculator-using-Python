import tkinter as tk
from tkinter import ttk, messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator (NYCTA) Made by SAHIL")
        self.root.geometry("400x600")  # Increased window size
        self.root.resizable(False, False)
        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying expressions and results
        self.display = tk.Entry(self.root, font=('Helvetica', 28), justify='right', bd=15, insertwidth=4, width=14)
        self.display.grid(row=0, column=0, columnspan=4, pady=20)

        # Button layout with larger buttons and more spacing
        buttons = [
            ('C', '⌫', '÷', '×'),
            ('7', '8', '9', '-'),
            ('4', '5', '6', '+'),
            ('1', '2', '3', '='),
            ('±', '0', '.', '')
        ]

        for i, row_values in enumerate(buttons):
            for j, value in enumerate(row_values):
                if value:
                    button = tk.Button(
                        self.root,
                        text=value,
                        font=('Helvetica', 22),  # Increased font size for easier clicking
                        bd=3,
                        relief='ridge',
                        command=lambda v=value: self.on_button_click(v)
                    )
                    button.grid(row=i+1, column=j, sticky='nsew', padx=10, pady=10)

        # Configure grid weights for responsiveness
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

        # Key bindings
        self.root.bind("<Key>", self.on_key_press)

    def on_button_click(self, char):
        if char == 'C':
            self.clear()
        elif char == '⌫':
            self.backspace()
        elif char == '=':
            self.calculate()
        elif char == '±':
            self.plus_minus()
        elif char in ('+', '-', '×', '÷'):
            self.add_operator(char)
        else:
            self.add_to_expression(char)

    def on_key_press(self, event):
        key = event.char
        if key.isdigit() or key == '.':
            self.add_to_expression(key)
        elif key in '+-*/':
            self.add_operator(key)
        elif key == '\r':
            self.calculate()
        elif key == '\x08':
            self.backspace()
        elif key.lower() == 'c':
            self.clear()

    def add_to_expression(self, value):
        self.expression += str(value)
        self.update_display()

    def add_operator(self, operator):
        if self.expression and self.expression[-1] in '+-×÷':
            self.expression = self.expression[:-1]
        self.expression += self.convert_operator(operator)
        self.update_display()

    def convert_operator(self, operator):
        return {
            '+': '+',
            '-': '-',
            '*': '×',
            '/': '÷',
            '×': '*',
            '÷': '/'
        }.get(operator, '')

    def clear(self):
        self.expression = ""
        self.update_display()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def plus_minus(self):
        if self.expression and self.expression[0] == '-':
            self.expression = self.expression[1:]
        else:
            self.expression = '-' + self.expression
        self.update_display()

    def calculate(self):
        try:
            expression = self.expression.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            self.expression = str(result)
            self.update_display()
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            self.clear()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
