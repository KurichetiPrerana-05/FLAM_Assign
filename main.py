from src.fit_curve import generate_curve
from src.utils import data_load
from src.optimizer import optimize_parameters
import numpy as np

def main():
    points=data_load()
    T,M,X,loss=optimize_parameters(points)
    print("Theta(radians):",T)
    print("Theta(degrees):",np.rad2deg(T))
    print("M:",M)
    print("X:",X)
    print("Loss:",loss)

if __name__=="__main__":
    main()
