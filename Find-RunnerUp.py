def findRunnerUp(arr):
    '''
    Function to find 2nd highest value in a sequence.
    '''
    runnerUpScore = sorted(set(arr))[-2]
    print(runnerUpScore)
    return

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    findRunnerUp(arr)    
