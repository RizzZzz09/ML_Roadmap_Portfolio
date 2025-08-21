def main():
    a = [1, 2, 3, 2]
    b = [3, 4, 5]
    new_list = []

    for number in a + b:
        if number in new_list:
            continue

        new_list.append(number)

    print(new_list)


if __name__ == "__main__":
    main()
