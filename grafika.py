import tkinter as tk
import obrazki

class grafikaWojny(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        print("Grafika uruchomiona")
        self.grid_columnconfigure(0, minsize = 100)
        self.grid_columnconfigure(1, minsize = 100)
        self.grid_columnconfigure(2, minsize = 200)
        self.grid_columnconfigure(3, minsize = 100)
        self.grid_columnconfigure(4, minsize = 100)
        self.grid_rowconfigure(0, minsize = 20)
        self.grid_rowconfigure(1, minsize = 20)
        self.grid_rowconfigure(2, minsize = 250)
        self.grid_rowconfigure(3, minsize = 100)
        self.grid_rowconfigure(4, minsize = 100)
        self.grid_rowconfigure(5, minsize = 20)


    def wyswietlEkranPoczatkowy(self, tekst):
        self.rewers = obrazki.rewers()

        self.info = tk.Label(text = tekst)
        self.info.grid(row = 2, column = 2)

        self.imie1 = tk.Entry(width = 15, bd = 5)
        self.imie1.grid(row = 3, column = 1)
        self.imie1.insert(0, "Gracz 1")
        self.imie2 = tk.Entry(width = 15, bd = 5)
        self.imie2.grid(row = 3, column = 2)
        self.imie2.insert(0, "Gracz 2")
        self.imie3 = tk.Entry(width = 15, bd = 5)
        self.imie3.grid(row = 3, column = 3)
        self.imie3.insert(0, "Gracz 3")



    def stworzPrzyciskRuchu(self, komenda):
        self.ruch = tk.Button(image = self.rewers, command = komenda)
        self.ruch.grid(row = 1, column = 2)


    def stworzPrzyciskWyjscia(self):
        tk.Button(text = "Wyjdz", command = self.quit).grid(row = 5, column = 2)



    def liczniki(self, runda, gracz1, gracz2, gracz3):
        self.licznik_rund = tk.Label(text = "Runda: " + str(runda))
        self.licznik_rund.grid(row = 0, column = 2)

        self.licznik_kart1 = tk.Label(text = self.imie1.get() + "\nLiczba kart: " + str(len(gracz1)))
        self.licznik_kart1.grid(row = 1, column = 0)
        self.licznik_kart2 = tk.Label(text = self.imie2.get() + "\nLiczba kart: " + str(len(gracz2)))
        self.licznik_kart2.grid(row = 1, column = 4)
        self.licznik_kart3 = tk.Label(text = self.imie3.get() + "\nLiczba kart: " + str(len(gracz3)))
        self.licznik_kart3.grid(row = 4, column = 1)



    def wyswietlRozdanieKart(self):
        self.imie1.grid_forget()
        self.imie2.grid_forget()
        self.imie3.grid_forget()

        self.rewers1 = tk.Label(image = self.rewers)
        self.rewers1.grid(row = 2, column = 0)
        self.rewers2 = tk.Label(image = self.rewers)
        self.rewers2.grid(row = 2, column = 4)
        self.rewers3 = tk.Label(image = self.rewers)
        self.rewers3.grid(row = 4, column = 2)



    def stworzRamkiGraczy(self):
        self.frame1 = tk.Frame()
        self.frame1.grid(row = 2, column = 1)
        self.karta11 = tk.Label(self.frame1)
        self.karta11.grid(row = 0, column = 0)
        self.karta12 = tk.Label(self.frame1)
        self.karta12.grid(row = 1, column = 0)
        self.karta13 = tk.Label(self.frame1)
        self.karta13.grid(row = 2, column = 0)

        self.frame2 = tk.Frame()
        self.frame2.grid(row = 2, column = 3)
        self.karta21 = tk.Label(self.frame2)
        self.karta21.grid(row = 0, column = 0)
        self.karta22 = tk.Label(self.frame2)
        self.karta22.grid(row = 1, column = 0)
        self.karta23 = tk.Label(self.frame2)
        self.karta23.grid(row = 2, column = 0)

        self.frame3 = tk.Frame()
        self.frame3.grid(row = 3, column = 2)
        self.karta31 = tk.Label(self.frame3 )
        self.karta31.grid(row = 0, column = 0)
        self.karta32 = tk.Label(self.frame3)
        self.karta32.grid(row = 0, column = 1)
        self.karta33 = tk.Label(self.frame3)
        self.karta33.grid(row = 0, column = 2)
