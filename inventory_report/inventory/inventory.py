from abc import ABC, abstractmethod
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


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


class Inventory:
    @classmethod
    def read_report_file(cls, path: str) -> list[dict]:
        with open(path) as file:
            read_file = csv.DictReader(file)
            formatted_file = [row for row in read_file]
            return formatted_file

    @classmethod
    def import_data(cls, path: str, type: str):
        report = cls.read_report_file(path)
        type_class = type.capitalize()
        return eval(type_class).get_report(report)
