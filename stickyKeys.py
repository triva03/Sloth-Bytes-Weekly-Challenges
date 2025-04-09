import re

def isLongPressed(original, typed):
    newString = ""
    for letter in original:
        newString += letter + "+"
    
    match = re.fullmatch(newString, typed)
    
    if match:
        return True
    else:
        return False

output1 = isLongPressed("alex", "aaleex")
print(output1)
output2 = isLongPressed("saeed", "ssaaedd")
print(output2)
output3 = isLongPressed("leelee", "lleeelee") 
print(output3)
output4 = isLongPressed("Tokyo", "TTokkyoh")
print(output4)
output5 = isLongPressed("laiden", "laiden")
print(output5)
