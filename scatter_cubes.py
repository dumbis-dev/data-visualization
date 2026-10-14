import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=5, c=y_values, cmap=plt.cm.YlGnBu)

ax.set_xlabel("Value", fontsize=20)
ax.set_ylabel("Cubed Value", fontsize=20)

plt.show()
# plt.savefig("squares_plotx.png", bbox_inches="tight")
