from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys

importers = [CsvImporter, XmlImporter, JsonImporter]


def main():
    try:
        file_path = sys.argv[1]
        report_type = sys.argv[2]
        picked_importer = file_path.split(".")[-1].capitalize() + "Importer"
        importer_class = [
            importer
            for importer in importers
            if picked_importer in str(importer)
        ][0]
        inventory = InventoryRefactor(importer_class)
        sys.stdout.write(inventory.import_data(file_path, report_type))
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")
