from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto_test = Product(
        44,
        "Papel A4",
        "Dunder Mifflin",
        "2005-03-24",
        "2013-05-16",
        201,
        "em lugar seco",
    )

    representation = str(produto_test.__repr__())

    assert representation == (
        "O produto Papel A4"
        " fabricado em 2005-03-24"
        " por Dunder Mifflin com validade"
        " até 2013-05-16"
        " precisa ser armazenado em lugar seco."
    )
