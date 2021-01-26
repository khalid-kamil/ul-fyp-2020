import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np

def importData(source):
    df = pd.read_csv(source)
    data = df[df["Specimen_no"] == 1]
    ########## START - MANAGE THE PRELOAD ##########
    offsetValue = data["Force_N"][0]
    for i in data.index:
        data.at[i, "Force_N"] -= offsetValue
    print(data)
    ########## END - MANAGE THE PRELOAD ##########
    return data


def formatChart(data, maxLoadId, maxLoad, fig, ax):
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
    ax.scatter(
            data["Extension_mm"][maxLoadId],
            data["Force_N"][maxLoadId],
            color="#e63946",
            label="Max. Load = {} N".format(maxLoad),
        )
    
    # ax.scatter(
    #         data["Extension_mm"][50],
    #         data["Force_N"][50],
    #         color="#e63946",
    #         label="Max. Load = {} N".format(data["Force_N"][50]),
    #     )
    slope = round((data["Force_N"][50]-0)/(data["Extension_mm"][50]-0))
    ax.plot([0, data["Extension_mm"][50]],[0, data["Force_N"][50]], "r", label="Stiffness: {} N/mm".format(slope))

    ########## START - MANAGE THE STIFFNESS ##########
    value = 25
    initialData = data.head(value)
    z = np.polyfit(x=initialData.loc[:, "Extension_mm"], y=initialData.loc[:, "Force_N"], deg=1)
    p = np.poly1d(z)
    ax.plot(initialData["Extension_mm"],p(initialData["Extension_mm"]), "b--")
    ax.plot(initialData["Extension_mm"]+0.01,p(initialData["Extension_mm"]), "b--")
    initialData['trendline'] = p(initialData.loc[:, "Extension_mm"])
    print(initialData)
    ########## END - MANAGE THE STIFFNESS ##########
    ax.legend(loc="upper left", fontsize="x-small")


def plotChart(data, maxLoadId, maxLoad):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    formatChart(data, maxLoadId, maxLoad, fig, ax)
    plt.savefig("outputs/plots/test.png")
    plt.close(fig)


def main():
    source = "outputs/cleaned-data.csv"
    data = importData(source)
    maxLoadId = data["Force_N"].astype(float).idxmax()
    maxLoad = round(data["Force_N"].max(), 3)
    plotChart(data, maxLoadId, maxLoad)


if __name__ == "__main__":
    main()
