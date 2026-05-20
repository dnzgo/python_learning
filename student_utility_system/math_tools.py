def calculate_average(scores):
    """
    this function finds average of the given list
    """
    sum = 0
    for score in scores:
        sum += score
    average = sum / len(scores)

    return average


def find_highest(scores):
    """
    this function finds highest number in given list
    """
    return max(scores)


def find_lowest(scores):
    """
    this function finds lowest number in given list
    """
    return min(scores)
