import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import os

# Funções de Utilidade
def log_login(username):
    with open("login_log.txt", "a") as f:
        f.write(f"{username} logged in at {datetime.now()}\n")

def clear_monthly_log():
    log_file = "login_log.txt"
    if os.path.exists(log_file):
        os.remove(log_file)

# Limpar log mensalmente (simulação)
clear_monthly_log()

# Funções de Login/Cadastro
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    
    with open("login.txt", "a") as file:
        file.write(f"{username},{password}\n")
    messagebox.showinfo("Registration", "Registration successful!")
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

def login_user():
    username = entry_username.get()
    password = entry_password.get()
    
    with open("login.txt", "r") as file:
        users = file.readlines()
    
    for user in users:
        stored_username, stored_password = user.strip().split(',')
        if stored_username == username and stored_password == password:
            log_login(username)
            open_task_manager(username)
            return
    
    messagebox.showerror("Login Failed", "Invalid username or password")

class TaskManager:
    def __init__(self, username):
        self.username = username
        self.conn = sqlite3.connect('tasks.db')
        self.create_table()

        self.window = tk.Tk()
        self.window.title(f"Task Manager - {self.username}")

        self.setup_ui()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.conn.commit()

    def setup_ui(self):
        self.title_entry = tk.Entry(self.window, width=50)
        self.title_entry.pack()

        self.description_entry = tk.Entry(self.window, width=50)
        self.description_entry.pack()

        tk.Button(self.window, text="Add Task", command=self.add_task).pack()
        tk.Button(self.window, text="Update Task", command=self.update_task).pack()
        tk.Button(self.window, text="Delete Task", command=self.delete_task).pack()
        tk.Button(self.window, text="View Tasks", command=self.view_tasks).pack()

        self.tasks_listbox = tk.Listbox(self.window, width=50, height=10)
        self.tasks_listbox.pack()

        self.window.mainloop()

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()

        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
        self.conn.commit()

        messagebox.showinfo("Success", "Task added successfully")
        self.view_tasks()

    def update_task(self):
        try:
            selected_task = self.tasks_listbox.get(self.tasks_listbox.curselection())
            task_id = selected_task.split(" ")[0]
            title = self.title_entry.get()
            description = self.description_entry.get()

            cursor = self.conn.cursor()
            cursor.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?', (title, description, task_id))
            self.conn.commit()

            messagebox.showinfo("Success", "Task updated successfully")
            self.view_tasks()
        except:
            messagebox.showerror("Error", "No task selected")

    def delete_task(self):
        try:
            selected_task = self.tasks_listbox.get(self.tasks_listbox.curselection())
            task_id = selected_task.split(" ")[0]

            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            self.conn.commit()

            messagebox.showinfo("Success", "Task deleted successfully")
            self.view_tasks()
        except:
            messagebox.showerror("Error", "No task selected")

    def view_tasks(self):
        self.tasks_listbox.delete(0, tk.END)

        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()

        for task in tasks:
            self.tasks_listbox.insert(tk.END, f"{task[0]} - {task[1]}: {task[2]}")


def open_task_manager(username):
    login_window.destroy()
    TaskManager(username)

# Interface de Login
login_window = tk.Tk()
login_window.title("Login/Cadastro")

tk.Label(login_window, text="Username:").pack()
entry_username = tk.Entry(login_window)
entry_username.pack()

tk.Label(login_window, text="Password:").pack()
entry_password = tk.Entry(login_window, show="*")
entry_password.pack()

tk.Button(login_window, text="Login", command=login_user).pack()
tk.Button(login_window, text="Register", command=register_user).pack()

login_window.mainloop()

