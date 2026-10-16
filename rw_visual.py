from matplotlib.cm import Blues
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Kepp making new walks, as long as program is active
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(15, 9))
    # point_numbers = range(rw.num_points)
    ax.plot(
        rw.x_values,
        rw.y_values,
        linewidth=1,
        # c=point_numbers,
        # cmap=plt.cm.Blues,
        # edgecolors="none",
    )
    ax.set_aspect("equal")

    # Emphasize the first and last points
    ax.scatter(0, 0, c="green", edgecolors="black", s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="black", s=50)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n)")

    if keep_running == "n":
        break
