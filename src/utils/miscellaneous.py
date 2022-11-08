import csv
from itertools import zip_longest
import pandas as pd

def calDistribution(logFile):
    record = pd.read_csv(logFile, header=None)
    prob = [{} for _ in range(12)]

    for _,row in record.iterrows():
        prob[0][row[0]] = prob[0][row[0]] + 1 if prob[0].get(row[0]) else 1
        prob[1][row[1]] = prob[1][row[1]] + 1 if prob[1].get(row[1]) else 1
        prob[2][row[2]] = prob[2][row[2]] + 1 if prob[2].get(row[2]) else 1
        prob[3][row[3]] = prob[3][row[3]] + 1 if prob[3].get(row[3]) else 1
        prob[4][row[4]] = prob[4][row[4]] + 1 if prob[4].get(row[4]) else 1
        prob[5][row[5]] = prob[5][row[5]] + 1 if prob[5].get(row[5]) else 1
        prob[6][row[6]] = prob[6][row[6]] + 1 if prob[6].get(row[6]) else 1
        prob[7][row[7]] = prob[7][row[7]] + 1 if prob[7].get(row[7]) else 1
        prob[8][row[8]] = prob[8][row[8]] + 1 if prob[8].get(row[8]) else 1
        prob[9][row[9]] = prob[9][row[9]] + 1 if prob[9].get(row[9]) else 1
        prob[10][row[10]] =prob[10][row[10]] + 1 if prob[10].get(row[10]) else 1
        prob[11][row[11]] =prob[11][row[11]] + 1 if prob[11].get(row[11]) else 1

    output = []
    for i in prob:
        output.append(list(i.keys()))
        output.append(list(i.values()))

    exportData = zip_longest(*output, fillvalue = '')
    with open("out/prob/distribution.csv", 'w', newline='') as outputFile:
        wr = csv.writer(outputFile)
        wr.writerows(exportData)
        outputFile.close()