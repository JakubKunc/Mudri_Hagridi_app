from tkinter import *
from data import *
from tkinter import colorchooser
from tkinter.messagebox import *
import webbrowser

aktualni_otazka = 0
odpoved = 0
spravne_odpovedi_pocet = 0
spatne_odpovedi_pocet = 0

a = 0

def Past(*NT):
    pass

def Start(*args):
    spustit.destroy()
    nastaveni.destroy()
    window.bind("<S>", Past)
    window.bind("<s>", Past)
    window.bind(1, Past)
    window.bind("<N>", Past)
    window.bind("<n>", Past)
    window.bind(2, Past)
    Okno()

def NaHru(*args):
    platno.destroy()
    na_hru.destroy()
    Hra()

def Nastaveni(*args):
    global nastavenia
    global nastavenib
    global cistabarva
    global spinavabarva
    global ramovabarva
    global zednibarva
    global barva1
    global barva2
    global znastaveni
    global jazyky
    global jazyky_command
    global barva
    global mluv

    spustit.destroy()
    nastaveni.destroy()
    window.bind("<s>", Past)
    window.bind("<S>", Past)
    window.bind(1, Past)
    window.bind("<n>", Past)
    window.bind("<N>", Past)
    window.bind(2, Past)
    nastavenia = Frame(window, bg=barvy[1])
    nastavenia.pack()
    barva = Label(nastavenia, text=obar[a], bg=barvy[1], fg=barvy[0], padx=10, pady=15)
    barva.pack()
    cistabarva = Button(nastavenia, text=cisba[a], command=CistaBarva, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], padx=10, pady=10)
    cistabarva.pack()
    spinavabarva = Button(nastavenia, text=spinba[a], command=SpinavaBarva, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], padx=10, pady=10)
    spinavabarva.pack()
    ramovabarva = Button(nastavenia, text=ramba[a], command=RamovaBarva, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], padx=10, pady=10)
    ramovabarva.pack()
    zednibarva = Button(nastavenia, text=zdiba[a], command=ZedniBarva, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], padx=10, pady=10)
    zednibarva.pack()
    barva1 = Button(nastavenia, text=bar1[a], command=Barva1, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], padx=10, pady=10)
    barva1.pack()
    barva2 = Button(nastavenia, text=bar2[a], command=Barva2, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], padx=10, pady=10)
    barva2.pack()
    nastavenib = Frame(window, bg=barvy[1])
    nastavenib.pack()
    mluv = Label(nastavenia, text=mluvi[a], bg=barvy[1], fg=barvy[0], padx=10, pady=15)
    mluv.pack()
    jazyky = [cestina[a], anglictina[a], nemcina[a], moravstina[a]]
    jazyky_command = [Cestina, Anglictina, Nemcina, Moravstina]
    for i in range(len(jazyky)):
        jzyk = Button(nastavenib, text=jazyky[i], bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], command=jazyky_command[i], padx=10, pady=10)
        jzyk.pack()
    window.bind("<b>", NaUwod)
    window.bind("<B>", NaUwod)
    znastaveni = Button(window, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], text=znas[a], command=NaUwod, padx=10, pady=10)
    znastaveni.place(x=window.winfo_screenwidth()/2, y=window.winfo_screenheight()/1.1, anchor=CENTER)

def CistaBarva():
    barvy_okna.pop(0)
    barvy_okna.insert(0,colorchooser.askcolor()[1])

def SpinavaBarva():
    barvy_okna.pop(1)
    barvy_okna.insert(1,colorchooser.askcolor()[1])

def RamovaBarva():
    barvy_okna.pop(2)
    barvy_okna.insert(2,colorchooser.askcolor()[1])

def ZedniBarva():
    barvy_okna.pop(3)
    barvy_okna.insert(3,colorchooser.askcolor()[1])

def Barva1():
    global nastavenib
    barvy.pop(0)
    barvy.insert(0,colorchooser.askcolor()[1])
    barva.config(fg=barvy[0])
    cistabarva.config(fg=barvy[0], activeforeground=barvy[0])
    spinavabarva.config(fg=barvy[0], activeforeground=barvy[0])
    ramovabarva.config(fg=barvy[0], activeforeground=barvy[0])
    zednibarva.config(fg=barvy[0], activeforeground=barvy[0])
    barva1.config(fg=barvy[0], activeforeground=barvy[0])
    barva2.config(fg=barvy[0], activeforeground=barvy[0])
    mluv.config(fg=barvy[0])
    nastavenib.destroy()
    nastavenib = Frame(window, bg=barvy[1])
    nastavenib.pack()
    for i in range(len(jazyky)):
        jzyk = Button(nastavenib, text=jazyky[i], bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], command=jazyky_command[i], padx=10, pady=10)
        jzyk.pack()
    znastaveni.config(fg=barvy[0], activeforeground=barvy[0])

