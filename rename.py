import os

from tkinter import *
from tkinter import filedialog

def select_folder():
    folder_path = filedialog.askdirectory(title="Select folder to rename files")
    folder_path_input.delete(0, END)
    folder_path_input.insert(0, folder_path)

def rename_files():
    folder_path = folder_path_input.get()
    find_name = find_name_input.get()
    replace_name = replace_name_input.get()
    files = os.listdir(folder_path)
    for file in files:
        if find_name in file:
            new_name = file.replace(find_name, replace_name)
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

# create GUI
root = Tk()
root.title("Rename Master")

folder_path_label = Label(root, text="Folder:")
folder_path_label.grid(row=0, column=0)

folder_path_input = Entry(root, width=30)
folder_path_input.grid(row=0, column=1)

select_folder_button = Button(root, text="Select", command=select_folder)
select_folder_button.grid(row=0, column=2)

find_name_label = Label(root, text="Find:")
find_name_label.grid(row=1, column=0)

find_name_input = Entry(root, width=30)
find_name_input.grid(row=1, column=1)

replace_name_label = Label(root, text="Replace:")
replace_name_label.grid(row=2, column=0)

replace_name_input = Entry(root, width=30)
replace_name_input.grid(row=2, column=1)

rename_button = Button(root, text="Rename all", command=rename_files)
rename_button.grid(row=1, column=2, rowspan=2)

root.mainloop()
