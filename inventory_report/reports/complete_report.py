from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report: list[dict]) -> str:
        base_str = super().generate(report)
        companies_quantities = cls.get_most_common_company(report)
        companies_and_quantities = "".join(
            f"- {tup[0]}: {tup[1]}\n" for tup in companies_quantities
        )
        return (
            f"{base_str}\n"
            "Produtos estocados por empresa:\n" + companies_and_quantities
        )
