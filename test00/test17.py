def superEggDrop(K, N):
    drops = 0  # the number of eggs dropped 鸡蛋掉落的数量
    floors = [
        0 for _ in range(K + 1)
    ]  # floors[i] is the number of floors that can be checked with i eggs floor [i]是可以用鸡蛋检查的楼层数

    while floors[
            K] < N:  # until we can reach N floors with K eggs 直到我们可以用K蛋到达N层

        for eggs in range(K, 0, -1):
            floors[eggs] += 1 + floors[eggs - 1]
        drops += 1

    return drops


if __name__ == "__main__":
    K = 3
    N = 14
    step = superEggDrop(K, N)
    print(step)
