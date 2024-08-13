import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cars_2010_2020.csv')

# Calculate the average price for each make, take the columns from the original csv file
average_make = df.groupby(['Make', 'Year', 'Engine Size (L)', 'Fuel Type'])['Price (USD)'].mean().reset_index()
average_make.columns = ['Make', 'Year', 'Engine Size (L)', 'Fuel Type', 'Average_Price']
print(average_make)

average_make['Average_Price'] = average_make['Average_Price'].round(2)
print(average_make)

# Calculate the average price for each model, take the columns from the original csv file
average_model = df.groupby(['Make', 'Model', 'Year', 'Engine Size (L)', 'Fuel Type'])['Price (USD)'].mean().reset_index()
average_model.columns = ['Make', 'Model', 'Year', 'Engine Size (L)', 'Fuel Type', 'Average_Price']
print(average_model)

average_model['Average_Price'] = average_model['Average_Price'].round(2)
print(average_model)

#Do the same, but for plotting (Other DataFrame Holds Too Much Information Due to Extra Columns)
average_makeplot = df.groupby(['Make'])['Price (USD)'].mean().reset_index()
average_makeplot.columns = ['Make', 'Average_MakePlot']

#Do the same, but for plotting (Other DataFrame Holds Too Much Information Due to Extra Columns)
average_modelplot = df.groupby(['Model'])['Price (USD)'].mean().reset_index()
average_modelplot.columns = ['Model', 'Average_ModelPlot']

# Plot the average price for each make
average_makeplot.plot(
    kind='bar',
    x='Make',
    y='Average_MakePlot',
    color='blue',
    alpha=0.3,
    title="Comparison of Average Make Prices"
)



# Plot the average price for each model
average_modelplot.plot(
    kind='bar',
    x='Model',
    y='Average_ModelPlot',
    color='blue',
    alpha=0.3,
    title="Comparison of Average Model Prices"
)

plt.show()

average_make.to_csv('Average_Make.csv', index=False)
average_model.to_csv('Average_Model.csv', index=False)