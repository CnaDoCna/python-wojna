from PIL import Image, ImageTk


def rewers():
    return ImageTk.PhotoImage(Image.open(r"karty/back.jpg"))

def awersy(karta):
    if karta == "2♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Dwojka Pik.jpg"))
    elif karta == "3♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Trojka Pik.jpg"))
    elif karta == "4♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Czworka Pik.jpg"))
    elif karta == "5♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Piatka Pik.jpg"))
    elif karta == "6♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Szostka Pik.jpg"))
    elif karta == "7♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Siodemka Pik.jpg"))
    elif karta == "8♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Osemka Pik.jpg"))
    elif karta == "9♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Dziewiatka Pik.jpg"))
    elif karta == "10♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Dziesiatka Pik.jpg"))
    elif karta == "Walet♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Walet Pik.jpg"))
    elif karta == "Dama♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Dama Pik.jpg"))
    elif karta == "Krol♠":
        return ImageTk.PhotoImage(Image.open(r"karty/Krol Pik.jpg"))
    elif karta == "As♠":
        return ImageTk.PhotoImage(Image.open(r"karty/As Pik.jpg"))
    elif karta == "2♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Dwojka Trefl.jpg"))
    elif karta == "3♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Trojka Trefl.jpg"))
    elif karta == "4♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Czworka Trefl.jpg"))
    elif karta == "5♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Piatka Trefl.jpg"))
    elif karta == "6♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Szostka Trefl.jpg"))
    elif karta == "7♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Siodemka Trefl.jpg"))
    elif karta == "8♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Osemka Trefl.jpg"))
    elif karta == "9♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Dziewiatka Trefl.jpg"))
    elif karta == "10♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Dziesiatka Trefl.jpg"))
    elif karta == "Walet♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Walet Trefl.jpg"))
    elif karta == "Dama♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Dama Trefl.jpg"))
    elif karta == "Krol♣":
        return ImageTk.PhotoImage(Image.open(r"karty/Krol Trefl.jpg"))
    elif karta == "As♣":
        return ImageTk.PhotoImage(Image.open(r"karty/As Trefl.jpg"))
    elif karta == "2♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Dwojka Kier.jpg"))
    elif karta == "3♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Trojka Kier.jpg"))
    elif karta == "4♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Czworka Kier.jpg"))
    elif karta == "5♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Piatka Kier.jpg"))
    elif karta == "6♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Szostka Kier.jpg"))
    elif karta == "7♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Siodemka Kier.jpg"))
    elif karta == "8♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Osemka Kier.jpg"))
    elif karta == "9♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Dziewiatka Kier.jpg"))
    elif karta == "10♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Dziesiatka Kier.jpg"))
    elif karta == "Walet♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Walet Kier.jpg"))
    elif karta == "Dama♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Dama Kier.jpg"))
    elif karta == "Krol♥":
        return ImageTk.PhotoImage(Image.open(r"karty/Krol Kier.jpg"))
    elif karta == "As♥":
        return ImageTk.PhotoImage(Image.open(r"karty/As Kier.jpg"))
    elif karta == "2♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Dwojka Karo.jpg"))
    elif karta == "3♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Trojka Karo.jpg"))
    elif karta == "4♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Czworka Karo.jpg"))
    elif karta == "5♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Piatka Karo.jpg"))
    elif karta == "6♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Szostka Karo.jpg"))
    elif karta == "7♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Siodemka Karo.jpg"))
    elif karta == "8♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Osemka Karo.jpg"))
    elif karta == "9♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Dziewiatka Karo.jpg"))
    elif karta == "10♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Dziesiatka Karo.jpg"))
    elif karta == "Walet♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Walet Karo.jpg"))
    elif karta == "Dama♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Dama Karo.jpg"))
    elif karta == "Krol♦":
        return ImageTk.PhotoImage(Image.open(r"karty/Krol Karo.jpg"))
    elif karta == "As♦":
        return ImageTk.PhotoImage(Image.open(r"karty/As Karo.jpg"))
    else:
        return ''
