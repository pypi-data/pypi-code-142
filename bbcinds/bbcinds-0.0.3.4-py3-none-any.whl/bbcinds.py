'''
commands 
python setup.py sdist bdist_wheel
python -m twine upload --repository pypi dist/*
'''

def update():
    ## START
    """
    Parameters
    ----------
    name : str
        The name of the animal
    sound : str
        The sound the animal makes
    num_legs : int, optional
        The number of legs the animal (default is 4)
    """
    ## END

    print('Hi There!')
