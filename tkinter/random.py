import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

screen = Tk()
screen.title("Random Number Generator")

screen.geometry("450x400")
rnum = random.randint(1,255)

label = Label(
    screen,
    text = "Click the button bellow to generate a random number",
    font = ("Times New Roman", 16))

label.pack(ipadx = 10, ipady = 10)
style = Style()

style.configure('TButton', font =
               ('calibri', 20, 'bold'),
                    borderwidth = '4')
 
style.map('TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])


def rand_num():
    global rnum
    msg = messagebox.showinfo("Hasil Angka Random", str(rnum))
    rnum = random.randint(1,255)


tombol = Button(screen, text = "Generate Random Number", command = rand_num)
tombol.place(x = 80,y = 130)

leave = Button(screen, text = "Exit", command = screen.destroy)
leave.place(x = 150, y = 200)
screen.mainloop()
