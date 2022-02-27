from tkinter import *
from data import *

zadane_odpovedi = []

aktualni_otazka = 0
odpoved = 0
spravne_odpovedi_pocet = 0
spatne_odpovedi_pocet = 0

barvy_okna = ["#00BFFF","#442E1D"]

def start(*args):
    uvod.destroy()
    okno()

def nahru(*args):
    wokno.destroy()
    hra()

def kontrola(*args):
    global x
    global spravne_odpovedi_pocet
    global spatne_odpovedi_pocet
    global odpoved
    global aktualni_otazka

    if x.get() == spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy_okna[0])
        spravne_odpovedi_pocet += 1
        print("Otázka " + str(aktualni_otazka) + ": " + str(x.get()) + "==" + str(spravne_odpovedi[aktualni_otazka]) + " (Správně)")
    elif x.get() != spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy_okna[1])
        spatne_odpovedi_pocet += 1
        print("Otázka " + str(aktualni_otazka) + ": " + str(x.get()) + "!=" + str(spravne_odpovedi[aktualni_otazka]) + " (Špatně)")
    
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
        herni_okno.destroy()
        okno()

def otazka_1():
    global frame1
    global odeslani_odpovedi1
    global x

    otazky_prostor.config(text=otazky[aktualni_otazka])
    aktualni_moznost = 0
    x = IntVar()
    frame1 = Frame(herni_okno)
    frame1.pack()
    for i in range(len(moznosti[aktualni_otazka])):
            moznostni_prostor = Radiobutton(frame1, text=moznosti[aktualni_otazka][aktualni_moznost], variable=x, value=i)
            moznostni_prostor.pack()
            aktualni_moznost+=1
    odeslani_odpovedi1 = Button(herni_okno, text="Zkontrolovat otázku", command=kontrola)
    odeslani_odpovedi1.pack()

def otazka_2():
    global frame2
    global odeslani_odpovedi2
    global x

    otazky_prostor.config(text=otazky[aktualni_otazka])
    aktualni_moznost = 0
    x = IntVar()
    frame2 = Frame(herni_okno)
    frame2.pack()
    for i in range(len(moznosti[aktualni_otazka])):
            moznostni_prostor = Radiobutton(frame2, text=moznosti[aktualni_otazka][aktualni_moznost], variable=x, value=i)
            moznostni_prostor.pack()
            aktualni_moznost+=1
    odeslani_odpovedi2 = Button(herni_okno, text="Zkontrolovat otázku", command=kontrola)
    odeslani_odpovedi2.pack()

def otazka_3():
    global frame3
    global odeslani_odpovedi3
    global x

    otazky_prostor.config(text=otazky[aktualni_otazka])
    aktualni_moznost = 0
    x = IntVar()
    frame3 = Frame(herni_okno)
    frame3.pack()
    for i in range(len(moznosti[aktualni_otazka])):
            moznostni_prostor = Radiobutton(frame3, text=moznosti[aktualni_otazka][aktualni_moznost], variable=x, value=i)
            moznostni_prostor.pack()
            aktualni_moznost+=1
    odeslani_odpovedi3 = Button(herni_okno, text="Zkontrolovat otázku", command=kontrola)
    odeslani_odpovedi3.pack()

def otazka_4():
    global frame4
    global odeslani_odpovedi4
    global x

    otazky_prostor.config(text=otazky[aktualni_otazka])
    aktualni_moznost = 0
    x = IntVar()
    frame4 = Frame(herni_okno)
    frame4.pack()
    for i in range(len(moznosti[aktualni_otazka])):
            moznostni_prostor = Radiobutton(frame4, text=moznosti[aktualni_otazka][aktualni_moznost], variable=x, value=i)
            moznostni_prostor.pack()
            aktualni_moznost+=1
    odeslani_odpovedi4 = Button(herni_okno, text="Zkontrolovat otázku", command=kontrola)
    odeslani_odpovedi4.pack()

