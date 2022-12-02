# standard library imports
import csv
import re
import os
import json  # json config file parsing
import readline  # overwrites input() for arrow key navigation
import datetime as dt

# external imports
import readchar  # used for menu navigation
import colorama  # cross-platform terminal colors
import pandas as pd # easier csv file modification 

# local library imports
from worksheet_grading.util import *
import worksheet_grading.config as config


# ========== DATA STRUCTURE ========== #

class Exercise:
    def __init__(self, ex_num, num_answ, max_points):
        self.ex_num = ex_num
        self.answers = []
        self.num_answ = num_answ
        for i in range(0, num_answ):
            x = Answer(i + 1)
            self.answers.append(x)
        self.max_points = max_points

    def deduct(self, answer_num, reason, points):
        if answer_num > self.num_answ:
            print_err("Invalid Answer")
            return
        self.answers[answer_num - 1].deduct(reason, points)

    def _is_graded(self):
        ans_status = []
        for a in self.answers:
            ans_status.append(a.graded)
        if True not in ans_status:
            return config.UNGRADED
        else:
            if False not in ans_status:
                return config.GRADED
            else:
                return config.PARTIALLY_GRADED

    def mark_correct(self, ans_num):
        self.answers[ans_num - 1].mark_correct()

    def _calc_points(self):
        p = self.max_points
        for a in self.answers:
            p += a.deductions.deducted_points()
        if p < 0:
            p = 0
        # don't format as float if not necessary
        if p == round(p):
            p = int(p)
        return p

    graded = property(_is_graded)
    act_points = property(_calc_points)

    def csv_feedback(self):
        if self.graded == config.GRADED:
            fb_str = ""
            for ans in self.answers:
                fb_str += ans.csv_feedback_string()
            # remove last newline
            if fb_str != "":
                fb_str = fb_str[:-1]
            return fb_str
        else:
            return config.NA
     
    def csv_points(self):
        if self.graded == config.GRADED:
            points = self.act_points
        else:
            points = config.NA
        return points

    def short_rep(self):
        return "Exercise {} ({})".format(self.ex_num, self._grade_string())

    def _grade_string(self):
        grade_string = "not graded"
        if self.graded == config.GRADED:
            grade_string = "{}/{} Points".format(self.act_points, self.max_points)
        elif self.graded == config.PARTIALLY_GRADED:
            grade_string = "partially graded"
        return grade_string

    def long_rep(self):
        rep = "Exercise {} ({})\n\n".format(self.ex_num, self._grade_string())
        for a in self.answers:
            rep += a.rep(self.ex_num, key=True)
        return rep

    def html_string(self):
        s = "<p>\n<b>Exercise {} (max {}P): {}P</b><ul>".format(self.ex_num, self.max_points, self.act_points)
        for answer in self.answers:
            s += answer.html_string(self.ex_num) + "\n"
        s += "</ul></p>"
        return s


class Answer:
    def __init__(self, ans_num):
        self.num = ans_num
        self.deductions = Deductions(ans_num)
        self.graded = False

    def deduct(self, reason, points):
        self.deductions.add(reason, points)
        self.graded = True

    def mark_correct(self):
        self.deductions.clear()
        self.graded = True

    def html_string(self, ex_num):
        return "<li>{}.{}: {}</li>".format(ex_num, self.num, self.deductions.html_string())

    def feedback_string(self):
        return self.deductions.feedback_string()

    def csv_feedback_string(self):
        return self.deductions.csv_feedback_string()

    def rep(self, ex_num, key=False):
        repstr = ""
        if key:
            repstr += "\t[{}] ".format(magenta(self.num))
        grade_string = "not graded"
        if self.graded:
            grade_string = self.deductions.rep()
        repstr += "{}.{}: {}\n".format(ex_num, self.num, grade_string)
        return repstr


