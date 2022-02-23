import pandas as pd
import pingouin as pg
import numpy as np

def Cronbach(df):
    """
    This method is wrapper for Pingouin's cronbach_alpha function, to present reliability of an instrument
    in the same manner as SPSS does.
    :param df:  An MxN dataframe, where M is the number of responders and N is the number of items.
                All values has to be numeric.
    :return:    None
                Prints out Cronbach's alpha value & CI; per item statistics; items correlation matrix;
                scale statistics; and per item analysis.
    """

    IQR = lambda x: x.quantile(0.75) - x.quantile(0.25)

    alpha = pg.cronbach_alpha(df)
    print(f"Number of items: {df.shape[1]}\tNumber of responders: {df.shape[0]}")
    print(f"Cronbach's alpha: {alpha[0]:.3f}, CI: {alpha[1][0]} - {alpha[1][1]}\n")

    print('Items statistics:\n------------------')
    print(df.aggregate(['mean', 'std', 'count']).T.round(3))

    print('\nItem inter-correlation matrix:\n--------------------------------')
    print(df.corr().round(3))

    print('\nScale statistics:\n------------------')
    print(pd.DataFrame(df.sum(axis=1).aggregate(['mean', 'var', 'std', 'median', IQR])).T)

    print('\nItem-Total statistics:\n-----------------------')
    temp = {'Scale mean if removed': [], 'Scale var if removed': [], 'Cronbach alpha if removed': []}
    for c in df.columns:
        d = df[df.columns.drop(c)]
        temp['Scale mean if removed'].append(d.sum(axis=1).mean())
        temp['Scale var if removed'].append(d.sum(axis=1).var())
        temp['Cronbach alpha if removed'].append(pg.cronbach_alpha(d)[0])
    print(pd.DataFrame(temp, index=df.columns))

# # example:
# # a not so elegant way to create a 4x20 dataframe with values between 1 and 7
# x1 = np.random.randint(1,7,20)
# x2 = x1 + np.random.randint(-3, 3, 20)
# x3 = x1 + np.random.randint(0, 5, 20)
# x4 = -x1
#
# df = pd.DataFrame({'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4})
# scale = np.where((df < 1) | (df > 7))
# new = np.random.randint(1,7,len(scale[0]))
# for c,(i,j) in enumerate(zip(scale[0], scale[1])):
#     df.iloc[i,j] = new[c]
# 
# Cronbach(df)
