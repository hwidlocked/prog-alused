def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False
    assert students_study(24, False) is True
    assert students_study(15, False) is False
    assert students_study(15, True) is True