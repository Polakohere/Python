imie = input("Jak masz na imię: ")
wiek = int(input("Ile masz lat: "))
print("Cześć",imie)
print("Za 3 lata skończysz", wiek + 3, "lat")
if (wiek >= 18):
    print ("Możesz pić alkohol")
else:
    print ("Nie możesz pić alkoholu")