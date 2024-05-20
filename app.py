from flask import Flask, render_template, request, Response
import csv
from io import StringIO

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

        # Crie um arquivo CSV em memória
        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)
        csv_writer.writerow(['name', 'email', 'cpf', 'data', 'horas', 'bugs', 'tarefas'])
        csv_writer.writerow([name, email, cpf, data, horas, bugs, tarefas])

        # Retorne o arquivo CSV como resposta para download
        return Response(
            csv_data.getvalue(),
            mimetype='text/csv',
            headers={"Content-disposition":
                     "attachment; filename=data.csv"})

if __name__ == '__main__':
    app.run(debug=True)
