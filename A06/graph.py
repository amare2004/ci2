import sys

import pandas as pd
import matplotlib.pyplot as plt


def create_graph(csv_path, image_path): #Create a graph from a CSV file and save it as an image
    data = pd.read_csv(
        csv_path,
        sep=";",
        decimal=",",
        encoding="utf-8-sig",
        usecols=["x", "y"],
    )

    plt.plot(data["x"], data["y"], marker="o") #Create a line plot with markers for the data points
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("y = 1/x")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(image_path, dpi=150)
    plt.close()


if __name__ == "__main__": #Check if the script is being run directly
    if len(sys.argv) != 3:
        print("Usage: python graph.py <input.csv> <output.png>")
        raise SystemExit(1)

    create_graph(sys.argv[1], sys.argv[2])