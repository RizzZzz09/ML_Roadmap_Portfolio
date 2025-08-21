def main(data, size):
    for i in range(0, len(data), size):
        yield data[i : i + size]


if __name__ == "__main__":
    gen = main([1, 2, 3, 4, 5, 6, 7], 3)
    for batch in gen:
        print(batch)
