import pytest
from src.taxes import calculate_taxes


@pytest.fixture
def prices():
    return [100, 200, 300]


@pytest.mark.parametrize("tax_rate, expected", [(10, [110, 220, 330]),
                                                (15, [115, 230, 345]),
                                                (20, [120, 240, 360]),])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_tax_rate(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate=-1)


def test_calculate_taxes_invalid_price():
    with pytest.raises(ValueError):
        calculate_taxes(prices=[0, -1], tax_rate=10)
