import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('cars_2010_2020.csv')

def Sorting_Make():
    global df

df = df.sort_values('Make')

Sorting_Make()



def Sorting_Model():
    global df

df = df.sort_values('Model')

Sorting_Model()

print(df)

#def outputting_model():
   # global plt

df.plot(
    kind = 'bar',
    x ='Make',
    y='Price (USD)',
    color='blue',
    alpha=0.3,
    title="Plot"
    )

plt.show()

#print(df['Price (USD)'].mean())
#print(df['Model'].value_counts())


#print(df.describe())

