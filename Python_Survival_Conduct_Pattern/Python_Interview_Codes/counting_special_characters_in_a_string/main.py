

count = 0


def count_sp_char(string) :
    sp_char = "!@#$?%^&*(){}:;~`"

    count = 0

    for i in string :
        if i in sp_char:
            count+=1
            return count


text = "Hello ! How are you? specialchars!"


result = count_sp_char(text)

print(count)
