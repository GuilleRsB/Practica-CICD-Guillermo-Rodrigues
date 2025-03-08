import pytest
from app import dias_vividos

def test_dias_vividos():
    # Para 10 años se espera 3650 días (10 * 365)
    assert dias_vividos(10) == 3650, "Error: 10 años deberían dar 3650 días."
