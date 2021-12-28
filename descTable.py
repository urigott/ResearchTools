import pandas as pd
from IPython.display import display

def descTable(data, group = None, r = 1):
    """
    :param data: Pandas DataFrame
    :param group: Grouping variable
    :param r: number of decimals for rounding
    :return: strings data frame of mean (SD) of all columns, grouped by `group`
    """
    if group:
        l = list(data.columns)

        m = data.groupby(group)[l].mean().T.round(r).astype(str)
        s = data.groupby(group)[l].std().T.round(r).astype(str)

        t = (m + ' (' + s + ')')
        return t
    else:
        m = data.mean().T.round(r).astype(str)
        s = data.std().T.round(r).astype(str)

        t = (m + ' (' + s + ')')
        return t

# example:
data = pd.DataFrame({'gender': ['m', 'm', 'm', 'f', 'm', 'f', 'f', 'f'],
                     'height': [1.76, 1.83, 1.6, 1.65, 1.88, 1.72, 1.59, 1.61],
                     'weight': [83, 70, 59, 59, 70, 90, 72, 42]
                     })

display(descTable(data = data,
                  group = 'gender',
                  r = 1))