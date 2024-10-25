def Input():
    name = str(input("What is ur name: "))
    age = int(input("How old are you: "))

    sex = str(input("What is your gender, Male of Female: "))
    status = str(input("Your status? Single/ Date/ Married: "))
    return name, age, sex, status

def Process(name, age, sex, status):
    message = None
    result = None
    if age < 18:
        message = f"{name}, too young to have lover, focus on study first!"
    else:
        if status == "Date" or status == "Married":
            result = f"{name}, dont cheating on your love!"
        else:
            result = f"{name}, still single let date with someone!"


    return message, result

def Output(name, message, result):
    if message:
        print(message)
    print(result)

name, age, sex, status = Input()
message, result = Process(name, age, sex, status)
Output(name, message, result)
