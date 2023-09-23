"""
Main cli or app entry point
"""
import pandas as pd
import matplotlib.pyplot as plt


# Read the uploaded csv file: population.csv
population = pd.read_csv("population.csv")


# Calculate the descriptive statistics
rows = population.shape[0]
columns = population.shape[1]

# plot Mean, Median, Standard Deviation of 65 years population all over the world.
def viz_population():
    summary_stats = {
        "Mean": population[["2018", "2019", "2020", "2021", "2022"]].mean(),
        "Median": population[["2018", "2019", "2020", "2021", "2022"]].median(),
        "Std Dev": population[["2018", "2019", "2020", "2021", "2022"]].std(),
    }
    plt.figure(figsize=(8, 6))
    plt.plot(summary_stats["Mean"].index, summary_stats["Mean"].values, label="Mean")
    plt.plot(
        summary_stats["Median"].index, summary_stats["Median"].values, label="Median"
    )
    plt.plot(
        summary_stats["Std Dev"].index, summary_stats["Std Dev"].values, label="Std Dev"
    )
    plt.xlabel("Statistics")
    plt.ylabel("Values")
    plt.title("Summary Statistics")
    plt.legend()
    plt.tight_layout()
    plt.show()