class Sheet:
    def __init__(self):
        self.exercises = []

    def html_string(self):
        s = ""
        for e in self.exercises:
            if e.max_points > 0:
                s += e.html_string() + "\n"
        max_points = 0
        reached_points = 0
        for e in self.exercises:
            max_points += e.max_points
            reached_points += e.act_points
        s += "<p><b>Total (max {}P): {}P</b></p>\n".format(max_points, reached_points)
        return s

    def print_html(self):
        print(self.html_string())

    def deduct(self, ex_num, answer_num, grade_text, deduction):
        self.exercises[ex_num - 1].deduct(answer_num, grade_text, deduction)

    def mark_correct(self, ex_num, ans_num):
        self.exercises[ex_num - 1].mark_correct(ans_num)

    def range_points(self, ex_range=None):
        max_points = 0
        act_points = 0
        for e in self.exercises:
            if ex_range is None or e.ex_num in ex_range:
                max_points += e.max_points
                act_points += e.act_points
        return act_points, max_points

    def grade_status(self, ex_range=None):
        ex_status = []
        for e in self.exercises:
            if ex_range is None or e.ex_num in ex_range:
                ex_status.append(e.graded)
        if not (config.GRADED in ex_status or config.PARTIALLY_GRADED in ex_status):
            return config.UNGRADED
        else:
            if not (config.PARTIALLY_GRADED in ex_status or config.UNGRADED in ex_status):
                return config.GRADED
            else:
                return config.PARTIALLY_GRADED

    def filter_exercises(self, first_ex, last_ex):
        new_exs = []
        for e in self.exercises:
            if first_ex <= e.ex_num <= last_ex:
                new_exs.append(e)
        self.exercises = new_exs


class Deductions:
    def __init__(self, ans_num):
        self.deds = []
        self.ans_num = ans_num

    def add(self, reason, points):
        self.deds.append((reason, points))

    def feedback_string(self):
        s = ""
        if len(self.deds) == 0:
            s += "-{}: correct\n".format(self.ans_num)
        else:
            for d in self.deds:
                if d[1] == 0:
                    s += "-{}: {}\n".format(self.ans_num, d[0])
                else:
                    s += "-{}: {} ({:.2f}P)\n".format(self.ans_num, d[0], d[1])
            s = s[:-1]
        return s

    def csv_feedback_string(self):
        s = ""
        if len(self.deds) == 0:
            s += "@{}@0@correct\n".format(self.ans_num)
        else:
            for d in self.deds:
                s += "@{}@{:.2f}@{}\n".format(self.ans_num, d[1], d[0])
        return s

    def html_string(self):
        if len(self.deds) == 0:
            return "correct"
        elif len(self.deds) == 1:
            if self.deds[0][1] == 0:
                return self.deds[0][0]
            else:
                return "{} ({:.2f}P)".format(self.deds[0][0], self.deds[0][1])
        else:
            s = "<ul>\n"
            for d in self.deds:
                if d[1] == 0:
                    s += "<li>{}</li>".format(d[0])
                else:
                    s += "<li>{} ({:.2f}P)</li>\n".format(d[0], d[1])
            s += "</ul>"
            return s

    def rep(self):
        if len(self.deds) == 0:
            return "correct"
        elif len(self.deds) == 1:
            if self.deds[0][1] == 0:
                return self.deds[0][0]
            else:
                return "{} ({:.2f}P)".format(self.deds[0][0], self.deds[0][1])
        else:
            s = "\n"
            for d in self.deds:
                if d[1] == 0:
                    s += "\t\t- {}\n".format(d[0])
                else:
                    s += "\t\t- {} ({:.2f}P)\n".format(d[0], d[1])
            s = s[:-1]
            return s

    def deducted_points(self):
        p = 0
        for d in self.deds:
            p += float(d[1])
        return p

    def clear(self):
        self.deds.clear()


class FrameEntry:
    def __init__(self, group, students):
        self.group = group
        self.students = students
        self.sheet = init_sheet()

    def parse_feedback(self, deds, ex_num, points, feedback):
        if points != config.NA:
            for fb in feedback.split("\n"):
                ln = re.finditer(config.FEEDBACK_PATTERN, fb)
                for m in ln:
                    ans_num = m[1]
                    deduction = m[2]
                    grade_text = m[4]
                    if float(deduction) == 0 and re.match(r"\s*correct\s*", grade_text):
                        self.sheet.mark_correct(int(ex_num), int(ans_num))
                    else:
                        self.sheet.deduct(int(ex_num), int(ans_num), grade_text, float(deduction))
                        deds.add_entry(int(ex_num), int(ans_num), grade_text, float(deduction))

    def name_len(self):
        # +2 for brackets
        return len(", ".join(self.students))+2

    def group_len(self):
        return len(self.group)

    def group_string(self, state):
        student_str = ", ".join(self.students)
        student_str = "(" + student_str + ")"
        ex_range = range(state.frame.first_ex, state.frame.last_ex + 1)
        grade_status = self.sheet.grade_status(ex_range)
        if grade_status == config.GRADED:
            act_points, max_points = self.sheet.range_points(ex_range)
            grade_str = light_green("{}/{} Points".format(act_points, max_points))
        elif grade_status == config.PARTIALLY_GRADED:
            grade_str = light_yellow("partially graded")
        elif grade_status == config.UNGRADED:
            grade_str = light_red("ungraded")
        else:
            raise RuntimeError("invalid grade status observed")
        return "{0:<{group_len}} {1:<{name_len}} | {2}".format(self.group, student_str, grade_str, group_len=config.MAX_GROUP_LEN,
                                                               name_len=config.MAX_NAMES_LEN)


