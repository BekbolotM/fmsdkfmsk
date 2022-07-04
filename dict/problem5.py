south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
dupes = [x for n, x in enumerate(south_american_countries) if x in south_american_countries[:n]]
south_american_countries.remove('Suriname')
print(south_american_countries)
