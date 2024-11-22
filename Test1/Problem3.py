def giai_ma(code_str):
    package = []
    current_str = ""
    current_num = 0

    for char in code_str:
        if char.isdigit():
            current_num = current_num*10 + int(char)
        elif char == "[":
            package.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == "]":
            prev_str, num = package.pop()
            current_str = prev_str + current_str * num
        else:
            current_str = current_str + char
    
    return current_str

code_str = "2[abc]3[cd]ef"
print("code_str: 2[abc]3[cd]ef \n", "giai ma: ",giai_ma(code_str))