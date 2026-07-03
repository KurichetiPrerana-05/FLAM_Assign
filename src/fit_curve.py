import numpy as np

def generate_curve(T,M,X):
    t=np.linspace(6,60,4000)
    k=np.exp(M*np.abs(t))*np.sin(0.3*t)
    # given equations
    x=t*np.cos(T)-k*np.sin(T)+X
    y=42+t*np.sin(T)+k*np.cos(T)
    curve=np.column_stack((x,y))
    return curve

def loss_Calculate(parameters,original_points):
    T,M,X=parameters # T is Theta
    # Generate the predicted curve
    curve=generate_curve(T,M,X)
    total_loss=0
    # Each original point is compared with the generated curve
    for point in original_points:
        # calculating the L1 distance to every point on the generated curve
        dist=np.abs(curve[:,0]-point[0])+np.abs(curve[:,1]-point[1])
        # Minimum distance is taken
        total_loss+=np.min(dist)
    # Avg loss is returned
    return total_loss/len(original_points)
