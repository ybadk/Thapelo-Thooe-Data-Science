
#importing regular expression library

import re

name = "python is the 1 "

digitCount = re.sub("[^0-9]", "", name)
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.sub("[ \s]", "", name)


print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))
