import pandas as ps
import matplotlib.pyplot as plt

climatic_2016 = ps.read_csv('MortalitateEU.csv')
#print('Dimensiunea tabelului este: ' ,climatic_2016.shape)
#print('Numarul toral de celule: ' ,climatic_2016.size)
#print(climatic_2016.info())
#climatic_2016 = climatic_2016.astype({'ALT': 'float32', 'TMED': 'float32', 'TMAX': 'float32', 'TMIN': 'float32', 'R24': 'float32'})
#print(climatic_2016.info())
diff = climatic_2016.LAT- climatic_2016.LAT.astype('float32')
#print(diff)
#print(diff.abs().max())
#print(diff.abs().min())
#print(type(climatic_2016.DATCLIM[0]))
#climatic_2016 = climatic_2016.astype({'DATCLIM': 'datetime64'})
#print(climatic_2016.head())

statii_meteo = climatic_2016[['CODST', 'ALT', 'LAT', 'LON']]

#print(statii_meteo)
#climatic_2016=climatic_2016.drop(columns=['ALT', 'LAT', 'LON'])
#print(climatic_2016)
statii_meteo = statii_meteo.drop_duplicates()
#print(statii_meteo.reset_index())
statii_meteo = statii_meteo.set_index('CODST')
nume_statii_str = '15015-Ocna Sugatag, 15020-Botosani, 15090-Iasi, 15108-Ceahlau Toaca, 15120-Cluj-Napoca, 15150-Bacau, 15170-Miercurea Ciuc, 15200-Arad, 15230-Deva, 15260-Sibiu, 15280-Varfu Omu, 15292-Caransebes, 15310-Galati, 15335-Tulcea, 15346-Ramnicu Valcea, 15350-Buzau, 15360-Sulina, 15410-Drobeta Turnu Severin, 15420-Bucuresti-Baneasa, 15450-Craiova, 15460-Calarasi, 15470-Rosiorii de Vede, 15480-Constanta'
nume_statii_list = [x.split('-',1) for x in nume_statii_str.split(',')]
#print(nume_statii_list)
nume_statii = ps.DataFrame(nume_statii_list, columns=['CODST', 'Nume']).astype({'CODST': 'int64'}).set_index('CODST')
statii_meteo = statii_meteo.join(nume_statii)
#print(statii_meteo)
#print('T minima inregistrata in anul 2016 a fost de %.lf grade Celsius' % climatic_2016.TMIN.min())
#print(climatic_2016.describe())
#temperatuta_minima = climatic_2016[climatic_2016.TMIN == climatic_2016.TMIN.min()]
#temperatuta_minima.join(statii_meteo, on='CODST')
#print(temperatuta_minima)
#print('Statii ALT>1000',statii_meteo[statii_meteo.ALT>1000])
#print('Statii ALT<1000', statii_meteo[statii_meteo.ALT<1000])

statii_meteo_minime = statii_meteo.join(climatic_2016.groupby('CODST').min().TMIN)
'''print(statii_meteo_minime)
plt.figure(figsize=(30,5))
plt.bar(statii_meteo_minime.Nume, statii_meteo_minime.TMIN)
plt.xlabel('Statia meterologica')
plt.ylabel('Tmin in Grade Celsius')
plt.title('Temperatura minima din Romania pemtru 2016 din toate statiile meteorologice')
plt.show()'''
plt.figure()
plt.pie(statii_meteo_minime.TMIN.abs(), labels=statii_meteo_minime.Nume)
plt.title('Temperatura minima din Romania pemtru 2016 din toate statiile meteorologice')
plt.show()




