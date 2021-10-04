from fractions import Fraction


def iteration(matrix, x_i, accuracy, steps):
    new_x = x_i.copy()
    for i, var in enumerate(matrix):
        new_x[i] = var[-1] / matrix[i][i]
        for j, v in enumerate(var[:-1]):
            if j != i:
                new_x[i] -= v / matrix[i][i] * new_x[j]
    steps.append(new_x)
    if max([abs(new_x[i] - x_i[i]) for i in range(len(x_i))]) <= accuracy:
        return new_x
    else:
        return iteration(matrix, new_x, accuracy, steps)


def zeidel(matrix, accuracy=0.001):
    x = []
    steps = []
    for i, var in enumerate(matrix):
        sum_ = 0
        for j, v in enumerate(var[:-1]):
            if j != i:
                sum_ += abs(v)
        if abs(matrix[i][i]) < sum_:
            return None, None
        x.append(0)
    x = iteration(matrix, x, accuracy, steps)
    return x, steps
