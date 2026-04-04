## Approach
Put all values in a **hash set** for O(1) membership. For each number `num`, only start counting a sequence when the number before it (`num - 1`) is **not** in the set (so each sequence is counted once, from its minimum element). Count upward with `current + 1` while it exists in the set and track the streak length.

## Complexity
- **Time:** O(n) — each value is visited as a “start” at most once, and each value is stepped past in the inner `while` at most once across the whole run.
- **Space:** O(n) for the set (same order as the distinct input values).

## Key Insights
- If we used sorting it would be O(n log n); the set + “start only if no left neighbor” pattern keeps work linear.
- Duplicates in `nums` do not change the answer; a set deduplicates items naturally.
- The inner loop does not make the overall complexity quadratic because each integer belongs to at most one extended chain and is advanced over a bounded number of times in total.
