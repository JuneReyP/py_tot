
import pandas as pd  # import the pandas library for data manipulation/file reading
import matplotlib.pyplot as plt # import the matplotlib library for data visualization


df = pd.read_csv('health.csv')
# plot the data
ax = df.plot()
plt.title('Health Data Overview')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend(title='Legend')
# display the plot
plt.show()