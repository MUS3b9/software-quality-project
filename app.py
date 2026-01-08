import tkinter as tk
from tkinter import messagebox


def login(username, password):
    if not username or not password:
        return "Fields cannot be empty"

    if username == "admin" and password == "1234":
        return "Login successful"

    return "Invalid credentials"


def run_gui():
    def handle_login():
        user = entry_username.get()
        pwd = entry_password.get()
        result = login(user, pwd)

        if result == "Login successful":
            messagebox.showinfo("Success", result)
        else:
            messagebox.showerror("Error", result)

    window = tk.Tk()
    window.title("Login System")
    window.geometry("300x200")

    tk.Label(window, text="Username").pack(pady=5)
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="Password").pack(pady=5)
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    tk.Button(window, text="Login", command=handle_login).pack(pady=15)

    window.mainloop()


# ✅ الواجهة تشتغل فقط هنا
if __name__ == "__main__":
    run_gui()
