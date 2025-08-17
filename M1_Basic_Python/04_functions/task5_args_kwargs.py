def demo(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


if __name__ == "__main__":
    demo(1, 2, 3, name="Danil", age=20)
