######################################################################
# script to fetch data for members of Brazil's lower house
# Initial date: 15/09/2016
######################################################################
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import squarify

df = pd.read_csv('../data/lower_house.csv', header=0, index_col=[0])
df_con = df.groupby('partido')['partido'].count().sort_values(ascending=False,
                                                              inplace=False)
parties = dict((k.encode('utf-8'), df_con[k]) for k in df_con.index)

_coalision = ["PMDB", "PSDB", "DEM", "PPS", "PR", "PP", "PV", "PTB", "PRP",
              "PSD", "PRB", "PROS", "PSL", "PSC", "PSB"]

_not_committed = ["PMDB", "PR", "PP", "PTB", "PRP", "PSD", "PRB"]

def _coalision_col(party):
    return 'blue' if party in _coalision else 'red'

def _committed(party):
    return 0.3 if party in _not_committed else 0.6


def gen_chart(title):
    x = 0.
    y = 0.
    width = 100.
    height = 100.

    values = parties.values()

    normed = squarify.normalize_sizes(values, width, height)
    rects = squarify.squarify(normed, x, y, width, height)

    shapes = []
    annotations = []
    counter = 0

    for r in rects:
        shapes.append(
            dict(
            type ='rect',
                x0=r['x'],
                y0=r['y'],
                x1=r['x']+r['dx'],
                y1=r['y']+r['dy'],
                line=dict(width=2),
                fillcolor=_coalision_col(parties.keys()[counter]),
                opacity=_committed(parties.keys()[counter])
            )
        )
        annotations.append(
        dict(
            x=r['x']+(r['dx']/2),
            y=r['y']+(r['dy']/2),
            text=parties.keys()[counter],
            showarrow=False
        )
        )
        counter = counter + 1


    # For hover text
    trace0 = go.Scatter(
        x=[r['x']+(r['dx']/2) for r in rects],
        y=[r['y']+(r['dy']/2) for r in rects],
        text=[str(v) for v in values],
        mode='text')

    layout = dict(
        title="{}".format(title),
        font=dict(size=18),
        height=700,
        width=700,
        xaxis=dict(showgrid=False, zeroline=False,
                   ticks='', showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False,
                   ticks='', showticklabels=False),
        shapes=shapes,
        annotations=annotations,
        hovermode='closest')

    # Without hovertext
    return dict(data=[go.Scatter()], layout=layout)


figure = gen_chart("Temer's Coalision Base - Lower House")
py.image.save_as(figure, filename='treemap_lower_house.jpeg', format='jpeg')
