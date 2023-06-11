import pandas as pd
from matplotlib import pyplot as plt

# Accedemos a los datos del csv
df = pd.read_csv('test.csv')

# Cogemos un par de muestras
lista = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

df_muestras = df[df['id'].isin(lista)]


def mcqueen():
    vel = df_muestras[['id', 'clock_speed']].to_string(index=False)
    df_muestras[['id', 'clock_speed']].plot(x='id', kind='bar')
    # leyenda
    plt.xlabel('ID')
    plt.ylabel('Velocidad de CPU')
    plt.title('Velocidad de CElPhone')
    plt.show()

    print(vel)


def pixeles():
    px = df_muestras[['id', 'fc']].to_string(index=False)
    df_muestras[['id', 'fc']].plot(x='id', kind='bar')
    # leyenda
    plt.xlabel('ID')
    plt.ylabel('Megapixeles')
    plt.title('Megapixeles de las muestras')
    plt.show()

    print(px)


def btery():
    bateria = df_muestras[['id', 'battery_power']].to_string(index=False)
    df_muestras[['id', 'battery_power']].plot(x='id', kind='bar')
    # leyenda
    plt.xlabel('ID')
    plt.ylabel('Bateria')
    plt.title('Bateria de las muestras')
    plt.show()

    print(bateria)


def main():
    print("-------Velocidades-------")
    mcqueen()
    print("-------Megapixeles-------")
    pixeles()
    print("-------Baterias-------")
    btery()


main()
