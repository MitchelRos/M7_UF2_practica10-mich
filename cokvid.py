import pandas as pd
import matplotlib.pyplot as plt


def totalescaos(lista):
    paises = lista.groupby('location')['total_cases'].sum().nlargest(10)
    #tarda pero funciona
    for pais in paises.index:
        casosMes = lista[lista['location'] == pais].groupby('date')['total_cases'].sum()
        plt.plot(casosMes.index, casosMes.values, label=pais)

    #funciona pls!!
    plt.xlabel('Mes')
    plt.ylabel('Casos - totales')
    plt.title('Casos - totales por país y mes')
    plt.legend()
    plt.show()


def cityDeadMes(lista):
    city = lista.groupby('location')['total_deaths'].sum().nlargest(10)
    #tarda mas pero funciona
    for ciudad in city.index:
        muertesMes = lista[lista['location'] == ciudad].groupby('date')['total_deaths'].sum()
        plt.plot(muertesMes.index, muertesMes.values, label=ciudad)
    plt.xlabel('Mes')
    plt.ylabel('Muertes - totales')
    plt.title('Muertes - totales por ciudad y mes')
    plt.legend()
    plt.show()


def paisDeadMes(lista):
    paises = lista.groupby('location')['total_deaths'].sum().nlargest(10)
    #tarda aun mas pero funciona
    for pais in paises.index:
        muertesMes = lista[lista['location'] == pais].groupby('date')['total_deaths'].sum()
        plt.plot(muertesMes.index, muertesMes.values, label=pais)
    plt.xlabel('Mes')
    plt.ylabel('Muertes - totales')
    plt.title('Muertes - totales por mes y país')
    plt.legend()
    plt.show()


def main():
    lista = pd.read_csv('covid.csv')
    totalescaos(lista)
    cityDeadMes(lista)
    paisDeadMes(lista)


main()
