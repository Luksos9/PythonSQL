import matplotlib.pyplot as plt


def create_pie_chart(options):
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)

    axes.pie(
        [option[1] for option in options],
        labels=[option[0] for option in options],
        autopct="%1.1%%"
    )

    return figure
