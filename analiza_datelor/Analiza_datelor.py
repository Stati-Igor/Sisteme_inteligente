import pandas as ps
import matplotlib.pyplot as plt

euStat = ps.read_csv('analiza_datelor/MortalitateEU.csv')
top10 = euStat.nlargest(10, 'Alcohol')
# statistica reprezentata in terminal
grupTari = euStat.groupby('Country').max().Alcohol
s = ps.Series(grupTari)
print('Top 10 tari din Europa unde rata de mortalitate la 10000 de locuitori cauzata de alcool este cea mai inalta:')
print(s.nlargest(10, keep='all'))
# statistica reprezentata in forma grafica
plt.figure(figsize=(30,4))
plt.bar(top10.Country, top10.Alcohol)
plt.xlabel('Tara din Europa')
plt.ylabel('Rate de mortalitate la 10000 de locuitori')
plt.title('Top 10 tari din Europa unde rata de mortalitate la 10000 de locuitori cauzata de alcool este cea mai inalta:')
plt.show()









