import matplotlib.pyplot as plt

import seaborn as sns

def show_dataframe_hist(
    df
):

    df.hist(
        bins=15,
        color='steelblue',
        edgecolor='black',
        linewidth=1.0,
        xlabelsize=8,
        ylabelsize=8,
        grid=False
    )

    plt.tight_layout(rect=(0, 0, 1.2, 1.2))
    plt.show()


def show_heatmap(
    df
):
    f, ax = plt.subplots(figsize=(10, 6))
    corr = df.corr()

    hm = sns.heatmap(round(corr, 2), annot=True, ax=ax, cmap="coolwarm", fmt='.2f',
                     linewidths=.05)
    f.subplots_adjust(top=0.93)
    t = f.suptitle('Correlation Heatmap', fontsize=8)
    plt.show()
