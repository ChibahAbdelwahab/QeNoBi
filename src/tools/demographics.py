from pandas import np


def age_class(age):
    """User age to range classes """
    age = np.int(age)
    if age <= 25:
        return 0
    if age <= 45:
        return 1
    return 2
