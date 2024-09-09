def main(list, target):
    low = list[0]
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif target < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    print(main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))