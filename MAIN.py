import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))


def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result:")


root = tk.Tk()
root.title("Simple Calculator")


tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)


tk.Button(root, text="Add", command=lambda: calculate("add"), width=10).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract"), width=10).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply"), width=10).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Divide", command=lambda: calculate("divide"), width=10).grid(row=3, column=1, padx=10, pady=10)


tk.Button(root, text="Clear", command=clear, width=10, bg="lightgray").grid(row=4, column=0, columnspan=2, pady=10)


result_label = tk.Label(root, text="Result:", font=("Arial", 12, "bold"))
result_label.grid(row=5, column=0, columnspan=2, pady=10)


root.mainloop()
