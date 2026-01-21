import math
import tkinter as tk


def przycisk0():
    wyswietlanie.insert(tk.END,"0")
def przycisk1():
    wyswietlanie.insert(tk.END, "1")
def przycisk2():
    wyswietlanie.insert(tk.END, "2")
def przycisk3():
    wyswietlanie.insert(tk.END, "3")
def przycisk4():
    wyswietlanie.insert(tk.END, "4")
def przycisk5():
    wyswietlanie.insert(tk.END, "5")
def przycisk6():
    wyswietlanie.insert(tk.END, "6")
def przycisk7():
    wyswietlanie.insert(tk.END, "7")
def przycisk8():
    wyswietlanie.insert(tk.END, "8")
def przycisk9():
    wyswietlanie.insert(tk.END, "9")
def przyciskprzecinek():
    wyswietlanie.insert(tk.END, ",")
def dodawanie():
    wyswietlanie.insert(tk.END, "+")
def odejmowanie():
    wyswietlanie.insert(tk.END, "-")
def mnozenie():
    wyswietlanie.insert(tk.END, "*")
def iloraz():
    wyswietlanie.insert(tk.END, "/")
def usuwanie():
    wyswietlanie.delete(0,tk.END)
def procent():
    try:
        aktualnawartosc= wyswietlanie.get()
        liczba=float(aktualnawartosc)
        wynik=liczba/100
        wyswietlanie.delete(0,tk.END)
        wyswietlanie.insert(tk.END,str(wynik))
    except ValueError:
        wyswietlanie.delete(0,tk.END)
        wyswietlanie.insert(0,"BŁĄD")
def minus():
    wyswietlanie.insert(tk.END, "-")

def suma():
    try:
        rownanie=wyswietlanie.get()
        wynik=eval(rownanie)
        wyswietlanie.delete(0,tk.END)
        wyswietlanie.insert(tk.END,str(wynik))
    except Exception:
        wyswietlanie.delete(0,tk.END)
        wyswietlanie.insert(0,"BŁĄD")
def pierwiastek():
    try:
        pierwiastek1=wyswietlanie.get()
        liczb=float(pierwiastek1)
        wynik=math.sqrt(liczb)
        wyswietlanie.delete(0,tk.END)
        wyswietlanie.insert(tk.END,str(wynik))
    except ValueError:
        wyswietlanie.delete(0,tk.END)
        wyswietlanie.insert(0,"Tylko dodatnie liczby")

root = tk.Tk()
root.title("Kalkulator")
root.geometry("190x300")
root.resizable(False,False)
root.lift()
root.attributes("-topmost", True)



button0 = tk.Button(root, text="0", command=przycisk0,width=1,height=1,fg="black")
button0.grid(column=1, row=3)

button1 = tk.Button(root, text="1", command=przycisk1,width=1,height=1,fg="black")
button1.grid(column=2, row=3)

button2 = tk.Button(root, text="2", command=przycisk2,width=1,height=1,fg="black")
button2.grid(column=3,row=3)

button3 = tk.Button(root, text="3", command=przycisk3,width=1,height=1,fg="black")
button3.grid(column=1,row=4)

button4 = tk.Button(root, text="4", command=przycisk4,width=1,height=1,fg="black")
button4.grid(column=2, row=4)

button5 = tk.Button(root, text="5", command=przycisk5,width=1,height=1,fg="black")
button5.grid(column=3,row=4)

button6 = tk.Button(root, text="6", command=przycisk6,width=1,height=1,fg="black")
button6.grid(column=1, row=5)

button7 = tk.Button(root, text="7", command=przycisk7,width=1,height=1,fg="black")
button7.grid(column=2,row=5)

button8 = tk.Button(root, text="8", command=przycisk8,width=1,height=1,fg="black")
button8.grid(column=3,row=5)

button9 = tk.Button(root, text="9", command=przycisk9,width=1,height=1,fg="black")
button9.grid(column=2,row=6)

buttonmnozenie = tk.Button(root, text="*", command=mnozenie,width=1,height=1,fg="black")
buttonmnozenie.grid(column=4,row=2)

buttonodejmowanie= tk.Button(root, text="-", command=minus,width=1,height=1,fg="black")
buttonodejmowanie.grid(column=4,row=4)

buttondodawanie= tk.Button(root, text="+", command=dodawanie,width=1,height=1,fg="black")
buttondodawanie.grid(column=4,row=3)

buttoniloraz = tk.Button(root, text="\u00F7", command=iloraz,width=1,height=1,fg="black")
buttoniloraz.grid(column=4,row=5)

buttonprocent= tk.Button(root, text="%", command=procent,width=1,height=1,fg="black")
buttonprocent.grid(column=3,row=2)

buttonusuwanie= tk.Button(root, text="AC", command=usuwanie,width=1,height=1,fg="black")
buttonusuwanie.grid(column=1,row=2)

buttonminus=tk.Button(root, text="+/-", command=minus,width=1,height=1,fg="black")
buttonminus.grid(column=2,row=2)

buttonsuma = tk.Button(root, text="=", command=suma,width=1,height=1,fg="black")
buttonsuma.grid(column=4,row=6)

buttonprzecinek=tk.Button(root, text=",", command=przyciskprzecinek,width=1,height=1,fg="black")
buttonprzecinek.grid(column=1,row=6)

buttonpierwiastek=tk.Button(root, text="\u221A", command=pierwiastek,width=1,height=1,fg="black")
buttonpierwiastek.grid(column=3,row=6)

wyswietlanie=tk.Entry(root,font=("Cosmic Sans MS",15),justify="center")
wyswietlanie.grid(column=1,row=1, ipady=8,columnspan=9,pady=(100,1))


root.mainloop()