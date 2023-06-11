import pandas as pd
import matplotlib.pyplot as plt


def CityPopu(lista):
    cities = lista.head(10)
    cityPopu = cities['Population'].str.replace(',', '').astype(float)
    return cityPopu


def CityDensyKm(lista):
    cities = lista.head(10)
    densidadKM = cities['Density KM2'].str.replace(',', '').astype(float)
    return densidadKM


def CityDensyM(lista):
    cities = lista.head(10)
    densidadM = cities['Density M2'].str.replace(',', '').astype(float)
    return densidadM


def QuesitosGraph():
    list = pd.read_csv("List_B.csv", skiprows=1)
    list.columns = ['Rank', 'City', 'Population', 'Area KM2', 'Area M2', 'Density KM2', 'Density M2', 'Country', 'Year']

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

    # Total population
    ax1 = axes[0]
    cityPopural = CityPopu(list)
    ax1.pie(cityPopural, labels=list['City'].head(10), autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.set_title('Total Population')

    # Density per KM2
    ax2 = axes[1]
    densidadKM = CityDensyKm(list)
    ax2.pie(densidadKM, labels=list['City'].head(10), autopct='%1.1f%%', shadow=True, startangle=90)
    ax2.set_title('Density per KM2')

    # Density per M2
    ax3 = axes[2]
    densidadM = CityDensyM(list)
    ax3.pie(densidadM, labels=list['City'].head(10), autopct='%1.1f%%', shadow=True, startangle=90)
    ax3.set_title('Density per M2')

    plt.tight_layout()
    plt.show()


QuesitosGraph()