def Barva2():
    global nastavenib
    barvy.pop(1)
    barvy.insert(1,colorchooser.askcolor()[1])
    barva.config(bg=barvy[1])
    cistabarva.config(bg=barvy[1], activebackground=barvy[1])
    spinavabarva.config(bg=barvy[1], activebackground=barvy[1])
    ramovabarva.config(bg=barvy[1], activebackground=barvy[1])
    zednibarva.config(bg=barvy[1], activebackground=barvy[1])
    barva1.config(bg=barvy[1], activebackground=barvy[1])
    barva2.config(bg=barvy[1], activebackground=barvy[1])
    mluv.config(bg=barvy[1])
    nastavenia.config(bg=barvy[1])
    nastavenib.destroy()
    nastavenib = Frame(window, bg=barvy[1])
    nastavenib.pack()
    for i in range(len(jazyky)):
        jzyk = Button(nastavenib, text=jazyky[i], bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0], command=jazyky_command[i], padx=10, pady=10)
        jzyk.pack()
    znastaveni.config(bg=barvy[1], activebackground=barvy[1])
    window.config(bg=barvy[1])

def NaUwod(*args):
    nastavenia.destroy()
    nastavenib.destroy()
    znastaveni.destroy()
    window.config(bg=barvy[1])
    window.bind("<b>", Past)
    window.bind("<B>", Past)
    Uwod()

def ZkusitZnovu(*args):
    global aktualni_otazka
    global spravne_odpovedi_pocet
    global spatne_odpovedi_pocet
    b = askyesnocancel(title=infox[a], message=nenekonecne[a]) 
    if b == True:
        znovu.destroy()
        platno.destroy()
        cteni_vysledku.destroy()
        aktualni_otazka = 0
        spravne_odpovedi_pocet = 0
        spatne_odpovedi_pocet = 0
        Okno()
    elif b == False:
        pass
    else:
        Pryc()

def Kontrola(*args):
    global x
    global spravne_odpovedi_pocet
    global spatne_odpovedi_pocet
    global odpoved
    global aktualni_otazka

    if x.get() == spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy_okna[0])
        spravne_odpovedi_pocet += 1
    elif x.get() != spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy_okna[1])
        spatne_odpovedi_pocet += 1

    aktualni_otazka += 1
    if 1 <= aktualni_otazka <= 3:
        frame.destroy()
        odeslaniodpovedi.destroy()
        Otazka()

    elif aktualni_otazka == 4:
        frame.destroy()
        otazky_prostor.destroy()
        Okno()

def Webpage():
    webbrowser.open_new("http://mudrihagridi.cz/")

def Pryc():
    window.destroy()

def Jazyk():
    global a
    global j
    global spravne_odpovedi_pocet
    global spatne_odpovedi_pocet
    global aktualni_otazka
    global zadane_odpovedi

    if a != j:
        a = j
        spravne_odpovedi_pocet = 0
        spatne_odpovedi_pocet = 0
        aktualni_otazka = 0
        zadane_odpovedi.clear()

        if askokcancel(title=restart_okna_t[a], message=restart_okna[a]):
            window.destroy()
            if len(otazky[a]) == 4:
                Oknow()
            else:
                win = Tk()
                Label(win, text="1/0").pack()
                win.mainloop()
    else:
        showinfo(title=infox[a], message=bezezmeny[a])

def Cestina():
    global j
    j = 0
    Jazyk()

def Anglictina():
    global j
    j = 1
    Jazyk()

def Nemcina():
    global j
    j = 2
    Jazyk()

def Moravstina():
    global j
    j = 3
    Jazyk()

