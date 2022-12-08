import json
import os
import random
import sys
from typing import List

import numpy as np
import pandas as pd
import pkg_resources
import torch
from torch import Tensor

import Sagittarius.webserver_files.EvoDevo_utils as EvoDevo_utils
from Sagittarius.webserver_files.Sagittarius import Sagittarius


def initialize_random_seed(seed=3):
    """
    Initialize random seeds for an experiment.
    
    Parameters:
        seed (int): Random seed to use
    """
    np.random.seed(seed)
    torch.random.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True


def convert_species_to_tensor(species: str, device='cpu'):
    """
    Produces the tensor representation for a given EvoDevo species.
    
    Parameters:
        species (str): EvoDevo species to consider; must be one of {Chicken, Human, Mouse, Opossum,
            Rabbit, Rat, RhesusMacaque} (no spaces in R.M.).
        device (str): device to put result on; cpu by default.
    
    Returns:
        Tensor of shape (1,) with the integer representation for the given species.
    """
    SP_LIST = ['chicken', 'human', 'mouse', 'opossum', 'rabbit', 'rat', 'rhesusmacaque']
    assert species.lower() in SP_LIST, "Unknown species: {}".format(species)
    return torch.tensor([SP_LIST.index(species.lower())])  # shape (1,) tensor


def convert_species_list_to_tensor(species: List[str], device='cpu'):
    """
    Produces the tensor representation for a set of EvoDevo species.
    
    Parameters:
        species (List[str]): list of length N, where each element is a species in the EvoDevo dataset;
            species[i] must be in {Chicken, Human, Mouse, Opossum, Rabbit, Rat, RhesusMacaque} (no 
            spaces in R.M.) for all i.
        device (str): device to put result on; cpu by default.
        
    Returns:
        Tensor of shape (N,) where each element is the integer representation for the given species element.
    """
    return torch.cat([convert_species_to_tensor(s, device=device) for s in species], dim=0)  # shape (N,) tensor


def convert_organ_to_tensor(organ: str, device='cpu'):
    """
    Produces the tensor representation for a given EvoDevo organ.
    
    Parameters:
        organ (str): EvoDevo organ to consider; must be one of {Brain, Cerebellum, Heart, Kidney,
            Liver, Ovary, Testis}.
        device (str): device to put result on; cpu by default.
    
    Returns:
        Tensor of shape (1,) with the integer representation for the given organ.
    """
    ORG_LIST = ['brain', 'cerebellum', 'heart', 'kidney', 'liver', 'ovary', 'testis']
    assert organ.lower() in ORG_LIST, "Unknown organ: {}".format(organ)
    return torch.tensor([ORG_LIST.index(organ.lower())])  # shape (1,) tensor


def convert_organ_list_to_tensor(organs: List[str], device='cpu'):
    """
    Produces the tensor representation for a set of EvoDevo organs.
    
    Parameters:
        organs (List[str]): list of length N, where each element is an organ in the EvoDevo dataset;
            organs[i] must be in {Brain, Cerebellum, Heart, Kidney, Ovary, Testis} for all i.
        device (str): device to put result on; cpu by default.
        
    Returns:
        Tensor of shape (N,) where each element is the integer representation for the given organ element.
    """
    return torch.cat([convert_organ_to_tensor(o, device=device) for o in organs], dim=0)  # shape (N,) tensor


def convert_timepoints_to_tensor(timepoints: List[float], device='cpu'):
    """
    Get timepoint query as tensor.
    
    Parameters:
        timepoints (List[float]): list of length T with timepoints to simulate.
        device (str): device to put result on; cpu by default.
        
    Returns:
        Tensor of shape (T,) with timepoints for simulation.
    """
    return torch.tensor(timepoints).to(device)  # shape (T,) tensor


