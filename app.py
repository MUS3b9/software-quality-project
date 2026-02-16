import tkinter as tk
from tkinter import messagebox


def login(username, password):
    if not username or not password:
        return "Fields cannot be empty"

    if username == "admin" and password == "1234":
        return "Login successful"

    return "Invalid credentials"


def run_gui():
    window = tk.Tk()
    window.title("Login System")
    window.geometry("300x200")

    tk.Label(window, text="Username").pack()
    entry_user = tk.Entry(window)
    entry_user.pack()

    tk.Label(window, text="Password").pack()
    entry_pass = tk.Entry(window, show="*")
    entry_pass.pack()

    def submit():
        result = login(entry_user.get(), entry_pass.get())
        if result == "Login successful":
            messagebox.showinfo("Success", result)
        else:
            messagebox.showerror("Error", result)

    tk.Button(window, text="Login", command=submit).pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    run_gui()
