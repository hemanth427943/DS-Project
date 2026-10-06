import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df=pd.read_csv(url)
print("First Five Records:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
#-------------------------------------
# 1. Matplotlib - Line Plot
#-------------------------------------
plt.figure(figsize=(8,5))
plt.plot(df.index,df["sepal_length"],label="Sepal Length")
plt.plot(df.index,df["petal_length"],label="Petal Length")
plt.xlabel("Sample Index")
plt.ylabel("Length")
plt.title("Sepal Length and Petal Length")
plt.legend()
plt.grid()
plt.show()
#-----------------------------------------
# 2. Seaborn - Scatter Plot
#-----------------------------------------
plt.figure(figsize=(9,6))
sns.scatterplot(
    data=df,
    x="sepal_length",
    y="petal_length",
    hue="species"
)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()
#---------------------------------------------
# 3. Seaborn - Histogram
#---------------------------------------------
plt.figure(figsize=(9,6))
sns.hisplot(
    data=df,
    x="sepal_length",
    hue="species",
    kde=True
)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()
#------------------------------------------
# 4. Seaborn - Box Plot
#------------------------------------------
plt.figure(figsize=(9,6))

sns.boxplot(
    data=df,
    x="species",
    y="petal_length"
)

plt.title("Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length")
plt.show()
# ---------------------------------------------------
# 5. Seaborn - Pair Plot
# ---------------------------------------------------

sns.pairplot(
    df,
    hue="species"
)

plt.show()

