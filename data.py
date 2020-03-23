import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px


with open('auto-mpg.txt') as datafile:
    f = datafile.readlines()

data = [line.strip() for line in f]
data = [line.split('"') for line in data]
dataset = []
for line in data:
    line1 = line[0].split()
    line1.append(line[1])
    dataset.append(line1)

df_auto = pd.DataFrame(dataset, columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name'])
df_auto = df_auto.replace('?', np.nan)
df_auto['mpg'] = [float(item) for item in df_auto['mpg']]
df_auto['cylinders'] = [int(item) for item in df_auto['cylinders']]
df_auto['displacement'] = [float(item) for item in df_auto['displacement']]
df_auto['horsepower'] = [float(item) for item in df_auto['horsepower']]
df_auto['weight'] = [int(float(item)) for item in df_auto['weight']]
df_auto['acceleration'] = [float(item) for item in df_auto['acceleration']]
df_auto['model year'] = [int(item) for item in df_auto['model year']]
df_auto['origin'] = [int(item) for item in df_auto['origin']]
df_auto['km/L'] = df_auto['mpg']*0.42

#pd.DataFrame.to_csv(df_auto, 'auto_dataset.csv')
#df_auto.head()




# ## Analysis on the auto data


df_auto["origin"] = df_auto["origin"].replace(1, 'United States')
df_auto["origin"] = df_auto["origin"].replace(2, 'Europe')
df_auto["origin"] = df_auto["origin"].replace(3, 'Japan')
df_auto["horsepower"] = df_auto.horsepower.fillna(0)


options = list(set(df_auto['cylinders']))
trace_list = []


Layout = go.Layout(xaxis=dict(showgrid=True, zeroline=True, showticklabels=True),
               yaxis=dict(showgrid=True, zeroline=True, showticklabels=True),
               yaxis_title="miles per gallon",
               xaxis_title="Weight (kg)",
               title='weight x mpg',
                )

for option in options:
    trace = go.Scatter(y=df_auto.loc[df_auto['cylinders'] ==option].mpg,
            x=df_auto.loc[df_auto['cylinders'] ==option].weight,
            name = '{} cylinders'.format(option),
            mode='markers'
            )
    trace_list.append(trace)
x1 = df_auto.groupby('origin', as_index=False).count().origin
y1 = df_auto.groupby('origin', as_index=False).count().name
trace2 = go.Bar(x = x1 , y = y1, name='background')

fig = go.Figure(data=trace_list, layout=Layout)
fig


x1 = df_auto.groupby('origin', as_index=False).count().origin
y1 = df_auto.groupby('origin', as_index=False).count().name
trace2 = go.Bar(x = x1 , y = y1, name='background')
fig = go.Figure(data=trace2, layout=Layout)
fig


df_auto["cylinders"] = df_auto["cylinders"].astype(str)
fig =px.scatter(df_auto, x='weight', y='mpg', color='cylinders', trendline="ols", marginal_x='violin', marginal_y = 'box', title='Relation between mpg and weight of the car')
fig 

fig = px.scatter_matrix(df_auto, dimensions=['weight', 'mpg'], color='origin')
fig 

fig = px.scatter(df_auto, x='weight', y='mpg', color='origin', trendline=False, marginal_x='violin', marginal_y = 'box')
fig

fig = px.scatter(df_auto, x="weight", y="mpg", animation_frame="model year",
                 size='horsepower',color="origin", hover_name="name",
           log_x=False, size_max=45, range_x=[1000,5000], range_y=[5,50])
fig

