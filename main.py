#MapPlot.py
#Name: Meg Aerni
#Date: 11.16.2025
#Assignment: Lab 10

import ingredients
import pandas
import matplotlib as plt
import matplotlib.pyplot as plt

report = ingredients.get_report()
cholList = []
proteinList = []

for item in report:
    chol = item["Data"]["Cholesterol"]
    protein = item["Data"]["Protein"]
    if chol <= 500:
        cholList.append(chol)
        proteinList.append(protein)

df = pandas.DataFrame({"Cholesterol": cholList,
                        "Protein": proteinList})

df.plot(kind = 'scatter', x = 'Cholesterol', y = 'Protein')
#plt.plot(cholList, proteinList, 'ro')
plt.savefig("output")

#Interpretation: This scatter plot shows that most foods have low cholesterol and low-to-moderate protein levels, while only a few items have both high cholesterol and high protein. That suggests many protein-rich foods (like beans or fish) don’t necessarily have extreme cholesterol values. Visualizing the data made this clear because the cluster near the lower-left corner highlights where most foods fall, while a few outliers to the right show the high-cholesterol exceptions.