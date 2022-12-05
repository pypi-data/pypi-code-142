import pyodbc, logging, os
import pandas as pd
import numpy as np

class sql_connect():
    
    def __init__(self,
                 db_user=None,
                 db_pass=None,
                 driver='PostgreSQL ODBC Driver(Unicode)',
                 server_name='om-hq-db1.ad.optimedpharmacy.com',
                 db_name='django',
                 port='5432',
                 conn_type='pyodbc',
                 conn_str_format='postgres-django',
                 env_variables=False
                 ):
                        
        # When env_variables is true, all params act like os env keys
        if env_variables == True:
            args_keys = set(locals().keys()).difference(['self', 'env_variables'])
            for k in args_keys:
                v = locals()[k]
                self.__dict__[k] = os.getenv(v)

        # when env_variables is False, all creds are read as regular str args
        elif env_variables == False:
            args_keys = set(locals().keys()).difference(['self'])
            for k in args_keys:
                self.__dict__[k] = locals()[k]
        
        # when env_variables is a dict, then we have a mix of the two above ideas
        elif type(env_variables) == dict:
            args_keys = set(locals().keys()).difference(['self', 'env_variables']
                                                        + list(env_variables.keys()))
            for k in args_keys:
                self.__dict__[k] = locals()[k]
            for k, v in env_variables.items():
                self.__dict__[k] = os.getenv(v)
        
        # raise an exception for any other env_variables setting...
        else:
            raise Exception('env_variables must be one of True, False, or {param:varkey, ...}')
            
        self.env_variables = env_variables
        
        # make sure we got a user and pass str one way or another...
        if self.db_user is None or self.db_pass is None:
            raise Exception('Must supply a db_user and db_pass')


    def build_conn_str(self):
        """ Build connection string, using self object, depends on conn_str_format
        return: nothing, just sets the conn_str based on init format string
        """
        
        if self.conn_str_format == 'postgres-django':
            
            self.conn_str = (
                f"DRIVER={self.driver};"
                f"SERVER={self.server_name};"
                f"DATABASE={self.db_name};"
                f"UID={self.db_user};"
                f"PWD={self.db_pass};"
                f"PORT={self.port};"
                )
            
        elif self.conn_str_format == 'mssql-cpr+':
            
            self.conn_str = (
                f"DRIVER={self.driver};"
                f"SERVER={self.server_name};"
                f"DATABASE={self.db_name};"
                f"UID={self.db_user};"
                f"PWD={self.db_pass};"
                )
            
        elif self.conn_str_format == 'mssql-azure':
            
            self.conn_str = (
                f'Driver={self.driver};'
                f'Server=tcp:{self.server_name},{self.port};'
                f'Database={self.db_name};'
                f'Uid={self.db_user};'
                f'Pwd={self.db_pass};'
                'Encrypt=yes;'
                'TrustServerCertificate=no;'
                'Connection Timeout=30;'
                'Authentication=ActiveDirectoryPassword;'
                )
        
        return self.conn_str

    def connect(self, set_encoding = True, db_encoding='utf-8',
                alternate_drivers=['PostgreSQL Unicode(x64)']):
        """ Connects to database through pyodbc using connection string format:
        return: pyodbc connection or raise an exception
        """
        
        # Grabs all installed drivers on local machine,
        # used if we have a connection string error below
        drivers = [self.driver] + alternate_drivers + pyodbc.drivers()
        
        try:
            logging.info("Obtaining connection to database...")
            
            for driver in drivers:
                try:
                    self.driver = driver
                    self.build_conn_str()
                    self.conn = pyodbc.connect(self.conn_str)
                    break
                except pyodbc.InterfaceError as e:
                    logging.warning(f'Error with connection string, trying alternate installed drivers: {e}')
                    continue
            
            logging.info("Connection obtained")
        
            if set_encoding is True:
                # Setting all the encoding to UTF-8 so both systems agree
                return self.set_encoding(db_encoding)
            else:
                return self.conn
            
        except pyodbc.DatabaseError as e:
            logging.error(f"Error connecting to database: {e}")
            raise e

    def set_encoding(self, db_encoding):
        '''Sets encoding on database, returns connection object'''
        
        try:
            self.conn.setdecoding(pyodbc.SQL_CHAR, encoding=db_encoding)
            self.conn.setdecoding(pyodbc.SQL_WCHAR, encoding=db_encoding)
            self.conn.setencoding(encoding=db_encoding)
            
            return self.conn
            
        except pyodbc.DatabaseError as e:
            logging.error(f"Error connecting to database: {e}")
            
            raise e


