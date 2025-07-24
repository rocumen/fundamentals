import tkinter as tk

# Function to evaluate the expression and show the result
def calculate():
    try:
        # Get the math expression from the entry field
        expression = entry.get()
        # Use eval to calculate the result (e.g., "3+2" becomes 5)
        result = str(eval(expression))
        # Clear the entry field and show the result
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        # Show "Error" if something goes wrong (like invalid input)
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create the entry field where the user will see the input/output
entry = tk.Entry(window, width=30, font=("Arial", 16), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# List of button labels to display
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create the buttons and place them in a grid
row = 1
col = 0

# Loop through each label and create a button
for label in button_labels:
    # This function will run when the button is clicked
    def on_click(value=label):
        if value == '=':
            calculate()  # Call the calculate function
        else:
            # Insert the button value into the entry field
            entry.insert(tk.END, value)

    # Create the button
    btn = tk.Button(window, text=label, width=5, height=2,
                    font=("Arial", 14), command=on_click)
    btn.grid(row=row, column=col, padx=5, pady=5)

    # Move to the next column
    col += 1
    if col > 3:
        # Go to the next row after 4 columns
        col = 0
        row += 1

# Add a clear button at the bottom
clear_button = tk.Button(window, text="Clear", width=22, height=2,
                         font=("Arial", 14), command=clear)
clear_button.grid(row=row, column=0, columnspan=4, pady=10)

# Start the Tkinter event loop (show the window)
window.mainloop()
