import tkinter as tk       # Import Tkinter library for creating GUI
import math               # Import math module for scientific functions

expression = ""            # Variable to store the current mathematical expression

def click(event):          # Function executed whenever a calculator button is clicked
    global expression      # Allows modification of the global variable inside the function

    text = event.widget.cget("text")   # Get the text written on the clicked button

    if text == "=":                    # If '=' button is pressed
        try:
            result = str(eval(expression))   # Evaluate the expression using eval()
            screen_var.set(result)           # Display the result on the calculator screen

            # Save calculation history in a file
            with open("history.txt", "a") as f:
                f.write(expression + " = " + result + "\n")

            expression = result              # Store result so user can continue calculations

        except:                              # If evaluation fails
            screen_var.set("Error")          # Show error on screen
            expression = ""                  # Reset expression

    elif text == "C":                        # If clear button is pressed
        expression = ""                      # Clear stored expression
        screen_var.set("")                   # Clear the display

    elif text == "⌫":                        # Backspace button
        expression = expression[:-1]         # Remove the last character from expression
        screen_var.set(expression)           # Update the display

    elif text == "π":                        # Pi button
        expression += str(math.pi)           # Add value of pi to expression
        screen_var.set(expression)           # Show updated expression

    elif text == "e":                        # Euler constant button
        expression += str(math.e)            # Add value of e
        screen_var.set(expression)

    elif text == "sin":                      # Sine function button
        expression = str(math.sin(float(expression)))   # Calculate sine of number
        screen_var.set(expression)

    elif text == "cos":                      # Cosine function button
        expression = str(math.cos(float(expression)))   # Calculate cosine
        screen_var.set(expression)

    elif text == "tan":                      # Tangent function button
        expression = str(math.tan(float(expression)))   # Calculate tangent
        screen_var.set(expression)

    elif text == "√":                        # Square root button
        expression = str(math.sqrt(float(expression)))  # Calculate square root
        screen_var.set(expression)

    elif text == "log":                      # Log base 10 button
        expression = str(math.log10(float(expression))) # Calculate log base 10
        screen_var.set(expression)

    elif text == "ln":                       # Natural logarithm button
        expression = str(math.log(float(expression)))   # Calculate natural log
        screen_var.set(expression)

    elif text == "x!":                       # Factorial button
        expression = str(math.factorial(int(float(expression)))) # Calculate factorial
        screen_var.set(expression)

    elif text == "^":                        # Power button
        expression += "**"                   # Python uses ** for exponentiation
        screen_var.set(expression)

    else:                                    # If normal number/operator button
        expression += text                   # Add button text to expression
        screen_var.set(expression)           # Update display

def view_history():                          # Function to display calculation history
    win = tk.Toplevel(root)                  # Create a new window
    win.title("Calculation History")         # Set window title
    win.geometry("300x300")                  # Set window size

    text = tk.Text(win)                      # Create text widget to show history
    text.pack(fill="both", expand=True)      # Make text widget fill the window

    try:
        with open("history.txt", "r") as f:  # Open history file in read mode
            text.insert(tk.END, f.read())    # Display file content in text widget
    except:
        text.insert(tk.END, "No history available")  # Show message if file doesn't exist

root = tk.Tk()                               # Create main calculator window
root.title("Scientific Calculator")          # Set window title
root.geometry("350x520")                     # Set window size
root.configure(bg="#8B0000")                 # Set background color (dark red)

root.resizable(False, False)                 # Disable window resizing and maximize option

screen_var = tk.StringVar()                  # Variable used to control display text

# Entry widget used as calculator display screen
screen = tk.Entry(
    root,
    textvariable=screen_var,                 # Connect entry field to variable
    font="Arial 20",                         # Set font size
    bd=8,                                    # Border thickness
    relief=tk.RIDGE,                         # Border style
    justify='right'                          # Align numbers to the right
)

screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)  # Place screen in window with padding

# Disable keyboard typing so user can only use buttons
screen.bind("<Key>", lambda e: "break")

# Button layout using rows and columns
buttons = [

["7","8","9","/","sin"],
["4","5","6","*","cos"],
["1","2","3","-","tan"],
["0",".","=","+","√"],
["π","e","log","ln","^"],
["x!","⌫","C","",""]     # Empty cells keep the grid aligned

]

# Frame that will contain all calculator buttons
button_frame = tk.Frame(root, bg="#8B0000")
button_frame.pack(expand=True, fill="both")

# Loop through each row in the button layout
for r, row in enumerate(buttons):

    # Loop through each button in that row
    for c, btn_text in enumerate(row):

        if btn_text == "":                   # Skip empty spaces
            continue

        # Create button widget
        btn = tk.Button(
            button_frame,
            text=btn_text,                   # Text shown on button
            font="Arial 14",                 # Button font size
            bg="#FF4C4C",                    # Button background color
            fg="white"                       # Button text color
        )

        # Place button in grid layout
        btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

        # Bind button click event to click() function
        btn.bind("<Button-1>", click)

# Make rows expand equally
for i in range(6):
    button_frame.rowconfigure(i, weight=1)

# Make columns expand equally
for j in range(5):
    button_frame.columnconfigure(j, weight=1)

# Button to open calculation history window
history_btn = tk.Button(
    root,
    text="View History",                     # Button label
    font="Arial 14",                         # Font size
    bg="black",                              # Background color
    fg="white",                              # Text color
    command=view_history                     # Function executed when clicked
)
history_btn.pack(fill="x", padx=10, pady=10) # Place button at bottom of window

root.mainloop()                              # Start the GUI event loop so window stays open
