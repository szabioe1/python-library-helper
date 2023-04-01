import tkinter as tk
import subprocess

def getTxtLenght():
    with open("library.txt", "r") as libraryread:
        contents = libraryread.read()
        liblen = len(contents)
    return liblen



def getCommandNames():
    with open("library.txt", "r") as libraryread:
        for line in (line.strip() for line in libraryread):
            library_name = line.split()[2]
            yield library_name


lenght = getTxtLenght()

items = []

for command_name in getCommandNames():
    items.append(command_name)


root = tk.Tk()


checkbox_values = [tk.BooleanVar() for item in items]

checkbox_frame = tk.Frame(root)
checkbox_frame.grid(row=0, column=0, padx=10, pady=10)
for i, item in enumerate(items):
    row = i // 5
    col = i % 5

    checkbox = tk.Checkbutton(checkbox_frame, text=item, variable=checkbox_values[i])
    checkbox.grid(row=row, column=col, padx=5, pady=5)

install_button = tk.Button(root, text="Install", padx=10, pady=5, command=lambda: install_libraries(checkbox_values))
install_button.grid(row=1, column=0, padx=10, pady=10)

uninstall_button = tk.Button(root, text="Uninstall", padx=10, pady=5, command=lambda: uninstall_libraries(checkbox_values))
uninstall_button.grid(row=1, column=1, padx=10, pady=10)


def install_libraries(values):
    for i, value in enumerate(values):
        if value.get():
            library_name = items[i].lower().replace(" ", "-")
            subprocess.run(["pip", "install", library_name])

def uninstall_libraries(values):
    for i, value in enumerate(values):
        if value.get():
            library_name = items[i].lower().replace(" ", "-")
            subprocess.run(["pip", "uninstall", library_name], check=True, input='y\n'.encode())


root.mainloop()


