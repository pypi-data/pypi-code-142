import functools
import os
import re
import datetime
import uuid
import json
import requests

import os
import inspect
import sys
import datetime

try:
    import fitz
except Exception as err:
    print('ERROR WHILE IMPORINT MODULE "fitz"')
    print(err)
    
import pytz
from redminelib import Redmine

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def __pdf_make_text(words):
    """Return textstring output of get_text("words").
    Word items are sorted for reading sequence left to right,
    top to bottom.
    """
    line_dict = {}  # key: vertical coordinate, value: list of words
    words.sort(key=lambda w: w[0])  # sort by horizontal coordinate
    for w in words:  # fill the line dictionary
        y1 = round(w[3], 1)  # bottom of a word: don't be too picky!
        word = w[4]  # the text of the word
        line = line_dict.get(y1, [])  # read current line content
        line.append(word)  # append new word
        line_dict[y1] = line  # write back to dict
    lines = list(line_dict.items())
    lines.sort()  # sort vertically
    return "\n".join([" ".join(line[1]) for line in lines])


def __pdf_parse_dt(s):
    ss = s.split(':')[-1]
    sss, tz = ss.split('+')
    hours = int(tz.split("'")[0])
    offset = datetime.timedelta(hours=hours)
    dt_local = datetime.datetime.strptime(sss, '%Y%m%d%H%M%S')
    dt_naive = dt_local - offset
    dt_utc = dt_naive.replace(tzinfo=pytz.utc)
    return dt_utc


    
def __pdf_get_info(annot):
    

    page = annot.parent
    doc = page.parent

    words = page.get_text("words")  # list of words on page
    mywords = [w for w in words if fitz.Rect(w[:4]).intersects(annot.rect)]
    
    txt = __pdf_make_text(mywords)
    content = annot.info['content']
    
    if txt and content:
        text_md = f'*Text Passage:*\n_"{txt}"_\n\n*Observation*: {content}'.replace('\n\r', '\n').replace('\r\n', '\n').replace('\r', '\n')


        dc = {
            'doc_path': doc.name,
            'author': annot.info['title'],
            'doc_page': str(page.number),
            't_created': __pdf_parse_dt(annot.info['creationDate']),
            't_modified': __pdf_parse_dt(annot.info['modDate']),
            'initial_text_md': text_md
        }
    else:
        dc = None
    return dc
    




def __red_issue_dc_2_redmine_dc(issue_dc, link=None):

    (doc_page, initial_text_md, author, doc_path, author) = [issue_dc[k] for k in 'doc_page initial_text_md author doc_path author'.split()]

    doc_id = os.path.basename(doc_path)

    doc_id = doc_id.split('_COM')[0]
    doc_id = doc_id.split('.')[0]

    subject = f'{doc_id} | Page {doc_page}'

    txt_md = f'___\n\n**DESCRIPTION**:\n\n ' + initial_text_md
    txt_md = txt_md.replace('\n\n\n\n\n\n', '\n\n')
    txt_md = txt_md.replace('\n\n\n\n', '\n\n')
    

    description = f'h1. {subject}'
    description += f'\n\nOriginal Document: "{doc_id}"'
    if link:
        description += f':{link}'
    
    description += f'\n\nAuthored by: "{author}"'

    description += '\n\n'
    description += txt_md

    return subject, description


def upload2redmine(redmine, issues_dc, rproject_id, ignore_errors=False, link=None):

    status_dict = {r.name.upper():r.id for r in redmine.issue_status.all()}

    ret = []

    with redmine.session(return_response=True):
        for issue in issues_dc:
            try:
                subject, description = __red_issue_dc_2_redmine_dc(issue, link=link)
                
                inew = redmine.issue.new()
                inew.project_id = rproject_id
                inew.subject = subject
                inew.description = description
                inew.done_ratio = 0
                inew.status_id = status_dict['NEW']
                inew.save() 
                assert inew.id > 0, 'returned ID was 0!'
                ret.append(inew.id)
            except Exception as err:
                if ignore_errors:
                    print('ERROR encountered... skipping. Message: ' + str(err))
                    ret.append(None)
                else:
                    raise
    return ret



def read_pdf(pth, users=[]):
    doc = fitz.open(pth)
    ret = []
    for i in range(doc.page_count):
        page = doc[i]
        annots = list(page.annots())
        if annots:
            for annot in annots:
                if users and annot.info['title'] not in users:
                    continue
                try:
                    ret.append(__pdf_get_info(annot))
                except Exception as err:
                    print(err)

    ret = [r for r in ret if r]
    return ret



def read_and_upload(filepath:str, 
                    redmine_url:str, redmine_key:str, redmine_project_id:str, 
                    file_link:str=None, 
                    user_id_to_assign:int=None, 
                    proxy:str=None,
                    ignore_errors=False):
    """read and upload a document to a redmine system

    Args:
        filepath (str): the path to the pdf file to upload to
        redmine_url (str): url to the redmine server (root)
        redmine_key (str): the user key (token) to use for uploading to redmine
        redmine_project_id (str): the project id to upload to. Usually can be found in browser when browsing to the project and checking the link: <URL>/projects/<project_id>
        file_link (str, optional): a link to the file which is uploaded to add to the description
        user_id_to_assign (int, optional): The user to assign the newly generated issues to. NOTE: this must be the integer user id, which can be found by check a users link in redmine: <URL>/users/<user_id>. Defaults to None.
        proxy (str, optional): any proxy url to use for the requests module. Defaults to None.
        ignore_errors (bool, optional): whether or not to ignore an error while uploading of individual issues. Defaults to False.
    """

    print('Loading issues from PDF:')
    
    issues_dc = read_pdf(filepath)

    print('Connecting redmine:')
    
    dc = {'verify': False}
    if proxy:
         dc['proxies'] = {"http": 'http://' + proxy, "https": 'http://' + proxy}
    
    redmine = Redmine(redmine_url, key=redmine_key, requests=dc)

    print('Uploading issues:')
    issue_ids = upload2redmine(redmine, issues_dc, rproject_id=redmine_project_id, ignore_errors=ignore_errors, link=file_link)

    if user_id_to_assign:
        print('Setting USER for issues:')
        issues = [i for i in issue_ids if i is not None]
        for i in issues:
            redmine.issue.update(i, assigned_to_id=user_id_to_assign)
            print(f'   ISSUE: {i} User set to: {user_id_to_assign}')

    return issue_ids
