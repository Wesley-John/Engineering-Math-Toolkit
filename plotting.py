import matplotlib.pyplot as plt

def plot_function(f, x_min, x_max, num_points=500):
    x_values = [x_min + i * (x_max - x_min) / num_points for i in range(num_points + 1)]
    y_values = [f(x) for x in x_values]

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Function Plot')
    plt.grid(True)
    plt.show()