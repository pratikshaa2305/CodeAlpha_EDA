import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bbc_headlines.csv")

print("Dataset Info:\n")
print(df.info())

print("\nMissing Values:\n")
print(df.isnull().sum())

df["Headline_Length"] = df["Headline"].apply(len)

print("\nStatistical Summary:\n")
print(df["Headline_Length"].describe())

plt.figure()
plt.hist(df["Headline_Length"], bins=15)
plt.title("Headline Length Distribution")
plt.xlabel("Number of Characters")
plt.ylabel("Frequency")
plt.show()

print("\nLongest Headlines:\n")
print(df.sort_values(by="Headline_Length", ascending=False).head(5))

print("\nShortest Headlines:\n")
print(df.sort_values(by="Headline_Length").head(5))
