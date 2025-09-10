from collections import deque


def main():
    dq = deque([1, 2, 3, 4, 5])
    k = 2
    w = 3

    dq.rotate(k)
    rotated = " ".join(str(element) for element in dq)
    dq.rotate(-k)

    arr = list(dq)
    max_window_list = (
        [max(arr)] if w >= len(arr) else [max(arr[i : i + w]) for i in range(len(arr) - w + 1)]
    )
    max_window = " ".join(str(element) for element in max_window_list)

    print(f"rotated: {rotated}")
    print(f"window_max: {max_window}")


if __name__ == "__main__":
    main()
