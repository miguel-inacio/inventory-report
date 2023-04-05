from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):

        if not path.endswith("xml"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            read_file = file.read()
            formatted_file = xmltodict.parse(read_file)
            return formatted_file["dataset"]["record"]
