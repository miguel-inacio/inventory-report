from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def get_oldest_manufacturing_date(cls, report: list[dict]):
        all_manufacturing_dates = [
            entry["data_de_fabricacao"] for entry in report
        ]
        oldest_date = min(all_manufacturing_dates)
        # -> dentre tantas datas que já passaram, pegue a
        # data mais longe de hoje
        # 2023-04-03 está mais perto de 2023-04-04 do que 2023-03-23
        # e 2023-04-03 é também MAIOR que 2023-03-23 na comparação!
        return oldest_date

    @classmethod
    def get_nearest_expiration_date(cls, report: list[dict]):
        now = datetime.today().strftime("%Y-%m-%d")
        all_expiration_dates = [
            entry["data_de_validade"]
            for entry in report
            if entry["data_de_validade"] >= now
            # -> pega apenas as datas maiores ou
            # iguais que o valor da data de agora
            # 2023-05-04
            # 2023-08-01 -> será maior
        ]
        nearest_expiration_date = min(all_expiration_dates)
        # -> dentre tantas as datas futuras, pegue a data mais perto de hoje
        # 2023-04-07 está mais perto de 2023-04-04 do que 2025-08-01
        return nearest_expiration_date

    @classmethod
    def get_most_common_company(cls, report: list[dict]):
        companies = [entry["nome_da_empresa"] for entry in report]
        companies_and_frequency = Counter(companies)
        return companies_and_frequency.most_common()

    @classmethod
    def generate(cls, report: list[dict]):
        oldest_manufacturing_date = cls.get_oldest_manufacturing_date(report)
        nearest_expiration_date = cls.get_nearest_expiration_date(report)
        company_with_more_products = cls.get_most_common_company(report)

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products[0][0]}"
        )
