import pytest
from app import dias_vividos

def test_dias_vividos_valor_correcto():
    """Debe retornar la cantidad correcta de días para una edad válida."""
    assert dias_vividos(1) == 365
    assert dias_vividos(10) == 3650
    assert dias_vividos(0) == 0
    assert dias_vividos(100) == 36500

def test_dias_vividos_valor_negativo():
    """Debe lanzar ValueError si la edad es negativa."""
    with pytest.raises(ValueError, match="La edad no puede ser negativa"):
        dias_vividos(-5)
