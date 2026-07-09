import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

print(df.head())

df["species"].value_counts().plot(kind="bar")

plt.title("Iris Species Count")
plt.xlabel("Species")
plt.ylabel("Count")

plt.show()
# Pie Chart
plt.figure()
df["species"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Species Percentage")
plt.ylabel("")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(df["sepal_length"], df["petal_length"])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()