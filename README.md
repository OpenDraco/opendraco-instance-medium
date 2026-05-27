# evomas-instance-medium

Synthetic SWE-bench instance for EvoMas APR evaluation — **medium** difficulty tier.

`rotate_left(arr, n)` slices the input with `arr[n:] + arr[:n]`. This works
for `n < len(arr)` but **silently breaks for `n >= len(arr)`**: e.g.
`rotate_left([1, 2, 3], 3)` returns `[]` instead of `[1, 2, 3]`, and
`rotate_left([1, 2, 3], 5)` returns `[]` instead of `[2, 3, 1]`.

The fix is one line — normalize `n` modulo the array length before the
slice (`n = n % len(arr)`). Test cases for `n == len(arr)` and
`n > len(arr)` will fail until the fix lands.

Single file, single-line fix, but spotting it requires reading the
failing tests to recognize the missing modulo arithmetic — a step above
the "easy" arithmetic-flip tier and a step below the "hard" mutable-
default-argument pitfall.
