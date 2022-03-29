import pythonping
import time 
import os
while True:
    response_list = ping('8.8.8.8', size=40, count=1)
    (int(response_list.rtt_avg_ms))
    time.sleep(1)
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import os
import pythonping

plt.style.use('fivethirtyeight')

x_values = []
y_values = []

index = count()

def animate(i):
    response_list = ping('8.8.8.8', size=40, count=1)
    x_values.append(next(index))
    y_values.append(int(response_list.rtt_avg_ms))
    plt.cla()
    plt.plot(x_values, y_values)

ani = FuncAnimation(plt.gcf(), animate, 1000)

time.sleep(1)
plt.tight_layout()
plt.show()
