def main():
    temps = [36.6, 37.2, 38.5, 39.0, 36.9, 37.8, 38.1, 36.7]
    result = [temp for temp in temps if temp > 37.5]
    print(result)


if __name__ == "__main__":
    main()
