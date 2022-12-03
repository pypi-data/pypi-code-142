import pandas as pd
import requests
import os

location = os.path.dirname(os.path.realpath(__file__))
ncbidb = pd.read_csv(os.path.join(location, '.', 'Homo_sapiens.gene_info.gz'),sep='\t')
tab_uni =  pd.read_csv(os.path.join(location, '.', 'HUMAN_9606_idmapping.dat.gz'),sep='\t')


def update_mapping_datasets():
	ncbidb=requests.get('https://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz')
	tab_uni=requests.get('https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/HUMAN_9606_idmapping.dat.gz')	 
	with open(os.path.join(location, '.', 'Homo_sapiens.gene_info.gz','w'))as f:
		f.write(ncbidb)
	with open(os.path.join(location, '.', 'HUMAN_9606_idmapping.dat.gz','w')) as f:
		f.write(tab_uni)
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
	    dictio=dict(zip(tab_uni[tab_uni.mapper=='Ensembl'].id.tolist(),
			    tab_uni[tab_uni.mapper=='Ensembl'].uniprot.tolist()))
	    return list(map(dictio.get,query_list))

	elif source=='entrez' and target=='ensembl':
	    ense=ncbidb['dbXrefs'].apply(lambda x : re.sub(r'.+?(?=ENS)', '', x))
	    dictio=dict((y, x.split('|')[0]) for x, y in list(zip(ense,ncbidb['GeneID'])) if 'ENS' in x)
	    return list(map(dictio.get,query_list))

	elif source == 'entrez' and target == 'symbol':
	    dictio=dict((x, y) for x, y in list(zip(ncbidb['GeneID'],ncbidb['Symbol'])))
	    return list(map(dictio.get,query_list))

	elif source=='entrez' and target=='uniprot':
	    dictio=dict(zip(tab_uni[tab_uni.mapper=='GeneID'].id.tolist(),
			    tab_uni[tab_uni.mapper=='GeneID'].uniprot.tolist()))
	    return list(map(dictio.get,query_list))

	elif source=='symbol' and target=='ensembl':
	    ense=ncbidb['dbXrefs'].apply(lambda x : re.sub(r'.+?(?=ENS)', '', x))
	    dictio=dict((y, x.split('|')[0]) for x, y in list(zip(ense,ncbidb['Symbol'])) if 'ENS' in x)
	    return list(map(dictio.get,query_list))

	elif source == 'symbol' and target == 'entrez':
	    dictio=dict((y, x) for x, y in list(zip(ncbidb['GeneID'],ncbidb['Symbol'])))
	    return list(map(dictio.get,query_list))

	elif source=='symbol' and target=='uniprot':
	    dictio=dict(zip(tab_uni[tab_uni.mapper=='Gene_Name'].id.tolist(),
			    tab_uni[tab_uni.mapper=='Gene_Name'].uniprot.tolist()))
	    return list(map(dictio.get,query_list))

	elif source=='uniprot' and target=='ensembl':
	    dictio=dict(zip(tab_uni[tab_uni.mapper=='Ensembl'].uniprot.tolist(),
			    tab_uni[tab_uni.mapper=='Ensembl'].id.tolist()))
	    return list(map(dictio.get,query_list))

