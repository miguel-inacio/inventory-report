from abc import ABC, abstractmethod
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.importer.importer import Importer

from collections.abc import Iterable


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


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer) -> None:
        self.importer = importer
        self.data = []

    def read_report_file(self, path: str):
        formatted_file = self.importer.import_data(path)
        self.data.extend(formatted_file)

    def import_data(self, path: str, type: str):
        self.read_report_file(path)
        type_class = type.capitalize()
        report = eval(type_class).get_report(self.data)
        return report

    def __iter__(self):
        return InventoryIterator(self.data)
