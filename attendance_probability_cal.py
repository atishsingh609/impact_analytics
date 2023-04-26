memo = {}


def counts_ways(n, k):
    if (n, k) in memo:
        return memo[(n, k)]

    # Base cases
    if k >= 4:
        return 0
    elif n == 0:
        return 1
    ways = counts_ways(n-1, k+1) + counts_ways(n-1, 0)
    memo[(n, k)] = ways
    return ways


def probability_of_missing(n):
    total_ways = counts_ways(n, 0)
    miss_ways = 0
    for i in range(1, n+1):
        miss_ways += counts_ways(n-i, 1)

        # calculate the probility
        probability = miss_ways/total_ways
        return f"{miss_ways}/{total_ways}"


if __name__ == "__main__":
    input_n = input("provide number of days: ")
    print("Total number of attending class is", counts_ways(int(input_n), 0))
    print("Probability of missing ", probability_of_missing(int(input_n)))



