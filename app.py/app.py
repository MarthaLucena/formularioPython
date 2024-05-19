from flask import Flask, render_template, request, redirect, url_for
import csv

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

        # Salve os dados em um arquivo CSV
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, cpf, data, horas, bugs, tarefas])

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
