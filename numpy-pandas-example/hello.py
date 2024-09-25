import numpy as np
import pandas as pd

def main():
    h = np.array([116.7, 156.5, 148.6, 158.0, 133.8, 153.6, 165.9, 127.6, 137.8, 169.8])
    age = np.array([6.1, 14.0, 14.6, 17.0, 9.0, 12.0, 12.5, 8.0, 8.1, 16.0])
    w = np.array([21.7, 50.0, 48.8, 52.5, 31.3, 45.2, 48.8, 27.0, 27.1, 60.5])

    data = pd.DataFrame({'Heihgt': h, 'Age': age, 'Weight': w})

    print(f'{data}')


if __name__ == "__main__":
    main()
