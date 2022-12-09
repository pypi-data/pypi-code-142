import re


class judger:

    def __init__(self, suspect):
        self.suspect = suspect

    def isdigit(self):
        return False if re.match("^\d+\.\d+$|^\d+$", self.suspect) == None else True


# def filterlist_(lst, exp):
    # match = [re.search(exp, item) for item in lst]
    # return [item.group() for item in match if item is not None]


def filter_list(lst, pattern=None, judge_func=None):
    if pattern is not None:
        for item in lst:
            match_obj = re.search(pattern,item)
            if match_obj is not None:
                yield item
        return
    if judge_func is not None:
        for item in lst:
            if judge_func(item):
                yield item
        return
    raise TypeError("filter_list() missing arguments:either 'pattern' or 'judge_func' should be provided")


def cert_validate(cert_no):
    coef_lst = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    rmd_dict={0:"1",1:"0",2:"X",3:"9",4:"8",5:"7",6:"6",7:"5",8:"4",9:"3",10:"2"}
    cert_17 = [int(_) for _ in str(cert_no)[:-1]]
    if rmd_dict[sum([_[0]*_[1] for _ in zip(cert_17,coef_lst)])%11]==str(cert_no)[-1]:
        return True
    return False



if __name__ == "__main__":
    # print(list(filter_list(["aasdfs", "110dfadf"], "^\d+.*")))
    # print(list(filter_list(["8899adf", "1109d09"], "^\d+.*")))
    # print(list(filter_list(["eace", "123dfadf"], "^\d+.*")))
    # print(list(filter_list(["eace", "123dfadf"])))
    # print(judger("1.23").isdigit())
    # print(judger("3").isdigit())
    print(cert_validate(350204199508276531))
    print(cert_validate(421281198807239878))
