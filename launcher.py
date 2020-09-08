import random
from grafika import grafikaWojny
import obrazki


class graWojna():
    talia = []
    karty_na_stole = []
    gracz1 = []
    gracz2 = []
    gracz3 = []
    # imie1 = "Gracz 1"
    # imie2 = "Gracz 2"
    # imie3 = "Gracz 3"
    jest_wojna = False



    def __init__(self, graf):
        self.graf = graf
        self.graf.wyswietlEkranPoczatkowy("Witaj w grze karcianej Wojna! \n\n Podaj imiona trzech graczy, następnie \nkliknij na talię, aby rozdać \n karty i rozpocząć grę. \n\nW celu kontynuowania \n rozgrywki klikaj [Kontynuuj]. \n\nKliknij [Wyjdź] aby zakończyć grę. ")
        self.graf.stworzPrzyciskRuchu(self.rozpocznijGre)
        self.graf.stworzPrzyciskWyjscia()



    def istnieje(self, obiekt):
        if not obiekt:
            return 0
        else:
            return 1


    def utworzPotasujTalie(self):
        for i in range (2, 15):
            for j in ["♠", "♣", "♥", "♦"]:
                if i < 11:
                    self.talia.append([i, str(i) + j])
                elif i == 11:
                    self.talia.append([i, "Walet" + j])
                elif i == 12:
                    self.talia.append([i, "Dama" + j])
                elif i == 13:
                    self.talia.append([i, "Krol" + j])
                elif i == 14:
                    self.talia.append([i, "As" + j])
        print(self.talia)
        self.talia = random.sample(self.talia, len(self.talia))
        print("Liczba kart w talii: ", len(self.talia))


    def podzialKart(self):
        liczba = int(round(len(self.talia)/3, 0))
        self.gracz1 = self.talia[: liczba]
        self.gracz2 = self.talia[liczba : liczba*2]
        self.gracz3 = self.talia[liczba*2 : liczba*3]
        print("Karty rozdane")


    def polozKarty(self, gracz):
        if self.istnieje(gracz):
            self.karty_na_stole.append(gracz[0])
            gracz.remove(gracz[0])
            return self.karty_na_stole[-1]
        else:
            return [random.random(), 0]


    def zgarnijKarty(self, gracz):
        gracz.extend(self.karty_na_stole)
        self.karty_na_stole.clear()


    def pokazKartyNaStole(self):
        for karta in self.karty_na_stole:
            print(karta[1])
        print("\n\n")


    def wyswietlPolozoneKarty(self, gracz, wierzchnia):
        if gracz == self.gracz1:
            print(self.graf.imie1.get(), ":", wierzchnia[1],"\nLiczba kart: ",len(self.gracz1))
            self.img1 = obrazki.awersy(wierzchnia[1])
            self.graf.karta12.config(image = self.img1)

        elif gracz == self.gracz2:
            print(self.graf.imie2.get(), ":", wierzchnia[1],"\nLiczba kart: ",len(self.gracz2))
            self.img2 = obrazki.awersy(wierzchnia[1])
            self.graf.karta22.config(image = self.img2)

        elif gracz == self.gracz3:
            print(self.graf.imie3.get(), ":", wierzchnia[1],"\nLiczba kart: ",len(self.gracz3))
            self.img3 = obrazki.awersy(wierzchnia[1])
            self.graf.karta32.config(image = self.img3)


    def wyswietlWojne(self, gracz):
        if gracz == self.gracz1:

            self.graf.karta11.config(image = self.img1)

            if self.istnieje(gracz):
                self.ukryta1 = obrazki.awersy(self.polozKarty(gracz)[1])
                self.graf.karta12.config(image = self.graf.rewers)
                print("▓")
            else: self.graf.karta12.config(image = "")


            if self.istnieje(gracz):
                self.img11 = obrazki.awersy(gracz[0][1])
                self.graf.karta13.config(image = self.img11)
                print(gracz[0][1])
            else: self.graf.karta13.config(image = "")


        elif gracz == self.gracz2:

            self.graf.karta21.config(image = self.img2)

            if self.istnieje(gracz):
                self.ukryta2 = obrazki.awersy(self.polozKarty(gracz)[1])
                self.graf.karta22.config(image = self.graf.rewers)
                print("▓")
            else: self.graf.karta22.config(image = "")

            if self.istnieje(gracz):
                self.img21 = obrazki.awersy(gracz[0][1])
                self.graf.karta23.config(image = self.img21)
                print(gracz[0][1])
            else: self.graf.karta23.config(image = "")


        elif gracz == self.gracz3:

            self.graf.karta31.config(image = self.img3)

            if self.istnieje(gracz):
                self.ukryta3 = obrazki.awersy(self.polozKarty(gracz)[1])
                self.graf.karta32.config(image = self.graf.rewers)
                print("▓")
            else: self.graf.karta32.config(image = "")

            if self.istnieje(gracz):
                self.img31 = obrazki.awersy(gracz[0][1])
                self.graf.karta33.config(image = self.img31)
                print(gracz[0][1])
            else: self.graf.karta33.config(image = "")


    def odkryjKarty(self, gracz):
        if gracz == self.gracz1 and self.istnieje(self.ukryta1):
            self.graf.karta12.config(image = self.ukryta1)

        elif gracz == self.gracz2 and self.istnieje(self.ukryta2):
            self.graf.karta22.config(image = self.ukryta2)

        elif gracz == self.gracz3 and self.istnieje(self.ukryta3):
            self.graf.karta32.config(image = self.ukryta3)



    def odswiez(self):
        self.graf.info.config(text = "")
        self.graf.frame1.destroy()
        self.graf.frame2.destroy()
        self.graf.frame3.destroy()
        self.graf.liczniki(self.runda, self.gracz1, self.gracz2, self.gracz3)

        if not self.gracz1:
            self.graf.rewers1.destroy()
        if not self.gracz2:
            self.graf.rewers2.destroy()
        if not self.gracz3:
            self.graf.rewers3.destroy()

        self.graf.ruch.config(command = self.rozgrywka)




    def koniecGry(self, imie):
        self.graf.info.config(text = "Grę wygrywa " + imie + "! \n\n Aby rozpocząć nową grę \n kliknij [Nowa gra] \n\n Kliknij [Wyjdź] aby zakończyć")
        self.graf.ruch.config(text = "Nowa gra", command = self.rozpocznijGre)



    def rozpocznijGre(self):
        self.graf.info.config(text = "Niech rozpęta się Wojna!")
        self.runda = 1
        self.utworzPotasujTalie()
        self.podzialKart()
        self.graf.liczniki(self.runda, self.gracz1, self.gracz2, self.gracz3)
        self.graf.wyswietlRozdanieKart()

        self.graf.ruch.config(text = "Kontynuuj", image = '', command = lambda: self.rozgrywka())



    def rozgrywka(self):
        self.runda += 1
        self.graf.stworzRamkiGraczy()

        if not self.gracz1 and not self.gracz2:
            self.koniecGry(self.graf.imie3.get())

        elif not self.gracz1 and not self.gracz3:
            self.koniecGry(self.graf.imie2.get())

        elif not self.gracz3 and not self.gracz2:
            self.koniecGry(self.graf.imie1.get())

        else:
            if not self.gracz1:
                self.walkaDwoch(self.gracz2, self.gracz3, self.graf.imie2.get(), self.graf.imie3.get())

            elif not self.gracz2:
                self.walkaDwoch(self.gracz1, self.gracz3, self.graf.imie1.get(), self.graf.imie3.get())

            elif not self.gracz3:
                self.walkaDwoch(self.gracz1, self.gracz2, self.graf.imie1.get(), self.graf.imie2.get())

            else:
                self.walkaTrzech()



    def walkaTrzech(self):
        self.graf.info.config(text = "")

        self.wierzchnia_karta1 = self.polozKarty(self.gracz1)
        self.wierzchnia_karta2 = self.polozKarty(self.gracz2)
        self.wierzchnia_karta3 = self.polozKarty(self.gracz3)

        if not self.jest_wojna:
            self.wyswietlPolozoneKarty(self.gracz1, self.wierzchnia_karta1)
            self.wyswietlPolozoneKarty(self.gracz2, self.wierzchnia_karta2)
            self.wyswietlPolozoneKarty(self.gracz3, self.wierzchnia_karta3)

        self.graf.ruch.config(command = self.rozstrzygnijWalkeTrzech)



    def rozstrzygnijWalkeTrzech(self):
        if self.jest_wojna:
            self.odkryjKarty(self.gracz1)
            self.odkryjKarty(self.gracz2)
            self.odkryjKarty(self.gracz3)

        if self.wierzchnia_karta1[0] > self.wierzchnia_karta2[0] and self.wierzchnia_karta1[0] > self.wierzchnia_karta3[0]:
            self.jest_wojna = False
            self.kto = "Wygrywa " + self.graf.imie1.get() + "\nDostaje kart: " + str(len(self.karty_na_stole))
            print(self.kto)
            self.graf.info.config(text = self.kto)
            self.pokazKartyNaStole()
            self.zgarnijKarty(self.gracz1)

            self.graf.ruch.config(command = self.odswiez)


        elif self.wierzchnia_karta2[0] > self.wierzchnia_karta1[0] and self.wierzchnia_karta2[0] > self.wierzchnia_karta3[0]:
            self.jest_wojna = False
            self.kto = "Wygrywa " + self.graf.imie2.get() + "\nDostaje kart: " + str(len(self.karty_na_stole))
            print(self.kto)
            self.graf.info.config(text = self.kto)
            self.pokazKartyNaStole()
            self.zgarnijKarty(self.gracz2)

            self.graf.ruch.config(command = self.odswiez)


        elif self.wierzchnia_karta3[0] > self.wierzchnia_karta2[0] and self.wierzchnia_karta3[0] > self.wierzchnia_karta1[0]:
            self.jest_wojna = False
            self.kto = "Wygrywa " + self.graf.imie3.get() + "\nDostaje kart: " + str(len(self.karty_na_stole))
            print(self.kto)
            self.graf.info.config(text = self.kto)
            self.pokazKartyNaStole()
            self.zgarnijKarty(self.gracz3)

            self.graf.ruch.config(command = self.odswiez)

        else:
            self.jest_wojna = True
            print("\n WOJNAAA!\n")
            self.graf.info.config(text = "WOJNAAA!")
            self.wojnaTrzech()



    def walkaDwoch(self, gracz1, gracz2, imie1, imie2):
        self.graf.info.config(text = "")

        self.wierzchnia_karta1 = self.polozKarty(gracz1)
        self.wierzchnia_karta2 = self.polozKarty(gracz2)
        self.wierzchnia_karta3 = None

        if not self.jest_wojna:
            self.wyswietlPolozoneKarty(gracz1, self.wierzchnia_karta1)
            self.wyswietlPolozoneKarty(gracz2, self.wierzchnia_karta2)

        self.graf.ruch.config(command = lambda: self.rozstrzygnijWalkeDwoch(gracz1, gracz2, imie1, imie2))



    def rozstrzygnijWalkeDwoch(self, gracz1, gracz2, imie1, imie2):
        if self.jest_wojna:
            self.odkryjKarty(gracz1)
            self.odkryjKarty(gracz2)

        if self.wierzchnia_karta1[0] > self.wierzchnia_karta2[0]:
            self.jest_wojna = False
            self.kto = "Wygrywa " + imie1 + "\nDostaje kart: " + str(len(self.karty_na_stole))
            print("\n\n", self.kto)
            self.graf.info.config(text = self.kto)
            self.pokazKartyNaStole()
            self.zgarnijKarty(gracz1)

            self.graf.ruch.config(command = self.odswiez)

        elif self.wierzchnia_karta1[0] < self.wierzchnia_karta2[0]:
            self.jest_wojna = False
            self.kto = "Wygrywa " + imie2 + "\nDostaje kart: " + str(len(self.karty_na_stole))
            print("\n\n", self.kto)
            self.graf.info.config(text = self.kto)
            self.pokazKartyNaStole()
            self.zgarnijKarty(gracz2)

            self.graf.ruch.config(command = self.odswiez)

        else:
            self.jest_wojna = True
            print("\n WOJNAAA!\n")
            self.graf.info.config(text = "WOJNAAA!")
            self.graf.ruch.config(command = lambda: self.wojnaDwoch(gracz1, gracz2, imie1, imie2))




    def wojnaTrzech(self):
        if self.wierzchnia_karta1[0] == self.wierzchnia_karta2[0] == self.wierzchnia_karta3[0]:
            self.kto = "Wojnę toczą gracze: "  + "\n" +  self.graf.imie1.get() + "\n" + self.graf.imie2.get() + "\n" + self.graf.imie3.get()
            print(self.kto)
            self.graf.info.config(text = self.kto)
            self.wyswietlWojne(self.gracz1)
            self.wyswietlWojne(self.gracz2)
            self.wyswietlWojne(self.gracz3)

            self.graf.ruch.config(command = self.walkaTrzech)

        else:
            if self.wierzchnia_karta1[0] == self.wierzchnia_karta2[0]:
                self.wojnaDwoch(self.gracz1, self.gracz2, self.graf.imie1.get(), self.graf.imie2.get())

            elif self.wierzchnia_karta1[0] == self.wierzchnia_karta3[0]:
                self.wojnaDwoch(self.gracz1, self.gracz3, self.graf.imie1.get(), self.graf.imie3.get())

            elif self.wierzchnia_karta2[0] == self.wierzchnia_karta3[0]:
                self.wojnaDwoch(self.gracz2, self.gracz3, self.graf.imie2.get(), self.graf.imie3.get())


    def wojnaDwoch(self, gracz1, gracz2, imie1, imie2): #istnieje po to żeby algorytm nie sprawdzał elementu listy ktora nie istnieje gdy jeden gracz odpadnie
        self.kto = "Wojnę toczą gracze: " + "\n" + imie1 + "\n" + imie2
        print(self.kto)
        self.graf.info.config(text = self.kto)
        self.wyswietlWojne(gracz1)
        self.wyswietlWojne(gracz2)

        self.graf.ruch.config(command = lambda: self.walkaDwoch(gracz1, gracz2, imie1, imie2))



def main():
    app_grx = grafikaWojny()
    app = graWojna(app_grx)

    app_grx.geometry("600x550")
    app_grx.title("Wojna - INTERAKTYWNA Gra karciana")
    app_grx.mainloop()


main()
