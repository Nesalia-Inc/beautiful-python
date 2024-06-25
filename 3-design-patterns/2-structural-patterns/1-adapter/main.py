from typing import Protocol
import json 
import xml.etree.ElementTree as ET


class DataGetter(Protocol):
    def get(self) -> str: ...


class JSONData(DataGetter):
    def __init__(self, data : dict) -> None:
        self.data = data
        
    
    def get(self) -> str:
        return json.dumps(self.data)
    
    
class XMLData(DataGetter):
    def __init__(self, data : str) -> None:
        self.data = data 
        
        
    def get(self) -> str:
        return self.data
    
    
class XMLToJSONAdapter(JSONData):
    def __init__(self, xml_data : XMLData) -> None:
        self.xml_data = xml_data
        
    def get(self) -> str:
        xml_root = ET.fromstring(self.xml_data.get())
        json_data = self._xml_to_dict(xml_root)
        return json.dumps(json_data)
    
    def _xml_to_dict(self, element : ET.Element) -> dict[str, str] | str | None:
        if len(element) == 0:
            return element.text
        result : dict[str, str] = {}
        for child in element:
            result[child.tag] = self._xml_to_dict(child) # type: ignore
        return result
    
    
if __name__ == '__main__':
    xml_data = XMLData("<person><name>Alice</name><age>30</age></person>")
    adapter = XMLToJSONAdapter(xml_data)
    print("Adapted JSON Data:", adapter.get())