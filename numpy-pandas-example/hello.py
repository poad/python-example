import numpy as np
import random
import pandas as pd

def main():
    random.seed()

    weights = np.array(list(map(lambda i: random.uniform(50.0, 100.0), range(20))))
    v = np.var(weights)

    print(f'{pd.DataFrame({'体重': weights})}\n')
    print(f'平均値: {np.mean(weights)}')
    print(f'分散: {v}')
    print(f'標準偏差: {np.sqrt(v)}')

if __name__ == "__main__":
    main()
