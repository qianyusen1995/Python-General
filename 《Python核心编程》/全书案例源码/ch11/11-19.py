plt.subplot2grid((3, 3), (0, 0))
plt.subplot2grid((3, 3), (0, 1), rowspan=2)
plt.subplot2grid((3, 3), (0, 2), rowspan=3)
plt.subplot2grid((3, 3), (1, 0))
plt.subplot2grid((3, 3), (2, 0), colspan=2)
plt.show()