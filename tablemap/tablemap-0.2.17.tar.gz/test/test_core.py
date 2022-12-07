import os
import unittest
from itertools import product
from pathlib import Path

from tablemap import Conn


class TestCore(unittest.TestCase):
    def setUp(self):
        self.dbfile = 'test/sample.db'
        self.dbfile1 = 'test/sample1.db'

        self.t1 = [
            {'col1': 'a', 'col2': 4},
            {'col1': 'a', 'col2': 5},
            {'col1': 'b', 'col2': 1},
            {'col1': 'c', 'col2': 3},
            {'col1': 'c', 'col2': 4},
            {'col1': 'c', 'col2': 7},
            {'col1': 'd', 'col2': 2},

        ]

        self.t2 = [
            {'col1': 'd', 'col3': 3},
            {'col1': 'b', 'col3': 1},
            {'col1': 'e', 'col3': 3},
            {'col1': 'e', 'col3': 4},
            {'col1': 'd', 'col3': 2},
        ]

    def tearDown(self):
        if Path(self.dbfile).is_file():
            os.remove(self.dbfile)
        if Path(self.dbfile1).is_file():
            os.remove(self.dbfile1)

    def test_do_later(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1

        xs, ys = conn['t1'].tee(2)
        xs.by('col1')
        tot = sum(ys['col2'])
        xs.fold(
            col3=lambda rs: sum(rs['col2']),
            col4=tot
        )
        self.assertEqual(xs.list(),
                         [{'col1': 'a', 'col3': 9, 'col4': 26},
                          {'col1': 'b', 'col3': 1, 'col4': 26},
                          {'col1': 'c', 'col3': 14, 'col4': 26},
                          {'col1': 'd', 'col3': 2, 'col4': 26}])

    def test_zip(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1

        def tempfn(rs):
            return rs.zip([
                {'n': 1},
                {'n': 2}
            ])

        conn['t1_1'] = conn['t1'].by('col1').map(tempfn)
        self.assertEqual(conn['t1_1'].list(),
                         [{'col1': 'a', 'col2': 4, 'n': 1},
                          {'col1': 'a', 'col2': 5, 'n': 2},
                          {'col1': 'b', 'col2': 1, 'n': 1},
                          {'col1': 'c', 'col2': 3, 'n': 1},
                          {'col1': 'c', 'col2': 4, 'n': 2},
                          {'col1': 'd', 'col2': 2, 'n': 1}]
                         )

    def test_tee_n_new(self):
        conn = Conn(self.dbfile)

        def tempfn(rs):
            rs1, rs2 = rs.tee(2)
            return rs1.order('col2 desc').chain(rs2.order('col2'))

        conn['t1'] = self.t1
        conn['t1_1'] = conn['t1'].by('col1').map(tempfn)
        self.assertEqual(conn['t1_1']['col2'],
                         [5, 4, 4, 5, 1, 1, 7, 4, 3, 3, 4, 7, 2, 2])

        def tempfn(rs):
            rs1, rs2 = rs.tee(2)
            rs1.update(col2=lambda r: r['col2'] + 1)
            return rs1.order('col2 desc').chain(rs2.order('col2'))

        conn['t1'] = self.t1
        conn['t1_1'] = conn['t1'].by('col1').map(tempfn)
        self.assertEqual(conn['t1_1']['col2'],
                         [6, 5, 5, 6, 2, 2, 8, 5, 4, 4, 5, 8, 3, 3])

        def tempfn(rs):
            rs1, rs2 = rs.tee(2)
            rs1.update(col2=lambda r: r['col2'] + 1)
            return rs1.order('col2 desc').chain(rs2.new().order('col2'))

        conn['t1'] = self.t1
        conn['t1_1'] = conn['t1'].by('col1').map(tempfn)
        self.assertEqual(conn['t1_1']['col2'],
                         [6, 5, 4, 5, 2, 1, 8, 5, 4, 3, 4, 7, 3, 2])

    def test_tee_n_new2(self):
        conn = Conn(self.dbfile)

        def tempfn(rs):
            rs1, rs2 = rs.tee(2)
            return rs1.order('col2').zip(rs2.order('col2 desc')
                                         .rename(col2_1='col2'))

        conn['t1'] = self.t1
        conn['t1_1'] = conn['t1'].by('col1').map(tempfn)
        xs = [{'col1': 'a', 'col2': 4, 'col2_1': 5},
              {'col1': 'a', 'col2': 5, 'col2_1': 4},
              {'col1': 'b', 'col2': 1, 'col2_1': 1},
              {'col1': 'c', 'col2': 3, 'col2_1': 7},
              {'col1': 'c', 'col2': 4, 'col2_1': 4},
              {'col1': 'c', 'col2': 7, 'col2_1': 3},
              {'col1': 'd', 'col2': 2, 'col2_1': 2}]
        self.assertEqual(conn['t1_1'].list(), xs)

        def tempfn1(rs):
            rs1, rs2 = rs.tee(2)
            rs1.update(col2=lambda r: r['col2'] + 1)
            return rs1.order('col2').zip(rs2.order('col2 desc')
                                         .rename(col2_1='col2'))

        conn['t1_1'] = conn['t1'].by('col1').map(tempfn1)

        xs = [{'col1': 'a', 'col2': 5, 'col2_1': 6},
              {'col1': 'a', 'col2': 6, 'col2_1': 5},
              {'col1': 'b', 'col2': 2, 'col2_1': 2},
              {'col1': 'c', 'col2': 4, 'col2_1': 8},
              {'col1': 'c', 'col2': 5, 'col2_1': 5},
              {'col1': 'c', 'col2': 8, 'col2_1': 4},
              {'col1': 'd', 'col2': 3, 'col2_1': 3}]
        self.assertEqual(conn['t1_1'].list(), xs)

        def tempfn2(rs):
            rs1, rs2 = rs.tee(2)
            rs1.update(col2=lambda r: r['col2'] + 1)
            return rs1.order('col2').zip(rs2.new().order('col2 desc')
                                         .rename(col2_1='col2'))

        conn['t1_1'] = conn['t1'].by('col1').map(tempfn2)

        xs = [{'col1': 'a', 'col2': 5, 'col2_1': 5},
              {'col1': 'a', 'col2': 6, 'col2_1': 4},
              {'col1': 'b', 'col2': 2, 'col2_1': 1},
              {'col1': 'c', 'col2': 4, 'col2_1': 7},
              {'col1': 'c', 'col2': 5, 'col2_1': 4},
              {'col1': 'c', 'col2': 8, 'col2_1': 3},
              {'col1': 'd', 'col2': 3, 'col2_1': 2}]
        self.assertEqual(conn['t1_1'].list(), xs)

    def test_index(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1

        def cnt():
            n = 0

            def innerfn(rs):
                nonlocal n
                n += 1
                return rs.update(n=n)
            return innerfn

        conn['t1_1'] = conn['t1'].by('col1').map(cnt())
        self.assertEqual(
            conn['t1_1'].list(), [{'col1': 'a', 'col2': 4, 'n': 1},
                                  {'col1': 'a', 'col2': 5, 'n': 1},
                                  {'col1': 'b', 'col2': 1, 'n': 2},
                                  {'col1': 'c', 'col2': 3, 'n': 3},
                                  {'col1': 'c', 'col2': 4, 'n': 3},
                                  {'col1': 'c', 'col2': 7, 'n': 3},
                                  {'col1': 'd', 'col2': 2, 'n': 4}])

    def test_fold1(self):
        conn = Conn(self.dbfile)

        def minmax(col):
            def fn(rs):
                xs = [r[col] for r in rs]
                return [min(xs), max(xs)]
            return fn

        conn['t1'] = self.t1
        conn['t1_1'] = conn['t1'].by('col1').fold(
            sum=lambda rs: sum(rs['col2']),
            mm0=lambda rs: min(rs['col2']),
            mm1=lambda rs: max(rs['col2'])
        )

        self.assertEqual(conn['t1_1'].list(),
                         [{'col1': 'a', 'sum': 9, 'mm0': 4, 'mm1': 5},
                          {'col1': 'b', 'sum': 1, 'mm0': 1, 'mm1': 1},
                          {'col1': 'c', 'sum': 14, 'mm0': 3, 'mm1': 7},
                          {'col1': 'd', 'sum': 2, 'mm0': 2, 'mm1': 2}])

        conn['t1_1'] = conn['t1'].windowed(4, 3).fold(
            sum=lambda rs: sum(rs['col2']),
            mm0=lambda rs: min(rs['col2']),
            mm1=lambda rs: max(rs['col2'])
        )
        self.assertEqual(conn['t1_1'].list(),
                         [{'sum': 13, 'mm0': 1, 'mm1': 5},
                          {'sum': 16, 'mm0': 2, 'mm1': 7}
                          ])

        conn['t1_1'] = conn['t1'].windowed(4, 5).fold(
            sum=lambda rs: sum(rs['col2']),
            mm0=lambda rs: min(rs['col2']),
            mm1=lambda rs: max(rs['col2'])
        ).rename(
            mm1='mm0',
            mm0='mm1'
        )
        self.assertEqual(conn['t1_1'].list(),
                         [{'sum': 13, 'mm1': 1, 'mm0': 5},
                          {'sum': 9, 'mm1': 2, 'mm0': 7}
                          ])

    def test_by(self):
        def sum_by_col1(rs):
            tot = sum(rs['col2'])
            return rs.update(col2=tot).islice(1)

        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        conn['t1_sum'] = conn['t1'].by('col1')\
            .map(sum_by_col1)

        self.assertEqual(list(conn['t1_sum'].iter()),
                         [{'col1': 'a', 'col2': 9},
                          {'col1': 'b', 'col2': 1},
                          {'col1': 'c', 'col2': 14},
                          {'col1': 'd', 'col2': 2}]
                         )
        conn['t1_sum2'] = conn['t1']\
            .by('col1').map(sum_by_col1)

        self.assertEqual(conn['t1_sum'].list(), conn['t1_sum2'].list())

    def test_chain(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        conn['t1_double'] = conn['t1'].chain(conn['t1'])
        self.assertEqual(conn['t1'].list() + conn['t1'].list(),
                         conn['t1_double'].list())

        conn['t1_double'] = conn['t1'].chain(self.t1)
        self.assertEqual(conn['t1'].list() + conn['t1'].list(),
                         conn['t1_double'].list())

    def test_df(self):
        import pandas as pd
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        df = pd.DataFrame(conn['t1'].iter())
        conn['t1_copy'] = df.to_dict('records')
        self.assertEqual(conn['t1'].list(), conn['t1_copy'].list())

    def test_by_after_map(self):
        def sumit(rs):
            tot = sum(rs['col2'])
            return rs.update(tot=tot)

        def count(rs):
            n = len(rs.list())
            return rs.update(cnt=n)

        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        conn['t1_sum'] = conn['t1'].by('col1')\
            .map(sumit).by('tot').map(count)

        # on another db
        conn1 = Conn(self.dbfile1)
        conn1['t1_sum'] = conn['t1'].by('col1').map(sumit).by('tot').map(count)
        conn1['t1_sum2'] = conn['t1'].by('col1').map(sumit)\
            .by('tot').map(count).iter()

        self.assertEqual(conn['t1_sum'].list(), conn1['t1_sum'].list())
        self.assertEqual(conn['t1_sum'].list(), conn1['t1_sum2'].list())

    def test_multiple_by(self):

        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        conn['t1_1'] = conn['t1'].update(col3=1).by('col1', 'col3')\
            .map(lambda rs: rs)

        conn['t1_2'] = conn['t1'].update(col3=1).by('col1').map(lambda rs: rs)
        self.assertEqual(conn['t1_1'].list(), conn['t1_2'].list())

        conn['t1_1_double'] = conn['t1_1']\
            .chain(conn['t1'].update(col3=1).by('col1', 'col3')
                   .map(lambda rs: rs))
        conn['t1_1_double2'] = conn['t1_1'].chain(conn['t1_1'])

        self.assertEqual(conn['t1_1_double'].list(),
                         conn['t1_1_double2'].list())

    def test_islice(self):

        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        conn['t2'] = self.t2

        self.assertEqual(len(conn['t1'].islice(3).list()), 3)
        self.assertEqual(len(conn['t1'].islice(3, None).list()), 4)
        self.assertEqual(len(conn['t1'].islice(0, None, 3).list()), 3)

        xs = conn['t1'].iter()
        ys = conn['t2'].iter()

        conn['t1_2'] = ({**x, **y} for x, y in product(xs, ys))

        n1 = len(conn['t1'].list())
        n2 = len(conn['t2'].list())
        n3 = len(conn['t1_2'].list())

        self.assertEqual(n3, n1 * n2)

    def test_takewhile(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1

        self.assertEqual(len(conn['t1']
                             .takewhile(lambda r: r['col2'] > 1).list()), 2)

        self.assertEqual(len(conn['t1']
                             .order('col2 desc')
                             .takewhile(lambda r: r['col2'] > 1).list()), 6)

    def test_dropwhile(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1

        self.assertEqual(len(conn['t1']
                             .dropwhile(lambda r: r['col2'] > 1).list()), 5)

        self.assertEqual(len(conn['t1']
                             .order('col2')
                             .dropwhile(lambda r: r['col2'] < 4).list()), 4)

    def test_windowed(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1

        def add1(rs):
            return rs.update(col2=lambda r: r['col2'] + 1)

        self.assertEqual(conn['t1'].windowed(4, 2).map(add1).list(),
                         [{'col1': 'a', 'col2': 5},
                          {'col1': 'a', 'col2': 6},
                          {'col1': 'b', 'col2': 2},
                          {'col1': 'c', 'col2': 4},
                          {'col1': 'b', 'col2': 2},
                          {'col1': 'c', 'col2': 4},
                          {'col1': 'c', 'col2': 5},
                          {'col1': 'c', 'col2': 8},
                          {'col1': 'c', 'col2': 5},
                          {'col1': 'c', 'col2': 8},
                          {'col1': 'd', 'col2': 3}])

    def test_filter(self):
        conn = Conn(self.dbfile)

        conn['t1'] = self.t1
        conn['t1_1'] = conn['t1'].filter(lambda r: r['col2'] > 2)

        self.assertEqual(len(conn['t1_1'].list()), 5)

    def test_update(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        conn['t1_1'] = conn['t1'].update(
            col2=lambda r: r['col2'] + 1,
            col3=lambda r: r['col1'] + str(r['col2'])
        )
        # table is fetched as it's inserted. not sure if it's a feature.
        self.assertEqual(conn['t1_1'].list()[0],
                         {'col1': 'a', 'col2': 5, 'col3': 'a5'})

    def test_select(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1

        # for r in conn['t1'].iter():
        #     print(r)

        conn['t1_1'] = conn['t1'].update(
            col2=lambda r: r['col2'] + 1,
            col3=lambda r: r['col1'] + str(r['col2'])
        )

        r = next(conn['t1_1'].select('col1', 'col3').iter())
        self.assertEqual(len(r), 2)

        # test deselect
        r = next(conn['t1_1'].deselect('col1', 'col3').iter())
        self.assertEqual(len(r), 1)

    def test_join(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        conn['t2'] = self.t2

        conn['t1_1'] = conn['t1'].by('col1').inner_join(conn['t2'].by('col1'))

        self.assertEqual(len(conn['t1_1'].list()), 3)

        conn['t1_2'] = conn['t1'].by('col1').left_join(conn['t2'].by('col1'))

        self.assertEqual(len(conn['t1_2'].list()), 8)

        conn['t1_3'] = conn['t1'].by('col1').right_join(conn['t2'].by('col1'))

        self.assertEqual(len(conn['t1_3'].list()), 5)

        conn['t1_4'] = conn['t1'].by('col1').full_join(conn['t2'].by('col1'))

        self.assertEqual(conn['t1_4'].list(), [
            {'col1': 'a', 'col2': 4, 'col3': ''},
            {'col1': 'a', 'col2': 5, 'col3': ''},
            {'col1': 'b', 'col2': 1, 'col3': 1},
            {'col1': 'c', 'col2': 3, 'col3': ''},
            {'col1': 'c', 'col2': 4, 'col3': ''},
            {'col1': 'c', 'col2': 7, 'col3': ''},
            {'col1': 'd', 'col2': 2, 'col3': 3},
            {'col1': 'd', 'col2': 2, 'col3': 2},
            {'col1': 'e', 'col2': '', 'col3': 3},
            {'col1': 'e', 'col2': '', 'col3': 4}]
        )

    def test_join2(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        conn['t2'] = self.t2

        conn['t1_1'] = conn['t1'].chain([{'col1': 'd', 'col2': 9}, {
            'col1': 'd', 'col2': 19}]).by('col1')\
            .full_join(conn['t2'].by('col1'))

        self.assertEqual(conn['t1_1'].list(),
                         [{'col1': 'a', 'col2': 4, 'col3': ''},
                          {'col1': 'a', 'col2': 5, 'col3': ''},
                          {'col1': 'b', 'col2': 1, 'col3': 1},
                          {'col1': 'c', 'col2': 3, 'col3': ''},
                          {'col1': 'c', 'col2': 4, 'col3': ''},
                          {'col1': 'c', 'col2': 7, 'col3': ''},
                          {'col1': 'd', 'col2': 2, 'col3': 3},
                          {'col1': 'd', 'col2': 2, 'col3': 2},
                          {'col1': 'd', 'col2': 9, 'col3': 3},
                          {'col1': 'd', 'col2': 9, 'col3': 2},
                          {'col1': 'd', 'col2': 19, 'col3': 3},
                          {'col1': 'd', 'col2': 19, 'col3': 2},
                          {'col1': 'e', 'col2': '', 'col3': 3},
                          {'col1': 'e', 'col2': '', 'col3': 4}])

    def test_distinct(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1
        conn['t1_1'] = conn['t1'].distinct('col1')
        self.assertEqual(len(conn['t1_1'].list()), 4)
        conn['t1_2'] = conn['t1'].distinct('col1', 'col2')
        self.assertEqual(len(conn['t1_2'].list()), 7)

    def test_order(self):
        conn = Conn(self.dbfile)
        conn['t1'] = self.t1

        [g1, g2, g3, g4] = [list(xs) for _, xs in conn['t1'].order(
            'col1', 'col2 desc').group('col1').iter()]
        self.assertEqual(
            g1, [{'col1': 'a', 'col2': 5}, {'col1': 'a', 'col2': 4}]
        )
        self.assertEqual(g2, [{'col1': 'b', 'col2': 1}])
        self.assertEqual(g3, [{'col1': 'c', 'col2': 7}, {
                         'col1': 'c', 'col2': 4}, {'col1': 'c', 'col2': 3}])
        self.assertEqual(g4, [{'col1': 'd', 'col2': 2}])

    def test_readme(self):
        t1 = [
            {'col1': 'a', 'col2': 4},
            {'col1': 'a', 'col2': 5},
            {'col1': 'b', 'col2': 1},
        ]

        conn = Conn(self.dbfile)
        conn['t1'] = t1

        for r1, r2 in zip(conn['t1'].list(), conn['t1'].iter()):
            self.assertEqual(r1, r2)

        import pandas as pd

        df = pd.DataFrame(conn['t1'].iter())
        conn['t1_copy'] = df.to_dict('records')

        self.assertEqual(conn['t1'].list(), conn['t1_copy'].list())

        conn['t1_1'] = conn['t1']\
            .filter(lambda r: r['col2'] > 2)\
            .update(col2=lambda r: r['col2'] + 1)

        self.assertEqual(conn['t1_1'].list()[0]['col2'], 5)

        conn['t1_col2sum_groupby_col1'] = conn['t1'].by('col1')\
            .fold(col2_sum=lambda rs: sum(rs['col2']))\
            .deselect('col2')

        conn['t1_col2sum_groupby_col1_1'] = conn['t1']\
            .order('col1', 'col2 desc').group('col1')\
            .fold(col2_sum=lambda rs: sum(rs['col2']))\
            .deselect('col2')

        self.assertEqual(conn['t1_col2sum_groupby_col1'].list(),
                         conn['t1_col2sum_groupby_col1_1'].list())

        conn['t1_double'] = conn['t1'].chain(conn['t1'])
        self.assertEqual(len(conn['t1_double'].list()),
                         2 * len(conn['t1'].list()))

        conn['t1_double'] = conn['t1'].chain(t1)

        self.assertEqual(len(conn['t1_double'].list()),
                         2 * len(conn['t1'].list()))

        conn['t1_1'] = conn['t1']\
            .filter(lambda r: r['col2'] > 2)\
            .update(
                col2=lambda r: r['col2'] + 1,
                col3=lambda r: r['col1'] + str(r['col2'])
        )
        self.assertEqual(conn['t1_1'].list(),
                         [{'col1': 'a', 'col2': 5, 'col3': 'a5'},
                          {'col1': 'a', 'col2': 6, 'col3': 'a6'}])

        conn['t1_1'] = conn['t1'].update(col3=lambda r: r['col2'] + 1)\
            .deselect('col1', 'col2')

        self.assertEqual(conn['t1_1'].list(),
                         [{'col3': 5}, {'col3': 6}, {'col3': 2}])

        conn['t1_1'] = conn['t1'].distinct('col1')
        self.assertEqual(conn['t1_1'].list(), [
                         {'col1': 'a', 'col2': 4}, {'col1': 'b', 'col2': 1}])

        conn['t2'] = [
            {'col1': 'b', 'col3': -1},
            {'col1': 'c', 'col3': 3},
            {'col1': 'b', 'col3': ''},
        ]

        conn['t1_col3'] = conn['t1'].by('col1')\
            .full_join(conn['t2'].by('col1'))

        self.assertEqual(conn['t1_col3'].list(),
                         [{'col1': 'a', 'col2': 4, 'col3': ''},
                         {'col1': 'a', 'col2': 5, 'col3': ''},
                         {'col1': 'b', 'col2': 1, 'col3': -1},
                         {'col1': 'b', 'col2': 1, 'col3': ''},
                          {'col1': 'c', 'col2': '', 'col3': 3}]
                         )
