import pytest
from app import dias_vividos

def test_dias_vividos():
    # Con 10 años se espera 3650 días (10 * 365)
    resultado = dias_vividos(10)
    assert resultado == 3650, f"Se esperaba 3650 pero se obtuvo {resultado}"
