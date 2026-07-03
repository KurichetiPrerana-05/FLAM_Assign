# Parametric Curve Estimation
## overview of the assignment

This work estimates the parameters which are unknown of a parametric curve using optimization

The given parametric equations are:
```text
x(t)=t*cos(θ) - e^(M|t|)*sin(0.3t)*sin(θ)+X

y(t)=42+t*sin(θ) + e^(M|t|)*sin(0.3t)*cos(θ)

```

The objective of this work is to determine the values of unknown variables which are:
- θ (theta)
- M
- X

using only the provided csv file ('xy_data.csv')

---
## Structure of the project

```
project/
|
├── data/
|    └── xy_data.csv
|
|── src/
|    ├──fit_curve.py
|    ├──optimizer.py
|    ├──utils.py
|
├── main.py
├──requirements.txt
└── README.md
```
---
## Approach

### 1.Loading the Dataset

The input csv file contains sampled '(x,y)' coordinates from the unknown curve.

The data is loaded by importing pandas and converted into a NumPy array.

---
### 2. Generating the curve

The parametric curve is generated using:
-θ (rotation)
-M (exponential scaling factor)
-X (Horizontal shifting factor)

4000 values of t are uniformly sampled between 6 and 60 to create smooth curve.

---
### 3. Loss function

For every point(x,y) in the csv file:

- compute L1 distance to every point on the curve.
- select the minimum distance out of all.
- Average these minimum distances over all points.

This average L1 distance is used as the objective function of optimization.

---

### 4.Optimization

The unknown parameters are estimated using SciPy's **Differential Evolution** optimizer.

Search ranges:

| Parameter | Range      |
|-----------|------------|
|     θ     | 0° – 50°   |
|     M     |-0.05 – 0.05|
|     X     |  0 - 100   |

The optimizer searches for the combination that minimiaes the average L1 loss.

---

## Libraries which are used:

- Python
- NumPy
- Pandas
- SciPy
---
## Results
Estimated Parameters:
```
Theta ≈ 30°
M ≈ 0.03
X ≈ 55
```
Average L1 loss:
```
0.005
```

The predicted curve closely overlaps the provided data points on the curve.

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

---

# Output

the program prints:
- Theta (radians)
- Theta (degrees)
- M
- X
- Total L1 loss

---
# References
1. SciPy Documentation for Differential Evolution
   https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html
2. Desmos Parametric Graph for analysis
   https://www.desmos.com/calculator/rfj91yrxob



