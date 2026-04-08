import re
text = "Python is easy"
#print(re.match("Python", text))
#print(re.match("pRiYaNsHu", text))

text1= "cat bat rat mat at statate sttaat state"
#print(re.findall("at", text1))

#print(re.sub("easy","difficult", text))

text2= "apple, banana; grapes"
#print(re.split("[,;]", text2))

#print(re.findall(".at",text1))

text3="abc123"
#print(re.findall("[a-z]+", text3))

text4="aaditya aditya aaaditya @ditya"
print(re.findall("a{2}ditya", text4))