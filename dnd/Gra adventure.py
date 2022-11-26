import time
import random
print("Witamy w gildii poszukiwaczy przygód")
time.sleep(2)
imie = input("Jak się nazywasz bohaterze?: ")
time.sleep(1)
print(imie, "...Cudowne imię, znam jednego prawdziwego poszukiwacza przygód z takim imieniem")
time.sleep(1)
print("Wybierz zatem klasę w której chcesz się specjalizować: ")
print("1. Szermierz")
print("2. Mag")
print("3. Złodziej")
print("4. Strzelec")
Wybór = input("Wybierz numer od 1 do 4: ")
time.sleep(1)
if Wybór == "1":
    print("Wybrałeś Szermierza!")
    time.sleep(1)
    print("Świetny wybór jeżeli polegasz na swoim mieczu.")
if Wybór == "2":
    print("Wybrałeś Maga!")
    time.sleep(1)
    print("Świetny wybór jeżeli kochasz sztuczki magiczne.")
if Wybór == "3":
    print("Wybrałeś Złodzieja!")
    time.sleep(1)
    print("Świetny wybór jeżeli umiesz posługiwać się nożami.")
if Wybór == "4":
    print("Wybrałeś Strzelca!")
    time.sleep(1)
    print("Musisz mieć bystre oko skoro go wypatrzyłeś.")

