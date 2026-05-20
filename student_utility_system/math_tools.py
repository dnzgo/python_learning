def calculate_average(scores):
    sum = 0
    for score in scores:
        sum += score
    average = sum / len(scores)

    return average

def find_highest(scores):
    return max(scores)

def find_lowest(scores):
    return min(scores)
