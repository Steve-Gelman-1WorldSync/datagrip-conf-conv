import xml.etree.ElementTree as ET

from dbconfig import DBConfig


def load_xml(filename):
   tree = ET.parse(filename)
   return tree.getroot()


def extract_db_configurations(root):
    configurations = []
    component = root.find('component')
    for configuration in component.iter('data-source'):
        name = configuration.get('name')
        remarks = configuration.find('remarks').text if configuration.find('remarks') is not None else ''
        url = configuration.find('jdbc-url').text if configuration.find('jdbc-url') is not None else ''

        configurations.append(DBConfig(name, remarks, url))

    return configurations

if __name__ == '__main__':
    root = load_xml('/Users/sgelman/Downloads/settings/options/dataSources.xml')
    databases = extract_db_configurations(root)
    for database in databases:
        print(database)
        print()
