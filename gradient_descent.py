import numpy as np
import matplotlib.pyplot as plt


def gradient(h=0.1, size=20, info=True):
    bounds = np.array([[-10, 10]])
    inputs = []
    outputs = []
    solutions = []
    evolutions = []
    x = 0

    def derivative(x):
        return 3 * x ** 2 - 1

    for _ in range(1000):
        x = bounds[:, 0] + np.random.rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
        y = x ** 3 - 3
        inputs.append(x)
        outputs.append(y)

    for _ in range(size):
        solutions.append(x)
        evolutions.append(x ** 3 - 3)
        gradient = derivative(x)
        new_x = x - h * gradient
        if info == 1:
            print(f'{_ + 1}){x} - {h} * {gradient} = {new_x}')
        x = new_x
    plt.scatter(inputs, outputs)
    plt.scatter(solutions, evolutions, color='red')
    plt.show()


if __name__ == '__main__':
    gradient()


