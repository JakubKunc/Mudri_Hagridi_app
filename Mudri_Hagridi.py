from tkinter import *
from data import *
from tkinter import colorchooser

aktualni_otazka = 0
odpoved = 0
spravne_odpovedi_pocet = 0
spatne_odpovedi_pocet = 0

a = 0

def Past(nt):
    pass

def Start(*args):
    spustit.destroy()
    nastaveni.destroy()
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
    cistabarva = Button(nastavenia, text="Nastavte barvu pro vyčestěné části okna", command=CistaBarva, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0])
    cistabarva.pack()
    spinavabarva = Button(nastavenia, text="Nastavte barvu pro špinavé části okna", command=SpinavaBarva, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0])
    spinavabarva.pack()
    ramovabarva = Button(nastavenia, text="Nastavte barvu pro rám okna", command=RamovaBarva, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0])
    ramovabarva.pack()
    zednibarva = Button(nastavenia, text="Nastavte barvu zdi, na které je okno", command=ZedniBarva, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0])
    zednibarva.pack()
    nastavenib = Frame(window, bg=barvy[1])
    nastavenib.pack()
    barva1 = Button(nastavenib, text="Nastavte barvu textu", command=Barva1, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0])
    barva1.pack()
    barva2 = Button(nastavenib, text="Nastavte barvu pro pozadí", command=Barva2, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0])
    barva2.pack()
    window.bind("<b>", NaUwod)
    window.bind("<B>", NaUwod)

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
    barvy.pop(0)
    barvy.insert(0,colorchooser.askcolor()[1])
    cistabarva.config(fg=barvy[0], activeforeground=barvy[0])
    spinavabarva.config(fg=barvy[0], activeforeground=barvy[0])
    ramovabarva.config(fg=barvy[0], activeforeground=barvy[0])
    zednibarva.config(fg=barvy[0], activeforeground=barvy[0])
    barva1.config(fg=barvy[0], activeforeground=barvy[0])
    barva2.config(fg=barvy[0], activeforeground=barvy[0])

def Barva2():
    barvy.pop()
    barvy.insert(1,colorchooser.askcolor()[1])
    cistabarva.config(bg=barvy[1], activebackground=barvy[1])
    spinavabarva.config(bg=barvy[1], activebackground=barvy[1])
    ramovabarva.config(bg=barvy[1], activebackground=barvy[1])
    zednibarva.config(bg=barvy[1], activebackground=barvy[1])
    barva1.config(bg=barvy[1], activebackground=barvy[1])
    barva2.config(bg=barvy[1], activebackground=barvy[1])
    nastavenia.config(bg=barvy[1])
    nastavenib.config(bg=barvy[1])
    window.config(bg=barvy[1])

def NaUwod(*args):
    nastavenia.destroy()
    nastavenib.destroy()
    window.config(bg=barvy[1])
    window.bind("<b>", Past)
    window.bind("<B>", Past)
    Uwod()

def ZkusitZnovu():
    global aktualni_otazka
    znovu.destroy()
    platno.destroy()
    cteni_vysledku.destroy()
    aktualni_otazka = 0
    Okno()

def Kontrola(*args):
    global x
    global spravne_odpovedi_pocet
    global spatne_odpovedi_pocet
    global odpoved
    global aktualni_otazka

    if x.get() == spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy_okna[0])
        spravne_odpovedi_pocet += 1
        print("Otázka " + str(aktualni_otazka+1) + ": " + str(x.get()) + "==" + str(spravne_odpovedi[aktualni_otazka]) + " (Správně)")
    elif x.get() != spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy_okna[1])
        spatne_odpovedi_pocet += 1
        print("Otázka " + str(aktualni_otazka+1) + ": " + str(x.get()) + "!=" + str(spravne_odpovedi[aktualni_otazka]) + " (Špatně)")
    
    aktualni_otazka += 1
    if aktualni_otazka == 1:
        frame1.destroy()
        odeslani_odpovedi1.destroy()
        Otazka_2()

    elif aktualni_otazka == 2:
        frame2.destroy()
        odeslani_odpovedi2.destroy()
        Otazka_3()
    
    elif aktualni_otazka == 3:
        frame3.destroy()
        odeslani_odpovedi3.destroy()
        Otazka_4()

    elif aktualni_otazka == 4:
        frame4.destroy()
        otazky_prostor.destroy()
        Okno()