def convert_timepoint_list_to_tensor(timepoints: List[List[float]], device='cpu'):
    """
    Get timepoint queries as tensor.
    
    Parameters:
        timepoints (List[List[float]]): list of length N, where the longest nested list has length T;
            timepoints at which to simulate for each of N queries.
        device (str): device to put result on; cpu by default.
        
    Returns:
        tps (Tensor): tensor of shape (N, T) with timepoints for simulation
        mask (Tensor): binary tensor of shape (N, T) where mask[i, t] = 1 indicates that we should
            simulate at that time.
    """
    T = max([len(timepoints[i]) for i in range(len(tps))])
    tps = torch.stack([torch.cat(torch.tensor(tp), torch.zeros(T-len(tp)))
                       for tp in timepoints], dim=0).to(device)  # shape (N,T) tensor
    mask = torch.stack([torch.cat(torch.ones(len(tp)), torch.zeros(T-len(tp))) 
                        for tp in timepoints], dim=0).to(device)
    return tps, mask


def get_single_nearest_EvoDevo_source_sequence(species: str, organ: str, device: str='cpu',
                                               restrict_to_nonstationary: bool=True):
    """
    Get the closest sequence in the EvoDevo dataset for a given target sequence. The "closest" sequence
    is defined as the target sequence itself except for the (Rhesus Macaque, Ovary) query, which does not
    exist in the dataset. In this case, we define (Rhesus Macaque, Testis) to be the closest sequence.
    
    Parameters:
        species (str): species within the EvoDevo dataset; must be in {Chicken, Human, Mouse, Opossum,
            Rabbit, Rat, RhesusMacaque} (no spaces in R.M.)
        organ (str): organ within the EvoDevo dataset; must be in {Brain, Cerebellum, Heart, Kidney,
            Ovary, Testis}
        device (str): device to put result on; cpu by default
        restrict_to_nonstationary (bool): True iff we should restrict the input genes to be those deemed
            non-stationary by one random sequence; True by default to align with paper.
    
    Returns:
        sp (Tensor): long tensor of shape (1,) indicating the EvoDevo species
        org (Tensor): long tensor of shape (1,) indicating the EvoDevo organ
        expr (Tensor): tensor of shape (1, T, M) indicating the expression of sp and org in the EvoDevo data
        ts (Tensor): tensor of shape (1, T) indicating the timepoints of sp and org in the EvoDevo data
        mask (Tensor): binary tensor of shape (1, T) where `mask[0, t]` indicates that `ts[t]` was measured in
            the EvoDevo data
        non_stationary_mask (Tensor): binary tensor of shape (M') where `non_stationary_mask[g]` indicates that
            the gene `g` was retained in expr
    """
    if species.lower() != 'rhesusmacaque' or organ.lower() != 'ovary':  # we know it's directly in the dataset
        querySpec = species[0].upper() + species[1:].lower()
        queryOrg = organ[0].upper() + organ[1:].lower()
        sp, org, expr, ts, mask = EvoDevo_utils.limit_data_to_species_organ_combo(querySpec, queryOrg, device)
    else: # otherwise, take (RhesusMacaque, Testis)
        sp, org, expr, ts, mask = EvoDevo_utils.limit_data_to_species_organ_combo('RhesusMacaque', 'Testis', device)
    if restrict_to_nonstationary:  # need to do this in a standard way! Same as during training
        initialize_random_seed(0)
        data_path = pkg_resources.resource_filename('Sagittarius', 'webserver_files')
        non_stationary_mask = np.loadtxt(f'{data_path}/non_stationary_mask.txt')
        non_stationary_mask = torch.tensor(non_stationary_mask).to(device)
        # now apply to our expr.
        expr = torch.masked_select(expr, non_stationary_mask.view(1, -1).bool()).view(*expr.shape[:-1], -1)
    else:
        non_stationary_mask = torch.ones(expr.shape[-1]).to(device)  # don't remove anything
    return sp[:, 0].long(), org[:, 0].long(), expr, ts, mask, non_stationary_mask


def load_config_file(config_file):
    """
    Loads a configuration file.
    
    Parameters:
        config_file (str): configuration file to load.
    
    Returns:
        Loaded config file result (typically a dictionary).
    """
    with open(config_file, 'r') as f:
        return json.load(f)


