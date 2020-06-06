from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
@app.route('/powitanie')
def home():
    return "Witam na moim API!"

@app.route('/powitanie/<string:name>')
def hello_you(name):
    return "Witam serdecznie, " + name

@app.route('/index.html')
def index():
    return render_template('index.html')


# Sprawdzam, czy program jest uruchomiony z tego pliku
# (Wówczas Python ustawi magiczny parametr __name__ jako "__main__")
if __name__=="__main__":
    # Jeśli tak, to uruchom aplikację
    app.run(debug=True)
