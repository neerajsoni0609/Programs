input_range = [[1, 3], [2, 6], [8, 10], [15, 18]]

def merge_intervals(intervals):
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        # If merged list is empty or there's no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge overlapping intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
        
calculated_range = merge_intervals(input_range)
print(calculated_range)

# Question asked in Persistent