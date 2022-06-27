from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Perhitungan Resistor")
root.config(background ="lightblue")

w = 520
h = 325

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pos_top = int(screen_height/2 - h/2)
pos_right = int(screen_width/2 - w/2)

root.geometry(f"{w}x{h}+{pos_right}+{pos_top-25}")

#judul
l1 = Label(text="Masukkan warna Gelang ",bg ="lightblue", font="normal 30")
l1.grid(row=0, column=0, columnspan=4, pady=20, padx=30)
  

#bagian button
b1 = Button(text = "Gelang pertama", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", width=20)
b1.grid(row=1, column =0)

b2 = Button(text = "Gelang kedua", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", width=20)
b2.grid(row=2, column =0)

b3 = Button(text = "Gelang ketiga", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", width=20)
b3.grid(row=3, column =0)

b4 = Button(text = "Gelang keempat", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", width=20)
b4.grid(row=4, column =0)

e1, e2, e3, e4 = Entry(root, font=('Arial 15'), justify=CENTER), Entry(root, font=('Arial 15'), justify=CENTER), Entry(root, font=('Arial 15'), justify=CENTER), Entry(root, font=('Arial 15'), justify=CENTER)
e1.grid(row=1, column=3)
e2.grid(row=2, column=3)
e3.grid(row=3, column=3)
e4.grid(row=4, column=3)

a = ""
b = ""
c = ""
d = ""

#fungsi
def total():
    global a, b, c, d
    t1 = e1.get()
    t2 = e2.get()
    t3 = e3.get()
    t4 = e4.get()

    col_lst1 = ["hitam", "coklat", "merah", "orange", "kuning", "hijau", "biru", "ungu", "abu-abu", "putih"]
    col_lst2 = ["emas", "perak"]
    if (t1) in col_lst1:
        a = f"{col_lst1.index(t1)}"
    else:
        a = ""
    
    if (t2) in col_lst1:
        b = f"{col_lst1.index(t2)}"
    else:
        b = ""

    if (t3) in col_lst1:
        c = f"{10**(col_lst1.index(t3))}"
    elif (t3) in col_lst2:
        c = f"{10**(-(col_lst2.index(t3)+1))}"
    else:
        c = ""

    if (t4) in col_lst2:
        d = f"{5*((col_lst2.index(t4))+1)}"
    elif (t4) == "tak berwarna":
        d = "20"
    else:
        d = ""

    try:
        if d != "":
            ab = int(a+b)
            rumus = f"{ab} × {c} Ω ± {d}%"
            l2.config(text=rumus)
        else:
            rumus = f"{ab} × {c} Ω"
            l2.config(text=rumus)            
    except:
        messagebox.showinfo("Isian", "Isi dengan benar")

l2 = Label (text="", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", width=20)
l2.grid(row=5, column =3)

b1 = Button(text = "Hasil", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", width=20,command=total)
b1.grid(row=5, column =0)


root.mainloop()