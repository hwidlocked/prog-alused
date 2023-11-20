"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if time <= 4 and time >= 1:
        return False
    elif time <= 24 and time >= 18:
        return True
    elif time <= 17 and time >= 5 and coffee_needed:
        return True
    return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b and a == c:
        if a == 5:
            return 10
        return 5
    elif a == b or a == c:
        return 0
    else:
        return 1


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    kg = small_baskets + big_baskets * 5
    if kg == ordered_amount:
        return small_baskets
    return -1