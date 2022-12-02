def multiple_choice(prompt, options, key):
    """"""
    for k in range(len(key)):
        key[k] = key[k].capitalize()
    print("-------------------------------------------------------------------")
    print(prompt)
    for i in range(len(options)):
        print(options[i], "- Key:", key[i])
    print("-------------------------------------------------------------------")
    answer = input("Answer here: ")
    answer = answer.capitalize()
    print("-------------------------------------------------------------------")
    while answer not in key:
        print("Your answer was not found in the key.")
        answer = input("Answer here: ")
        answer = answer.capitalize()
        print("-------------------------------------------------------------------")
    return options[key.index(answer)]
