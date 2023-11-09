
## reading data and Libraries 
import matplotlib.pyplot as plt
import pandas as pd
# Replace 'your_file.csv' with the path to your CSV file.
df = pd.read_csv("C:\\Users\\user\\Downloads\\drinks (1).csv")
print(df.head())
import pandas as pd
import matplotlib.pyplot as plt


## Bar Chart 
top_beer_countries = df.sort_values(by='beer_servings', ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_beer_countries['country'], top_beer_countries['beer_servings'])
plt.xlabel('Beer Servings')
plt.ylabel('Country')
plt.title('Top 10 Beer-Serving Countries')
plt.gca().invert_yaxis()
plt.show()

## Line Plot
df_sorted = df.sort_values(by='total_litres_of_pure_alcohol', ascending=False)
N = 10
top_N_countries = df_sorted.head(N)

plt.plot(top_N_countries['country'], top_N_countries['total_litres_of_pure_alcohol'], marker='o', linestyle='-', markersize=8)
plt.xlabel('Country')
plt.ylabel('Total Litres of Pure Alcohol')
plt.title(f'Top {N} Countries with the Highest Total Litres of Pure Alcohol')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

## scatter plot.
plt.scatter(df['wine_servings'], df['spirit_servings'])
plt.xlabel('Wine Servings')
plt.ylabel('Spirit Servings')
plt.title('Wine Servings vs. Spirit Servings')
plt.show()


