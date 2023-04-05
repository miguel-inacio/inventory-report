from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():

    products_list = [
        {
            "id": "44",
            "nome_do_produto": "Papel A4",
            "nome_da_empresa": "Dunder Mifflin",
            "data_de_fabricacao": "2005-03-24",
            "data_de_validade": "2033-08-10",
            "numero_de_serie": "101",
            "instrucoes_de_armazenamento": "em lugar seco",
        },
        {
            "id": "2",
            "nome_do_produto": "Papel sulfite",
            "nome_da_empresa": "Dunder Mifflin",
            "data_de_fabricacao": "2005-09-20",
            "data_de_validade": "2025-02-13",
            "numero_de_serie": "201",
            "instrucoes_de_armazenamento": "em lugar seco",
        },
    ]
    report_decorator = ColoredReport(SimpleReport)
    decorated_report = report_decorator.generate(products_list)

    assert decorated_report == (
        "\033[32mData de fabricação mais antiga:\033[0m "
        "\033[36m2005-03-24\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m "
        "\033[36m2025-02-13\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m "
        "\033[31mDunder Mifflin\033[0m"
    )
