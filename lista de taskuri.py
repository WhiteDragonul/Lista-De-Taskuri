import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Lista de taskuri")
root.geometry("800x600")

task_listbox=tk.Listbox(root,width=50)
task_listbox.pack(pady=10)

task_entry=tk.Entry(root,width=50)
task_entry.pack(pady=10)

def adauga_task():
    task=task_entry.get().strip()
    if task:
        tasks=task_listbox.get(0,tk.END)
        if task in tasks:
            messagebox.showwarning("Warning","Taskul exista deja")
            return
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","Introduceti un task")

def sterge_task():
    try:
        index=task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning","Selectati un task pentru a-l sterge")

def marcheaza_task_ca_finalizat():
    try:
        index=task_listbox.curselection()[0]
        task_listbox.itemconfig(index,{'bg':'light green'})
    except IndexError:
        messagebox.showwarning("Warning","Selectati un task pentru a-l marca ca finalizat")

def salveaza_task_dintrun_fisier():
    try:
        with open("taskuri.txt","w") as file:
            tasks=task_listbox.get(0,tk.END)
            for task in tasks:
                file.write(task+"\n")
        messagebox.showinfo("Info","Taskurile au fost salvate in fisier")
    except Exception as e:
        messagebox.showwarning("Warning","Nu s-a putut salva taskurile")

add_task_button=tk.Button(root,text="Adauga task",command=adauga_task)
add_task_button.pack(pady=5)

delete_task_button=tk.Button(root,text="Sterge task",command=sterge_task)
delete_task_button.pack(pady=5)

mark_as_done_button=tk.Button(root,text="Marcheaza task ca finalizat",command=marcheaza_task_ca_finalizat)
mark_as_done_button.pack(pady=5)

save_tasks_button=tk.Button(root,text="Salveaza taskurile",command=salveaza_task_dintrun_fisier)
save_tasks_button.pack(pady=5)

root.mainloop()
