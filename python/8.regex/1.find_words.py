import re

txt = " in 2015 i want to learning persuasice technology"
# x = re.search("^i.*technology$", txt) ===> "<re.Match object; span=(0, 40), match='i want to learning persuasice technology'>"
# x = re.findall("e", txt)              ===> "['e', 'e', 'e', 'e']"
# x = re.findall("[a-m]",txt)           ===> "['i', 'a', 'l', 'e', 'a', 'i', 'g', 'e', 'a', 'i', 'c', 'e', 'e', 'c', 'h', 'l', 'g']"
x = re.findall("\d", txt)
print(x)