def Otazka():
    global frame
    global odeslaniodpovedi
    global x

    otazky_prostor.config(text=otazky[a][aktualni_otazka])
    aktualni_moznost = 0
    x = IntVar()
    frame = Frame(window, bg=barvy[1])
    frame.pack()
    for i in range(len(moznosti[a][aktualni_otazka])):
            moznostni_prostor = Radiobutton(frame, text=moznosti[a][aktualni_otazka][aktualni_moznost], variable=x, value=i, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
            moznostni_prostor.pack()
            aktualni_moznost+=1
    odeslaniodpovedi = Button(frame, text=kontrot[a], command=Kontrola, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
    odeslaniodpovedi.pack()

def Oknow():
    global window
    window = Tk()
    window.title("Múdří Hagridi")
    window.state("zoomed")
    window.resizable(False, False)
    window.config(background=barvy[1])
    menu = Menu(window)
    window.config(menu=menu)
    zavrit = Menu(menu, tearoff=False)
    menu.add_cascade(label=exit[a], menu=zavrit)
    zavrit.add_command(label=zavritw[a], command=Pryc)
    jazyk = Menu(menu, tearoff=False)
    menu.add_cascade(label=jaz[a], menu=jazyk)
    jazyk.add_command(label=cestina[a], command=Cestina)
    jazyk.add_command(label=anglictina[a], command=Anglictina)
    jazyk.add_command(label=nemcina[a], command=Nemcina)
    jazyk.add_command(label=moravstina[a], command=Moravstina)
    o = Menu(menu, tearoff=False)
    menu.add_cascade(label=infox[a],menu=o)
    o.add_command(label=web[a],command=Webpage)
    Uwod()
    window.mainloop()

def Uwod():
    global spustit
    global nastaveni
    spustit = Button(window, text=spust[a], command=Start, height=5, width=100, bg=barvy[0], activebackground=barvy[0])
    spustit.place(x=window.winfo_screenwidth()/2, y=window.winfo_screenheight()/2-50, anchor=CENTER)
    window.bind("<S>", Start)
    window.bind("<s>", Start)
    window.bind(1, Start)
    nastaveni = Button(window, text=nast[a], command=Nastaveni, height=5, width=100, bg=barvy[0], activebackground=barvy[0])
    nastaveni.place(x=window.winfo_screenwidth()/2, y=window.winfo_screenheight()/2+50, anchor=CENTER)
    window.bind("<N>", Nastaveni)
    window.bind("<n>", Nastaveni)
    window.bind(2, Start)

def Hra():
    global window
    global otazky_prostor
    global aktualni_otazka
    global posledni_otazka
    global zobrazena_otazka
    global x

    aktualni_otazka = 0
    zobrazena_otazka = 0
    posledni_otazka = 0

    otazky_prostor = Label(window, bg=barvy[1], fg=barvy[0])
    otazky_prostor.pack()
    window.bind("<Return>", Kontrola)

    Otazka()

def Okno():
    global window
    global zadane_odpovedi
    global aktualni_otazka
    global spravne_odpovedi_pocet
    global platno
    global na_hru
    global znovu
    global cteni_vysledku

    window.bind("<Return>", Past)

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    sirka_ramu = round(width/50)
    platno = Canvas(window, width=width, height=height, background=barvy_okna[3])
    height = window.winfo_screenheight()-round(window.winfo_screenheight()/20)

    if zadane_odpovedi == []:
        for i in range(0,4):
            zadane_odpovedi.append(barvy_okna[1])

    souradnice_ramu_1 = [width/2, height/2, width/2-width/5.5, height/2, width/2-width/5.5, height/2-height/2.3, width/2, height/2-height/2.3] #horní levé
    souradnice_ramu_2 = [width/2, height/2, width/2+width/5.5, height/2, width/2+width/5.5, height/2-height/2.3, width/2, height/2-height/2.3] #horní pravé
    souradnice_ramu_3 = [width/2, height/2, width/2-width/5.5, height/2, width/2-width/5.5, height/2+height/2.3, width/2, height/2+height/2.3] #dolní levé
    souradnice_ramu_4 = [width/2, height/2, width/2+width/5.5, height/2, width/2+width/5.5, height/2+height/2.3, width/2, height/2+height/2.3] #dolní pravé
    platno.create_polygon(souradnice_ramu_1, fill=zadane_odpovedi[0], outline=barvy_okna[2],width=sirka_ramu)
    platno.create_polygon(souradnice_ramu_2, fill=zadane_odpovedi[1], outline=barvy_okna[2],width=sirka_ramu)
    platno.create_polygon(souradnice_ramu_3, fill=zadane_odpovedi[2], outline=barvy_okna[2],width=sirka_ramu)
    platno.create_polygon(souradnice_ramu_4, fill=zadane_odpovedi[3], outline=barvy_okna[2],width=sirka_ramu)

    zadane_odpovedi.clear()

    platno.pack()
    if aktualni_otazka == 0:    
        na_hru = Button(window, text=vyčok[a], command=NaHru, bg=barvy_okna[2], activebackground=barvy_okna[2])
        na_hru.place(x=width/2, y=height/2+height/2.3, anchor=CENTER)
        window.bind("<Return>", NaHru)

    else:
        if spravne_odpovedi_pocet == 0:
            cteni_vysledku = Label(window, text=vyčnic[a], background=barvy_okna[2])
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        elif spravne_odpovedi_pocet < len(otazky[a]):
            cteni_vysledku = Label(window, text=vyčvíc[a].format(spravne_odpovedi_pocet, len(otazky[a])), background=barvy_okna[2])
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        elif spravne_odpovedi_pocet == len(otazky[a]):
            cteni_vysledku = Label(window, text=vyčvše[a], background=barvy_okna[2])
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        
        znovu = Button(platno, text=znov[a], command=ZkusitZnovu, bg=barvy_okna[2], activebackground=barvy_okna[2])
        znovu.place(x=width/2, y=height/2+height/2.3, anchor=CENTER)
        window.bind("<Return>", ZkusitZnovu)

if len(otazky[a]) == 4:
    Oknow()
else:
    win = Tk()
    Label(win, text="1/0").pack()
    win.mainloop()