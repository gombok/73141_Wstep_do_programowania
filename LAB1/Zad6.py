#Amelia Kawik 73141 

import random

print("Zadanie szoste")

droga = float(input("\nPodaj drogę (w kilometrach): "))

spalanie = float(input("\nPodaj spalanie (na 100 km): "))

cena_paliwa = 6.5  # zł za litr

ilosc_paliwa = (droga / 100) * spalanie

koszt_podrozy = ilosc_paliwa * cena_paliwa

print("\nIlość potrzebnego paliwa:", round(ilosc_paliwa, 2), "litrów")

print("\nKoszt podróży wynosi:", round(koszt_podrozy, 2), "zł")


print("\nA")

losowa_droga = random.randint(50, 500)

print("\nDroga do przebycia wynosi:", losowa_droga, "km")

aktualna_cena_paliwa = float(input("\nPodaj aktualną cenę paliwa (za litr): "))

ilosc_paliwa2 = (losowa_droga / 100) * spalanie

przewidywany_koszt2 = ilosc_paliwa2 * aktualna_cena_paliwa

print("\nIlość potrzebnego paliwa wynosi:", round(ilosc_paliwa2, 2), "litrów")

print("\nPrzewidywany koszt podróży wynosi:", round(przewidywany_koszt2, 2), "zł")


print("\nB")

losowa_droga2 = random.randint(50, 500)

print("\nDroga do przebycia wynosi:", losowa_droga2, "km")

cena_aktualnego_paliwa = float(input("\nPodaj aktualną cenę paliwa (za litr): "))

ilosc_paliwa2 = (losowa_droga2 / 100) * spalanie

przewidywany_koszt2 = ilosc_paliwa2 * cena_aktualnego_paliwa

wynik1 = f"\nIlość potrzebnego paliwa wynosi: {round(ilosc_paliwa2, 2)} litrów"

wynik2 = f"\nPrzewidywany koszt podróży wynosi: {round(przewidywany_koszt2, 2)} zł"

print(wynik1)

print(wynik2)

#Amelia Kawik 73141

