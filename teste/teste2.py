def main_screen():
    main_root = tk.Tk()
    main_root.title("Task Manager")

    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  task TEXT,
                  description TEXT)''')
    conn.commit()

    def add_task():
        task = entry_task.get()
        description = entry_description.get()
        c.execute("INSERT INTO tasks (task, description) VALUES (?, ?)", (task, description))
        conn.commit()
        refresh_tasks()
    
    def delete_task():
        selected_task = task_listbox.get(task_listbox.curselection())
        task_id = selected_task.split(":")[0]
        c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        refresh_tasks()

    def update_task():
        selected_task = task_listbox.get(task_listbox.curselection())
        task_id = selected_task.split(":")[0]
        task = entry_task.get()
        description = entry_description.get()
        c.execute("UPDATE tasks SET task=?, description=? WHERE id=?", (task, description, task_id))
        conn.commit()
        refresh_tasks()
    
    def refresh_tasks():
        task_listbox.delete(0, tk.END)
        c.execute("SELECT * FROM tasks")
        for row in c.fetchall():
            task_listbox.insert(tk.END, f"{row[0]}: {row[1]} - {row[2]}")

    tk.Label(main_root, text="Task").grid(row=0, column=0)
    entry_task = tk.Entry(main_root)
    entry_task.grid(row=0, column=1)

    tk.Label(main_root, text="Description").grid(row=1, column=0)
    entry_description = tk.Entry(main_root)
    entry_description.grid(row=1, column=1)

    tk.Button(main_root, text="Add Task", command=add_task).grid(row=2, column=0)
    tk.Button(main_root, text="Delete Task", command=delete_task).grid(row=2, column=1)
    tk.Button(main_root, text="Update Task", command=update_task).grid(row=3, column=0)
    tk.Button(main_root, text="Refresh Tasks", command=refresh_tasks).grid(row=3, column=1)

    task_listbox = tk.Listbox(main_root)
    task_listbox.grid(row=4, column=0, columnspan=2)

    refresh_tasks()
    main_root.mainloop()
