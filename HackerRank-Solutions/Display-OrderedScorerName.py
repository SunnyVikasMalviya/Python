def displayOrderedScorerName(records, score):
    '''
    Function to display names in ascending order from records having a certain score.
    Records = dict<str name, float score>
    '''
    names = sorted([x for x in records if records[x] == score])
    for name in names:
        print(name)

def findSecondLowestScore(arr):
    '''
    Function to find 2nd lowest score in a list of scores.
    '''
    return min([x for x in arr if x != min(arr)])

if __name__ == '__main__':
    records = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score
    secondLowestScore = findSecondLowestScore(list(records.values()))
    displayOrderedScorerName(records, secondLowestScore) 
    
    
