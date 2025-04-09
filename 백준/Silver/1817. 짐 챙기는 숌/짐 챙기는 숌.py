def main():
    N, M = map(int, input().split())

    if N == 0:
        print(0)
        return

    books = list(map(int, input().split()))

    box_count = 0
    current_box_weight = 0

    for weight in books:
        if current_box_weight + weight <= M:
            current_box_weight += weight
        else:
            box_count += 1
            current_box_weight = weight

    if current_box_weight > 0:
        box_count += 1

    print(box_count)


if __name__ == '__main__':
    main()
