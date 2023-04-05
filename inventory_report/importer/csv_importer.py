import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str):

        if not path.endswith("csv"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            read_file = csv.DictReader(file)
            formatted_file = [row for row in read_file]
            return formatted_file
