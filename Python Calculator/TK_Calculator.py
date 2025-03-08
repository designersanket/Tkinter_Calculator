import tkinter as tk

def click_button(number):
    output_screen.insert(tk.END, number)

def clear_screen():
    output_screen.delete(0, tk.END)

def delet_one():
    current_no = output_screen.get()
    if current_no:
        output_screen.delete(len(current_no) - 1, tk.END)

def calculate():
    try:
        result = eval(output_screen.get())
        output_screen.delete(0, tk.END)
        output_screen.insert(tk.END, str(result))
    except Exception:
        output_screen.delete(0, tk.END)
        output_screen.insert(tk.END, "ERROR..!")

def insert_bracket(bracket):
    output_screen.insert(tk.END, bracket)

root = tk.Tk()
root.title("Python Calculator")
root.geometry("400x400")

# Output Screen
output_screen = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
output_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Buttons (Numbers)
button7 = tk.Button(root, text="7", font=("Arial", 10), bg="light gray",width=4, height=2, command=lambda: click_button("7"), bd=5, relief="ridge", highlightthickness=0)
button7.grid(row=2, column=0, padx=5, pady=5)

button8 = tk.Button(root, text="8", font=("Arial", 10), bg="light gray",width=4, height=2, command=lambda: click_button("8"), bd=5, relief="ridge", highlightthickness=0)
button8.grid(row=2, column=1, padx=5, pady=5)

button9 = tk.Button(root, text="9", font=("Arial", 10),bg="light gray", width=4, height=2, command=lambda: click_button("9"), bd=5, relief="ridge", highlightthickness=0)
button9.grid(row=2, column=2, padx=5, pady=5)

button4 = tk.Button(root, text="4", font=("Arial", 10), bg="light gray",width=4, height=2, command=lambda: click_button("4"), bd=5, relief="ridge", highlightthickness=0)
button4.grid(row=3, column=0, padx=5, pady=5)

button5 = tk.Button(root, text="5", font=("Arial", 10),bg="light gray", width=4, height=2, command=lambda: click_button("5"), bd=5, relief="ridge", highlightthickness=0)
button5.grid(row=3, column=1, padx=5, pady=5)

button6 = tk.Button(root, text="6", font=("Arial", 10), bg="light gray",width=4, height=2, command=lambda: click_button("6"), bd=5, relief="ridge", highlightthickness=0)
button6.grid(row=3, column=2, padx=5, pady=5)

button1 = tk.Button(root, text="1", font=("Arial", 10), bg="light gray",width=4, height=2, command=lambda: click_button("1"), bd=5, relief="ridge", highlightthickness=0)
button1.grid(row=4, column=0, padx=5, pady=5)

button2 = tk.Button(root, text="2", font=("Arial", 10), bg="light gray",width=4, height=2, command=lambda: click_button("2"), bd=5, relief="ridge", highlightthickness=0)
button2.grid(row=4, column=1, padx=5, pady=5)

button3 = tk.Button(root, text="3", font=("Arial", 10), bg="light gray",width=4, height=2, command=lambda: click_button("3"), bd=5, relief="ridge", highlightthickness=0)
button3.grid(row=4, column=2, padx=5, pady=5)

button_0 = tk.Button(root, text="0", font=("Arial", 10),bg="light gray", width=4, height=2, command=lambda: click_button("0"), bd=5, relief="ridge", highlightthickness=0)
button_0.grid(row=5, column=1, padx=5, pady=5)

# Arithmetic operations
button_div = tk.Button(root, text="/", font=("Arial", 10), bg="light gray",fg="green",width=4, height=2, command=lambda: click_button("/"), bd=5, relief="ridge", highlightthickness=0)
button_div.grid(row=1, column=3, padx=5, pady=5)

button_mul = tk.Button(root, text="*", font=("Arial", 10), bg="light gray",fg="green",width=4, height=2, command=lambda: click_button("*"), bd=5, relief="ridge", highlightthickness=0)
button_mul.grid(row=2, column=3, padx=5, pady=5)

button_sub = tk.Button(root, text="-", font=("Arial", 10), bg="light gray",fg="green",width=4, height=2, command=lambda: click_button("-"), bd=5, relief="ridge", highlightthickness=0)
button_sub.grid(row=3, column=3, padx=5, pady=5)

button_add = tk.Button(root, text="+", font=("Arial", 10), bg="light gray",fg="green",width=4, height=2, command=lambda: click_button("+"), bd=5, relief="ridge", highlightthickness=0)
button_add.grid(row=4, column=3, padx=5, pady=5)

# Brackets
# Brackets
button_open_paran = tk.Button(root, text="(", font=("Arial", 10), bg="light gray",fg="green",width=4, height=2, command=lambda: insert_bracket("("), bd=5, relief="ridge", highlightthickness=0)
button_open_paran.grid(row=1, column=1, padx=5, pady=5)

button_close_paran = tk.Button(root, text=")", font=("Arial", 10),bg="light gray",fg="green", width=4, height=2, command=lambda: insert_bracket(")"), bd=5, relief="ridge", highlightthickness=0)
button_close_paran.grid(row=1, column=2, padx=5, pady=5)

# Modulo
button_modulo = tk.Button(root, text="%", font=("Arial", 10), bg="light gray",fg="green",width=4, height=2, command=lambda: click_button("%"), bd=5, relief="ridge", highlightthickness=0)
button_modulo.grid(row=1, column=0, padx=5, pady=5)  


# Equal Button
button_eql = tk.Button(root, text="=", font=("Arial", 10), bg="light gray",fg="green",width=4, height=2, command=calculate, bd=5, relief="ridge", highlightthickness=0)
button_eql.grid(row=5, column=3, padx=5, pady=5)

button_dot = tk.Button(root, text=".", font=("Arial", 10),bg="light gray", width=4, height=2, command=lambda: click_button("."), bd=5, relief="ridge", highlightthickness=0)
button_dot.grid(row=5, column=2, padx=5, pady=5)

button_backspace = tk.Button(root, text="⌫", font=("Arial", 10), bg="light gray",fg="green",width=4, height=2, command=delet_one, bd=5, relief="ridge", highlightthickness=0)
button_backspace.grid(row=5, column=0, padx=5, pady=5)

button_clear = tk.Button(root, text="C", font=("Arial", 10), bg="light gray", fg="red",width=4, height=2, command=clear_screen, bd=5, relief="ridge", highlightthickness=0)
button_clear.grid(row=1, column=0, padx=5, pady=5)


root.mainloop()
