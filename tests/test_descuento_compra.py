import pytest

from descuento_compra import calcular_total


def test_sin_descuento():
    assert calcular_total(500) == 500
    assert calcular_total(1000) == 1000  # límite


def test_con_descuento():
    assert calcular_total(1200) == 1080
    assert calcular_total(1001) == pytest.approx(1001 - 100.1)


def test_valores_decimales():
    assert calcular_total(1500.75) == pytest.approx(1500.75 - (1500.75 * 0.10))


def test_cero():
    assert calcular_total(0) == 0