def load_pretrained_EvoDevo_model(model_file: str, config_file: str, M_genes: int, T: int, device: str='cpu'):
    """
    Load a pre-trained Sagittarius model for EvoDevo.
    
    Parameters:
        model_file (str): name of file with pretrained model.
        config_file (str): name of file with configuration details.
        M_genes (int): number of input/output genes for the model.
        T (int): maximum time point to use in the reference space.
        device (str): device to put the model on; cpu by default.
    """
    net = Sagittarius(M_genes, 2, [7, 7], minT=0, maxT=T, **load_config_file(config_file), device=device).to(device)
    net.load_state_dict(torch.load(model_file, map_location=device))
    return net


def simulate_single_EvoDevo(net: Sagittarius, tgt_spec: Tensor, tgt_org: Tensor, tgt_ts: Tensor, 
                            src_expr: Tensor, src_spec: Tensor, src_org: Tensor, src_ts: Tensor, src_mask: Tensor,
                            sampling_k: int=10):
    """
    Simulate a single measurement from EvoDevo.
    
    Parameters:
        net (Sagittarius): trained model to simulate from.
        tgt_spec (Tensor): tensor of shape (1,) indicating species to generate for.
        tgt_org (Tensor): tensor of shape (1,) indicating organ to generate for.
        tgt_ts (Tensor): tensor of shape (1,T) indicating timepoints to generate at.
        src_expr (Tensor): tensor of shape (1,T',M) indicating source expression data.
        src_spec (Tensor): tensor of shape (1,) indicating the species for `src_expr`.
        src_org (Tensor): tensor of shape (1,) indicating the organ for `src_expr`.
        src_ts (Tensor): tensor of shape (1,T') indicating the timepoints for `src_expr`.
        src_mask (Tensor): binary tensor of shape (1,T') where `src_mask[0, t] = 1` indicates that
            `src_expr[0, t, :]` was measured in the dataset.
        sampling_k (int): number of samples to draw and average from Sagittarius's latent space; 10
            by default to stabilize generation.
            
    Returns:
        sim_expr (Tensor): tensor of shape (1,T,M) with simulated expression for `tgt_spec`, `tgt_org`,
            and `tgt_ts`.
    """
    T_tgt = tgt_ts.shape[-1]
    T_src = src_ts.shape[-1]
    stacked_tgt_y = [torch.stack([tgt_spec for _ in range(T_tgt)], dim=1),
                     torch.stack([tgt_org for _ in range(T_tgt)], dim=1)]
    stacked_src_y = [torch.stack([src_spec for _ in range(T_src)], dim=1),
                     torch.stack([src_org for _ in range(T_src)], dim=1)]
    sim_expr = net.generate(
        src_expr, src_ts, tgt_ts.unsqueeze(0), stacked_src_y, stacked_tgt_y, src_mask, k=sampling_k)[0]
    return sim_expr


def get_EvoDevo_gene_names(gene_mask: Tensor=None):
    """
    Get list of genes as human-readable names.
    
    Parameters:
        gene_mask (Tensor): binary tensor of shape (5037,) indicating whether the gene at that
            index should be retained in the result; None by default, indicating that all indices
            should be retained.
    
    Returns:
        Dictionary with key `gene`, value as numpy array of gene names that should be included, 
            where the length of the value array is the same as the number of non-zero entries in
            `gene_mask`.
    """
    data_path = pkg_resources.resource_filename('Sagittarius', 'webserver_files')
    gene_mapping = pd.read_csv(f'{data_path}/EvoDevo:idx_to_gene.txt',
        names=['gene'], index_col=0)
    name_mapping = {}
    with open(f'{data_path}/EvoDevo:gene_name_mapping.txt', 'r') as f:
        for idx, line in enumerate(f.readlines()):
            if idx == 0:  # header row
                continue
            names = line.strip().split('\t')
            if len(names) < 5:  # missing ensembl id
                continue
            ensembl_id = names[4]
            symbol = names[0]
            name_mapping[ensembl_id] = symbol

    genes_included = []
    for idx in range(5037):
        if gene_mask is not None and gene_mask[idx] == 0:  # not included
            continue
        genes_included.append(name_mapping[gene_mapping.loc[idx]['gene']])
        
    return {'gene': np.asarray(genes_included)}
