import requests
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

zakazenia = requests.get("https://api.covid19api.com/country/poland")
df=pd.read_json(zakazenia.content)
plot=df['Active'].plot()
plt.show()
