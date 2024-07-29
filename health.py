import time
print("hello in sysm healthy app")


def print_pause(statement):
    print(statement)
    time.sleep(2)


def get_input(prompt, validate):
    while True:
        value = input(prompt)
        if validate(value):
            return value
        else:
            print("Please enter a valid input.")


def is_valid_name(name):
    return len(name.strip()) > 0


def is_valid_age(age):
    return age.isdigit() and int(age) > 0


def is_valid_height(height):
    try:
        return float(height) > 0
    except ValueError:
        return False


def is_valid_weight(weight):
    try:
        return float(weight) > 0
    except ValueError:
        return False


def is_valid_sleep(hours):
    try:
        return 0 <= float(hours) <= 24
    except ValueError:
        return False


def is_valid_activity(level):
    try:
        level_val = int(level)
        return 1 <= level_val <= 10
    except ValueError:
        return False


name = get_input("Please enter your name: ", is_valid_name)
age = int(get_input("Please enter your age: ", is_valid_age))
height = int(get_input(
    "Please enter your height (in centimeters): ", is_valid_height))
weight = int(get_input(
    "Please enter your weight (in kilograms): ", is_valid_weight))
sleep_hours = int(get_input(
    "Please enter your average sleep hours per day: ", is_valid_sleep))
activity_level = int(get_input(
    "Please rate your daily activity level (1-10): ", is_valid_activity))


def preteens():
    if height < 130:
        print_pause("Yor are shorter than normal.")
    elif height > 150:
        print_pause("You are longer than normal")
    else:
        print_pause("height test passed.")

    if weight < 25:
        print_pause(
            "You are lighter than normal, please cheek for excessive slimness and eat more.")
    elif weight > 45:
        print_pause(
            "you are are heavier than Normal, please check for overweight and eat less.")
    else:
        print_pause("wight test passed.")

    if sleep_hours < 9:
        print_pause("According to your age, you need to sleep more.")
    elif sleep_hours > 12:
        print_pause("According to your age, you need to sleep less")
    else:
        print_pause("sleep test passed")


def teenagers():
    if height < 145:
        print_pause("Yor are shorter than normal.")
    elif height > 160:
        print_pause("You are longer than normal")
    else:
        print_pause("height test passed.")

    if weight < 35:
        print_pause(
            "You are lighter than normal, please cheek for excessive slimness and eat more.")
    elif weight > 60:
        print_pause(
            "you are are heavier than Normal, please check for overweight and eat less.")
    else:
        print_pause("wight test passed.")

    if sleep_hours < 8:
        print_pause("According to your age, you need to sleep more.")
    elif sleep_hours > 10:
        print_pause("According to your age, you need to sleep less")
    else:
        print_pause("sleep test passed")


def youth():
    if height < 150:
        print_pause("Yor are shorter than normal.")
    elif height > 175:
        print_pause("You are longer than normal")
    else:
        print_pause("height test passed.")

    if weight < 50:
        print_pause(
            "You are lighter than normal, please cheek for excessive slimness and eat more.")
    elif weight > 80:
        print_pause(
            "you are are heavier than Normal, please check for overweight and eat less.")
    else:
        print_pause("wight test passed.")

    if sleep_hours < 8:
        print_pause("According to your age, you need to sleep more.")
    elif sleep_hours > 10:
        print_pause("According to your age, you need to sleep less")
    else:
        print_pause("sleep test passed")


def adults():
    if height < 150:
        print_pause("Yor are shorter than normal.")
    elif height > 190:
        print_pause("You are longer than normal")
    else:
        print_pause("height test passed.")

    if weight > 50:
        print_pause(
            "You are lighter than normal, please cheek for excessive slimness and eat more.")
    elif weight < 100:
        print_pause(
            "you are are heavier than Normal, please check for overweight and eat less.")
    else:
        print_pause("wight test passed.")

    if sleep_hours > 7:
        print_pause("According to your age, you need to sleep more.")
    elif sleep_hours > 9:
        print_pause("According to your age, you need to sleep less")
    else:
        print_pause("sleep test passed")


if age >= 9 and age <= 12:
    preteens()
elif age >= 12 and age <= 14:
    teenagers()
elif age >= 14 and age <= 17:
    youth()
elif age >= 18:
    adults()
else:
    print("this app isn't made for your age")
