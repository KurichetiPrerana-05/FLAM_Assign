from scipy.optimize import differential_evolution
from src.fit_curve import loss_Calculate
import numpy as np

def optimize_parameters(original_points):
    # search range
    bounds=[
        (0,np.deg2rad(50)), # T: Theta  0 to 50 ( in radians)
        (-0.05,0.05), # M : Exponential factor
        (0,100) # X: horizontal shifting factor
    ]
    
    # optimization
    # minimizing the L1 loss
    result=differential_evolution(
        func=loss_Calculate,
        bounds=bounds,
        args=(original_points,)
    )
    # extracting the optimized values
    T,M,X=result.x
    # minimum loss value 
    loss=result.fun
    return T,M,X,loss