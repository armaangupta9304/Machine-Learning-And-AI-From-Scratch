import numpy as np
from LinearRegression import LinearRegression

def main():
    l = LinearRegression(5)
    print(l.predict(np.array([1,2,3,4,5])))

if __name__ == '__main__':
    main()