def main():
    names = [" Alice ", "", "Bob", "  Carol"]
    new_list = [name.strip() for name in names if name.strip()]
    new_list.sort(key=len)
    print(new_list)


if __name__ == "__main__":
    main()
