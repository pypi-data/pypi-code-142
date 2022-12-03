import pandas as pd
import requests
import os
import re
import wget

location = os.path.dirname(os.path.realpath(__file__))
ncbidb = pd.read_csv(os.path.join(location, 'datasets', 'Homo_sapiens.gene_info.gz'),sep='\t')
tab_uni =  pd.read_csv(os.path.join(location, 'datasets', 'HUMAN_9606_idmapping_selected.dat.gz'),sep='\t',names=['uniprot','mapper','id'])


def update_mapping_datasets():
	out = os.path.join(location, 'datasets')
	ncbidb='https://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz'
	tab_uni='https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/HUMAN_9606_idmapping_selected.dat.gz'	 
	print('Downloading NCBI mapping file')
	wget.download(ncbidb,out)
	print('Downloading UniProt mapping file')
	wget.download(tab_uni,out)
	print('!!DATABASES UPDATED!!')


def gene_mapping_many(query_list,source,target):

	if source=='ensembl' and target=='symbol':
	    ense=ncbidb['dbXrefs'].apply(lambda x : re.sub(r'.+?(?=ENS)', '', x))
	    dictio=dict((x.split('|')[0], y) for x, y in list(zip(ense,ncbidb['Symbol'])) if 'ENS' in x)
	    return list(map(dictio.get,query_list))

	elif source=='ensembl' and target=='entrez':
	    ense=ncbidb['dbXrefs'].apply(lambda x : re.sub(r'.+?(?=ENS)', '', x))
	    dictio=dict((x.split('|')[0], y) for x, y in list(zip(ense,ncbidb['GeneID'])) if 'ENS' in x)
	    return list(map(dictio.get,query_list))

	elif source=='ensembl' and target=='uniprot':
	    dictio=dict(zip(list(reversed(tab_uni[tab_uni.mapper=='Ensembl'].id.tolist())),
			    list(reversed(tab_uni[tab_uni.mapper=='Ensembl'].uniprot.tolist()))))
	    return list(map(dictio.get,query_list))

	elif source=='entrez' and target=='ensembl':
	    ense=ncbidb['dbXrefs'].apply(lambda x : re.sub(r'.+?(?=ENS)', '', x))
	    dictio=dict((y, x.split('|')[0]) for x, y in list(zip(ense,ncbidb['GeneID'])) if 'ENS' in x)
	    return list(map(dictio.get,query_list))

	elif source == 'entrez' and target == 'symbol':
	    dictio=dict((x, y) for x, y in list(zip(ncbidb['GeneID'],ncbidb['Symbol'])))
	    return list(map(dictio.get,query_list))

	elif source=='entrez' and target=='uniprot':
	    dictio=dict(zip(list(reversed(tab_uni[tab_uni.mapper=='GeneID'].id.tolist())),
			    list(reversed(tab_uni[tab_uni.mapper=='GeneID'].uniprot.tolist()))))
	    return list(map(dictio.get,query_list))

	elif source=='symbol' and target=='ensembl':
	    ense=ncbidb['dbXrefs'].apply(lambda x : re.sub(r'.+?(?=ENS)', '', x))
	    dictio=dict((y, x.split('|')[0]) for x, y in list(zip(ense,ncbidb['Symbol'])) if 'ENS' in x)
	    return list(map(dictio.get,query_list))

	elif source == 'symbol' and target == 'entrez':
	    dictio=dict((y, x) for x, y in list(zip(ncbidb['GeneID'],ncbidb['Symbol'])))
	    return list(map(dictio.get,query_list))

	elif source=='symbol' and target=='uniprot':
	    dictio=dict(zip(list(reversed(tab_uni[tab_uni.mapper=='Gene_Name'].id.tolist())),
			    list(reversed(tab_uni[tab_uni.mapper=='Gene_Name'].uniprot.tolist()))))
	    return list(map(dictio.get,query_list))

	elif source=='uniprot' and target=='ensembl':
	    dictio=dict(zip(list(reversed(tab_uni[tab_uni.mapper=='Ensembl'].uniprot.tolist())),
			    list(reversed(tab_uni[tab_uni.mapper=='Ensembl'].id.tolist()))))
	    return list(map(dictio.get,query_list))

