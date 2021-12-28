import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")

mathScore_list = df["math score"].to_list()

fig = ff.create_distplot([mathScore_list], ["math"])
fig.show()

mean = sum(mathScore_list)/len(mathScore_list)
print("mean of this data is", mean)