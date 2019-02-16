from random import randint

while True:        
    try:
        random_list = [randint(1,50) for i in range(6)]
        random_list.sort()
        typowane_e = input("Podaj 6 liczb od 1-49 (liczby oddziel spacją): ").split()
        typowane = list(set(typowane_e))
        typowane1 = []
        if len(typowane) != 6:
            raise ValueError
        for i in typowane:           
            i = int(i)
            if i>49 or i<1:
                print("Liczba spoza zakresu 1-49!")
                typowane.remove(i)     
            typowane1.append(i)
        typowane1.sort()
        wynik = []   
        for i in typowane1:
            if i in random_list:
                wynik.append(i)
        print("Podałeś liczby: ", typowane1)
        print("Wylosowane liczby: ", random_list)
        if len(wynik) >= 3:
            print("Trafiłeś {}!".format(len(wynik))) 
        else:
            print("Spróbuj ponownie :-(")     
    except ValueError:
        print("Podaj 6 liczb!")



        
        
        

