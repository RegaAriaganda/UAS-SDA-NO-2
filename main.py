def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    indices = []

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            indices.append(mid)
            # Cari lagi di sebelah kiri dan kanan jika ada angka yang sama
            left_idx = mid - 1
            right_idx = mid + 1
            while left_idx >= 0 and arr[left_idx] == target:
                indices.append(left_idx)
                left_idx -= 1
            while right_idx < len(arr) and arr[right_idx] == target:
                indices.append(right_idx)
                right_idx += 1
            return indices
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

arr = [19, 40, 10, 90, 2, 50, 60, 50, 1]

# Test Case 1
target1 = 1
result1 = binary_search(arr, target1)
if result1 is not None:
    print(f"Input: {target1}")
    print(f"Output: Angka {target1} ada di indeks ke {', '.join(map(str, result1))}")
else:
    print(f"Input: {target1}")
    print(f"Output: Angka {target1} tidak ada dalam array")

# Test Case 2
target2 = 50
result2 = binary_search(arr, target2)
if result2 is not None:
    print(f"Input: {target2}")
    print(f"Output: Angka {target2} ada di indeks ke {', '.join(map(str, result2))}")
else:
    print(f"Input: {target2}")
    print(f"Output: Angka {target2} tidak ada dalam array")

# Test Case 3
target3 = 100
result3 = binary_search(arr, target3)
if result3 is not None:
    print(f"Input: {target3}")
    print(f"Output: Angka {target3} ada di indeks ke {', '.join(map(str, result3))}")
else:
    print(f"Input: {target3}")
    print(f"Output: Angka {target3} tidak ada dalam array")
