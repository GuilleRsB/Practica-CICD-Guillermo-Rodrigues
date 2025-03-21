from app import dias_vividos


def test_dias_vividos():
    """Verifica que se calculen correctamente los días vividos."""
    assert dias_vividos(10) == 3650  # nosec
    assert dias_vividos(0) == 0  # nosec
    assert dias_vividos(1) == 365  # nosec
