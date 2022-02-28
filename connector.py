# We will use two libraries that are part of the Python distribution for working with
#XML and JSON: xml.etree.ElementTree and json as follows:

import xml.etree.ElementTree as etree
import json

#The JSONConnector class parses the JSON file and has a parsed_data() method
#that returns all data as a dictionary ( dict ). The property decorator is used to make
#parsed_data() appear as a normal variable instead of a method as follows:

class JSONConnector:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data



#The XMLConnector class parses the XML file and has a parsed_data() method that
#returns all data as a list of xml.etree.Element as follows:

class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)
   
    @property
    def parsed_data(self):
        return self.tree

        