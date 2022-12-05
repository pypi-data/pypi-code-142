import pkg_resources

from Sagittarius import simulate_measurements


def EvoDevoSimulation(species: str, organ: str, timepoint):
    """
    Simulate new EvoDevo measurements for the webserver.
    
    Parameters:
        species (str): EvoDevo species to generate. Must be in {Chicken, Human, Mouse, Opossum,
            Rabbit, Rat, RhesusMacaque} (no spaces in R.M.).
        organ (str): EvoDevo organ to generate. Must be in {Brain, Cerebellum, Heart, Kidney,
            Liver, Ovary, Testis}.
        timepoint: comma-separated floats indicating the timepoints at which to simulate.
        
    Returns:
        df_res (pandas.DataFrame): dataframe object, where the index indicates the timepoint and the
            column names indicate the gene. Then, `df_res.loc[tp, g]` gives the simulated expression
            value at to,e `tp` (in `timepoint`) for gene `g`.
    """
    if isinstance(timepoint, float):
        timepoint = [timepoint]
    elif isinstance(timepoint, str):  # expect csv
        timepoint = timepoint.split(',')
        timepoint = [float(t) for t in timepoint]
    data_path = pkg_resources.resource_filename('Sagittarius', 'webserver_files')
    pretrained_model = f'{data_path}/EvoDevo:Sagittarius_pretrained.pth'
    config_file = f'{data_path}/EvoDevo_config.json'
    adata_res = simulate_measurements.simulate_single_EvoDevo(
        pretrained_model, config_file, species, organ, timepoint)
    
    df_res = adata_res.to_df()
    name_mapper = adata_res.var
    name_mapper = {idx: row['gene'] for idx, row in name_mapper.iterrows()}
    df_res.rename(mapper=name_mapper, inplace=True, axis='columns')
    df_res.insert(0, 'timepoint', adata_res.obs['time'].tolist())
    df_res.set_index('timepoint', inplace=True)
    return df_res
