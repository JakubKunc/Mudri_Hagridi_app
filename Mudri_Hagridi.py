from tkinter import *
from data import *

zadane_odpovedi = []

odpoved = 0
spravne_odpovedi_pocet = 0
spatne_odpovedi_pocet = 0
aktualni_otazka = 0

barvy_okna = ["#00BFFF","#442E1D"]

def start():
    uvod.destroy()
    okno()

def nahru():
    wokno.destroy()
    hra()

def kontrola():
    global x
    global spravne_odpovedi_pocet
    global spatne_odpovedi_pocet
    global odpoved
    if x.get() == spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy_okna[0])
        spravne_odpovedi_pocet += 1
        print("Otázka " + str(aktualni_otazka) + ": " + str(x.get()) + "==" + str(spravne_odpovedi[aktualni_otazka]) + " (Správně)")
    elif x.get() != spravne_odpovedi[aktualni_otazka]:
        zadane_odpovedi.append(barvy_okna[1])
        spatne_odpovedi_pocet += 1
        print("Otázka " + str(aktualni_otazka) + ": " + str(x.get()) + "!=" + str(spravne_odpovedi[aktualni_otazka]) + " (Špatně)")
    herni_okno.destroy()

    if aktualni_otazka == len(otazky)-1:
        okno()
    

def uwod():
    global uvod

    uvod = Tk()
    uvod.title("Múdří Hagridi")
    uvod.state("zoomed")
    uvod.resizable(False, False)

    spustit = Button(uvod, text="Spustit", command=start, height=5, width=100)
    spustit.pack()

    uvod.mainloop()

def hra():
    global herni_okno
    global otazky_prostor
    global aktualni_otazka
    global posledni_otazka
    global odeslani_odpovedi
    global x

    posledni_otazka = 0

    while aktualni_otazka < len(otazky):
        herni_okno = Tk()
        herni_okno.title("Múdří Hagridi")
        herni_okno.state("zoomed")
        herni_okno.resizable(False, False)
        
        otazky_prostor = Label(herni_okno, text=otazky[aktualni_otazka])
        otazky_prostor.pack()
        aktualni_moznost = 0
        x = IntVar()
        for i in range(len(moznosti[aktualni_otazka])):
            moznostni_prostor = Radiobutton(herni_okno, text=moznosti[aktualni_otazka][aktualni_moznost], variable=x, value=i)
            moznostni_prostor.pack()
            aktualni_moznost+=1

        odeslani_odpovedi = Button(herni_okno, text="Zkontrolovat otázku", command=kontrola)
        odeslani_odpovedi.pack()

        herni_okno.mainloop()
        aktualni_otazka+=1

def okno():
    global wokno
    global zadane_odpovedi
    global aktualni_otazka
    global spravne_odpovedi_pocet

    wokno = Tk()
    wokno.title("Múdří Hagridi")
    wokno.state("zoomed")
    wokno.resizable(False, False)

    width = wokno.winfo_screenwidth()
    height = wokno.winfo_screenheight()-round(wokno.winfo_screenheight()/16)
    sirka_ramu = round(width/50)
    platno = Canvas(wokno, width=width, height=height)

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
        na_hru = Button(wokno, text="vyčistit okno", command=nahru)
        na_hru.pack()

    else:
        if spravne_odpovedi_pocet == 0:
            cteni_vysledku = Label(wokno, text=("Nepovedlo se vám vyčistit okno"))
            cteni_vysledku.pack()
        elif spravne_odpovedi_pocet < len(otazky):
            cteni_vysledku = Label(wokno, text=("Vyčistili jste {}/{} okna").format(spravne_odpovedi_pocet, len(otazky)))
            cteni_vysledku.pack()
        elif spravne_odpovedi_pocet == len(otazky):
            cteni_vysledku = Label(wokno, text=("Vyčistili jste celé okno"))
            cteni_vysledku.pack()

    wokno.mainloop()

uwod()