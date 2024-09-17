import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

root = tk.Tk()  # Create the main window
root.title("Simple GUI")

label = tk.Label(root, text="Welcome!")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)

root.mainloop()  # Run the application
