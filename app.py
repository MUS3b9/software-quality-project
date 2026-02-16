import tkinter as tk
from tkinter import messagebox
import json


# ===== Data =====
def load_users():
    with open("users.json", "r") as f:
        return json.load(f)


def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=2)


# ===== Logic =====
def login(username, password):
    if not username or not password:
        return "Fields cannot be empty"

    for user in load_users():
        if user["username"] == username and user["password"] == password:
            return "Login successful"

    return "Invalid credentials"


def signup(username, password):
    if not username or not password:
        return "Fields cannot be empty"

    users = load_users()
    for user in users:
        if user["username"] == username:
            return "User already exists"

    users.append({"username": username, "password": password})
    save_users(users)
    return "Account created successfully"


# ===== GUI =====
window = tk.Tk()
window.title("Login System")
window.geometry("300x300")

mode = tk.StringVar(value="login")


def submit():
    user = entry_user.get()
    pwd = entry_pass.get()

    if mode.get() == "login":
        result = login(user, pwd)
    else:
        result = signup(user, pwd)

    if "successful" in result:
        messagebox.showinfo("Success", result)
    else:
        messagebox.showerror("Error", result)


def switch_to_signup():
    mode.set("signup")
    title.config(text="Create Account")
    btn_submit.config(text="Sign Up")


def switch_to_login():
    mode.set("login")
    title.config(text="Login")
    btn_submit.config(text="Login")


title = tk.Label(window, text="Login", font=("Arial", 14))
title.pack(pady=10)

tk.Label(window, text="Username").pack()
entry_user = tk.Entry(window)
entry_user.pack()

tk.Label(window, text="Password").pack()
entry_pass = tk.Entry(window, show="*")
entry_pass.pack()

btn_submit = tk.Button(window, text="Login", command=submit)
btn_submit.pack(pady=5)

tk.Button(window, text="Create Account", command=switch_to_signup).pack()
tk.Button(window, text="Back to Login", command=switch_to_login).pack(pady=5)

window.mainloop()
