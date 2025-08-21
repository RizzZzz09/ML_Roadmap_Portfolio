def main():
    prices = ["1 299", "999", "2,499"]
    integers = [int(number.replace(" ", "").replace(",", "")) for number in prices]
    print(integers)


if __name__ == "__main__":
    main()
