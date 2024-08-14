import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cars_2010_2020.csv')

# Calculate the average price for each make, take the columns from the original csv file
average_make = df.groupby(['Make'])['Price (USD)'].mean().reset_index()
average_make.columns = ['Make', 'Average_Price']

# Round to 2 decimal places
average_make['Average_Price'] = average_make['Average_Price'].round(2)
print(average_make)

# Calculate the price for each model, take the columns from the original csv file
average_model = df.groupby(['Make', 'Model', 'Year', 'Engine Size (L)', 'Fuel Type'])['Price (USD)'].mean().reset_index()
average_model.columns = ['Make', 'Model', 'Year', 'Engine Size (L)', 'Fuel Type', 'Price']

# Round to 2 decimal places
average_model['Price'] = average_model['Price'].round(2)
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

# Storing only model because we need each individual car with all attributes. The other dataframe is simply for the graph and for finding what is the cheapest average make.
average_model.to_csv('Average_Model.csv', index=False)