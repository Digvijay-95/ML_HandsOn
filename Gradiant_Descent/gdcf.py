# Gradient Descent and Cost Function
import numpy as np
import pandas as pd
import math

df=pd.read_csv("test_scores.csv")
x=np.array(df.math)
y=np.array(df.cs)


def gradient_descent(x,y):
    m=c=0
    cost_previous=0
    iter=1000000
    step=0.0002111
    n=len(x)
    for i in range(iter):
        y_predicted = m*x + c
        cost =(1/n)*sum([(val**2) for val in (y-y_predicted)])
        md =-(2/n)*sum(x*(y-y_predicted))
        cd =-(2/n)*sum(y- y_predicted)
        m =m-step*md
        c =c-step*cd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous=cost        
        print(f"m={m}\nc = {c}\ncost= {cost}")

#print(x,y)
gradient_descent(x,y)