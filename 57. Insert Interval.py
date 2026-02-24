class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for i, interval in enumerate(intervals):
            # The new interval comes before the current interval
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                # Append all remaining intervals at once for optimal speed
                result.extend(intervals[i:])
                return result
            
            # The new interval comes after the current interval
            elif newInterval[0] > interval[1]:
                result.append(interval)
                
            # Overlap exists, merge into the newInterval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # Add the final interval if it was merged to the very end
        result.append(newInterval)
        return result
