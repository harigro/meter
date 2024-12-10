from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    # nilai kembalian {'nilai': '12', 'satuan': 'cm'}
    meter = request.form.to_dict()
    print(meter)
    if meter:
        greeting = {'km': '1200000', 'hm': '12000000', 'dam': '120000000', 
                    'm': '1200000000', 'dm': '12000000000', 'cm': '120000000000', 'mm': '1200000000000'}
    else:
        greeting = "Halo, siapa namamu?"
    
    return jsonify(greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
