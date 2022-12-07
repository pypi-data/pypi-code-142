# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals, print_function
from xyz_util.mongoutils import Store, drop_id_field
from xyz_util.datautils import access
import hashlib


class QuestionStore(Store):
    name = 'exam_question'
    field_types = {int: ['year', 'month', 'ownerId', 'paperId', 'papers']}
    fields = ['year', 'month', 'ownerId', 'paperId', 'papers', 'ownerType', 'outline', 'type']

    def gen_paper(self, cond={}, limit=100, type_name_orders=[]):
        ordering = [('typeName', 1), ('year', -1), ('month', -1)]
        ts = {}
        for q in self.find(cond, {'_id': 0}, sort=ordering, limit=limit):
            qs = ts.setdefault(q['typeName'], [])
            qs.append(q)
            q['number'] = len(qs)
        return ts

def gen_question_uid(q, g):
    if 'uid' in q:
        return q['uid']
    gids = g.get('memo', '')
    qids = '%s%s%s' % (gids, q['type'], q['title'])
    return hashlib.md5(qids.encode('utf8')).hexdigest()[:7]


def store_paper_questions(paper):
    from .helper import group_name_sumary
    qs = QuestionStore()
    p = paper.content.data  # content_object
    if paper.owner_type is None:
        return
    pws = '.'.join(paper.owner_type.natural_key())
    import re
    m = re.compile(r'(\d{4})年').search(p['title'])
    year = m.group(1) if m else None
    m = re.compile(r'(\d+)月').search(p['title'])
    month = m.group(1) if m else None
    qs.update({'papers': paper.id}, {}, pull=dict(papers=paper.id))

    for g in p['groups']:
        for q in g['questions']:
            #if g.get('memo'):
            q['group'] = dict([(k, v) for k, v in g.items() if k in ['title', 'memo', 'inputs', 'number']])
            q['ownerType'] = pws
            q['typeName'] = group_name_sumary(g['title'])
            q['ownerId'] = paper.owner_id
            if year:
                q['year'] = int(year)
            if month:
                q['month'] = int(month)
            uid = gen_question_uid(q, g)
            q.pop('papers', [])
            qs.upsert(dict(uid=uid), q, addToSet=dict(papers=paper.id))


def group_paper_questions(qset, group='outline'):
    ids = list(qset.values_list('id', flat=True))
    st = QuestionStore()
    return st.count_by(group, {'papers': {'$in': ids}}, output='dict')


class PaperStore(Store):
    name = 'exam_paper'
    fields = ['ownerId', 'id', 'ownerType']

    def gen_paper(self, outlines):
        qs = QuestionStore()
        # qs.find(cond)

    def save_paper(self, paper):
        self.upsert(
            {'id': paper.id},
            {
                'source': paper.content,
                'data': paper.content_object,
                'title': paper.title
            }
        )
