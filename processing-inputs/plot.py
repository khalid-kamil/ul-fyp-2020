import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


def importData(source):
    df = pd.read_csv(source)
    data = df[df["Specimen_no"] == 1]
    return data


def formatChart(data, fig, ax):
    ax.grid(color="#000000", linestyle="-", linewidth=0.5, alpha=0.3)
    ax.set_xlabel(
        "Extension (mm)", family="Arial", fontsize="medium", fontweight="semibold"
    )
    ax.set_ylabel("Load (N)", family="Arial", fontsize="medium", fontweight="semibold")
    ax.set_title(
        "Load-Displacement Chart for USW Joint - Material Name",
        family="Arial",
        fontsize="medium",
        fontweight="semibold",
    )
    ax.set(
        xlim=(0, 1.1 * data["Extension_mm"].max()),
        ylim=(0, 1.1 * data["Force_N"].max()),
    )
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(labelsize="small")

    ax.fill_between(
        data["Extension_mm"],
        0,
        data["Force_N"],
        facecolor="#d0c7ff",
        alpha=0.5,
        label="Work to Failure",
    )
    ax.scatter(
        data["Extension_mm"],
        data["Force_N"],
        s=4,
        c="#b787b3",
        marker="D",
        alpha=1,
        label="Test-Data",
    )
    ax.legend(loc="upper left", fontsize="x-small")


def plotChart(data):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    formatChart(data, fig, ax)
    plt.savefig("outputs/plots/test.png")
    plt.close(fig)


def main():
    source = "outputs/cleaned-data.csv"
    data = importData(source)
    plotChart(data)


if __name__ == "__main__":
    main()
