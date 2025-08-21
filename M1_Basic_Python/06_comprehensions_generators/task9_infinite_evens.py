def main():
    number = 0
    while True:
        yield number
        number += 2


if __name__ == "__main__":
    gen = main()
    result = []
    for _ in range(10):
        result.append(next(gen))
    print(result)
