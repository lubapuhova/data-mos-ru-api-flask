from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)
app.debug = True

def get_data():
    url = "http://api.data.mos.ru/v1/datasets/2462/rows"
    r = requests.get(url)
    return r.json()


@app.route('/')
def list_rows():
    return render_template("list_rows.html",
                           data=get_data())

@app.route('/table/<int:n>')
def show_table(n):
    data = get_data()
    row = data[n]
    return render_template("show_table.html",
                           table=row)

@app.route('/json_table/<int:n>')
def json_table (n):
    data = get_data()
    table = data[n]
    x = []
    y = []
    for row in table['Cells']['IndexValues']:
        x.append("{}, {}".format(row['Year'], row['Quarter']))
        y.append(row['Value'])
    return jsonify(x=x, y=y)

if __name__ == '__main__':
    app.run()
