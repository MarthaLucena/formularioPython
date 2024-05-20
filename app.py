from flask import Flask, render_template, request, redirect, url_for, Response
import csv
import os

app = Flask(__name__)

# Função para verificar se o arquivo CSV existe
def file_exists(file_path):
    return os.path.exists(file_path)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Pegue os dados do formulário
        name = request.form['name']
        email = request.form['email']
        cpf = request.form['cpf']
        data = request.form['data']
        horas = request.form['horas']
        bugs = request.form['bugs']
        tarefas = request.form['tarefas']

        # Diretório onde o arquivo CSV será salvo
        csv_file_path = os.path.join(os.getcwd(), 'data.csv')

        try:
            # Salve os dados em um arquivo CSV
            with open(csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)

                # Verifique se o arquivo já existe para evitar escrever o título novamente
                if not file_exists(csv_file_path):
                    writer.writerow(['Nome', 'Email', 'CPF', 'Data', 'Horas', 'Bugs', 'Tarefas'])

                writer.writerow([name, email, cpf, data, horas, bugs, tarefas])
        except Exception as e:
            return f"An error occurred while writing to the CSV file: {e}"

        # Retorna o arquivo CSV como resposta para o download
        def generate():
            with open(csv_file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    yield ','.join(row) + '\n'

        response = Response(generate(), mimetype='text/csv')
        response.headers.set("Content-Disposition", "attachment", filename="data.csv")
        return response

if __name__ == '__main__':
    app.run(debug=True)
