def main(num: int) -> int:
    res = (num >> 8) | (num << 8)
    return res


if __name__ == '__main__':
    num = int(input('Введите число: '))
    ans = main(num)
    print(ans)
