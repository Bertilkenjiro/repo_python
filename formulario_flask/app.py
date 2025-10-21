from flask import Flask, render_template, request
import csv
from datetime import datetime
import os

app = Flask(__name__)

# Caminho do csv 
csv_file = 'respostas.csv'

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    idade = request.form['idade']
    email = request.form['email']

    # 🕒 cria o timestamp antes de salvar
    data_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Verifica se o arquivo existe e cria cabeçalhos se for novo
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Data', 'Nome', 'Idade', 'E-mail'])
        writer.writerow([data_envio, nome, idade, email])

    return f"""
    <h2>Dados recebidos!</h2>
    <p><b>Nome:</b> {nome}</p>
    <p><b>Idade:</b> {idade}</p>
    <p><b>E-mail:</b> {email}</p>
    <a href="/">Voltar</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
