import xml.etree.ElementTree as etree

xml = '\n'.join([input() for _ in range(int(input()))])

xml_tree = etree.ElementTree(etree.fromstring(xml))

print (len(xml_tree.getroot().attrib + sum([len(element.attrib) for element in xml_tree.findall('.//')]))
