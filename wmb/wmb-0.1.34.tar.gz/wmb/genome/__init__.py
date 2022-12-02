import numpy as np
import pandas as pd
import xarray as xr

from ..files import *


class MM10GenomeRef:
    def __init__(self, annot_version='GENCODE_vm23'):
        self.ENCODE_BLACKLIST_PATH = ENCODE_BLACKLIST_PATH
        self.GENCODE_MM10_vm22 = GENCODE_MM10_vm22
        self.GENCODE_MM10_vm23 = GENCODE_MM10_vm23
        self.TF_GENE_TABLE_PATH = MM10_TF_GENE_TABLE_PATH
        self.MAIN_CHROM_SIZES_PATH = MM10_MAIN_CHROM_SIZES_PATH
        self.MAIN_CHROM_NOCHRM_SIZES_PATH = MM10_MAIN_CHROM_NOCHRM_SIZES_PATH
        self.MAIN_CHROM_NOCHRM_NOCHRY_SIZES_PATH = MM10_MAIN_CHROM_NOCHRM_NOCHRY_SIZES_PATH
        self.CISTARGET_MGI_MOTIF_TF_TABLE_PATH = CISTARGET_MGI_MOTIF_TF_TABLE_PATH

        self._gene_id_to_name = None
        self._gene_name_to_id = None
        self._gene_id_base_to_name = None
        self._gene_name_to_id_base = None
        self._tf_gene_table = None
        self._get_gene_id_name_dict(annot_version=annot_version)
        return

    def get_gene_metadata(self, annot_version='GENCODE_vm23'):
        if annot_version == 'GENCODE_vm22':
            gene_meta = pd.read_csv(self.GENCODE_MM10_vm22, sep='\t', index_col='gene_id')
        elif annot_version == 'GENCODE_vm23':
            gene_meta = pd.read_csv(self.GENCODE_MM10_vm23, sep='\t', index_col='gene_id')
        else:
            raise NotImplementedError
        return gene_meta

    def _get_gene_id_name_dict(self, annot_version='GENCODE_vm23'):
        self._gene_id_to_name = self.get_gene_metadata(annot_version)['gene_name'].to_dict()

        self._gene_name_to_id = {v: k for k, v in self._gene_id_to_name.items()}
        self._gene_id_base_to_name = {k.split('.')[0]: v for k, v in self._gene_id_to_name.items()}
        self._gene_id_base_to_id = {k.split('.')[0]: k for k in self._gene_id_to_name.keys()}
        self._gene_name_to_id_base = {v: k for k, v in self._gene_id_base_to_name.items()}
        return

    def gene_id_to_name(self, gene_id, allow_nan=True):
        try:
            return self._gene_id_to_name[gene_id]
        except KeyError as e:
            try:
                return self._gene_id_base_to_name[gene_id]
            except KeyError:
                if allow_nan:
                    return np.nan
                else:
                    raise e

    def gene_name_to_id(self, gene_name, allow_nan=True):
        try:
            return self._gene_name_to_id[gene_name]
        except KeyError as e:
            if allow_nan:
                return np.nan
            else:
                raise e

    def gene_name_to_id_base(self, gene_name, allow_nan=True):
        try:
            return self._gene_name_to_id_base[gene_name]
        except KeyError as e:
            if allow_nan:
                return np.nan
            else:
                raise e

    def gene_id_base_to_id(self, gene_id_base, allow_nan=True):
        try:
            return self._gene_id_base_to_id[gene_id_base]
        except KeyError as e:
            if allow_nan:
                return np.nan
            else:
                raise e

    def get_tf_gene_table(self):
        if self._tf_gene_table is None:
            self._tf_gene_table = pd.read_csv(self.TF_GENE_TABLE_PATH)
        return self._tf_gene_table

    def get_tf_gene_ids(self):
        return pd.Index(self.get_tf_gene_table()['gene_id'].unique())

    def get_tf_gene_names(self):
        return pd.Index(self.get_tf_gene_table()['gene_name'].unique())

    def get_tf_motif_table(self):
        df = pd.read_csv(self.CISTARGET_MGI_MOTIF_TF_TABLE_PATH, sep='\t')
        return df


mm10 = MM10GenomeRef()


class MotifDSmm10:
    def __init__(self, motif_ds_dir, motif_cluster_meta_path, chrom_sizes_path):
        self._motif_ds_dir = motif_ds_dir
        self._chrom_sizes = pd.read_csv(chrom_sizes_path, header=None, sep='\t', index_col=0).squeeze()

        motif_cluster_meta = pd.read_csv(motif_cluster_meta_path)
        motif_cluster_meta.index.name = 'motif_cluster'
        self.motif_cluster_meta = motif_cluster_meta
        self._chrom_cache = {}

    def fetch(self, chrom):
        if chrom in self._chrom_cache:
            return self._chrom_cache[chrom]
        else:
            ds = xr.open_zarr(f'{self._motif_ds_dir}/{chrom}/')
            for col, col_data in self.motif_cluster_meta.items():
                if col_data.dtype == 'O':
                    ds.coords[col] = col_data.to_xarray().astype(str)
                else:
                    ds.coords[col] = col_data
            self._chrom_cache[chrom] = ds
        return ds

    def query_chrom_motif_position(self, chrom, motif_id, base_pos, score_cutoff=0):
        ds = self.fetch(chrom)
        pos_motif = np.where(ds['motif'].sel(motif_cluster=motif_id).values > score_cutoff)[0]
        neg_motif = np.where(ds['motif'].sel(motif_cluster=motif_id).values < score_cutoff)[0]
        motif_position = np.concatenate([pos_motif + base_pos, neg_motif - base_pos])
        motif_position.sort()
        return motif_position

    def query_motif_position_chrom_dict(self, motif_id, base_pos, score_cutoff=0):
        motif_position_chrom_dict = {}
        for chrom in self._chrom_sizes.index:
            motif_position_chrom_dict[chrom] = self.query_chrom_motif_position(chrom,
                                                                               motif_id,
                                                                               base_pos,
                                                                               score_cutoff=score_cutoff)
        return motif_position_chrom_dict


try:
    motif_ds = MotifDSmm10(motif_ds_dir=MOTIF_VIERSTRA_DS_PATH,
                           motif_cluster_meta_path=MOTIF_VIERSTRA_CLUSTER_META_PATH,
                           chrom_sizes_path=mm10.MAIN_CHROM_NOCHRM_NOCHRY_SIZES_PATH)
except FileNotFoundError:
    motif_ds = None
