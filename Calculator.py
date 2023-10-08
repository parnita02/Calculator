import tkinter as tk
import math
import re

    
def calculate():
    try:
        expression = entry.get()
        expression = re.sub(r'√(\d+)', r'math.sqrt(\1)', expression)
        expression = expression.replace('^', '**')
        result = eval(expression)
        result_label.config(text="Result: " + str(result))

    except Exception as e:
        result_label.config(text="Error")


def delete_text():
    entry.delete(len(entry.get()) - 1)

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result: ")


def append_text(text):
     if text == 'C':
        clear()
     elif text == '=':
         calculate()
     elif text == 'Dlt':
        delete_text() 
     else:
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + text)


window = tk.Tk()
window.title("Arithmetic Calculator")
window.configure(bg="black")


entry_font = ("Helvetica", 16)
entry = tk.Entry(window, font=entry_font, bg="black", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")  


result_font = ("Helvetica", 16)
result_label = tk.Label(window, text="Result: ", font=result_font, bg="black", fg="white")
result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

button_font = ("Helvetica", 14, "bold")

button_bg_color = "black"
button_fg_color = "white"
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')', '√', '^',
    'Dlt','C'
]

row, col = 2, 0
for button_text in buttons:
    if button_text in {'=', 'C', '√', '^'}:
        button_fg_color = "white"
    else:
        button_fg_color = "white"

   
    button = tk.Button(window, text=button_text, width=5, height=2, command=lambda text=button_text: append_text(text), bg="#333333", fg=button_fg_color, relief="raised", font=button_font)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1


calculate_button = tk.Button(window, text="Calculate", width=5, height=2, command=calculate, bg="#333333", fg="white", relief="raised", font=button_font)
calculate_button.grid(row=7, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")


for i in range(8):
    window.grid_rowconfigure(i, weight=1)


for i in range(4):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
