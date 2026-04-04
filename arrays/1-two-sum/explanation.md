## Approach
Scan `nums` left to right. Keep a map `index` from **value → index** for elements seen so far. For each `num` at `i`, compute `find = target - num`. If `find` is already in `index`, those two indices are the answer; otherwise store `index[num] = i` and continue.

## Complexity
- **Time:** O(n) — one pass over `nums`; map lookups and inserts are O(1) on average.
- **Space:** O(n) — the map holds at most one entry per distinct value seen before the match.

## Key Insights
- Complement `target - num` turns the pair search into a single lookup.
- Storing **index** (not just presence) gives the required return format.
- Processing in one pass works because when you see the second number of the pair, the first is already in the map.
