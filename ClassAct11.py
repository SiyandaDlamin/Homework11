import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

mpg = pd.read_csv(r"C:\Users\u1502\OneDrive\Desktop\Siyanda Class Activity 10\mpg.csv")
print(mpg)
#add calculated column
mpg["Force"] = mpg["weight"] * mpg["acceleration"]
#subset of data based on conditions
print(mpg)
usa = mpg[mpg.origin == "usa"]
print(usa)
#Correlation Coeffiecient 
core = mpg["cylinders"].corr(mpg["horsepower"])
print(core)
##Print graph
x = mpg["weight"]
y = mpg["acceleration"]

z = x*y

plt.xlabel('Weight')
plt.ylabel('Acceleration')

plt.title("Force Plot")



plt.scatter(x,y)
plt.show()