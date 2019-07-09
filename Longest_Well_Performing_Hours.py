def findLongest(hours, limit):
    period = 0
    length_of_well_performing_periods = [0]
    hours = hours + hours
    #print(hours)
    for daily_hours in hours:
        if daily_hours >= limit:
            period = period + 1
            #length_of_well_performing_periods.append(period)
        else :
            if period != 0:
                length_of_well_performing_periods.append(period)
                period = 0
    return max(length_of_well_performing_periods)

hours = [5, 10, 8, 9]
limit = 8
print(findLongest(hours, limit))


"""
period = 0
    for daily_hours in hours:
        if daily_hours >= limit:
            period = period +1
    return period
    """
