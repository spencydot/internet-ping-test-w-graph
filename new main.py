from pythonping import ping
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

plt.style.use('dark_background')
x_values = []
y_values = []

index = count()

def animate(i):
    response_list = ping('www.google.com', size=40, count=1)
    x_values.append(next(index))
    y_values.append(int(response_list.rtt_avg_ms))
    plt.cla()
    plt.plot(x_values, y_values)
    time.sleep(0.9)
    plt.xlabel(int(response_list.rtt_avg_ms), fontsize=16)

ani = FuncAnimation(plt.gcf(), animate, 1000,)
plt.tight_layout()
plt.show()
