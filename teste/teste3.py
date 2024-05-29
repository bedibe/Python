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

# Limpar log mensalmente
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
        stored
