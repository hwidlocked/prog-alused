"""Does testing, very cool."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(1, True) is False


def test__students_study__night_without_coffee__no_studying():
    """During night without coffee students do not study."""
    assert students_study(4, False) is False


def test__students_study__evening_without_coffee__no_studying():
    """Does test, very cool."""
    assert students_study(24, False) is True


def test__students_study__evening_with_coffee__no_studying():
    """Does test, very cool."""
    assert students_study(24, True) is True


def test__students_study__day_without_coffee__no_studying():
    """During day without coffee students do not study."""
    assert students_study(17, False) is False


def test__students_study__day_with_coffee__no_studying():
    """During day with coffee students do study."""
    assert students_study(5, True) is True


def test__students_study__evening_edge_case():
    """Does test, very cool."""
    assert students_study(24, True) == students_study(18, True) is True


def test__students_study__evening_edge_case_no_coffee():
    """Does test, very cool."""
    assert students_study(24, False) == students_study(18, False) is True


def test__students_study__night_edge_case():
    """Does test, very cool."""
    assert students_study(1, True) == students_study(4, True) is False


def test__students_study__night_edge_case_no_coffee():
    """Does test, very cool."""
    assert students_study(1, False) == students_study(4, False) is False


def test__students_study__day_edge_case():
    """Does test, very cool."""
    assert students_study(17, True) == students_study(5, True) is True


def test__students_study__day_edge_case_no_coffee():
    """Does test, very cool."""
    assert students_study(17, False) == students_study(5, False) is False


def test__lottery__all_fives():
    """Does test, very cool."""
    assert lottery(5, 5, 5) == 10


def test__lottery__all_same_positive():
    """Does test, very cool."""
    assert lottery(3, 3, 3) == 5


def test__lottery__all_same_negative():
    """Does test, very cool."""
    assert lottery(-3, -3, -3) == 5


def test__lottery__all_same_zero():
    """Does test, very cool."""
    assert lottery(0, 0, 0) == 5


def test__lottery__a_b_same_c_diff():
    """Does test, very cool."""
    assert lottery(4, 4, 2) == 0


def test__lottery__a_c_same_b_diff():
    """Does test, very cool."""
    assert lottery(4, 2, 4) == 0


def test__lottery__b_c_same_a_diff():
    """Does test, very cool."""
    assert lottery(2, 4, 4) == 1


def test__lottery__all_diff():
    """Does test, very cool."""
    assert lottery(2, 3, 1) == 1


def test__fruit_order__all_zero():
    """Does test, very cool."""
    assert fruit_order(0, 0, 0) == 0


def test__fruit_order__zero_amount_zero_big():
    """Does test, very cool."""
    assert fruit_order(5, 0, 0) == 0


def test__fruit_order__zero_amount_zero_small():
    """Does test, very cool."""
    assert fruit_order(0, 2, 0) == 0


def test__fruit_order__zero_amount_others_not_zero():
    """Does test, very cool."""
    assert fruit_order(7, 2, 0) == 0


def test__fruit_order__only_big_exact_match():
    """Does test, very cool."""
    assert fruit_order(0, 2, 10) == 0


def test__fruit_order__only_big_not_enough_but_multiple_of_5():
    """Does test, very cool."""
    assert fruit_order(0, 10, 50) == 0


def test__fruit_order__only_big_not_enough():
    """Does test, very cool."""
    assert fruit_order(0, 2, 20) == -1


def test__fruit_order__only_big_more_than_required_match():
    """Does test, very cool."""
    assert fruit_order(0, 10, 20) == 0


def test__fruit_order__only_big_more_than_required_no_match():
    """Does test, very cool."""
    assert fruit_order(0, 10, 24) == -1


def test__fruit_order__only_small_match_more_than_5_smalls():
    """Does test, very cool."""
    assert fruit_order(7, 0, 7) == 7


def test__fruit_order__only_small_not_enough_more_than_5_smalls():
    """Does test, very cool."""
    assert fruit_order(6, 0, 7) == -1


def test__fruit_order__only_small_exact_match():
    """Does test, very cool."""
    assert fruit_order(1, 0, 1) == 1


def test__fruit_order__only_small_not_enough():
    """Does test, very cool."""
    assert fruit_order(1, 0, 3) == -1


def test__fruit_order__only_small_more_than_required():
    """Does test, very cool."""
    assert fruit_order(5, 0, 3) == 3


def test__fruit_order__match_with_more_than_5_smalls():
    """Does test, very cool."""
    assert fruit_order(50, 15, 100) == 25


def test__fruit_order__all_positive_exact_match():
    """Does test, very cool."""
    assert fruit_order(50, 10, 100) == 50


def test__fruit_order__use_all_smalls_some_bigs():
    """Does test, very cool."""
    assert fruit_order(10, 10, 10) == 0


def test__fruit_order__use_all_bigs_some_smalls():
    """Does test, very cool."""
    assert fruit_order(1, 19, 100) == -1


def test__fruit_order__not_enough():
    """Does test, very cool."""
    assert fruit_order(1, 1, 50) == -1


def test__fruit_order__enough_bigs_not_enough_smalls():
    """Does test, very cool."""
    assert fruit_order(4, 1, 10) == -1


def test__fruit_order__enough_smalls_not_enough_bigs():
    """Does test, very cool."""
    assert fruit_order(9, 1, 15) == -1


def test__fruit_order__not_enough_with_more_than_5_smalls():
    """Does test, very cool."""
    assert fruit_order(20, 1, 50) == -1


def test__fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Does test, very cool."""
    assert fruit_order(0, 24911, 124555) == 0


def test__fruit_order__match_large_numbers():
    """Does test, very cool."""
    assert fruit_order(121515, 24911, 124559) == 4