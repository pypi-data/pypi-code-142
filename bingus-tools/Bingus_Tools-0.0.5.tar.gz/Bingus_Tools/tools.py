def random_number(start:int, end:int):
    import random
    print(random.randint(start, end))
def random_letter(case:str):
    if case == "lower-case" or case == "lowercase" or case == "lower case":
        import string
        import random
        print(random.choice(string.ascii_lowercase))
    elif case == "upper-case" or case == "uppercase" or case == "upper case":
        import string
        import random
        print(random.choice(string.ascii_uppercase))
def random_string(length:int):
    import random
    import string
    print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=int(length))))
def random_words(numberofwords:int):
    for i in range(numberofwords):
        import random
        words = open('words.txt').read().splitlines()
        randomword = random.choice(words)
        print(randomword)
def random_country():
    import pycountry
    import random
    country = random.choice(list(pycountry.countries))
    print(f"Name = {country.name}")
    if hasattr(country, 'official_name'):
        print(f"Official Name = {country.official_name}")

