import tkinter as tk
from math import sqrt

# Function to handle button clicks
def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            # Evaluate the expression
            result = eval(expression)
            screen_var.set(result)
            expression = str(result)
        except Exception:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    elif text == "⌫":
        # Backspace functionality
        expression = expression[:-1]
        screen_var.set(expression)
    elif text == "√":
        try:
            result = sqrt(float(expression)) if expression else 0
            screen_var.set(result)
            expression = str(result)
        except Exception:
            screen_var.set("Error")
            expression = ""
    else:
        expression += text
        screen_var.set(expression)

# Initialize the application
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.resizable(False, False)

expression = ""
screen_var = tk.StringVar()

# Display Screen
screen = tk.Entry(
    root,
    textvar=screen_var,
    font=("Arial", 24),
    bd=8,
    relief=tk.SUNKEN,
    justify=tk.RIGHT,
    bg="#f4f4f4",
    fg="#333"
)
screen.pack(fill=tk.BOTH, ipadx=8, ipady=20, pady=10)

# Button layout
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["√", "0", ".", "="],
]

# Button styles
button_colors = {
    "operators": "#ff8c00",
    "numbers": "#4CAF50",
    "special": "#f44336",
    "equal": "#3f51b5"
}

# Create buttons dynamically
for row in buttons:
    button_frame = tk.Frame(root, bg="#ffffff")
    button_frame.pack(expand=True, fill="both")
    for char in row:
        color = (
            button_colors["operators"]
            if char in {"+", "-", "*", "/", "%"}
            else button_colors["special"]
            if char in {"C", "⌫", "√"}
            else button_colors["equal"]
            if char == "="
            else button_colors["numbers"]
        )
        button = tk.Button(
            button_frame,
            text=char,
            font=("Arial", 18),
            relief=tk.RAISED,
            border=0,
            bg=color,
            fg="white",
            activebackground="#ffffff",
            activeforeground=color,
        )
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        button.bind("<Button-1>", click)

# Run the application
root.mainloop()
