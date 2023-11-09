import matplotlib.pyplot as plt


def function_f1_convex(x: int):
    return x*x  # just to show my function is x^2


def function_f1_convex_derivative(x: int):
    return 2*x  # derivative of the convex function is 2*x


def function_f2_non_convex(x: int):
    return x*x*x  # my non-convex function is -x^2


def function_f2_non_convex_derivative(x: int):
    return 3*x*x  # derivative of the non-convex function is -2*x


def function_f1_convex_gradient(first: int, index: int, n: float):
    while index != 0:
        second = first - n * function_f1_convex_derivative(first)
        first = second
        index -= 1

    return second


def function_f2_non_convex_gradient(first: int, index: int, n: float):
    while index != 0:
        second = first - n * function_f2_non_convex_derivative(first)
        first = second
        index -= 1

    return second


def main():
    x0 = int(input("\u001b[95m" + "Please insert x0, integer: "))
    n = float(input("Please insert an n, learning rate: "))

    values1 = []
    values2 = []

    index_values = input("Please input the indexes of x: ")
    index_values = index_values.split()
    index_values = [int(i) for i in index_values]

    for i in range(0, len(index_values)):
        values1.append(function_f1_convex_gradient(x0, index_values[i], n))

    for i in range(0, len(index_values)):
        values2.append(function_f2_non_convex_gradient(x0, index_values[i], n))

    last_index = index_values[len(index_values)-1]
    print()

    print("These are the values for f(x)=x^2: ")
    print(values1)
    print()

    plt.figure(figsize=(8, 6))
    plt.plot(index_values, values1, color='#fc72b7', marker='p', linestyle='-')
    plt.xlabel('indexes of x', color='#fc72b7')
    plt.ylabel('values of xi', color='#fc72b7')
    plt.scatter(last_index, 0, color='#29b8ff', marker='*', s=150)
    plt.title("The graph of the gradient, f(x) = x^2 - convex", color='#fc72b7')
    plt.grid(True)
    plt.show()

    print("These are the values for f(x)=x^3: ")
    print(values2)

    plt.figure(figsize=(8, 6))
    plt.plot(index_values, values2, color='#fc72b7', marker='p', linestyle='-')
    plt.xlabel('indexes of x', color='#fc72b7')
    plt.ylabel('values of xi', color='#fc72b7')
    plt.scatter(last_index, 0, color='#29b8ff', marker='*', s=150)
    plt.title("The graph of the gradient, f(x) = x^3 - non-convex", color='#fc72b7')
    plt.grid(True)
    plt.show()

    print()
    print("The tables have been generated!")


main()
