from csv import DictReader
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str):

        with open(path) as file:
            try:
                read_file = DictReader(file)
                formatted_file = [row for row in read_file]
                # -> DictReader() não dispara erro ao
                # ler arquivo de outras extensões.
                # Linha necessária para disparar erro forçado
                formatted_file[0]["id"]
                return formatted_file
            except KeyError:
                raise ValueError("Arquivo inválido")
