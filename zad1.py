from random import randint

x = randint(1,100)
print(x) 
while True:
        try:
            y = int(input("Zgadnij liczbę: "))
            if y < x:
                print("Za mało!")
            elif y > x:
                print("Za dużo!")
            else:
                print("Zgadłeś!")
                break
        except ValueError:
            print("To nie jest liczba!")
            continue
   
