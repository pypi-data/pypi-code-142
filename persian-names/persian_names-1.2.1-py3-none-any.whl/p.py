import os
from random import randrange

path = os.path.dirname(__file__)


def firstname_en(sex='r'):
    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    file = ['male_en.txt', 'female_en.txt']

    f = open(path + '/data/' + file[sex], 'r')
    names = f.read().split('\n')
    first = names[randrange(len(names))]
    return first


def lastname_en():
    isfx = [
        '', '', '', '', '', '', '', '', '', '',
        'pour',
        'zadeh',
        'far',
        'fard',
        'an',
        'kia',
        'rad',
        'zand',
        'khah',
        'nia'
    ]
    nsfx = [
        'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i',
        'pour',
        'zadeh',
        'far',
        'fard',
        'khani',
        'vand',
        'lou',
        'nia'
    ]

    f = open(path + '/data/male_en.txt', 'r')
    names = f.read().split('\n')
    last = names[randrange(len(names))]
    if last[1:] == 'ostafa' or last[1:] == 'ousa' or last[1:] == 'ahya':
        last += 'vi'
    elif last[1:] == 'orteza':
        last = last.replace('ez', 'az') + 'vi'
    elif last[1:] == 'hosro':
        last = last.replace('ro', 'ravi')
    elif last[-1] == 'a' or last[-1] == 'o' or last[-1] == 'u':
        last += 'ei'
    elif last[-1] == 'i':
        pass
    else:
        last += ['i', ''][randrange(2)]
    if len(last) > 10 and last[-1] == 'i':
        last += ''
    elif len(last) > 10 and last[-1] != 'i':
        last += 'i'
    elif last[-1] == 'i':
        last += isfx[randrange(len(isfx))]
    else:
        last += nsfx[randrange(len(nsfx))]
    return last


def fullname_en(sex='r'):
    if sex == 'male' or sex == 'm':
        return firstname_en('m') + ' ' + lastname_en()
    elif sex == 'female' or sex == 'f':
        return firstname_en('f') + ' ' + lastname_en()
    elif sex == 'random' or sex == 'r':
        return firstname_en('r') + ' ' + lastname_en()
    else:
        return None


def firstname_fa(sex='r'):
    if sex == 'male' or sex == 'm':
        sex = 0
    elif sex == 'female' or sex == 'f':
        sex = 1
    elif sex == 'random' or sex == 'r':
        sex = randrange(2)
    else:
        return None

    file = ['male_fa.txt', 'female_fa.txt']

    f = open(path + '/data/' + file[sex], 'r')
    names = f.read().split('\n')
    first = names[randrange(len(names))]
    return first


def lastname_fa():
    isfx = [
        '', '', '', '', '', '', '', '', '', '',
        ' پور',
        ' زاده',
        ' فر',
        ' فرد',
        'ان',
        ' کیا',
        ' راد',
        ' زند',
        ' خواه',
        ' نیا'
    ]
    nsfx = [
        'ی', 'ی', 'ی', 'ی', 'ی', 'ی', 'ی', 'ی',
        ' پور',
        ' زاده',
        ' فر',
        ' فرد',
        ' خانی',
        ' وند',
        ' لو',
        ' نیا'
    ]

    f = open(path + '/data/male_fa.txt', 'r')
    names = f.read().split('\n')
    last = names[randrange(len(names))]
    if last == 'مرتضی' or last == 'مصطفی' or last == 'موسی':
        last = last.replace('ی', 'وی')
    elif last == 'یحیی':
        last = last.replace('یی', 'یوی')
    elif last == 'خسرو':
        pass
    elif last[-1] == 'ا' or last[-1] == 'و':
        last += 'ئی'
    elif last[-1] == 'ی':
        pass
    else:
        last += ['ی', ''][randrange(2)]
    if last[-1] == 'ی':
        last += isfx[randrange(len(isfx))]
    else:
        last += nsfx[randrange(len(nsfx))]
    return last


def fullname_fa(sex='r'):
    if sex == 'male' or sex == 'm':
        return firstname_fa('m') + ' ' + lastname_fa()
    elif sex == 'female' or sex == 'f':
        return firstname_fa('f') + ' ' + lastname_fa()
    elif sex == 'random' or sex == 'r':
        return firstname_fa('r') + ' ' + lastname_fa()
    else:
        return None


print(firstname_fa('m'))
print(firstname_fa('f'))
print(firstname_fa('r'))
print('\n')
print(lastname_fa())
print(lastname_fa())
print(lastname_fa())
print('\n')
print(fullname_fa('m'))
print(fullname_fa('f'))
print(fullname_fa('r'))
print('\n')