def get_connection(conn_str):
    print('Attempting to connect to PSQL Server...')
    #create a connection to the psql server using the conn_str above
    conn = pyodbc.connect(conn_str)

    #Setting all the encoding to UTF-8 so both systems agree on encoding and we don't get surprises
    conn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
    conn.setencoding(encoding='utf-8')
    print('Connection successful - All encoding set to UTF-8')
    return conn

def rename_claims_todf(df):
    """Takes in a claims dataframe and renames the columns to the EHO names
    PARAMETERS:
    df | pandas.Dataframe | claims dataframe
    RETURNS:
    df | pandas.DataFrame | renamed claims dataframe
    """
    renamedict = {'Group #': 'groupnum', 'Claim #':'claimnum', 'NABP':'nabp',
              'Pharmacy Name':'pharmacyname', 'Last Name':'lastname',
              'First Name':'firstname', 'MI':'mi', 'Member ID':'memberid',
              'Birth Date':'birthdate', 'Gender':'gender', 'Division':'division',
              'Dr. DEA #':'drdeanum', 'Rx Number':'rxnum', 'Date Filled':'datefilled',
              'Date Processed':'dateprocessed', 'Time Processed':'timeprocessed',
              'NDC Number':'ndcnum', 'Drug Name':'drugname', 'Refill Number':'refillnum',
              'Compound Code':'compoundcode', 'Quantity':'quantity', 'Days Supply':'dayssupply',
              'AWP':'awp', 'U&C':'uandc', 'Ingredient Cost':'ingredientcost', 'Disp Fee':'dispfee',
              'Sales Tax':'salestax', 'Total Amount':'totalamount', 'Copay':'copay',
              'OOP':'oop', 'Amount Billed':'amountbilled', 'Network Savings(U&C-Total Allowed)':'networksavings',
              'Client Savings(Copay-OOP)':'clientsavings', 'DAW':'daw', 'Brand/Generic':'brandgeneric',
              'GPI Code':'gpicode', 'Tier':'tier', 'DEA Class':'deaclass', 'Diagnosis':'diagnosis',
              'Census Type':'censustype', 'Therapeutic Category':'therapy', 'Patient Effective Date':'patienteffdate',
              'Patient Expiration Date':'patientexpdate', 'Formulary Item?':'formitem', 'Benefit Code':'benefitcode',
              'Negative Formulary?':'negativeform', 'Deductible':'deductible', 'Out of Pocket Copay':'oopcopay',
              'Bin #':'binnum', 'Rev Flg':'revflg', 'Rev Date  ':'revdate'
              }
    #reverses the key and values of the above dictionary to change our psql column names back to the EHO report format
    reversedict = {v: k for k, v in renamedict.items()}

    df.rename(columns=reversedict,inplace=True)

    return df

def rename_patients_todf(df_patients):
    """Takes in a patients dataframe and renames the columns to the EHO names
    PARAMETERS:
    df | pandas.Dataframe | claims dataframe
    RETURNS:
    df | pandas.DataFrame | renamed patients dataframe
    """

    newcolumns = {"cardholdernum": "Cardholder Nbr", "dob": "DOB","effdate": "Effective Date", "expdate":"Expiration Date       "}
    
    df_patients.rename(columns=newcolumns,
                                inplace=True)

    return df_patients

