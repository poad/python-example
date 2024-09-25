import matplotlib.pyplot as plt
import numpy as np

def main():
    year = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
    population = np.array([23012, 24001, 23998, 24052, 24203, 24252, 24256, 24500, 24862, 25201])

    plt.plot(year, population)
    plt.xlim(2014, 2023)
    plt.ylim(23000, 26000)
    plt.xlabel('Year', fontsize = 16)
    plt.ylabel('Population', fontsize = 16)
    plt.grid(color = '0.8')
    plt.show()

if __name__ == "__main__":
    main()
