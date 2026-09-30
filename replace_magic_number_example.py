"""
Exemplo de refactoring:
Replace Magic Number with Symbolic Constant
"""


# ============================================================
# ANTES: usando Magic Numbers
# ============================================================

def validate_order_before(total, items):
    # Os números 100 e 10 são Magic Numbers.
    # Não fica claro imediatamente o que eles representam.

    if total < 100:
        print("O pedido não atinge o valor mínimo.")

    if items > 10:
        print("O pedido excede o limite de produtos.")


# ============================================================
# DEPOIS: usando Symbolic Constants
# ============================================================

# As constantes dão significado aos valores.
MIN_ORDER_VALUE = 100
MAX_ITEMS_PER_ORDER = 10


def validate_order_after(total, items):
    # Agora o código deixa claro o significado de cada valor.

    if total < MIN_ORDER_VALUE:
        print("O pedido não atinge o valor mínimo.")

    if items > MAX_ITEMS_PER_ORDER:
        print("O pedido excede o limite de produtos.")


# ============================================================
# EXEMPLO DE USO
# ============================================================

if __name__ == "__main__":
    total = 80
    items = 12

    print("ANTES:")
    validate_order_before(total, items)

    print("\nDEPOIS:")
    validate_order_after(total, items)
