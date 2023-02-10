def distinctAverage(array):
    """
    Function to return distinct average from an array.
    """
    dist_ele = set(array)
    dist_len = len(dist_ele)
    result = sum(dist_ele)/ dist_len
    return ("%.3f" % result)
