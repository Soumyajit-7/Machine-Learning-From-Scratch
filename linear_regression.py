from turtle import color
import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("Salary_Data.csv")

'''
x = df["YearsExperience"]

y = df["Salary"]

plt.scatter(x,y)

plt.xlabel("YearsExperience")

plt.ylabel("Salary")

plt.show()
'''

#will not be using it

def loss_function(w , b, points):
    Total_loss = 0
    for i in range(len(points)):
        x = points.iloc[i].YearsExperience
        y = points.iloc[i].Salary
        Total_loss += (y - (w * x + b)) ** 2

    return Total_loss / float(len(points))

def gradient_descent(w_now, b_now, points, L):
    w_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].YearsExperience
        y = points.iloc[i].Salary

        w_gradient += -(2/n) * (y - (w_now * x + b_now)) * x
        b_gradient += -(2/n) * (y - (w_now * x + b_now))

    w = w_now - w_gradient * L
    b = b_now - b_gradient * L

    return w, b

'''
here :
W = Weights
b = Bias
'''

w = 0
b = 0
L = 0.001
epochs = 10000

for i in range(epochs):
    if i % 50 == 0:
        print(f"epoch: {i}")
    w, b = gradient_descent(w, b, df, L)

print(w,b)
print(loss_function(w, b, df))
plt.scatter(df.YearsExperience, df.Salary, color='black')

plt.plot(list(range(0,15)), [w * x + b for x in range(0,15)], color='red')
plt.show()