import matplotlib.pyplot as plt
import pandas as pd

dataSource = \
    'https://raw.githubusercontent.com/COVID19-Malta/COVID19-Cases/master/COVID-19%20Malta%20-%20Aggregate%20Data%20Set.csv'
field1 = 'Date'
field2 = 'New Cases'
field3 = 'Active Cases'
field4 = 'Total Cases'


def retrieveData(url):
    return pd.read_csv(url, error_bad_lines=False, delimiter=',')


def parseCSV(data):
    return data[field1].tolist(), \
           data[field2].tolist(), \
           data[field3].tolist(), \
           data[field4].tolist()


def plotGraph(xdata, y1data, y2data, y3data):
    def labelDataPoints(dataset, x, y, rotation):
        for a, b in zip(xdata, dataset):
            label = "{}".format(b)
            plt.annotate(label, (a, b), textcoords="offset points", xytext=(x, y), ha='center',
                         va='center', size=7, weight='bold', rotation=rotation)

    def plotSeries(dataset, datasetname, colour):
        plt.plot(xdata, dataset, color=colour, linestyle='--', linewidth=2, marker='^', markerfacecolor=colour,
                 markersize=3, antialiased=True, label=datasetname)

    # Plot Data
    plotSeries(y1data, field2, 'red')
    plotSeries(y2data, field3, 'blue')
    # plotSeries(y3data, field4, 'green')

    # Label data points
    labelDataPoints(y1data, 0, -10, 0)
    labelDataPoints(y2data, 0, 10, 0)
    # labelDataPoints(y3data, 0, 10, 40)

    # Display graph
    plt.title('Covid-19 Malta')
    plt.xlabel('Date')
    plt.ylabel('Cases - Daily, Active, Total')
    plt.xticks(rotation=90)
    plt.autoscale(enable=True)
    plt.legend()
    plt.show()


# MAIN
csvData = retrieveData(dataSource)
dataCols = parseCSV(csvData)
plotGraph(dataCols[0], dataCols[1], dataCols[2], dataCols[3])
