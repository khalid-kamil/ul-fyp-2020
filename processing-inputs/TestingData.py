import sys
import os
from os import path

# from extensions import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

plt.style.use("classic")

import numpy as np
from numpy import trapz
import pymysql
from sqlalchemy import create_engine


class TestingData:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    def __init__(
        self,
        material,
        source,
        welding,
        db="materialtestsDB",
        user="khalid",
        pw="fyp2020",
        host="localhost",
        plots="outputs/plots",
    ):
        """
        Parameters
        ----------
        source : str
            The string directory of the file containing the testing data that the user would like to process
        database : str, optional
            The database connection properties to add the processed data to (default is "localhost, materialtestsDB, TestData, khalid, fyp2020")
        plots : str, optional
            The output directory to store plots of the precessed data
        """

        self.material = material
        self.source = source
        self.welding = welding
        self.db = db
        self.user = user
        self.pw = pw
        self.host = host
        self.plots = plots

        self.load(source, welding)
        self.process()
        self.output(material, db, user, pw, host)

    ### SUPPORT METHODS ###
    # Called in load() function. Checks if the directory provided for the source data is valid before loading into dataframe
    def isValidDirectory(self, source, welding):
        if not path.isfile(source) or not path.isfile(welding):
            sys.exit("Directory not found! Please try again.")

        print("Directories found: {} and {}".format(source, welding))

    # Called in loadToDataframe() function. Cleans data from excel file into a usable dataframe for processing.
    def cleanTestingData(self):
        print("Data loaded successfully.\nCleaning data...")
        self.cleaned_df = pd.DataFrame(
            columns=[
                "Specimen_no",
                "Curve_no",
                "Thickness_mm",
                "Width_mm",
                "Extension_mm",
                "Force_N",
            ]
        )

        self.testing_df = self.testing_df.dropna(how="all").reset_index(drop=True)
        self.lastRowIndex = self.testing_df.last_valid_index()
        self.index_df = self.testing_df[
            self.testing_df.iloc[:, 0] == "Curves for Specimen No:"
        ]
        self.specimenRowList = self.index_df.index.values.tolist()
        for row in range(len(self.index_df)):
            rangeStart = self.specimenRowList[row]
            if row == len(self.index_df) - 1:
                rangeEnd = self.lastRowIndex + 1
            else:
                rangeEnd = self.specimenRowList[row + 1]

            for index in range(rangeStart, rangeEnd):
                specimen = self.testing_df.iloc[rangeStart, 1]
                curve = self.testing_df.iloc[rangeStart + 1, 1]
                thickness = 1
                width = 1

                if index + 4 < rangeEnd:
                    extension = self.testing_df.iloc[index + 4, 0]
                    force = self.testing_df.iloc[index + 4, 1]
                else:
                    extension = None
                    force = None

                cleanedRow = {
                    "Specimen_no": specimen,
                    "Curve_no": curve,
                    "Thickness_mm": thickness,
                    "Width_mm": width,
                    "Extension_mm": extension,
                    "Force_N": force,
                }

                self.cleaned_df = self.cleaned_df.append(
                    cleanedRow,
                    ignore_index=True,
                )

        self.cleaned_df = self.cleaned_df.dropna(
            subset=["Extension_mm", "Force_N"], how="all"
        ).reset_index(drop=True)
        print("Data cleaned successfully.")

    # Called in load() function. Loads data into dataframe once confirmed to exist using isValidDirectory() function.
    def loadToDataframe(self, source, welding):
        self.testing_df = pd.read_excel(
            source, sheet_name=0, header=None, names=["Column 1", "Column 2"]
        )

        self.cleanTestingData()
        self.specimenCount = self.cleaned_df["Specimen_no"].nunique()
        print("Number of specimens found: {}".format(self.specimenCount))
        self.welding_df = pd.read_excel(welding, sheet_name=0, header=0)
        weldingHeader = self.welding_df.iloc[0]
        self.welding_df = self.welding_df[1:].reset_index(drop=True)
        self.welding_df.columns = weldingHeader

    # Called in process() function. Calculates stiffness for any one specimen.
    def calculateStiffness(self, initialExtension=0.2):
        self.maxLoadId = self.filtered_df["Force_N"].astype(float).idxmax()
        self.initialLength = int(round(self.maxLoadId * initialExtension))
        self.initialDisplacement = np.array(
            self.filtered_df["Extension_mm"][: self.initialLength], dtype=np.float64
        )
        self.initialLoad = np.array(
            self.filtered_df["Force_N"][: self.initialLength], dtype=np.float64
        )
        self.fit = np.polyfit(self.initialDisplacement, self.initialLoad, 1, cov=True)
        return round(self.fit[0][0], 3)

    # Called in process() function. Calculates max load for any one specimen.
    def calculateMaxLoad(self):
        return round(self.filtered_df["Force_N"].max(), 3)

    # Called in process() function. Calculates work to failure for any one specimen.
    def calculateWorkToFailure(self):
        return round(
            trapz(self.filtered_df["Force_N"], self.filtered_df["Extension_mm"]), 3
        )

    def formatChart(self, fig, ax, specimen):
        ax.scatter(
            self.filtered_df["Extension_mm"],
            self.filtered_df["Force_N"],
            color="#4290f5",
            alpha=0.4,
        )
        ax.scatter(
            self.filtered_df["Extension_mm"][self.maxLoadId],
            self.filtered_df["Force_N"][self.maxLoadId],
            color="red",
            # label="Max. Load = {} N".format(self.maxLoad),
        )
        # ax.fill_between(
        #     self.filtered_df["Extension_mm"],
        #     self.filtered_df["Force_N"],
        #     0,
        #     color="#4290f5",
        #     alpha=0.2,
        #     label="Work to Failure = {} Nmm".format(self.workToFailure),
        # )
        best_fit_y = self.fit[0][0] * self.initialDisplacement + self.fit[0][1]
        plt.plot(
            self.initialDisplacement,
            best_fit_y,
            "k",
            color="blue",
            linewidth=2,
            # label="Stiffness = {} N/mm".format(self.stiffness),
        )
        # Set plot labels and axis labels
        ax.set(
            title="Ultrasonic Welded Joint Test\n{} - Specimen {}".format(
                self.material, specimen + 1
            ),
            xlabel="Extension (mm)",
            ylabel="Force (N)",
        )
        plt.xlim(
            0,
            self.filtered_df["Extension_mm"].max()
            + 0.1 * self.filtered_df["Extension_mm"].max(),
        )
        plt.ylim(
            0,
            self.filtered_df["Force_N"].max() + 0.1 * self.filtered_df["Force_N"].max(),
        )

        # hide top and right ticks
        plt.axes().xaxis.tick_bottom()
        plt.axes().yaxis.tick_left()
        plt.grid(which="major", axis="both")
        plt.axes().xaxis.set_minor_locator(AutoMinorLocator())
        plt.axes().yaxis.set_minor_locator(AutoMinorLocator())
        plt.axes().tick_params(axis="both", which="major", labelsize="small")
        plt.legend(loc="upper left", fontsize="small", scatterpoints=1)

    # Called in process() function. Generates Load-Displacement charts for each specimen.
    def plotFigure(self, specimen):
        fig = plt.figure()
        ax = fig.add_subplot(
            111,
        )

        self.formatChart(fig, ax, specimen)

        fig.savefig(self.plotDirectory)
        plt.close(fig)

    # Called in process() function. Appends processed data for each specimen to processed_df Dataframe
    def addToProcessedDataframe(self, data):
        self.processed_df = self.processed_df.append(data, ignore_index=True)
        self.processed_df.to_csv("outputs/processeddf.csv", index=False)

    ### MAIN METHODS ###
    # Called when class is initialized. Checks if data exists and loads it to dataframe.
    def load(self, source=None, welding=None):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        # Check if directory provided at initialization is valid before loading into dataframe.
        self.isValidDirectory(source, welding)

        # Load testing data from source to dataframe
        self.loadToDataframe(source, welding)

    # Called when class is initialized. Calculates stiffness, max-load and work-to-failure for each specimen in the dataset.
    def process(self):
        print("Processing data...")
        # Creates an empty dataframe to append with processed data for each specimen
        self.processed_df = pd.DataFrame(
            columns=[
                "Specimen_no",
                "Curve_no",
                "Thickness_mm",
                "Width_mm",
                "Stiffness_N/mm",
                "Max-Load_N",
                "Work-To-Failure_Nmm",
                "Plot-Directory",
                "Welding-Conditions",
                "Welding-Energy",
                "Vibration-Amplitude",
                "Clamping-Pressure",
                "Peak-Power",
                "Collapse",
                "Time",
            ]
        )

        # Processes data for each specimen, generates a plot for it and appends to processed_df
        for specimen in range(self.specimenCount):
            print("Processing specimen: {}".format(specimen + 1))
            # Generates filtered dataframe for individual specimen for further processing
            self.filtered_df = self.cleaned_df.loc[
                self.cleaned_df["Specimen_no"] == specimen + 1
            ].reset_index(drop=True)

            # Calculate stiffness, max load and work to failure for individual specimen
            self.stiffness = self.calculateStiffness()
            self.maxLoad = self.calculateMaxLoad()
            self.workToFailure = self.calculateWorkToFailure()

            # Specify plot name and directory
            self.plotName = "Load-Displacement Chart - Specimen {}.png".format(
                specimen + 1
            )
            self.plotDirectory = "outputs/plots/{}".format(self.plotName)

            # Load processed data into object to append to processed dataframe
            self.processedData = {
                "Specimen_no": self.filtered_df["Specimen_no"].iloc[0],
                "Curve_no": self.filtered_df["Curve_no"].iloc[0],
                "Thickness_mm": self.filtered_df["Thickness_mm"].iloc[0],
                "Width_mm": self.filtered_df["Width_mm"].iloc[0],
                "Stiffness_N/mm": self.stiffness,
                "Max-Load_N": self.maxLoad,
                "Work-To-Failure_Nmm": self.workToFailure,
                "Plot-Directory": self.plotDirectory,
                "Welding-Conditions": self.welding_df.iloc[specimen][0],
                "Welding-Energy": self.welding_df.iloc[specimen][1],
                "Vibration-Amplitude": self.welding_df.iloc[specimen][2],
                "Clamping-Pressure": self.welding_df.iloc[specimen][3],
                "Peak-Power": self.welding_df.iloc[specimen][4],
                "Collapse": self.welding_df.iloc[specimen][5],
                "Time": self.welding_df.iloc[specimen][6],
            }

            # Add processed data to new dataframe
            self.addToProcessedDataframe(self.processedData)

            # Plot Chart
            self.plotFigure(specimen)

    # Called when class is initialized. Checks if checks if processed dataframe is generated and loads it to a database table.
    def output(self, material, db, user, pw, host):
        engine = create_engine(f"mysql+pymysql://{user}:{pw}@{host}/{db}")
        dbConnection = engine.connect()

        if self.processed_df.isnull().values.any():
            print("Error processing data.")
        else:
            try:
                frame = self.processed_df.to_sql(
                    self.material,
                    con=dbConnection,
                    if_exists="append",
                    chunksize=1000,
                    index=False,
                )
            except ValueError as vx:
                print(vx)
            except Exception as ex:
                print(ex)
            else:
                print("Data added to Table '{}' successfully.".format(self.material))
            finally:
                dbConnection.close()


test = TestingData(
    "Aluminium 5754-H111", "refData/Testing-Data.xlsx", "refData/Welding data.xlsx"
)
