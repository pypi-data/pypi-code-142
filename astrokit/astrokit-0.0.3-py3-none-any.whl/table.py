"""
A python module for process tables.

@author: Rui Zhu  
@creation time: 2022-11-29
"""
import pandas as pd
from astropy.table import Table
from astropy.coordinates import SkyCoord
import astropy.units as u


def fits2df(path_fits):
    """
    读取fits中的table, 并转换成pandas的DataFrame
    """
    tbl = Table.read(path_fits, character_as_bytes=False)
    df = tbl.to_pandas()
    return df


class MatchCatalog:
    """
    A class for matching two catalogs

    Parameter
    ---------
    cat1: DataFrame
        待交叉的catalog1
    cat2: DataFrame
        待交叉的catalog2
    coord_name1: tuple (optional)
        catalog1中ra, dec使用的名称
    coord_name2: tuple (optional)
        catalog2中ra, dec使用的名称
    """
    def __init__(self, cat1, cat2, coord_name1=('ra', 'dec'), coord_name2=('ra', 'dec')):
        self.cat1 = cat1
        self.cat2 = cat2
        self.coord_name1 = coord_name1
        self.coord_name2 = coord_name2

        self.result = None
        self.duplicated_num = None  # 多对应情况数量
        self.duplicated_cat = None

    def matching(self, sep=1):
        """
        Matching two catalogs.

        Parameter
        ---------
        sep: 1 (默认)
            match阈值, 单位arcsec

        Return
        ------
        matched_cat: DataFrame
            注意, 此表格保留近邻源
        """
        # * ------ 阈值 -----
        max_sep = sep*u.arcsec
        # * ----------------
        cat1 = self.cat1
        cat2 = self.cat2
        coord_name1 = self.coord_name1
        coord_name2 = self.coord_name2

        # ^ ----- step1: 检查与规范
        # Dataframe检查
        cat1.reset_index(inplace=True, drop=True)
        cat2.reset_index(inplace=True, drop=True)

        # 坐标列名调成('ra', 'dec')
        normal_coord_name = ('ra', 'dec')
        if coord_name1 != normal_coord_name:
            cat1.rename(columns={
                coord_name1[0]: normal_coord_name[0], 
                coord_name1[1]: normal_coord_name[1]
                }, inplace=True)
        if coord_name2 != normal_coord_name:
            cat2.rename(columns={
                coord_name2[0]: normal_coord_name[0], 
                coord_name2[1]: normal_coord_name[1]
                }, inplace=True)
        
        # ^ ----- step2: 构建坐标列
        # 创建坐标列
        ra1 = list(cat1['ra'])
        dec1 = list(cat1['dec'])

        ra2 = list(cat2['ra'])
        dec2 = list(cat2['dec'])

        coord1 = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree)
        coord2 = SkyCoord(ra=ra2*u.degree, dec=dec2*u.degree)

        # ^ ----- step3: match
        # 遍历coord1, 找到coord2中距离coord1中每个源最近的源的索引idx等信息
        idx, d2d, d3d = coord1.match_to_catalog_sky(coord2)
        sep_constraint = d2d < max_sep  # 条件满足则为True

        # 向cat1添加match信息
        cat1['idx'] = idx
        cat1['sep_constraint'] = sep_constraint
        cat1['d2d'] = d2d.to('arcsec').value  # 单位: 角秒

        # 设置cat2的索引列为id，用于merge
        cat2['idx'] = cat2.index

        # 合并两表(左边是cat1, 右边是match到的cat2)
        df_merge = pd.merge(left=cat1, right=cat2, on='idx')

        # 留下满足阈值条件的行
        matched_cat = df_merge.query("sep_constraint==True")

        # 整理表格
        ls_idx = matched_cat['idx']
        del matched_cat['idx']
        matched_cat.insert(0, 'idx', ls_idx)

        ls_d2d = matched_cat['d2d']
        del matched_cat['d2d']
        matched_cat.insert(0, 'd2d', ls_d2d)

        matched_cat.reset_index(inplace=True, drop=True)
        del matched_cat['sep_constraint']

        # ^ ----- step4: 多对应情况处理
        # 找到出现重复的idx
        list_idx_duplicated = list(matched_cat.loc[matched_cat['idx'].duplicated(), 'idx'])  # 查询出现重复的idx
        duplicated_num = len(list_idx_duplicated)
        self.duplicated_num = duplicated_num  # 多对应情况数量
        
        # 去除重复源
        if duplicated_num==0:
            cat_final = matched_cat.copy()
        else:
            print(f"==> {duplicated_num} sources have neighbors within {sep} arcsec")
            cat_final = matched_cat.copy()
            list_index_keep = []  # 收集近邻源中的保留源的index
            list_index_drop = []  # 收集drop掉的源的index列表

            # 分别处理重复的idx
            for idx_duplicated in list_idx_duplicated:
                # 找到保留源的index(只保留最近的源)
                index_keep= int(cat_final.loc[cat_final['idx']==idx_duplicated, 'd2d'].idxmin())
                list_index_keep.append(index_keep)
                # 找出待删除的源
                index_drop = list(cat_final.loc[cat_final['idx']==idx_duplicated].index)
                index_drop.remove(index_keep)
                for index in index_drop:
                    list_index_drop.append(index)
            cat_final = cat_final.drop(list_index_drop).reset_index(drop=True)
        
            # 制作重复源表格
            duplicated_cat = matched_cat.loc[list_index_keep + list_index_drop]
            duplicated_cat.sort_values('idx', inplace=True)
            self.duplicated_cat = duplicated_cat

        # ^ ----- step5: 回传结果
        self.result = cat_final
    
        return cat_final
