from main import calculate_sum

def test_calculate_sum():
    assert calculate_sum([1, 2, 3]) == 6
    assert calculate_sum([2, 2, 2]) == 6
    assert calculate_sum([-1, 0, 1]) == 0
