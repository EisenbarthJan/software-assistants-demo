from app.utils import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 0.1) == 90
    assert calculate_discount(50, 0.2) == 40