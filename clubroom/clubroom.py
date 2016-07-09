import sys

rl = lambda: sys.stdin.readline()

def dist(n, m):
    x = abs(int(n[0]) - int(m[0]))
    y = abs(int(n[1]) - int(m[1]))
    return max(x, y)


def check(current, array):
    # print("  current -> %s" % current)
    # print("  array -> %s" % array)
    if len(array) == 0:
        return "G"

    count = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            # for k in range(len(current)):
            # print("     --> A1: %d, B1: %d" % (current[j], array[i][j]))
            if current[j] >= array[i][j]:
                count += 1
                # print("       c --> %d" % c)
                # print("%d %d" % (array[i][j], current[j]))

    if count == (len(array) * len(array[0])):
        return "B"

    return "G"


def calc(arrayN, arrayM):
    result = []
    for n in arrayN:
        result2 = []
        for m in arrayM:
            result2.append(dist(n.split(" "), m.split(" ")))
        result.append(result2)

    print_str = ""

    for arr1 in range(len(result)):
        s = check(result[arr1], result[0:arr1])
        print_str += s + " "

    print(print_str)

def main():
    T = int(rl())
    # print("T: %d" % T)

    for i in range(T):
        MN = rl().split(" ")
        M = int(MN[0])
        N = int(MN[1])

        arrayM = []
        arrayN = []

        for m in range(M):
            arrayM.append(rl().replace('\n', ''))

        for n in range(N):
            arrayN.append(rl().replace('\n', ''))

        # print("M:%d" % M)
        # print(arrayM)
        # print("N:%d" % N)
        # print(arrayN)
        calc(arrayN, arrayM)
        # print("\n")


if __name__ == "__main__":
    main()