def uwod():
    global uvod

    uvod = Tk()
    uvod.title("Múdří Hagridi")
    uvod.state("zoomed")
    uvod.resizable(False, False)
    uvod.config(background=barvy_okna[1])

    spustit = Button(uvod, text="Spustit", command=start, height=5, width=100, bg=barvy_okna[0], activebackground=barvy_okna[0])
    spustit.place(x=uvod.winfo_screenwidth()/2, y=uvod.winfo_screenheight()/2, anchor=CENTER)
    uvod.bind("<Return>", start)


    uvod.mainloop()

def hra():
    global herni_okno
    global otazky_prostor
    global aktualni_otazka
    global posledni_otazka
    global zobrazena_otazka
    global x

    aktualni_otazka = 0
    zobrazena_otazka = 0
    posledni_otazka = 0

    herni_okno = Tk()
    herni_okno.title("Múdří Hagridi")
    herni_okno.state("zoomed")
    herni_okno.resizable(False, False)

    otazky_prostor = Label(herni_okno,)
    otazky_prostor.pack()
    herni_okno.bind("<Return>", kontrola)

    otazka_1()
    herni_okno.mainloop()

def okno():
    global wokno
    global zadane_odpovedi
    global aktualni_otazka
    global spravne_odpovedi_pocet

    wokno = Tk()
    wokno.title("Múdří Hagridi")
    wokno.state("zoomed")
    wokno.resizable(False, False)
    wokno.config(background="#239B11")

    width = wokno.winfo_screenwidth()
    height = wokno.winfo_screenheight()
    sirka_ramu = round(width/50)
    platno = Canvas(wokno, width=width, height=height, background="#239B11")

    if zadane_odpovedi == []:
        for i in range(0,4):
            zadane_odpovedi.append("#442E1D")

    souradnice_ramu_1 = [width/2, height/2, width/2-width/5.5, height/2, width/2-width/5.5, height/2-height/2.3, width/2, height/2-height/2.3] #horní levé
    souradnice_ramu_2 = [width/2, height/2, width/2+width/5.5, height/2, width/2+width/5.5, height/2-height/2.3, width/2, height/2-height/2.3] #horní pravé
    souradnice_ramu_3 = [width/2, height/2, width/2-width/5.5, height/2, width/2-width/5.5, height/2+height/2.3, width/2, height/2+height/2.3] #dolní levé
    souradnice_ramu_4 = [width/2, height/2, width/2+width/5.5, height/2, width/2+width/5.5, height/2+height/2.3, width/2, height/2+height/2.3] #dolní pravé
    platno.create_polygon(souradnice_ramu_1, fill=zadane_odpovedi[0], outline="#DC143C",width=sirka_ramu)
    platno.create_polygon(souradnice_ramu_2, fill=zadane_odpovedi[1], outline="#DC143C",width=sirka_ramu)
    platno.create_polygon(souradnice_ramu_3, fill=zadane_odpovedi[2], outline="#DC143C",width=sirka_ramu)
    platno.create_polygon(souradnice_ramu_4, fill=zadane_odpovedi[3], outline="#DC143C",width=sirka_ramu)

    zadane_odpovedi.clear()

    platno.pack()
    if aktualni_otazka == 0:    
        na_hru = Button(wokno, text="vyčistit okno", command=nahru, bg="#DC143C", activebackground="#DC143C")
        na_hru.place(x=width/2, y=height/2, anchor=CENTER)
        wokno.bind("<Return>", nahru)

    else:
        if spravne_odpovedi_pocet == 0:
            cteni_vysledku = Label(wokno, text=("Nepovedlo se vám vyčistit okno"), background="#DC143C")
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        elif spravne_odpovedi_pocet < len(otazky):
            cteni_vysledku = Label(wokno, text=("Vyčistili jste {}/{} okna").format(spravne_odpovedi_pocet, len(otazky)), background="#DC143C")
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)
        elif spravne_odpovedi_pocet == len(otazky):
            cteni_vysledku = Label(wokno, text=("Vyčistili jste celé okno"), background="#DC143C")
            cteni_vysledku.place(x=width/2, y=height/2, anchor=CENTER)

    wokno.mainloop()

uwod()