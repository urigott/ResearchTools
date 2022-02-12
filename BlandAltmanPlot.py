import matplotlib.pyplot as plt
import numpy as np

def bland_altman(data1, data2):
    if len(data1) != len(data2):
        print ("Datasets size mismatch")
        return

    mn = (data1 + data2) / 2
    diff = data1 - data2

    plt.figure(figsize=(10, 7))
    plt.scatter(mn, diff, color='gray')
    plt.plot([mn.min(), mn.max()], [diff.mean(), diff.mean()], lw='1.5')

    s = "Mean = " + str(round(diff.mean(), 2))
    plt.text(mn.max() - 1 / 2 * mn.std(), diff.mean(), s, fontweight='bold')

    plt.plot([mn.min(), mn.max()], [diff.mean() + 1.96 * diff.std(),
                                    diff.mean() + 1.96 * diff.std()], ls='--', lw='1.5', color='red')

    s = "+1.96 SD = " + str(round(diff.mean() + 1.96 * diff.std(), 2))
    plt.text(mn.max() - 1 / 2 * mn.std(), diff.mean() + 1.96 * diff.std(), s, fontweight='bold')

    plt.plot([mn.min(), mn.max()], [diff.mean() - 1.96 * diff.std(),
                                    diff.mean() - 1.96 * diff.std()], ls='--', lw='1.5', color='red')
    s = "-1.96 SD = " + str(round(diff.mean() - 1.96 * diff.std(), 2))
    plt.text(mn.max() - 1 / 2 * mn.std(), diff.mean() - 1.96 * diff.std(), s, fontweight='bold')

    plt.ylabel('Difference between methods')
    plt.xlabel('Mean of methods')
    plt.title('Bland-Altman plot')
    plt.show()

# # example:
# bland_altman(np.random.normal(size=50), np.random.normal(size=50))