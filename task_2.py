def main() -> int:
    N, w, d, P = map(int, input().split())

    sum = 0
    for i in range(1, N):
        sum += i * w

    if sum == P:
        return N
    else:
        return abs((P - sum)) // d


if __name__ == '__main__':
    print(f"Индекс горшка: {main()}")
