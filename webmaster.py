from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trips')
def trips():
    return render_template('trips.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('how-it-works.html')


@app.route('/references-sources')
def sources():
    return render_template('references-sources.html')

@app.route('/promotions')
def promotions():
    return render_template('promotions.html')

if __name__ == '__main__':
    app.run(debug=True)
