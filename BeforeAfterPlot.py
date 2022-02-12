import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('classic')
plt.rcParams['axes.grid'] = True


def BAplot(data, beforeLabel="Before", afterLabel='After', ax=None):
    """
    data        : Pandas Ix3 dataframe, where I is the number of samples.
                  Columns order should be ID, values before, values after
    beforeLabel : Name of data label before intervention (default: Before)
    afterLabel  : Name of data label after intervention (default: After)
    ax          : Matplotlib axes instance to plot into (default: None)
    """
    if (data.shape[1] != 3) or (type(data) != pd.DataFrame):
        print('data has to be Ix3 dataframe')
        return None

    data.columns = ['ID', beforeLabel, afterLabel]
    ax = plt.axes() if ax == None else ax

    meltData = data.melt(id_vars='ID', value_vars=[beforeLabel, afterLabel])
    sns.barplot(data=meltData,
                x="variable",
                y="value",
                alpha=0.5,
                ci=None,
                ax=ax
                )
    ax.set_xlabel('')
    ax.set_ylabel('')

    bRand = np.random.normal(loc=0, scale=0.025, size=len(data))
    aRand = np.random.normal(loc=0, scale=0.025, size=len(data))

    ax.plot([np.zeros_like(data[beforeLabel]) + bRand, np.ones_like(data[beforeLabel]) + aRand],
            [data[beforeLabel].values, data[afterLabel].values], color='black')

    ax.scatter([np.zeros_like(data[beforeLabel]) + bRand, np.ones_like(data[beforeLabel]) + aRand],
               [data[beforeLabel].values, data[afterLabel].values], edgecolor='black', color='white')

    miny = (data[[beforeLabel, afterLabel]].values.min() * 0.75) - 0.05
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(miny, ax.get_ylim()[1])
    return ax

# # # example:
# data = pd.read_csv('BAplot - FakeData.csv')
# ax = BAplot(data, beforeLabel= "pre-intervention", afterLabel='post-intervention')
# plt.savefig('before_after_plot.jpg',dpi = 300)
# plt.show()