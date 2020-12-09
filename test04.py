import re

file = open('E.txt')
keyStart = '<Package name="References">'
keyEnd = '</Package>'
buff = file.read()
pat = re.compile(keyStart + '(.*?)' + keyEnd, re.S)
result = pat.findall(buff)
print(result)
file.close()

#look unicode character reading