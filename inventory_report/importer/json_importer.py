import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):

        if not path.endswith("json"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            read_file = file.read()
            formatted_file = json.loads(read_file)
            return formatted_file
