def rotate_left(arr, n):
    """Rotate arr left by n positions.

    Example:
        rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    """
    if not arr:
        return arr
    return arr[n:] + arr[:n]