class Frame:
    def __init__(self, first_ex, last_ex):
        self.first_ex = int(first_ex)
        self.last_ex = int(last_ex)

        # get specified csv files
        potential_files = [config.CSV_BASENAME.format(i) for i in range(int(first_ex), int(last_ex) + 1)]
        d = os.listdir()
        files = list(set(potential_files) & set(d))

        # revise firstex and lastex based on available files
        exs = []
        for f in files:
            m = re.search(config.CSV_PATTERN, f)
            exs.append(int(m.group(1)))

        if len(exs) == 0:
            print_err("No matching csv files for specified exercises and suffix found, exiting")
            exit(1)

        if min(exs) != self.first_ex:
            self.first_ex = min(exs)
        if max(exs) != self.last_ex:
            self.last_ex = max(exs)

        # check if deductions file exists and create if not present
        if not os.path.isfile(config.DEDUCTION_FILE):
            print_info("No deduction file found, creating new one")
            with open(config.DEDUCTION_FILE, "w") as f:
                f.write(config.DEDUCTIONS_FIRSTLINE)

        self.deds = DeductionCollection()

        self.data = {}

        if config.AUTOSAVE_FILENAME in os.listdir():
            print_info("Restoring from autosave, delete \"{}\" if you want to start from scratch".format(
                config.AUTOSAVE_FILENAME))
            as_df = pd.read_csv(config.AUTOSAVE_FILENAME)
            as_df.fillna(config.NA, inplace=True)
            config.detect_group_size(as_df)
            for i, r in as_df.iterrows():
                group_name = r["group"]
                students = []
                for i in range(1,config.GROUP_SIZE+1):
                    s = r[config.STUDENT_FORMAT.format(i)]
                    if s != config.NA:
                         students.append(s)
                if group_name not in self.data.keys():
                    self.data[group_name] = FrameEntry(group_name, students)
                self.data[group_name].parse_feedback(self.deds, r["exercise"], r["points"], r["feedback"])
            self.csv_df = as_df

        else:
            print_info("No autosave found, starting from scratch.\n")
            # create data structure from first file
            df = pd.read_csv(files[0])
            df.fillna(config.NA, inplace=True)
            config.detect_group_size(df)
            for i, r in df.iterrows():
                group_name = r["group"]
                students = []
                for i in range(1,config.GROUP_SIZE+1):
                    s = r[config.STUDENT_FORMAT.format(i)]
                    if s != config.NA:
                        students.append(s)
                self.data[group_name] = FrameEntry(group_name, students)
                self.data[group_name].parse_feedback(self.deds, r["exercise"], r["points"], r["feedback"])
            self.csv_df = df

            # read other files
            for f in files[1::]:
                df = pd.read_csv(f)
                df.fillna(config.NA, inplace=True)
                for i, r in df.iterrows():
                    group_name = r["group"]
                    students = []
                    self.data[group_name].parse_feedback(self.deds, r["exercise"], r["points"], r["feedback"])
                self.csv_df = pd.concat([self.csv_df, df]) 
            self.csv_df.sort_values(["exercise", "group"], inplace=True)
                

    def update_feedback(self):
        self.csv_df["feedback"] = [self.data[r["group"]].sheet.exercises[int(r["exercise"])-1].csv_feedback() for _,r in self.csv_df.iterrows()]
        self.csv_df["points"] = [self.data[r["group"]].sheet.exercises[int(r["exercise"])-1].csv_points() for _,r in self.csv_df.iterrows()]


    def write_csv_files(self):
        self.update_feedback()
        basename = config.CSV_BASENAME

        for e in range(self.first_ex, self.last_ex + 1):
            # rename old file
            os.rename(basename.format(e), basename.format(e) + ".old")

            # save exercise files
            cf = self.csv_df[self.csv_df["exercise"] == e]
            cf.to_csv(basename.format(e), index=None)


    def autosave(self):
        self.update_feedback()

        self.csv_df.to_csv(config.AUTOSAVE_FILENAME, index=None)
        self.deds.write_csv()

    def ungraded_groups(self):
        return list(filter(lambda e: e.sheet.grade_status(ex_range=range(self.first_ex, self.last_ex + 1)) == config.UNGRADED,
                           self.data.values()))

    def partial_groups(self):
        return list(
            filter(lambda e: e.sheet.grade_status(ex_range=range(self.first_ex, self.last_ex + 1)) == config.PARTIALLY_GRADED,
                   self.data.values()))

    def graded_groups(self):
        return list(filter(lambda e: e.sheet.grade_status(ex_range=range(self.first_ex, self.last_ex + 1)) == config.GRADED,
                           self.data.values()))


