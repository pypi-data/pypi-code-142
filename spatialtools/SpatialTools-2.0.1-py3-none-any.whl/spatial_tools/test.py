#!/share/nas2/genome/biosoft/Python//3.7.3/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/11/23 11:00
# @Author : jmzhang
# @Email : zhangjm@biomarker.com.cn
import logging
import sys
sys.path.append('/Users/jmzhang/workspace/mygithub/SpatialTools/spatial_tools/')

import spatial_tools_v2
import anndata as ad
import pandas as pd
import json

s1000_level7 = spatial_tools_v2.SpatialTools.load_from('data_set/s1000_level7_reference.pkl.gz')
adata_level7 = ad.read_h5ad('/Users/jmzhang/workspace/mygithub/bioinfor_note/spatial_note/vignette_data/results/level7.h5ad')

# logging.info({'s1000_level7': s1000_level7})



# adata = pd.read_csv('/Users/jmzhang/workspace/mygithub/bioinfor_note/RCTD_note/level7_RCTD.xls', sep='\t')
# adata['_class'] = adata['class']
# spatial_tools_v2.SpatialApp.run_dash(spatial_tools_obj=s1000_level7, adata=adata_level7, port=2008, debug=True)

# spatial_tools_v2.SpatialApp.run_dash(spatial_tools_obj=s1000_level7, port=2008, debug=True)

spatial_tools_v2.SpatialApp.run_dash(port=2008, debug=True)