import pandas as pd
import numpy as np

def importdata():
    data=pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv")
    print(data.head())
    print(data.columns)
    print(data.index)
    print(data.values)

def cleandata():
    data = pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv")
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
    df1=data['Sport'].value_counts()
    print(df1)
    Ireland=data[data['Country']=='Ireland']
    print(Ireland)
    Ireland_gender=Ireland['Gender'].value_counts()
    print(Ireland_gender)
    IrishMedals=Ireland.groupby('Sport')['Medal'].count().sort_values(ascending=False)
    print(IrishMedals)
    cities=["Beijing","Sydney"]
    print(data[data["City"].isin(cities)])
    print(data_ind.loc[cities])
    print(data.iloc[0:5,2:4])
    print(data.loc["2000":"2008"])
    missing_val=data.isnull().sum()
    print(missing_val)
    data[data.isnull().any(axis=1)]
    data.dropna(axis=0, inplace=True)
    data.Year=data.Year.astype(int)
    data[['City','Year']].drop_duplicates().reset_index(drop=True)
    data4=pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv",index_col = 0)
    for lab,row in data4.iterrows():
        print(lab)

def analyzingdata():
    data = pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv")
    medals_by_country = data.groupby("Country")["Medal"].count()
    np_medals = np.array(medals_by_country)
    avg = np.mean(np_medals)
    print("Average per country is :" + str(avg))
    med = np.median(np_medals)
    print("Median per country is :" + str(med))
    host_country ={'Canada':'Montreal','Russia':'Moscow','USA':'Los Angeles','Japan':'Seoul','Spain':'Barcelona','Greece':'Athens','Australia':'Sydney','China':'Beijing'}
    for key, value in host_country.items():
        print("the host country was" + str (key)+"in the city called" + str (value))

import matplotlib.pyplot as plt
import seaborn as sns

def visualizeddata():
    data = pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv")
    box = data[data.Sport == 'Boxing'].groupby(['Country']).Medal.size()
    top_10_boxing = box.sort_values(ascending = False)[:10]
    top_10_boxing_bar = top_10_boxing.plot.bar()
    plt.xticks(rotation=25)
    plt.xlabel('Medal won in Boxing (Top 10 Countries)')
    plt.ylabel('No of medals')
    plt.show()

def visualizeddata2():
    data = pd.read_csv("Summer-Olympic-medals-1976-to-2008.csv")
    usa= data[data['Country_Code']=='USA']
    sns.countplot(x='Year',data=usa)
    plt.title("Medals won by USA per year")
    plt.show()

cleandata()









