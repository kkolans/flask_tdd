from flask import Flask, render_template
import pandas as pd
import requests
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.figure as Figure
from flask import Response

class SiteUtils():
    def request_active_covid_cases(self):
        zakazenia = requests.get("https://api.covid19api.com/country/poland")
        return zakazenia

    def prepare_data(self):
        # Pobieram zakażenia
        zakazenia=self.request_active_covid_cases()
        # Przerabiam pobrane dane (w formie JSONa) na DataFrame
        df = pd.read_json(zakazenia.content)
        return df

    def create_figure(self):
        # Pobieram przygotowane dane (to będzie DataFrame)
        df = self.prepare_data()
        # Stwórz wykres aktywnych przypadków
        plot = df['Active'].plot(colormap='jet', marker='.', title="Aktywne przypadki koronawirusa w Polsce")
        # Ustawimy sobie nazwy osi
        plot.set_xlabel("Dni")
        plot.set_ylabel("Liczba przypadków")
        # Tworzę obrazek z tego wykresu
        fig = plot.get_figure()
        return fig

app=Flask(__name__)
utils=SiteUtils()

@app.route('/powitanie')
def home():
    return "Witam na moim API!"

@app.route('/powitanie/<string:name>')
def hello_you(name):
    return "Witam serdecznie, " + name

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/aktywne.html')
def active():
    return render_template('aktywne.html')

@app.route('/plot.png')
def plot_png():
    # Tworzę obrazek z wykresu
    fig = utils.create_figure()
    # Skomplikowany proces pzerobienia na plik .png
    output=io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


# Sprawdzam, czy program jest uruchomiony z tego pliku
# (Wówczas Python ustawi magiczny parametr __name__ jako "__main__")
if __name__=="__main__":
    # Jeśli tak, to uruchom aplikację
    app.run(debug=True)
