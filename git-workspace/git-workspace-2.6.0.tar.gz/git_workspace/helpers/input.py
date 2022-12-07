def yes_no_input(prompt):
    while True:
        answer = input(f"{prompt} (y or n): ")
        if answer in ["y", "Y"]:
            return True
        elif answer in ["n", "N"]:
            return False
        else:
            continue
