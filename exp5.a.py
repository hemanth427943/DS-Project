import matplotlib.pyplot as plt
x=[5,6,7,8]
y=[5,12,15,19]
plt.plot(x,y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.savefig("line_plot.png")
plt.show()