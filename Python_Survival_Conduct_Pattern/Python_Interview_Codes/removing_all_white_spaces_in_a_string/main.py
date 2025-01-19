
import re 

string = "K G O T H A T S O"
spaces = re.compile(r'\s+')
result = re.sub(spaces, "", string)
print(result)


print("\n\n")



