import pandas as pd

data=pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv")

print(data.head())
print(data.columns)
print(data.index)
print(data.values)
data_ind = data.sort_values("Country")
print(data_ind.head())
Country=data["Country"]
print(Country.head(20))
year_2004 = data[data["Year"]>2004]
print(year_2004)
df=data['Year'].value_counts()
print(df)
medals_by_country=data.groupby("Country")["Medal"].count()
print(medals_by_country)
data_ind=data.set_index("City")
print(data_ind)
cities=["Beijing","Sydney"]
print(data[data["City"].isin(cities)])
print(data_ind.loc[cities])