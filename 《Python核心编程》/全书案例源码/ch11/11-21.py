import numpy as np
import matplotlib.pyplot as plt

N = 20
theta = np.linspace(0.0, 2*np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

foo = plt.subplot(1, 1, 1, projection="polar")
bars = foo.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)
    
plt.show()
