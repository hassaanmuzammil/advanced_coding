arrival = [1,2,3,3,5,7,8,9,10]
duration = [2,1,2,1,2,1,5,1,3]

def update_start_end_map(start_end_map, earliest_finish):
    start_end_map_updated = []
    for i,j in start_end_map:
        if i >= earliest_finish:
            start_end_map_updated.append((i,j))
    return start_end_map_updated  

def get_earliest_finish(start_time,start_end_map):
    end_times = []
    for i,j in start_end_map:
        if i >= start_time:
            end_times.append(j)
    return min(end_times)

def max_events_scheduler(arrival,duration):
    events_list = []
    max_events = 0
    start_time = arrival[0]

    if len(arrival) < 2:
        return len(arrival)
    
    else:
        start_end_map = get_start_end_map(arrival,duration)
        #print(start_end_map)
        
        while len(start_end_map) > 0:
            earliest_finish = get_earliest_finish(start_time,start_end_map)
            #print(earliest_finish)
            start_end_map = update_start_end_map(start_end_map, earliest_finish)
            max_events += 1
            #print(start_end_map)
        
        return max_events

max_events_scheduler(arrival,duration)
#returns 6