def get_allgroups_psql(conn, legacy=False):
    """Establishes a connection to psql database (REQUIRES conda ENVIROMENT VARIABLE for host and pwd), 
    and returns all groups plus their associated attributes as a dict in the form {groupnumber str: list of attributes}
    PARAMETERS:
    conn | connection object | connection object to use for SQL query, required
    legacy | boolean | setting for determining whether output should be df or group_names
    RETURNS:
    df | pandas.dataframte | nicely formatted dataframe containing the results of the query
    group_names | dict | legacy dictionary containing the results of the query {groupnumber str: list of attributes}
    """
    
    # connect and set encoding
    conn = get_connection(conn)
    
    # dataframe from SQL query, converting to legacy dict format
    sql = 'select * from ascendpbm_groups;'
    df = pd.read_sql(sql, conn)
    
    # df is nice and clean, prefer its use in the future
    if legacy == False:
        return df
    
    # group_names is a dict-based holdout from prior to having a working db
    else:
        df.loc[df['optimed_boolean'] == '1', 'optimed_boolean'] = True
        df.loc[df['optimed_boolean'] == '0', 'optimed_boolean'] = False
        df.loc[df['nonmember_boolean'] == '1', 'nonmember_boolean'] = True
        df.loc[df['nonmember_boolean'] == '0', 'nonmember_boolean'] = False
        group_names = df.set_index('group_number').to_dict(orient='index')
        for key, value in group_names.items():
            group_names[key] = list({k: value[k] for k in ('group_name', 'optimed_boolean', 'nonmember_boolean', 'employee_identifier')}.values())        
        return group_names

#turn the claims and formulary into str based dataframes
def get_allformulary_psql(conn, rebate_exclusions=False):
    """Establishes a connection to psql database (REQUIRES conda ENVIROMENT VARIABLE for host and pwd), 
    and returns all formulary as a dataframe.
    PARAMETERS:
    conn | connection object | connection object to use for SQL query, required
    RETURNS:
    df | pandas.dataframte | dataframe containing the results of the query
    """
    
    # connect and set encoding
    conn = get_connection(conn)
    
    # dataframe from SQL query, converting to legacy dict format
    if rebate_exclusions is False:
        sql = 'select * from formulary_2021;'
    else:
        sql = 'select * from formulary_with_rebate_exclusions;'
    
    df = pd.read_sql(sql, conn)
    
    return df

#turn the claims and formulary into str based dataframes
def get_allpharms_psql(conn):
    """Establishes a connection to psql database (REQUIRES conda ENVIROMENT VARIABLE for host and pwd), 
    and returns all formulary as a dataframe.
    PARAMETERS:
    conn | connection object | connection object to use for SQL query, required
    RETURNS:
    df | pandas.dataframte | dataframe containing the results of the query
    """
    
    # connect and set encoding
    conn = get_connection(conn)
    
    # dataframe from SQL query, converting to legacy dict format
    sql = 'select * from ehopharm_08062021;'
    df = pd.read_sql(sql, conn)
    
    return df

def get_paidclaims_psql(groupnums, startdate, enddate, conn, renamecols=True, convertdtypes=True):
    """Establishes a connection to psql database (REQUIRES conda ENVIROMENT VARIABLE for host and pwd), 
    and returns all net payable claims for the specified group for the given time period (based on date processed)
    PARAMETERS:
    groupnum | str/tuple | groupnum/s to get claims for
    startdate | str | YYYYMMDD format required - beginning date for query based on dateprocessed
    enddate | str | YYYYMMDD format required - end date for query based on dateprocessed
    conn | connection object | connection object to use for SQL query, required
    renamecols| Bool | True will convert column names to EHO report#21 naming, False = Raw psql column names
    convertdtypes| Bool | True will attempt to convert numeric cols to numpy.float64
    RETURNS:
    df | pandas.DataFrame | dataframe containing the results of the query
    """

    # connect and set encoding
    conn = get_connection(conn)

    #checks if one group num was given as string and formats it to work with the SQL query
    if type(groupnums) == str:
        groupnums = f"('{groupnums}')"

    print(f"Querying PSQL for group: {groupnums}")

    #This now pulls from a new view to give a better set of data
    sql = f"""
        SELECT
            *
        FROM paid_claims_reporting
        WHERE
            groupnum IN {groupnums}
            AND revflg IS NULL
            AND (dateprocessed::date BETWEEN to_date('{startdate}', 'YYYYMMDD') AND to_date('{enddate}', 'YYYYMMDD'));
        """

    df = pd.read_sql(sql, conn)
    print(f"Successfully pulled {groupnums} claim info from {startdate} to {enddate}")
    conn.close()

    if renamecols:
        df = rename_claims_todf(df)

    if convertdtypes:
        df = remove_column_white_space(df)
        df = convert_claim_dtypes(df)

    return df

