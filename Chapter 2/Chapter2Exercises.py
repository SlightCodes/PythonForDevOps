import pathlib

path = pathlib.Path("/Users/guzzi/PycharmProjects/PythonForDevOps/Chapter 2/bookofdreams.txt")
path.write_text(("Added this line using the pathlib module")
print(path.read_bytes())

#-------------------------------
# file_path = 'bookofdreams.txt'
# open_file = open(file_path, 'r')
# text = open_file.readlines()
#
# print(len(text))
# print(open_file)
# print(text[0])
#
# open_file.close()
#-------------------------------

# text = '''export STAGE=PROD
# export TABLE_ID=token-storage-1234'''
#
# with open('.envrc', 'w') as opened_file:
#     opened_file.write(text)



