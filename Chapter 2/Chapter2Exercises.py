# import pathlib
#
# path = pathlib.Path("/Users/guzzi/PycharmProjects/PythonForDevOps/Chapter 2/bookofdreams.txt")
# path.write_text(("Added this line using the pathlib module")
# print(path.read_bytes())
# -------------------------------
# file_path = 'bookofdreams.txt'
# open_file = open(file_path, 'r')
# text = open_file.readlines()
#
# print(len(text))
# print(open_file)
# print(text[0])
#
# open_file.close()
# -------------------------------
# text = '''export STAGE=PROD
# export TABLE_ID=token-storage-1234'''
#
# with open('.envrc', 'w') as opened_file:
#     opened_file.write(text)
# ---------------------------------------------------------------------------------------
# import json
# from pprint import pprint
#
# with open('sample.json', 'r') as opened_file:
#     glossEntry = json.load(opened_file)
#
#    # pprint(glossEntry)
#
#     glossEntry['glossary']['GlossDiv']['GlossList']['GlossEntry']['ID'] = 'ALTERED'
#
#     pprint(glossEntry)
#
# with open('sample.json', 'w') as opened_file:
#     glossEntry = json.dump(glossEntry, opened_file)
# ---------------------------------------------------------------------------------------
# import yaml
# from pprint import pprint
#
# with open('verify-apache.yml', 'r') as opened_file:
#     verify_apache = yaml.safe_load(opened_file)
#
#     pprint(verify_apache[0]['vars']['http_port'])
#
#     verify_apache[0]['vars']['http_port'] = 443
#
# with open('verify-apache.yml', 'w') as opened_file:
#     yaml.dump(verify_apache, opened_file)
# -----------------------------------------------------------------------
# import xml.etree.ElementTree as ET
#
# tree = ET.parse('sample.xml')
#
# root = tree.getroot()
#
# print(root)
#
# for child in root:
#     print(child.tag, child.attrib)
#
# for book in root.findall('book'):
#     author = book.find('author').text
#     title = book.find('title').text
#
#     print(author, ':', title)
# -------------------------------------------------------------------------