def Otazka_1():
    global frame1
    global odeslani_odpovedi1
    global x

    otazky_prostor.config(text=otazky[aktualni_otazka])
    aktualni_moznost = 0
    x = IntVar()
    frame1 = Frame(window, bg=barvy[1])
    frame1.pack()
    for i in range(len(moznosti[aktualni_otazka])):
            moznostni_prostor = Radiobutton(frame1, text=moznosti[aktualni_otazka][aktualni_moznost], variable=x, value=i, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
            moznostni_prostor.pack()
            aktualni_moznost+=1
    odeslani_odpovedi1 = Button(frame1, text="Zkontrolovat otázku", command=Kontrola, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
    odeslani_odpovedi1.pack()

def Otazka_2():
    global frame2
    global odeslani_odpovedi2
    global x

    otazky_prostor.config(text=otazky[aktualni_otazka])
    aktualni_moznost = 0
    x = IntVar()
    frame2 = Frame(window, bg=barvy[1])
    frame2.pack()
    for i in range(len(moznosti[aktualni_otazka])):
            moznostni_prostor = Radiobutton(frame2, text=moznosti[aktualni_otazka][aktualni_moznost], variable=x, value=i, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
            moznostni_prostor.pack()
            aktualni_moznost+=1
    odeslani_odpovedi2 = Button(frame2, text="Zkontrolovat otázku", command=Kontrola, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
    odeslani_odpovedi2.pack()

def Otazka_3():
    global frame3
    global odeslani_odpovedi3
    global x

    otazky_prostor.config(text=otazky[aktualni_otazka])
    aktualni_moznost = 0
    x = IntVar()
    frame3 = Frame(window, bg=barvy[1])
    frame3.pack()
    for i in range(len(moznosti[aktualni_otazka])):
            moznostni_prostor = Radiobutton(frame3, text=moznosti[aktualni_otazka][aktualni_moznost], variable=x, value=i, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
            moznostni_prostor.pack()
            aktualni_moznost+=1
    odeslani_odpovedi3 = Button(frame3, text="Zkontrolovat otázku", command=Kontrola, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
    odeslani_odpovedi3.pack()

def Otazka_4():
    global frame4
    global odeslani_odpovedi4
    global x

    otazky_prostor.config(text=otazky[aktualni_otazka])
    aktualni_moznost = 0
    x = IntVar()
    frame4 = Frame(window, bg=barvy[1])
    frame4.pack()
    for i in range(len(moznosti[aktualni_otazka])):
            moznostni_prostor = Radiobutton(frame4, text=moznosti[aktualni_otazka][aktualni_moznost], variable=x, value=i, bg=barvy[1], activebackground=barvy[1], fg=barvy[0], activeforeground=barvy[0])
            moznostni_prostor.pack()
            aktualni_moznost+=1
    odeslani_odpovedi4 = Button(frame4, text="Zkontrolovat otázku", command=Kontrola, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
    odeslani_odpovedi4.pack()

def Oknow():
    global window
    window = Tk()
    window.title("Múdří Hagridi")
    window.state("zoomed")
    window.resizable(False, False)
    window.config(background=barvy[1])
    Uwod()
    window.mainloop()

def Uwod():
    global spustit
    global nastaveni

    spustit = Button(window, text="Spustit", command=Start, height=5, width=100, bg=barvy[0], activebackground=barvy[0])
    spustit.place(x=window.winfo_screenwidth()/2, y=window.winfo_screenheight()/2-50, anchor=CENTER)
    window.bind("<S>", Start)
    window.bind("<s>", Start)
    window.bind(1, Start)
    nastaveni = Button(window, text="Nastaveni", command=Nastaveni, height=5, width=100, bg=barvy[0], activebackground=barvy[0])
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

    Otazka_1()

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
        na_hru = Button(window, text="vyčistit okno", command=NaHru, bg=barvy_okna[2], activebackground=barvy_okna[2])
        na_hru.place(x=width/2, y=height/2+height/2.3, anchor=CENTER)
        window.bind("<Return>", NaHru)

    else:
        if spravne_odpovedi_pocet == 0:
            cteni_vysledku = Label(window, text=("Nepovedlo se vám vyčistit okno"), background=barvy_okna[2])
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        elif spravne_odpovedi_pocet < len(otazky):
            cteni_vysledku = Label(window, text=("Vyčistili jste {}/{} okna").format(spravne_odpovedi_pocet, len(otazky)), background=barvy_okna[2])
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        elif spravne_odpovedi_pocet == len(otazky):
            cteni_vysledku = Label(window, text=("Vyčistili jste celé okno"), background=barvy_okna[2])
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        
        znovu = Button(platno, text="Spustit znovu", command=ZkusitZnovu, bg=barvy_okna[2], activebackground=barvy_okna[2])
        znovu.place(x=width/2, y=height/2+height/2.3, anchor=CENTER)

if len(otazky) == 4:
    Oknow()
else:
    win = Tk()
    Label(win, text="1/0").pack()
    win.mainloop()