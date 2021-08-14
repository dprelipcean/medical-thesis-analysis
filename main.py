import matplotlib.pyplot as plt
import pandas as pd
from numpy import isnan


def filter_data(values_x, values_y):
    array_length = len(values_x)
    for index in range(array_length):
        index_searched = array_length - index - 1
        value_x = values_x[index_searched]
        value_y = values_y[index_searched]

        if isnan(value_x) or isnan(value_y):
            values_x.pop(index_searched)
            values_y.pop(index_searched)
    return values_x, values_y


file = 'Chestionar date licenta.xlsx'
df = pd.read_excel(file, engine='openpyxl',  sheet_name='Sheet1')


dict = {
    'Care este sexul dumneavoastră biologic?': "SEX",
        'Vârsta împlinită în ani': "VARSTA",
    'Înălțimea dumneavoastră (în cm)': "INALTIME",
    'Greutatea dumneavoastră (în kilograme)': "GREUTATE",
    'Sunteți fumător? Da -1; Nu - 0 ': "FUMATOR",
    'Sunteți diagnosticat cu diabet? Da -1; Nu - 0': "DIABET",
    'Ați suferit vreodată un infarct miocardic? Nu - 0; Da - 1': "INFARCT",
    'Ați urmat vreodată un tratament cu antidepresive triciclice?  Nu - 0; Da - 1': "ANTIDEPRESIVE",
    'Urmați un tratament medicamentos pentru depresie sau boală coronariană? Nu - 0; Da - 1': "MEDICAMENTE",
    'SCOR MORISKY-4': "MORISKY-4",
    'Scor scala TICS': "TICS",
    'SCOR SCALA CAGE': "CAGE",
    'SCOR SCALA GAD7': "GAD7",
    'SCOR SCALA PHQ-9': "PHQ-9",
    'SCOR SCLeio': "SCLeio",
}

plot_customization = {
    "SEX": [2, [-0.5, 1.5]],
    "VARSTA": [10, [-0.5, 100.5]],
    "INALTIME": [20, [-0.5, 20.5]],
    "GREUTATE": [20, [-0.5, 20.5]],
    "FUMATOR": [2, [-0.5, 1.5]],
    "DIABET": [2, [-0.5, 1.5]],
    "INFARCT": [2, [-0.5, 1.5]],
    "ANTIDEPRESIVE": [2, [-0.5, 1.5]],
    "MEDICAMENTE": [2, [-0.5, 1.5]],
    "MORISKY-4": [5, [-0.5, 4.5]],
    "TICS": [3, [-0.5, 2.5]],
    "CAGE": [5, [-0.5, 4.5]],
    "GAD7": [23, [-0.5, 22.5]],
    "PHQ-9": [23, [-0.5, 22.5]],
    "SCLeio": [9, [-0.5, 8.5]],
}

df.rename(columns=dict,
          inplace=True)

keys = df.columns.values

for key1 in keys:
    for key2 in keys:
        if key2 in ["SEX", "VARSTA", "INALTIME", "GREUTATE", "FUMATOR", "DIABET", "INFARCT", "ANTIDEPRESIVE", "MEDICAMENTE"]:
            continue
        data_x = list(df[key1])
        data_y = list(df[key2])


        data_x, data_y = filter_data(data_x, data_y)
        hist, xbins, ybins, im = plt.hist2d(
            data_x, data_y,
            bins=[plot_customization[key1][0], plot_customization[key2][0]],
            range=[plot_customization[key1][1], plot_customization[key2][1]],
            cmap='Blues'
        )

        for i in range(len(ybins) - 1):
            for j in range(len(xbins) - 1):
                plt.text(xbins[j] + 0.5, ybins[i] + 0.5, hist.T[i, j],
                        color="orange", ha="center", va="center", fontweight="bold")

        plt.xlabel(key1)
        plt.ylabel(key2)

        plt.xticks(range(plot_customization[key1][0]))
        plt.yticks(range(plot_customization[key2][0]))

        plt.colorbar()
        # plt.show()

        plt.savefig(f"results/{key1}_vs_{key2}.png")
        plt.clf()