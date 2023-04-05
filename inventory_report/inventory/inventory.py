from abc import ABC, abstractmethod
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class ReportTypeStrategy(ABC):
    @abstractmethod
    def get_report(cls, report):
        raise NotImplementedError


class Simples(ReportTypeStrategy):
    @classmethod
    def get_report(cls, report):
        return SimpleReport.generate(report)


class Completo(ReportTypeStrategy):
    @classmethod
    def get_report(cls, report):
        return CompleteReport.generate(report)


importers = [CsvImporter, JsonImporter, XmlImporter]


class Inventory:
    @classmethod
    def read_report_file(cls, path: str) -> list[dict]:
        importer_strategy = path.split(".")[-1].capitalize() + "Importer"
        used_importer = [
            importer
            for importer in importers
            if importer_strategy in str(importer)
        ][0]
        formatted_file = used_importer.import_data(path)
        return formatted_file

    @classmethod
    def import_data(cls, path: str, type: str):
        report = cls.read_report_file(path)
        type_class = type.capitalize()
        return eval(type_class).get_report(report)
