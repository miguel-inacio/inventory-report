from inventory_report.inventory.product import Product


def test_cria_produto():
    produto_test = Product(
        44,
        "Dunder Mifflin",
        "Papel A4",
        "2005-03-24",
        "2013-05-16",
        201,
        "Coloque na TV e ria bastante",
    )

    assert produto_test.id == 44
    assert produto_test.nome_do_produto == "Dunder Mifflin"
    assert produto_test.nome_da_empresa == "Papel A4"
    assert produto_test.data_de_fabricacao == "2005-03-24"
    assert produto_test.data_de_validade == "2013-05-16"
    assert produto_test.numero_de_serie == 201
    assert (
        produto_test.instrucoes_de_armazenamento
        == "Coloque na TV e ria bastante"
    )
