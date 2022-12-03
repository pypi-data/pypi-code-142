class random:
    def number(start:int, end:int):
        import random
        return random.randint(start, end)
    def letter(case:str):
        if case == "lower-case" or case == "lowercase" or case == "lower case":
            import string
            import random
            return random.choice(string.ascii_lowercase)
        elif case == "upper-case" or case == "uppercase" or case == "upper case":
            import string
            import random
            return random.choice(string.ascii_uppercase)
    def string(length:int):
        import random
        import string
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=length))
    def words(numberofwords:int):
        for i in range(numberofwords):
            import random
            words = open('words.txt').read().splitlines()
            return random.choice(words)
    def country():
        import pycountry
        import random
        country = random.choice(list(pycountry.countries))
        return f"Name = {country.name}"
        if hasattr(country, 'official_name'):
            return f"Official Name = {country.official_name}"
    
