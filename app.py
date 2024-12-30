from flask import Flask, request, jsonify, render_template
from tools.meter import TabelSatuanMeter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    meter = request.form.to_dict()
    tabel = TabelSatuanMeter(meter.get("nilai"), meter.get("satuan"))
    if meter:
        greeting = tabel.tabel_new()
    else:
        greeting = 0
    return jsonify(greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
