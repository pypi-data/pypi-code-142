from io import StringIO
from unittest.mock import patch
import json

with open('https://aicore-files.s3.amazonaws.com/Movie-Recommendation/movies-head.json') as f:
    movies = json.load(f)

def get_avg_movie_description_length():
    total_len = 0
    for movie in movies:
        total_len += len(movie["description"])
    avg_description_len = total_len / len(movies)
    avg_description_len = round(avg_description_len, 1)
    return avg_description_len


def get_max_movie_name_length():
    title_of_movie_with_longest_title = None
    length_of_longest_movie_title = 0
    for movie in movies:
        title = movie["title"]
        if len(title) > length_of_longest_movie_title:
            length_of_longest_movie_title = len(title)
            title_of_movie_with_longest_title = title
    return length_of_longest_movie_title, title_of_movie_with_longest_title

def check_print_every_movie_name(func):
    # Check that the function prints every movie name
    with patch('sys.stdout', new=StringIO()) as fake_out:
        func()
        output = fake_out.getvalue()
        if output.count('Movie name:') != 5:
            print("The function doesn't print every movie name")
            print('Please, try again, and don\'t continue until you get the correct output')
            return False
        else:
            print('Great! The function prints every movie name')
            print('You can continue to the next task')
            return True

def check_get_movie_description_length(func, task_1):
    # Check that the function returns the correct length of the description\
    if not task_1:
        print("You haven't completed the previous task correctly")
        return False
    movie = movies[1]
    try:
        actual = func(movie)
    except Exception as e:
        print("Running the function with a movie as an argument results in an error")
        print('Check the error here: ', e)
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    if not actual:
        print("The function doesn't return anything")
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    elif not actual.isinstance(int):
        print("The function doesn't return an integer")
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    expected = len(movie['description'])
    if actual != expected:
        print("The function doesn't return the correct length of the description")
        print('Please, try again, and don\'t continue until you get the correct output')
        return False

def check_get_avg_movie_description_length(func, task_2):
    if not task_2:
        print("You haven't completed the previous task correctly")
        return False
    try:
        actual = func()
    except Exception as e:
        print('Running the "get_avg_movie_description_length" function results in an error')
        print('Check the error here: ', e)
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    if not actual:
        print("The function doesn't return anything")
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    elif not actual.isinstance(float):
        print("The function doesn't return a float, which results from dividing two integers")
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    expected = get_avg_movie_description_length()
    if actual != expected:
        print('The "get_avg_movie_description_length" function doesn\'t return the correct average length of the description')
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    else:
        print('Great! The "get_avg_movie_description_length" function returns the correct average length of the description: ', actual)
        print('You can continue to the next task')
        return True


def check_get_max_movie_name_length(func, task_3):
    if not task_3:
        print("You haven't completed the previous task correctly")
        return False
    try:
        actual = func()
    except Exception as e:
        print('Running the "get_max_movie_name_length" function results in an error')
        print('Check the error here: ', e)
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    if not actual:
        print("The function doesn't return anything")
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    elif len(actual) != 2:
        print("The function doesn't return a tuple with two elements")
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    elif not actual[0].isinstance(int):
        print("The function doesn't return a tuple with the first element being an integer")
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    elif not actual[1].isinstance(str):
        print("The function doesn't return a tuple with the second element being a string")
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    expected = get_max_movie_name_length()
    if actual != expected:
        print('The "get_max_movie_name_length" function doesn\'t return the correct maximum length of the movie name')
        print('Please, try again, and don\'t continue until you get the correct output')
        return False
    else:
        print('Great! The "get_max_movie_name_length" function returns the correct maximum length of the movie name: ', actual)
        print('You can continue to the next task')
        return True