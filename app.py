from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

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
                writer.writerow([name, email, cpf, data, horas, bugs, tarefas])
        except Exception as e:
            return f"An error occurred while writing to the CSV file: {e}"

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
