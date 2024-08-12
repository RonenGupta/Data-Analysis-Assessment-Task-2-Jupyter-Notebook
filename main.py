import pandas as pd

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



