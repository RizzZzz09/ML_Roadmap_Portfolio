def main():
    list_of_fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counting_dict = {
        key: sum(1 for word in list_of_fruits if word == key) for key in set(list_of_fruits)
    }
    print(counting_dict)


if __name__ == "__main__":
    main()
