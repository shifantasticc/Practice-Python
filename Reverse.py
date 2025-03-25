import tkinter as tk

def reverse_number():
    num = entry.get()
    reversed_num = num[::-1]
    result_label.config(text="Reversed Number: " + reversed_num)

root = tk.Tk()
root.title("Number Reverser")
root.geometry("300x200")

entry_label = tk.Label(root, text="Enter a number:")
entry_label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

reverse_button = tk.Button(root, text="Reverse", command=reverse_number)
reverse_button.pack(pady=10)

result_label = tk.Label(root, text="Reversed Number: ")
result_label.pack(pady=5)

root.mainloop()
