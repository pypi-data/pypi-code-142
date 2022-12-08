import pandas as pd
import io
import xmltodict
import logging
from bs4 import BeautifulSoup

log = logging.getLogger('pyodv')

class ODV_Struct(object):
    def __init__(self, odv_path):

        self.init_vars()

        # Read text file
        self.file_path = odv_path
        self.read_odv_file(odv_path)

        # Get ODV protocol details
        self.odv_format()

        # Check Input Validity
        if not self.valid_input():
            log.warning('Bad Input file')

        # Make Valid if not valid
        # TODO: Figure out the edge cases that break the normal flow and fix'em

        # Get some ODV columns
        self.split_columns()

        # Parse file into meaningful struct
        self.parse_odv_file()

        # Parse the header into something useful:
        self.parse_header()

        # Check Output Validity
        self.valid_output()

    def init_vars(self):
        '''
        Just here to keep track of all the variables contained in the class...
        Not very pythonic.
        '''
        self.cols_data = []
        self.file_path = ''
        self.odv_header = ''
        self.odv_df = pd.DataFrame()
        self.df_data = pd.DataFrame()
        self.df_var = pd.DataFrame()
        self.df_qc = pd.DataFrame()
        self.cols_data = []
        self.cols_quality = []
        self.cols_variable = []
        self.comments = []
        self.cols = {}
        self.valid_bio_odv = False
        self.valid_odv = False

    def read_odv_file(self, odv_path):
        '''
        Read file into pandas dataframe without
        doing too much guesswork on structure
        '''
        try:
            # Try to read it with UTF-8 encoding, if that fails
            # try to read it with Latin-1 encoding. If that fails
            # just read it with UTF-8 and ignore any errors.
            with open(odv_path, encoding='utf8') as f:
                    lines = f.read()
            split = lines.rsplit('\n//', 1)
            self.odv_df = pd.read_csv(io.StringIO(split[1]), sep='\t')
        except UnicodeDecodeError:
            try:
                with open(odv_path, encoding='latin1') as f:
                        lines = f.read()
                split = lines.rsplit('\n//', 1)
                self.odv_df = pd.read_csv(io.StringIO(split[1]), sep='\t', encoding='latin1')
                
            except:
                with open(odv_path, encoding='utf8', errors="ignore") as f:
                    lines = f.read()
                split = lines.rsplit('\n//', 1)
                self.odv_df = pd.read_csv(io.StringIO(split[1]), sep='\t')

        split = lines.rsplit('\n//', 1)
        self.odv_df = pd.read_csv(io.StringIO(split[1]), sep='\t')
        self.odv_header = split[0]
        return

    def odv_format(self):
        '''
        Store the protocol specific information for ODV and bio-ODV
        '''
        self.mandatory_columns = ['Cruise',
                                  'Station',
                                  'Type',
                                  'Longitude [degrees_east]',
                                  'Latitude [degrees_north]',
                                  'LOCAL_CDI_ID',
                                  'EDMO_code',
                                  'Bot. Depth [m]', ]

        timestamp_col = self.get_timestamp_format()
        if timestamp_col is not None:
            self.mandatory_columns.append(timestamp_col)

        self.mandatory_bio_columns = ['MinimumDepthOfObservation [m]',
                                      'MaximumDepthOfObservation [m]',
                                      'SampleID',
                                      'ScientificName',
                                      'ScientificNameID',
                                      'Sex',
                                      'LifeStage',
                                      'ObservedIndividualCount']
        sample_effort_col = self.get_samplingeffort_format()
        if sample_effort_col is not None:
            self.mandatory_bio_columns.append(sample_effort_col)
        return

    def parse_odv_file(self):
        '''
        Split ODV file into table part and metadata part
        return:
          - dataframe with data
          - dataframe with quality variables
          - metadata variables

        Also combine the variables into a multidimensional XArray
        '''
        self.df_data = self.odv_df[self.cols_data].fillna(method='ffill')
        self.df_var = self.odv_df[self.cols_variable]
        self.df_qc = self.odv_df[self.cols_quality]
        return

    def split_columns(self):
        '''
        Get column names for ODV DF for the three catagories of columns:
        return:
          - data columns: generally voyage or station data
          - variable columns: sensor readings for voyage data
          - quality columns: the QC value associated with each reading.
        '''
        columns = self.odv_df.columns
        self.cols_quality = [col for col in columns if col.startswith('QV:')]
        remaining_cols = [x for x in columns if x not in self.cols_quality]
        self.cols_variable = remaining_cols[-len(self.cols_quality):]
        self.cols_data = list(set(self.odv_df.columns) - set(self.cols_variable) - set(self.cols_quality))

        self.cols = {'data': self.cols_data,
                     'variable': self.cols_variable,
                     'quality': self.cols_quality, }
        return

    def get_timestamp_format(self):
        '''
        Get the isoformat used in the column names. This is used to identify the mandatory timestamp column
        as well as to parse the datetime columns.
        '''
        columns = self.odv_df.columns
        date_cols = [i for i in columns if i.startswith('YYYY')]
        if len(date_cols) == 1:
            date_col = date_cols[0]
        elif len(date_cols) == 0:
            # No columns detected!
            date_col = None
        else:
            # Warning, multiple columns detected!
            date_col = date_cols[0]

        return date_col

    def get_samplingeffort_format(self):
        '''
        Get the SamplingEffort col name used in the file.
        '''
        columns = self.odv_df.columns
        effort_cols = [i for i in columns if i.startswith('SamplingEffort [')]
        if len(effort_cols) == 1:
            effort_col = effort_cols[0]
        elif len(effort_cols) == 0:
            # No columns detected!
            effort_col = None
        return effort_col

    def valid_input(self):
        '''
        Check if file is valid odv.
        TODO: Check if metadata is valid
        '''
        if set(self.mandatory_columns).issubset(set(self.odv_df.columns)):
            self.valid_odv = True
        else:
            self.valid_odv = False
        self.tmp_data = []
        for mand_col in self.mandatory_bio_columns:
            if mand_col in self.odv_df.columns:
                self.valid_bio_odv = True
                self.tmp_data.append(mand_col)
            elif mand_col+':INDEXED_TEXT' in self.odv_df.columns:
                self.valid_bio_odv = True
                self.tmp_data.append(mand_col+':INDEXED_TEXT')
            else:
                self.valid_bio_odv = False

        return self.valid_odv

    def valid_output(self):
        '''
        Run some checks to see that the file was parsed correctly:
            - has header params
                - has one param per value col
            - has header refs
            - Dataframes are correct:
                - df_data has X by N shape
                    - Columns contain the required vars...
                - df_qc has X by Y shape
                - df_var has X by Y shape
                - Y + N == all columns?
            - Is valid ODV and/or BioODV
        '''
        good_file = False

        if len(self.params) > 0:
            logging.debug(f'Has {len(self.params)} params')
            good_file = True
        else:
            logging.warning('WARNING: No params parsed...')
            good_file = False

        if len(self.refs) > 0:
            logging.debug(f'Has {len(self.refs)} refs.')
            good_file = True
        else:
            logging.warning('WARNING: No refs parsed...')
            good_file = False

        if self.df_qc.shape == self.df_var.shape:
            logging.debug('Good file shape')
            good_file = True
        else:
            logging.warning('WARNING: Bad qc/var dimensions')
            good_file = False

        if self.valid_odv:
            good_file = True
        else:
            logging.warning('WARNING: Non-valid ODV file')
            good_file = False

        return good_file

    def parse_header(self):
        '''
        Parse the text header (the stuff filled with '//' cruft)
        into something readable
        '''
        refstr, paramstr = self.odv_header.split('//SDN_parameter_mapping\n//')
        refs = refstr.split('\n//')
        params = paramstr.split('\n//')

        self.refs = self.parse_psuedo_refs(refs)
        self.params = self.parse_psuedo_params(params)

        return

    def parse_psuedo_refs(self, xml_lines):
        '''
        Parse the pseudo xml from the headers into something meaningful.
        Return as a dict?
        '''
        parsed_list = []
        for line in xml_lines:
            if (line == '//') or (line == '\n'):
                # Empty lines of the pseudo xml header
                continue
            else:
                try:
                    line = line.lstrip('//')
                    soup = BeautifulSoup(line, "html.parser")
                    soup_dict = xmltodict.parse(str(soup)).get('sdn_reference')
                    parsed_list.append(soup_dict)
                except Exception as err:
                    # Possible Comment
                    self.comments.append(line)
                    logging.debug('--Problem Parsing Refs--')
                    logging.debug(err)
                    logging.debug(line)
        return parsed_list

    def parse_psuedo_params(self, xml_lines):
        '''
        Parse the pseudo xml from the headers into something meaningful.
        Return as a dict?
        '''
        parsed_list = []
        for line in xml_lines:
            try:
                line = line.lstrip('//')
                soup = BeautifulSoup(line, "html.parser")
                soup_dict = xmltodict.parse('<root>' + str(soup) + '</root>')['root']
                parsed_list.append(soup_dict)
            except Exception as err:
                logging.warning('--Problem Parsing Params--')
                logging.warning(err)
                logging.warning(line)
        return parsed_list
