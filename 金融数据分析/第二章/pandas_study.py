import numpy as np
def part1():
    d1 = [1, 2, 3, 4, 5, 6]
    d2 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    d3 = [(1, 2, 3, 4), (1, 2, 3, 4), (1, 2, 3, 4)]
    a1 = np.array(d1)
    a2 = np.array(d2)
    a3 = np.array(d3)

    for i in range(1, 4):
        print(eval(f'a{i}'))

def part2():
    pass

if __name__ == '__main__':
    part1()