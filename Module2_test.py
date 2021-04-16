import random
import math
import matplotlib.pyplot as plt
y = [math.sin(i/100)+random.uniform(-0.1,0.1) for i in range(314)]
x = [i for i in range(314)]
plt.plot(x, y)
plt.show()