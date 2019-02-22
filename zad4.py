#!/usr/bin/env python3

from flask import Flask, request
app = Flask(__name__)

my_min = 0
my_max = 1000
guess = int((my_max - my_min) / 2) + my_min
guess_no = 0

form_base = """<html>
            <head>
            <link rel="stylesheet" href="css/style.css">
            </head>
            <body>
            <div>{}</div>
            <input type="hidden" name="guess_no">
            <input type="hidden" name="my_max">
            <input type="hidden" name="my_min">
            <input type="hidden" name="guess">
            <form method="POST">   
            <label><input type="radio" name="user_resp" value="Trafiłeś">Trafiłeś!</label><br>
            <label><input type="radio" name="user_resp" value="Mniej">Mniej<label><br>
            <label><input type="radio" name="user_resp" value="Więcej">Więcej<label><br>
            <input type="submit" value ="OK">
            </label>
            </form>          
            </body>
            </html>"""

final_base = """<html>
                <head>
                <link rel="stylesheet" href="css/style.css">
                </head>
                <body>
                <div>{}</div>
                </body>
                </html>"""  

@app.route('/zgadula',methods=['GET','POST'])
def zgadula():

    global my_min 
    global my_max 
    global guess 
    global guess_no

    if request.method == 'GET':
        return form_base.format("Pomyśl liczbę od 1-1000, a ja ją zgadnę w max 10 próbach. Zgaduję... {}".format(guess)) 
  
    if request.method == 'POST':                                      
        user_resp = request.form['user_resp']
        if guess_no < 10:      
            if user_resp == "Trafiłeś":
                return final_base.format("Wygrałem!!!")   
            elif user_resp == "Mniej":
                my_max = guess  
                guess = int((my_max - my_min) / 2) + my_min
                guess_no +=1
                return form_base.format("Zgaduję: {}".format(guess))                 
            else:
                my_min = guess 
                guess = int((my_max - my_min) / 2) + my_min
                guess_no +=1
                return form_base.format("Zgaduję: {}".format(guess))  
        else:
            return final_base.format("Przegrałem!!!") 
           
app.run()
