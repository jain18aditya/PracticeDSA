"""
Given an array of intervals where intervals[i] = [start, end],
merge all overlapping intervals and return the result as a list
of non-overlapping intervals.

Intervals that touch (e.g., [1,4] and [4,5]) are considered overlapping.
"""

def merge(intervals):
    if not intervals:
        return []

    # Step 1: sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        # overlap
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged

def merge_int(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged

# Example
print(merge([[1,3], [2,6], [8,10], [15,18]]))
print(merge_int([[1,3], [2,6], [8,10], [15,18]]))

