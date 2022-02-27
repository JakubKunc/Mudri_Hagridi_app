from tkinter import *
from data import *

aktualni_otazka = 0
odpoved = 0
spravne_odpovedi_pocet = 0
spatne_odpovedi_pocet = 0

def start(*args):
    spustit.destroy()
    okno()

def nahru(*args):
    platno.destroy()
    na_hru.destroy()
    hra()

def kontrola(*args):
    global x
    global spravne_odpovedi_pocet
    global spatne_odpovedi_pocet
    global odpoved
    global aktualni_otazka

    if x.get() == spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy[0])
        spravne_odpovedi_pocet += 1
        print("Otázka " + str(aktualni_otazka+1) + ": " + str(x.get()) + "==" + str(spravne_odpovedi[aktualni_otazka]) + " (Správně)")
    elif x.get() != spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy[1])
        spatne_odpovedi_pocet += 1
        print("Otázka " + str(aktualni_otazka+1) + ": " + str(x.get()) + "!=" + str(spravne_odpovedi[aktualni_otazka]) + " (Špatně)")
    
    aktualni_otazka += 1
    if aktualni_otazka == 1:
        frame1.destroy()
        odeslani_odpovedi1.destroy()
        otazka_2()

    elif aktualni_otazka == 2:
        frame2.destroy()
        odeslani_odpovedi2.destroy()
        otazka_3()
    
    elif aktualni_otazka == 3:
        frame3.destroy()
        odeslani_odpovedi3.destroy()
        otazka_4()

    elif aktualni_otazka == 4:
        frame4.destroy()
        otazky_prostor.destroy()
        okno()

def otazka_1():
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
    odeslani_odpovedi1 = Button(frame1, text="Zkontrolovat otázku", command=kontrola, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
    odeslani_odpovedi1.pack()

def otazka_2():
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
    odeslani_odpovedi2 = Button(frame2, text="Zkontrolovat otázku", command=kontrola, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
    odeslani_odpovedi2.pack()

def otazka_3():
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
    odeslani_odpovedi3 = Button(frame3, text="Zkontrolovat otázku", command=kontrola, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
    odeslani_odpovedi3.pack()

def otazka_4():
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
    odeslani_odpovedi4 = Button(frame4, text="Zkontrolovat otázku", command=kontrola, bg=barvy[1], activebackground=barvy[1] ,fg=barvy[0], activeforeground=barvy[0])
    odeslani_odpovedi4.pack()

def oknow():
    global window
    window = Tk()
    window.title("Múdří Hagridi")
    window.state("zoomed")
    window.resizable(False, False)
    window.config(background=barvy[1])
    uwod()
    window.mainloop()

def uwod():
    global spustit

    spustit = Button(window, text="Spustit", command=start, height=5, width=100, bg=barvy[0], activebackground=barvy[0])
    spustit.place(x=window.winfo_screenwidth()/2, y=window.winfo_screenheight()/2, anchor=CENTER)
    window.bind("<Return>", start)

def hra():
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
    window.bind("<Return>", kontrola)

    otazka_1()

def okno():
    global window
    global zadane_odpovedi
    global aktualni_otazka
    global spravne_odpovedi_pocet
    global platno
    global na_hru

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    sirka_ramu = round(width/50)
    platno = Canvas(window, width=width, height=height, background=barvy[3])

    if zadane_odpovedi == []:
        for i in range(0,4):
            zadane_odpovedi.append("#442E1D")

    souradnice_ramu_1 = [width/2, height/2, width/2-width/5.5, height/2, width/2-width/5.5, height/2-height/2.3, width/2, height/2-height/2.3] #horní levé
    souradnice_ramu_2 = [width/2, height/2, width/2+width/5.5, height/2, width/2+width/5.5, height/2-height/2.3, width/2, height/2-height/2.3] #horní pravé
    souradnice_ramu_3 = [width/2, height/2, width/2-width/5.5, height/2, width/2-width/5.5, height/2+height/2.3, width/2, height/2+height/2.3] #dolní levé
    souradnice_ramu_4 = [width/2, height/2, width/2+width/5.5, height/2, width/2+width/5.5, height/2+height/2.3, width/2, height/2+height/2.3] #dolní pravé
    platno.create_polygon(souradnice_ramu_1, fill=zadane_odpovedi[0], outline=barvy[2],width=sirka_ramu)
    platno.create_polygon(souradnice_ramu_2, fill=zadane_odpovedi[1], outline=barvy[2],width=sirka_ramu)
    platno.create_polygon(souradnice_ramu_3, fill=zadane_odpovedi[2], outline=barvy[2],width=sirka_ramu)
    platno.create_polygon(souradnice_ramu_4, fill=zadane_odpovedi[3], outline=barvy[2],width=sirka_ramu)

    zadane_odpovedi.clear()

    platno.pack()
    if aktualni_otazka == 0:    
        na_hru = Button(window, text="vyčistit okno", command=nahru, bg=barvy[2], activebackground=barvy[2])
        na_hru.place(x=width/2, y=height/2, anchor=CENTER)
        window.bind("<Return>", nahru)

    else:
        if spravne_odpovedi_pocet == 0:
            cteni_vysledku = Label(window, text=("Nepovedlo se vám vyčistit okno"), background=barvy[2])
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        elif spravne_odpovedi_pocet < len(otazky):
            cteni_vysledku = Label(window, text=("Vyčistili jste {}/{} okna").format(spravne_odpovedi_pocet, len(otazky)), background=barvy[2])
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        elif spravne_odpovedi_pocet == len(otazky):
            cteni_vysledku = Label(window, text=("Vyčistili jste celé okno"), background=barvy[2])
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)

oknow()