def get_patients_psql(groupnums, conn):
    """Establishes a connection to psql database (REQUIRES conda ENVIROMENT VARIABLE for host and pwd), 
    and returns all patients for the specified group for the given time period (based on date processed)
    PARAMETERS:
    groupnum | str | groupnum to get claims for
    conn | connection object | connection object to use for SQL query, required
    RETURNS:
    df | pandas.DataFrame | dataframe containing the results of the query
    """

    conn = get_connection(conn)

    #checks if one group num was given as string and formats it to work with the SQL query 
    if type(groupnums) == str:
        groupnums = f"('{groupnums}')"

    print(f"Querying PSQL for group: {groupnums}")
    
    sql = f"""
        SELECT
            *
        FROM patients
        WHERE
            groupnum IN {groupnums};
        """

    df = pd.read_sql(sql, conn)
    df = rename_patients_todf(df)
    
    sql = f"""    
    select phe.newgroup, phe.newcard, phe.dob, min(oldeffdate)
    from patients_history_effdates as phe
    FULL OUTER JOIN patients as p
    on	p.groupnum = phe.newgroup AND
    	p.cardholdernum = phe.newcard AND
    	p.dob = phe.dob
    where	phe.newgroup IS NOT NULL AND
            phe.newgroup IN {groupnums} AND
    		p.status = 'A'
    GROUP BY phe.newgroup, phe.newcard, phe.dob
    ORDER BY phe.newgroup, phe.newcard;
    """

    print(f"Successfully pulled {groupnums} patients info")

    df_hist = pd.read_sql(sql, conn)

    conn.close()

    return df, df_hist

def convert_claim_dtypes(df):
    newtypes = {
                'Quantity': np.float64,
                'Days Supply': np.float64,
                'AWP': np.float64,
                'U&C': np.float64,
                'Ingredient Cost': np.float64,
                'Disp Fee': np.float64,
                'Sales Tax': np.float64,
                'Total Amount': np.float64,
                'Copay': np.float64,
                'OOP': np.float64,
                'Amount Billed': np.float64,
                'Network Savings(U&C-Total Allowed)': np.float64,
                'Client Savings(Copay-OOP)': np.float64,
                'Negative Formulary?': np.float64,
                'Deductible': np.float64,
                'Out of Pocket Copay': np.float64
    }
    
    df = df.astype(newtypes)

    return df

def remove_column_white_space(df, numcols=['Quantity', 'Days Supply', 'AWP',
                                           'U&C', 'Ingredient Cost', 'Disp Fee',
                                           'Sales Tax', 'Total Amount', 'Copay',
                                           'OOP', 'Amount Billed',
                                           'Network Savings(U&C-Total Allowed)',
                                           'Client Savings(Copay-OOP)',
                                           'Negative Formulary?',
                                           'Deductible', 'Out of Pocket Copay'
                                           ]
                              ):
    """Removes all white space from the columns provided
    PARAMETERS:
    df| pandas.DataFrame | Dataframe with columns for whitespace removal
    numcols| list/tuple | list or tuple containing names of columns to remove whitespace
    RETURNS
    df| pandas.DataFrame | DataFrame copy with whitespace removed from selected columns
    """
    for col in numcols:
        df[col] = df[col].str.replace(' ', '')
    
    return df


