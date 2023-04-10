from json import loads, JSONDecodeError
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):

        # if not path.endswith("json"):
        # raise ValueError("Arquivo inválido")

        with open(path) as file:
            try:
                read_file = file.read()
                formatted_file = loads(read_file)
                return formatted_file
            except JSONDecodeError:
                raise ValueError("Arquivo inválido")
