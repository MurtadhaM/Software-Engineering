import pandas as pd
import os
import matplotlib.pyplot as plt


class NameFrequency:

    def __init__(self):
        self.data_frame = pd.DataFrame()
        self.data_set = pd.DataFrame()
        self.plot_group1 = pd.DataFrame()
        self.plot_group2 = pd.DataFrame()
        self.result = []

    # Load CSV file
    # dropping null value columns to avoid errors
    # making data frame
    def preparingData(self, file_name, column_name):
        data = pd.read_csv(file_name)
        data.dropna(inplace=True)
        data_frame = dict(data[column_name].str.split(" ", n=1, expand=True))
        self.data_frame = data_frame
        if isinstance(self.data_frame, pd.DataFrame):
            return True
        return False

    # making separate data set column from specific data frame
    def selectingColumn(self, column_name, column_index):
        self.data_set[column_name] = self.data_frame[column_index]
        return self.data_set[column_name].count()

    def preparingVisualizationData(self, column_name1, column_name2):

        if column_name1 not in self.data_set.columns or column_name2 not in self.data_set.columns:
            return False
        self.plot_group1 = self.data_set.groupby([column_name1]).size().reset_index(name='counts').sort_values('counts',
                                                                                                               ascending=False).head(
            20)
        self.plot_group2 = self.data_set.groupby([column_name2]).size().reset_index(name='counts').sort_values('counts',                                                                                                               ascending=False).head(
            20)
        return True

    # plot
    def plot(self, column_name1, column_name2):
        plt.figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')
        plt.subplot(121)  # 1 row, 2 columns, 1 order
        plt.barh(self.plot_group1[column_name1], self.plot_group1["counts"])
        plt.title('Frequency of ' + column_name1)
        plt.xlabel('Count')
        plt.ylabel(column_name1)

        plt.subplot(122)  # 1 row, 2 columns, 2 order
        plt.barh(self.plot_group2[column_name2], self.plot_group2["counts"])
        plt.title('Frequency of ' + column_name2)
        plt.xlabel('Count')
        plt.ylabel(column_name2)

        plt.show()

    def inputIndex(self, input_value):
        while True:
            try:
                userInput = int(input(input_value))
            except ValueError:
                print("Not an Integer! Try again.")
                continue
            else:
                if userInput not in [0,1]:
                    print("Index does not exist! Try again.")
                    continue
                return userInput
                break

    def inputFileName(self, input_value):
        while True:
            userInput = input(input_value)
            if not os.path.isfile(userInput):
                print("File not exist! Try again.")
                continue
            else:
                return userInput
                break

    def inputColumnName(self, input_value, data_frame):
        while True:
            data = pd.read_csv(data_frame)
            userInput = input(input_value)
            if not userInput in data.columns:
                print("Column does not exist! Try again.")
                continue
            else:
                return userInput
                break



