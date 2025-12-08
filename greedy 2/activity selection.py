start = [10, 12, 20]
finish = [20,25,30]
# Output: 4

def activitySelection(start, finish):
        # pairing both together in one list
    activity = list(zip(start,finish))
    "sort on the basis of finish"
    activity.sort(key=lambda x :x[1])
        
    eTime = -1
    count = 0
        
    for s, e in activity :
        if s > eTime :
            
            eTime = e
            count += 1
    return count

print(activitySelection(start,finish))