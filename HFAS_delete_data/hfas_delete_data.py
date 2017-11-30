import psycopg2
from flask import Flask, request, render_template, redirect
from vsearch import search4letters


app = Flask(__name__)


def vsearch(frase: str, letras: str) -> None:
    dbconfg = {'host': '127.0.0.1',
               'user': 'hector',
               'password': '123',
               'database': 'borrardatos', }
    connection = psycopg2.connect(**dbconfg)
    resultado = str(search4letters(frase, letras))
    _SQL = """INSERT INTO data(phrase, letters, results) VALUES(%s, %s, %s)"""
    cursor = connection.cursor()
    cursor.execute(_SQL, (frase,
                          letras,
                          resultado,))
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/')
def home() -> '302':
    return redirect('/entry')


@app.route('/resultados', methods=['POST'])
def do_search() -> 'html':
    frase = request.form['frase']
    letras = request.form['letras']
    title = 'Aqui estan tus resultados:'
    resultado = search4letters(frase, letras)
    vsearch(frase, letras)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=frase,
                           the_letters=letras,
                           the_result= resultado)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Bienvenido a mi web')


@app.route('/delete', methods=['POST'])
def delete_data() -> 'html':
    params = {'host': '127.0.0.1',
              'user': 'hector',
              'password': '123',
              'database': 'borrardatos', }
    iden = request.form['identificador']
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE id = %s", (iden,))
    conn.commit()
    cur.close()
    conn.close()
    return render_template('entry.html')


@app.route('/data')
def view_data() -> 'html':
    params = {'host': '127.0.0.1',
              'user': 'hector',
              'password': '123',
              'database': 'borrardatos', }
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur2 = conn.cursor()
    _sql = """SELECT id, phrase, letters, results FROM data ORDER BY id"""
    _sql2 = """SELECT id FROM data"""
    cur.execute(_sql)
    cur2.execute(_sql2)
    rows = cur.fetchall()
    rows2 = cur2.fetchall()
    contents = []
    contentsid = []
    for row in rows:
        contents.append(row)
    for iden in rows2:
        contentsid.append(iden)
    cur.close()
    conn.close()
    titles = ('id', 'Frase', 'Letras', 'Resultado')
    return render_template('data.html',
                           the_title='Vista de la informacion',
                           the_row_titles=titles,
                           the_data=contents,
                           ids=contentsid,)


app.run(debug=True)
