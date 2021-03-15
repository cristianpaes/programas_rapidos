import matplotlib.pyplot as plt
import seaborn as sns

# Load data
titanic = sns.load_dataset("titanic")

# Set up a factorplot
#g = sns.factorplot("class", "survived", "sex", data=titanic, kind="bar", palette="muted", legend=False)

sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)

sns.catplot(y="deck", hue="class", kind="count",
            palette="pastel", edgecolor=".6",
            data=titanic)
# Show plot
plt.show()