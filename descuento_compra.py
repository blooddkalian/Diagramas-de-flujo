"""Calcula el total a pagar por una compra con posible descuento.

Si el monto supera 1000 pesos se aplica un 10% de descuento.
"""

def calcular_total(monto: float) -> float:
    """Devuelve el total a pagar según la regla de descuento.

    Args:
        monto: monto original de la compra.

    Returns:
        total con descuento aplicado si corresponde.
    """
    if monto > 1000:
        return monto - (monto * 0.10)
    else:
        return monto


if __name__ == "__main__":
    try:
        entrada = input("Ingrese el monto de la compra: ")
        monto = float(entrada)
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")
        exit(1)

    total = calcular_total(monto)
    print(f"El total a pagar es: {total}")
