import csv
import ujson as json
import warnings
from pathlib import Path
from typing import Callable, List, Optional, Tuple, Iterator, Union
from dbnomics_data_model.observations import Frequency, detect_period_format_strict, period_format_strict_regex_list
from oecd_toolbox.converters import SimpleConverter
from dbnomics_fetcher_toolbox.resources import Resource 
from slugify import slugify
import re
import daiquiri

logger = daiquiri.getLogger(__name__)


class FileResource(Resource):
    """ A resource-type consisting of a single downloadable file, identified by a URL
    and a target path where it should be deposited.
    """
    targetDataset: Path
    sourceFolder: Path
    fileToProcess: str
    query: Union[str, None] = None # '.TOVT+TOVV.G46+G47..I15.'
    

    def delete(self):
        """ Deletes the local representation of a dataset including its containing folder. """
        for f in self.targetDataset.glob('*.*'):
            f.unlink()
        self.targetDataset.rmdir
    
    def __str__(self) -> str:
        return f'target ds: {self.targetDataset}, source fold: {self.sourceFolder}, file: {self.fileToProcess}, filter: {self.query}'

class DataCaptureConverter(SimpleConverter):
    ''' A converter to create DataCapture ready files from DbNomics jsonl files for an entire project.'''
    def prepare_resources(self) -> Iterator[Resource]:
        #print('Create an iterator of resources - can be a similar function outside of a subclass')
        
        for f in self.source_dir.rglob('series.jsonl'):
            dirPath = f.parents[0]
            fileName = f.name
            relDirPath = dirPath.relative_to(self.source_dir)
            did = slugify(str(relDirPath))
            yield FileResource(id=did, sourceFolder = dirPath, targetDataset = self.target_dir / relDirPath, fileToProcess = fileName)
            

    def process_single_resource(self, res: Resource):
        if not res.targetDataset.exists():
            res.targetDataset.mkdir(parents=True)
        series_jsonl_to_DataCapturecsv(res.sourceFolder / res.fileToProcess, Path(res.targetDataset / res.fileToProcess).with_suffix('.csv'))


class DataCaptureConverterWithRegex(SimpleConverter):
    ''' A converter to create DataCapture ready files from DbNomics jsonl files for an entire project.
        params should be provided as a list of tuples to prepare_resources (datasetID, regexFilter on codes)
    '''
    
    def prepare_resources(self, params: list) -> Iterator[Resource]:
        #print('Create an iterator of resources - can be a similar function outside of a subclass')
        
        for dirPath, filter in params:
            did = slugify(str(dirPath))
            yield FileResource(id=did, sourceFolder = self.source_dir / dirPath, targetDataset = self.target_dir / dirPath, fileToProcess = 'series.jsonl', query=filter)

    def process_single_resource(self, res: Resource):
        if not res.targetDataset.exists():
            res.targetDataset.mkdir(parents=True)
        series_jsonl_to_DataCapturecsv(res.sourceFolder / res.fileToProcess, Path(res.targetDataset / res.fileToProcess).with_suffix('.csv'), get_pattern_from_query(res.query))


def dataset_json_to_csv(source_dir : Path):
    """Convert dataset.json into a csv file"""
    warnings.warn("Dataset.json to csv conversion is deprecated. Use the json file directly to access structural information.", warnings.DeprecationWarning)    


