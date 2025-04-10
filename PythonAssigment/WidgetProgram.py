import tkinter as tk
from tkinter import ttk, Menu, messagebox

def submit_form():
    print("Form Submitted!")
    messagebox.showinfo("Form Info", "Form Submitted")

def on_exit():
    root.quit()

root = tk.Tk()
root.title("User Form")
root.geometry("400x300")
root.configure(bg="purple")

form_frame = tk.LabelFrame(root, text="User Information", bg="pink", fg="black", font=("Arial", 10, "bold"))
form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

tk.Label(form_frame, text="Name:", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(form_frame, font=("Arial", 10))
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Gender:", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
gender_var = tk.StringVar()
tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male").grid(row=1, column=1, sticky="w")
tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female").grid(row=1, column=2, sticky="w")

tk.Label(form_frame, text="Age:", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky="w")
age_spinbox = tk.Spinbox(form_frame, from_=1, to=100, font=("Arial", 10))
age_spinbox.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Country:", font=("Arial", 10, "bold")).grid(row=3, column=0, padx=5, pady=5, sticky="w")
country_listbox = tk.Listbox(form_frame, height=3)
for country in ["India","South Korea", "Italy", "USA", "UK", "Germany"]:
    country_listbox.insert(tk.END, country)
country_listbox.grid(row=3, column=1, padx=5, pady=5)

agree_var = tk.BooleanVar()
agreement = tk.Checkbutton(form_frame, text="I Agree to the Terms", variable=agree_var, font=("Arial", 10))
agreement.grid(row=4, columnspan=2, pady=5)

submit_btn = ttk.Button(root, text="Submit", command=submit_form)
submit_btn.pack(pady=10)
root.mainloop()
