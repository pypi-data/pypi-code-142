from json import JSONEncoder
from datetime import datetime

def buildRoster(fin, fout):
    students = []
    try:
        with open(fin) as file:
            for student_line in file:
                newStudent = student_line.split(',')
                first = newStudent[0].replace('"','')
                last = newStudent[1].replace('"','')
                student = Student(first, last)
                for k in students:
                    #print(f'{k.nickname}')
                    if student.nickname == k.nickname:
                        student.nickname = f'{first.title()}{last[0].lower()}'
                students.append(student)
                #input("Press enter...")

        students.pop(0)
    except FileNotFoundError:
        print("No such file")

    try:
       with open(fout, 'w') as f:
            for s in students:
                studentJSON = StudentEncoder().encode(s)
                f.write(studentJSON)
                f.write('\n')
    except FileNotFoundError:
        print("No such file")

def copyStudent(oldStudent, nickname = ''):
    first = oldStudent.first
    last = oldStudent.last
    passes = {}
    for k,v in oldStudent.passes.items():
        passes[k] = v
    if nickname == '':
        nickname = oldStudent.nickname
    passno = oldStudent.passno
    return Student(first, last, passes, nickname, passno)

class Student():

    totalPasses = 10
    def __init__(self, first, last, passes = {}, nickname = '', passno = totalPasses):
        self.first = first.title()
        self.last = last.title()
        if nickname != '':
            self.nickname = nickname
        else:
            self.nickname = first.title()
        self.passes = {}
        for k,v in passes.items():
            self.passes[k] = v

        self.passno = passno
        self.flag = False

    def use_pass(self):
        newPass = Pass()
        self.passes[str(self.passno)] = (newPass.date, newPass.time)
        self.passno -= 1
        if self.passno == 0:
            self.flag = True

    def forgive_pass(self):
        self.clearscr()
        print(f'\33[0;0H', flush=True, end = '')
        print('Passes')
        if self.passno == self.totalPasses:
            print("No passes to forgive")
            return 0
        for k, v in self.passes.items():
            print(f'{k}: {v[0]} {v[1]}')

        choice = input("Which pass would you like to forgive? ")
        try:
            check = input("Are you sure? Pass data cannot be recovered... ")
            if check.title() == 'Yes':
                del self.passes[choice]
                self.passno += 1
        except KeyError:
            print('Not a valid choice')

        key = self.totalPasses
        newPasses = {}
        for k, v in self.passes.items():
            newPasses[str(key)] = v
            key -= 1
        
        self.passes = newPasses

    def edit_nickname(self):
        new_name = input("Enter the new Nickname: ")
        self.nickname = new_name
            
    def edit_pass(self, passno):
        print('soon...')
        '''
        currPass = self.passes[passno]
        self.clearscr()
        print("Pass Values")
        print(f'date: {currPass[0]}  time: {currPass[1]}')
        '''

    def clearscr(self):
        print('\33[0;0H')
        for i in range(0,25):
            for j in range (0,81):
                print(f'\33[{i};{j}H ', flush=True, end='')

    def display(self):
        self.clearscr()
        
        print(f'\33[0;0HStudent')
        print(f'{self.last}, {self.nickname}')
        print(f'Passes Left: {self.passno}')
        print('Date   Time')
        for v in self.passes.values():
            print(f'{v[0]}  {v[1]}')

        input("press enter...")
        

        
class Pass():

    def __init__(self):
        ts = datetime.timestamp(datetime.now())
        dt = datetime.fromtimestamp(ts)
        str_time = dt.strftime('%H:%M')
        str_date = dt.strftime('%m/%d')
        self.time = str_time
        self.date = str_date

class StudentEncoder(JSONEncoder):
    def default(self, student):
        return student.__dict__

if __name__ == '__main__':
    print("Classes to represent students, passes, and JSON Encoders")