#----------------------series_jsonl conversions----------------------
def series_jsonl_to_csv_base(source_file: Path, target_file: Path, obslist_fn: Callable[[List], None]):
    """ Convert series.jsonl into a csv file. 
    Base function.
    Needs to be called by a function that provides the fields and methods to convert to.
    """

    json_file = []
    for line in open(source_file, 'r', encoding="UTF-8"):
        json_file.append(json.loads(line))
    
    def create_csv_file(tf: Path):
        with open(tf, 'w', encoding="UTF-8", newline='') as csvfile:
            obslist = obslist_fn(json_file)
            fieldnames = list(obslist[0].keys())
            writer = csv.DictWriter(f=csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            for data in obslist[1:]:
                writer.writerow(data)
    
    create_csv_file(target_file)


def series_jsonl_to_csv(source_file: Path):
    """ Simple generic csv flavour of the convertor. """

    def create_observations_list(json_file: List) -> List:
        L=[]

        # construct header row
        takefirst = json_file[0]
        fieldnames = ['code', 'period']
        for v in takefirst['observations'][0][1:]:
            fieldnames.append(v)
        L.append({v:v for v in fieldnames}) 

        # append data rows
        for series in json_file:
            for obs in series['observations'][1:]:
                dim_dict=dict()
                dim_dict['code'] = series['code']
                dim_dict['PERIOD'] =  obs[0]
                for c, v in enumerate(series['observations'][0][1:]):
                        dim_dict[v] = obs[c+1]

                L.append(dim_dict)
        return L 

    series_jsonl_to_csv_base(source_file=source_file, target_file='series.csv',  obslist_fn=create_observations_list)       


DC_eligible_frequencies = [Frequency.ANNUAL, Frequency.QUARTERLY, Frequency.MONTHLY, Frequency.BI_ANNUAL]
DC_eligible_frequency_codes = [f.to_dimension_code() for f in DC_eligible_frequencies]


def series_jsonl_to_DataCapturecsv(source_file: Path, target_file: Path, regex: Union[re.Pattern, None] = None):
    """ DataCapture csv flavour of the convertor. """
    
    def create_DCobservations_list(json_file: List) -> List:
        L=[]

        # construct header row
        takefirst = json_file[0]
        fieldnames = ['code', 'year', 'freq', 'period']
        for v in takefirst['observations'][0][1:]:
            fieldnames.append(v)
        L.append({v:v for v in fieldnames})    

        # append data rows
        sm = None 
        for series in json_file:
            if regex:
                sm = regex.match(series['code'])
                if not sm: 
                   logger.debug(f'series {series["code"]} skipped, not matching regex') 
            
            if sm or not regex:        
                if isinstance(series['dimensions'], list):
                    series_freq = series['dimensions'][0]
                elif isinstance(series['dimensions'], dict):
                    series_freq = series['dimensions']['FREQ']

                if series_freq in DC_eligible_frequency_codes:
                    for obs in series['observations'][1:]:
                        dim_dict=dict()
                        dim_dict['code'] = series['code']
                        dim_dict['year'], dim_dict['freq'], dim_dict['period'] = get_DC_compatible_date(obs[0])
                        for c, v in enumerate(series['observations'][0][1:]):
                            dim_dict[v] = obs[c+1]

                        L.append(dim_dict)
                    
        return L 

    
    series_jsonl_to_csv_base(source_file=source_file, target_file=target_file, obslist_fn=create_DCobservations_list)


  

def get_DC_compatible_date(period: str) -> Optional[Tuple[int, str, int]]:
    """Return a tuple of (year, frequency_code, period_withinyear) or `None` if unable to detect.

    # Working examples:
    >>> get_DC_compatible_date("2014")
    2014, A, 1 
    >>> get_DC_compatible_date("2014-S1")
    2014, Q, 2
    >>> get_DC_compatible_date("2014-Q1")
    2014, Q, 1 
    >>> get_DC_compatible_date("2014-01")
    2014, M, 1

    # Invalid formats:
    >>> detect_period_format_strict("ABCDE")
    >>> detect_period_format_strict("2014Z01")
    """
    
    freq = detect_period_format_strict(period)
    if freq in DC_eligible_frequencies:
        for period_format, regex in period_format_strict_regex_list: 
            if freq == period_format:
                m = regex.match(period)
                if freq == Frequency.ANNUAL:
                    return int(m.group(1)), freq.to_dimension_code(), 1
                elif freq == Frequency.BI_ANNUAL:
                    return int(m.group(1)), "Q", int(m.group(2)) * 2
                else:
                    return int(m.group(1)), freq.to_dimension_code(), int(m.group(2))
    return None

    
def get_pattern_from_query(query: str) -> re.Pattern:
    """ Working example: 
    >>> get_pattern_from_query('.TOVT+TOVV.G46+G47..I15.')
    .+\.(TOVT|TOVV)\.(G46|G47)\..+\.(I15)\..+
    """ 
    
    seq = query.split('.')
    reseq = []
    for s in seq:
        if s == '':
            reseq.append(r'.+')
        else:
            plus_to_or = '(' + s.replace('+','|') + ')'
            reseq.append(plus_to_or)

    return re.compile(r'\.'.join(reseq))            
