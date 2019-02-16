#!/usr/bin/env python3

print("Wybierz liczbę od 0 do 1000, a ja ją zgadnę")
my_min = 0
my_max = 1000
while True:
    guess = int((my_max - my_min)/2)+my_min
    print("Zgaduję: {}".format(guess))
    print("1 - za mało\n2 - za dużo\n3 - zgadłeś")
    user_resp = input("Odpowiedź: ")
    if user_resp == "3":
        print("Wygrałem!")
        break
    elif user_resp == "2":
        my_max = guess
    elif user_resp == "1":
        my_min = guess
    else:
        print("Nie oszukuj!")
