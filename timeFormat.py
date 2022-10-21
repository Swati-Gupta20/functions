def clock(time):
    if time[-2:]=='am' and time[:2]=='12':
        return '00'+time[2:-2]
    elif time[-2:]=='pm' and time[:2]=='12':
        return time[:-2]
    elif time[-2:]=='am':
        return time[:-2]
    elif time[-2:]=='pm':
        return str(int(time[:2])+12)+time[2:-2]
print(clock(input('enter time:-')))
 

