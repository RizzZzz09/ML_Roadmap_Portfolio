def main():
    score = int(input("How many points did you score: "))

    if not (0 <= score <= 100):
        print("Invalid score")
    elif 90 <= score <= 100:
        print("A")
    elif 80 <= score <= 89:
        print("B")
    elif 70 <= score <= 79:
        print("C")
    elif 60 <= score <= 69:
        print("D")
    else:
        print("F")


if __name__ == "__main__":
    main()
