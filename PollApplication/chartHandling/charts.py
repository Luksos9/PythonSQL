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


def create_bar_chart(polls):
    figure = plt.figure(figsize=(10, 10))
    figure.subplots_adjust(bottom=0.35)  # gives more room underneath (works without it too)
    axes = figure.add_subplot(1, 1, 1)
    axes.set_title("Polls and their total votes")
    axes.set_ylabel("Vote count")

    axes.bar(
        range(len(polls)),  # how wide (x coordinates)
        [poll[1] for poll in polls],  # how many % of total voices were for this poll (height)
        tick_label=[poll[0] for poll in polls]  # labels for each bar
    )
    plt.xticks(rotation=30, ha="center")  # adds rotation, and center alignment to labels

    return figure
