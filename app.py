from flask import Flask, request, render_template, redirect, jsonify
from oauth2client.service_account import ServiceAccountCredentials
from random import *
import gspread
import os


# ////////////////////////////////////////////// STORAGE GOSTEIS ///////////////////////////////////////////////


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Contador-Escola").sheet1  # Prorcure na pasta aonde você tem permissão o nome XXXX e depois..

data = sheet.get_all_records()  # Obtenha todos as informaçoes desta arquivo.

coluna = sheet.col_values(1)[1:] # pegue os gosteis
    
    



def serveUP():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("Contador-Escola").sheet1  # Prorcure na pasta aonde você tem permissão o nome XXXX e depois..

    data = sheet.get_all_records()  # Obtenha todos as informaçoes desta arquivo.

    coluna = sheet.col_values(1)[1:] # pegue os gosteis
    
    sheet.update_cell(2, 1, int(coluna[0])+1) # LINHA / COLUNA

    







# ////////////////////////////////////////////// STORAGE GOSTEIS ///////////////////////////////////////////////


app = Flask(__name__)
app.secret_key = 'biosec'



# Rota para a página inicial
@app.route('/', methods=["GET", "POST"])
def index():
    
    if request.method == "GET":
        gostei = sheet.col_values(1)[1:] # pegue os gosteis
        return render_template('index.html', gosteis=gostei[0])
    else:
        print("CHEGOUUUUUUUU")
        serveUP()
        return "Ameis salvos!"


# Rota para a página inicial
@app.route('/donates', methods=["GET", "POST"])
def index2():
    return render_template('index2.html')
   

def main():
    p = randint(0, 500000)
    port = int(os.environ.get("PORT", p))
    app.run(host="0.0.0.0", port= port)
    

if __name__ == '__main__':
    main()
