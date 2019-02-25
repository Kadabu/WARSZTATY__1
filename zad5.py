from random import randint

def roll(n):

    list_n = []

    if "+" in n:
        list_n = n.split("+")
        change = int(list_n[-1])
    elif "-" in n:
        list_n = n.split("-")
        change = int(list_n[-1]) * (-1)
    else:
        list_n.append(n)
        change = 0
    

    params = list_n[0]
    turns = 0
    if params[0] == "D":
        turns = 1
        dice = int(params[1:])
    else:
        list_params = params.split("D")
        turns = int(list_params[0])
        dice = int(list_params[1])

    dices = [3, 4, 6, 8, 10, 12, 20, 100]
    if dice not in dices:
        raise Exception("No such dice!")

    list_results = [randint(1, dice) for i in range(turns)]
    result = 0
    for res in list_results: result += res

    return result + change


