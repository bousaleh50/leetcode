def myAtoi(s: str):
    if (s.isnumeric()):
        return int(s)
    number = "0"
    is_first = True
    sign = ""
    for i in s:
        if(i == " "):
            continue
        elif(i == "-" and is_first):
            sign = "-"
            continue
        elif(i.isnumeric()):
            number += i
        else:
            break
        is_first = False

    return int(number)*(-1) if sign=="-" else int(number)


print(myAtoi("words and 987"))
