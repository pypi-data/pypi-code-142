import os
import sys
from typing import List

import anndata

sys.path.append(os.path.join(sys.path[0], '../'))
# import api_utils
import numpy as np

from Sagittarius import api_utils


def simulate_single_EvoDevo(model_file: str, config_file: str, 
                            species: str, organ: str, timepoint: List[float], 
                            T: int=25, sampling_k: int=10, device: str='cpu'):
    """
    Simulate Evo-Devo measurement for a single environmental combination.
    
    Parameters:
        model_file (str): .pth filename to load with trained model parameters
        config_file (str): .json filename to load with model configuration
        species (str): species to simulate. Must be in: 
            ['Chicken', 'Human', 'Mouse', 'Opossum', 'Rabbit', 'Rat', 'RhesusMacaque'].
        organ (str): organ to simulate. Must be in:
            ['Brain', 'Cerebellum', 'Heart', 'Kidney', 'Liver', 'Ovary', 'Testis'].
        timepoint (List[float]): list of time indices to simulate at.
        T (int): maximum time threshold in Evo-Devo model for reference space points; 25 by default.
        sampling_k (int): number of samples to take and average from source latent space; 10 by default.
        device (str): device to simulate on; cpu by default.
    
    Returns:
        simulated_expr (AnnData): simulated gene expression vector for <species, organ> at each time in <timepoint>.
    """
    assert os.path.exists(model_file), "Model file does not exist: {}".format(model_file)
    assert os.path.exists(config_file), "Config file does not exist: {}".format(config_file)
    
    # determine the source and target sequences
    target_sp_tensor = api_utils.convert_species_to_tensor(species, device)
    target_org_tensor = api_utils.convert_organ_to_tensor(organ, device)
    target_ts = api_utils.convert_timepoints_to_tensor(timepoint, device)
    src_sp_tensor, src_org_tensor, src_expr, src_ts, src_mask, non_stationary = \
        api_utils.get_single_nearest_EvoDevo_source_sequence(species, organ, device)
    
    # define and load the pretrained model
    M_genes = src_expr.shape[-1]
    model = api_utils.load_pretrained_EvoDevo_model(model_file, config_file, M_genes, T, device=device)
    
    # simulate target time series
    simulated_expr = api_utils.simulate_single_EvoDevo(  # tensor of shape (1, len(timepoint), M_genes)
        model, target_sp_tensor, target_org_tensor, target_ts, src_expr, src_sp_tensor, src_org_tensor, src_ts, src_mask)
    
    # format for return
    gene_list = api_utils.get_EvoDevo_gene_names(non_stationary)  # dataframe, key "gene"; same ordering as expr
    obsm = {'time': np.asarray(timepoint)}
    adata = anndata.AnnData(X=simulated_expr[0].detach().cpu().numpy(), obs=obsm, var=gene_list)
    return adata