class DeductionCollection:
    def __init__(self):
        self.entries = []
        with open(config.DEDUCTION_FILE, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for (i, line) in enumerate(reader):
                if i != 0:
                    ex_num = line[0]
                    ans_num = line[1]
                    reason = line[2]
                    points = line[3]
                    count = line[4]
                    self.new_entry(ex_num, ans_num, reason, points, count)

    def add_entry(self, ex_num, ans_num, reason, points):
        found = False
        for e in self.entries:
            if e.ex_num == ex_num and e.ans_num == ans_num and \
                    e.reason == reason and e.points == points:
                #e.increment_count()
                found = True
                break
        if not found:
            self.new_entry(ex_num, ans_num, reason, points, 1)

    def new_entry(self, ex_num, ans_num, reason, points, count):
        self.entries.append(DeductionEntry(ex_num, ans_num, reason, points, count))

    def write_csv(self):
        with open(config.DEDUCTION_FILE, "w") as f:
            f.write(config.DEDUCTIONS_FIRSTLINE)
            for d in self.entries:
                f.write(d.csv_string())

    def get(self, ex_num, ans_num):
        deds = list(filter(lambda e: e.ex_num == ex_num and e.ans_num == ans_num, self.entries))
        deds.sort(key=lambda e: e.count, reverse=True)
        return deds

    def __str__(self):
        s = ""
        for d in self.entries:
            s += str(d) + "\n"
        return s


class DeductionEntry:
    def __init__(self, ex_num, ans_num, reason, points, count):
        self.ex_num = int(ex_num)
        self.ans_num = int(ans_num)
        self.reason = reason
        self.points = float(points)
        self.count = int(count)

    def increment_count(self):
        self.count += 1

    def csv_string(self):
        return "{},{},\"{}\",{},{}\n".format(self.ex_num, self.ans_num, self.reason, self.points, self.count)

    def __str__(self):
        return "{}.{}: {} ({} Points)".format(self.ex_num, self.ans_num, self.reason, self.points)


# ========== UTITLITY FUNCTIONS ========== #

def init_sheet():
    sh = Sheet()

    for i in range(config.DEFAULT_FIRSTEX, config.DEFAULT_LASTEX + 1):
        exc = config.EXERCISES.get(str(i))
        if exc is not None:
            sh.exercises.append(Exercise(i, len(exc), sum(exc)))

    return sh


def parse_config(config_path, suffix):
    # check whether json file exists
    if not os.path.exists(config_path):
        print_err("No configuration file found at path \"{}\", exiting".format(config_path))
        exit(1)

    # parse json and update globals

    sheet_config = json.loads(open(config_path).read())  # load json
    config.SHEETNAME = sheet_config[config.JSON_SHEETNAME]  # update sheet name
    if config.JSON_PDF_PATH in sheet_config:
        config.PDF_PATH = sheet_config[config.JSON_PDF_PATH] 
    if config.JSON_GROUPSIZE in sheet_config:
        config.GROUP_SIZE = int(sheet_config[config.JSON_GROUPSIZE])

    config.CSV_BASENAME = config.SHEETNAME + config.CSV_BASENAME
    config.CSV_PATTERN = config.SHEETNAME + config.CSV_PATTERN
    config.AUTOSAVE_FILENAME = config.AUTOSAVE_FILENAME.format(config.SHEETNAME)
    config.DEDUCTION_FILE = config.DEDUCTION_FILE.format(config.SHEETNAME)

    first_conf_ex = config.DEFAULT_FIRSTEX 

    for i in range(config.DEFAULT_FIRSTEX, config.DEFAULT_LASTEX + 1):
        if sheet_config.get(config.JSON_EXERCISES).get(str(i)) is not None:
            break
        first_conf_ex = i+1
    
    exercises = {}
    for i in range(first_conf_ex, config.DEFAULT_LASTEX + 1):
        ex_points = sheet_config.get(config.JSON_EXERCISES).get(str(i))
        if ex_points is None:  # break at first non-encountered exercise
            break
        exercises[str(i)] = ex_points
    config.EXERCISES = exercises

    # adapt suffix
    if suffix is not None:
        config.AUTOSAVE_FILENAME = suffix_string(config.AUTOSAVE_FILENAME, suffix)
        config.CSV_BASENAME = suffix_string(config.CSV_BASENAME, suffix)
        config.CSV_PATTERN = suffix_string(config.CSV_PATTERN, suffix)
    