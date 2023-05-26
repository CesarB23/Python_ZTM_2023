import re
#regex101.com

pattern = re.compile("this")
string = "search inside of this text please"
a = re.search("this",string)
b = pattern.search(string)
# print(b.group())
# print(a.start())
# print(a.end())
# print(a.span())
# print(a.group())