from app import dias_vividos


def test_dias_vividos():
    # Para 10 años se esperan 3650 días
    assert dias_vividos(10) == 3650  # nosec
