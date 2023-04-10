from inventory_report.importer.importer import Importer
from xmltodict import parse
from xml import parsers


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):

        # if not path.endswith("xml"):
        #     raise ValueError("Arquivo inválido")

        with open(path) as file:
            try:
                read_file = file.read()
                formatted_file = parse(read_file)
                return formatted_file["dataset"]["record"]
            except parsers.expat.ExpatError:
                raise ValueError("Arquivo inválido")
