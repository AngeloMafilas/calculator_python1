from tkinter import *
import ast

# Initialize the main application window with iPhone-style design
root = Tk()
root.title("Calculator")
root.configure(bg="#000000")
root.resizable(False, False)

# iPhone calculator color scheme
BG_COLOR = "#000000"
DISPLAY_FG = "#ffffff"
NUMBER_BG = "#333333"
NUMBER_HOVER = "#5c5c5c"
OPERATOR_BG = "#ff9f0a"
OPERATOR_HOVER = "#ffb340"
FUNCTION_BG = "#a5a5a5"
FUNCTION_HOVER = "#d4d4d4"

# Global variable to track cursor position in the display entry
cursor_position = 0
current_operator = None


def get_number(num):
    """
    Insert a number at the current cursor position in the display.
    
    Args:
        num: The number (0-9) to insert into the display
    """
    global cursor_position
    display.insert(cursor_position, num)
    cursor_position += 1
    reset_operator_highlight()


def get_operation(operator):
    """
    Insert an operator or mathematical function at the current cursor position.
    
    Args:
        operator: The operator string (e.g., '+', '-', '**', '(')
    """
    global cursor_position
    operator_length = len(operator)
    display.insert(cursor_position, operator)
    cursor_position += operator_length


def clear_all():
    """
    Clear the entire display and reset cursor position to the beginning.
    """
    global cursor_position
    display.delete(0, END)
    cursor_position = 0
    reset_operator_highlight()


def calculate():
    """
    Evaluate the mathematical expression in the display and show the result.
    
    Uses AST (Abstract Syntax Tree) parsing for safe evaluation of expressions.
    If an error occurs (invalid syntax, division by zero, etc.), displays "Error".
    """
    entire_string = display.get()
    try:
        # Parse the expression into an AST node for safe evaluation
        node = ast.parse(entire_string, mode="eval")
        # Compile and evaluate the expression
        result = eval(compile(node, '<string>', 'eval'))
        clear_all()
        display.insert(0, result)
    except Exception:
        # Handle any errors (syntax errors, math errors, etc.)
        clear_all()
        display.insert(0, "Error")
    reset_operator_highlight()


def toggle_sign():
    """
    Toggle between positive and negative for the current number.
    """
    global cursor_position
    entire_string = display.get()
    
    if entire_string and entire_string != "Error":
        try:
            value = float(entire_string)
            clear_all()
            display.insert(0, -value)
            cursor_position = len(str(-value))
        except:
            pass


def percentage():
    """
    Convert the current number to a percentage (divide by 100).
    """
    global cursor_position
    entire_string = display.get()
    
    if entire_string and entire_string != "Error":
        try:
            value = float(entire_string)
            result = value / 100
            clear_all()
            display.insert(0, result)
            cursor_position = len(str(result))
        except:
            pass


def reset_operator_highlight():
    """
    Reset all operator buttons to their default color.
    """
    global current_operator
    if current_operator:
        current_operator['bg'] = OPERATOR_BG
        current_operator = None


def create_button(text, row, col, command, bg_color, fg_color="#ffffff", width=11, columnspan=1, is_operator=False):
    """
    Create an iPhone-style circular button with hover effects.
    
    Args:
        text: Button text to display
        row: Grid row position
        col: Grid column position
        command: Function to call when clicked
        bg_color: Background color tuple (normal, hover)
        fg_color: Text color
        width: Button width
        columnspan: Number of columns to span
        is_operator: Whether this is an operator button
    """
    button = Button(
        root,
        text=text,
        width=width,
        height=5,
        font=("Helvetica Neue", 28),
        bg=bg_color[0],
        fg=fg_color,
        activebackground=bg_color[1],
        activeforeground=fg_color,
        bd=0,
        command=command,
        cursor="hand2",
        relief=FLAT
    )
    
    # Make button more circular for single column buttons
    if columnspan == 1:
        button.grid(row=row, column=col, columnspan=columnspan, padx=6, pady=6, sticky="nsew")
    else:
        button.grid(row=row, column=col, columnspan=columnspan, padx=6, pady=6, sticky="ew")
    
    # Add hover effect
    def on_enter(e):
        button['bg'] = bg_color[1]
    
    def on_leave(e):
        if not (is_operator and button == current_operator):
            button['bg'] = bg_color[0]
    
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    
    return button


# Create and position the display with iPhone styling
display_frame = Frame(root, bg=BG_COLOR)
display_frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)

display = Entry(
    display_frame,
    font=("Helvetica Neue", 70),
    justify=RIGHT,
    bd=0,
    bg=BG_COLOR,
    fg=DISPLAY_FG,
    insertbackground=OPERATOR_BG,
    relief=FLAT,
    highlightthickness=0
)
display.pack(fill=BOTH, expand=True, ipady=10)

# Configure grid weights for perfect circular buttons
for i in range(4):
    root.grid_columnconfigure(i, weight=1, uniform="col")
for i in range(6):
    root.grid_rowconfigure(i, weight=1, uniform="row")

# Row 1: Function buttons
create_button("AC", 1, 0, clear_all, (FUNCTION_BG, FUNCTION_HOVER), "#000000")
create_button("+/-", 1, 1, toggle_sign, (FUNCTION_BG, FUNCTION_HOVER), "#000000")
create_button("%", 1, 2, percentage, (FUNCTION_BG, FUNCTION_HOVER), "#000000")
create_button("÷", 1, 3, lambda: get_operation("/"), (OPERATOR_BG, OPERATOR_HOVER), is_operator=True)

# Row 2: 7, 8, 9, ×
create_button("7", 2, 0, lambda: get_number(7), (NUMBER_BG, NUMBER_HOVER))
create_button("8", 2, 1, lambda: get_number(8), (NUMBER_BG, NUMBER_HOVER))
create_button("9", 2, 2, lambda: get_number(9), (NUMBER_BG, NUMBER_HOVER))
create_button("×", 2, 3, lambda: get_operation("*"), (OPERATOR_BG, OPERATOR_HOVER), is_operator=True)

# Row 3: 4, 5, 6, -
create_button("4", 3, 0, lambda: get_number(4), (NUMBER_BG, NUMBER_HOVER))
create_button("5", 3, 1, lambda: get_number(5), (NUMBER_BG, NUMBER_HOVER))
create_button("6", 3, 2, lambda: get_number(6), (NUMBER_BG, NUMBER_HOVER))
create_button("−", 3, 3, lambda: get_operation("-"), (OPERATOR_BG, OPERATOR_HOVER), is_operator=True)

# Row 4: 1, 2, 3, +
create_button("1", 4, 0, lambda: get_number(1), (NUMBER_BG, NUMBER_HOVER))
create_button("2", 4, 1, lambda: get_number(2), (NUMBER_BG, NUMBER_HOVER))
create_button("3", 4, 2, lambda: get_number(3), (NUMBER_BG, NUMBER_HOVER))
create_button("+", 4, 3, lambda: get_operation("+"), (OPERATOR_BG, OPERATOR_HOVER), is_operator=True)

# Row 5: 0 (wide), ., =
create_button("0", 5, 0, lambda: get_number(0), (NUMBER_BG, NUMBER_HOVER), width=23, columnspan=2)
create_button(".", 5, 2, lambda: get_operation("."), (NUMBER_BG, NUMBER_HOVER))
create_button("=", 5, 3, calculate, (OPERATOR_BG, OPERATOR_HOVER), is_operator=True)

# Add some padding around the window
root.update()
root.geometry(f"400x600")

# Start the GUI event loop
root.mainloop()