from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Denomination Counter")
root.geometry("500x400")
root.config(bg="lightblue")

def calculator():
    try:
        amount = int(entry.get())

        n1000 = amount //1000
        amount = amount % 1000

        n500 = amount //500
        amount = amount % 500

        n100 = amount //100

        result.config(
            text = f"$1000 notes: {n1000}\n"
                   f"$500 notes: {n500}\n"
                   f"$100 notes: {n100}\n"
        )
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

Label(root, text="Denomination Counter",
      font=("Arial", 20), bg="Magenta").pack()

entry = Entry(root)
entry.pack(pady=10)

Button(root, text="Calculate", command=calculator,
       bg="violet", fg="orange").pack(pady=10)

result =  Label(root, text=" ",
                bg="lightblue", font=("Arial", 15))
result.pack(pady=10)

root.mainloop()