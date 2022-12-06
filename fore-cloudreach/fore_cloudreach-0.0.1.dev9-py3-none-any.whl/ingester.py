from fore_cloudreach.errors import AuthenticationError, ReadingMapFileError, EmptyMapFileError, ReportCreationError
from fore_cloudreach.auth import Auth
from fore_cloudreach.template import Template
import pandas as pd
import datetime

class Ingester:
    """ 
    *Ingester* loads data into new customer finance report
        
    In order to function properlly the object instantiated from this class
    will need to have defined mapping file (spreadsheet) ID which introduce
    the mapping of the customers' name/id to their spreadsheet file IDs.
    Each report must be as well cataloged in the tab sheet `Reports Catalog`
    of the same spreadsheet. 
    One Ingester object will work with one mapping file always. In case more
    mapping files have to be used, one object per each must be instantiated.

    """

    def __init__(self, mapping_file_id: str) -> None:
        """
        Instantiate an object from class Ingester

        Args:
            mapping_file_id: the spreadsheet ID of the Google's Sheets file that contains
            mapping data between the customer and the spreadsheet_id of the file used for 
            this customer's financial reports.
            If an empty string is provided, the default value set in the __init__ will be used.
            In case the default value is an empty string as well, the user will be prompted
            to enter a value.
        Returns:
            None  
        """
    
        # Set default value for map_id. In event of an empty string is assigned - the user will be prompted to enter one.
        map_id = "1fL3rZDj8tCP4povb3E2x_WmkqNmfEZIR_KT_Zbz7p0M"
        
        # Both customers_map and reports_catalog are list of lists, where lists are row values

        # customers_map columns: Customer_Name, Customer_ID, Spreadsheet_ID, AWS_Org_ID 
        customers_map = []
        # reports_catalog columns: ID, Report Name
        reports_catalog = []
        creds = None
        report_name = ""
        report_id = 0

        if mapping_file_id == "" and map_id == "":
            self.map_id = input("Enter the Google Sheet file ID from the URL for the customers' mapping file:\n")

        if mapping_file_id != "":
            map_id = mapping_file_id

        if map_id == "":
            raise FileNotFoundError("There is no defined mapping file id!")

        authet = Auth() 
        
        try:
            self.creds = authet.get()

            self._read_map_file(self.creds, map_id)

        except AuthenticationError:
            raise Exception("Unable to authenticate current user!")

        except ReadingMapFileError:
            raise Exception("Unable to read the customers to spreadsheets mapping file!")     
        
        except EmptyMapFileError:
            raise Exception("Unable to use customers map or Reports Catalog!")

    
    def load_from_df(self, customer: str, df: pd.DataFrame) -> object:
        """ 
        *load_from_df* will receive a pandas data frame with report's data to load in the customer's data spreadsheet.
        This method is sorta "driver" for the report's data for each customer.
        It will be called from reports data exporter ran in the Jupyter notebook.
            
        Args:
            customer: name or id as string for the customer for which the data is to be loaded
            df: the pandas dataframe contaning the data to load

        Returns:
            object: An object as returned by the Google's Sheets API with the result of the updated values.

        Raises:
            FileNotFoundError: Raises an exception.
            ValueError: ...
            ReportCreationError: ...
        """
        
        # TODO [dev] plan:
        # 1. Identify customer (name, id?) etc.
        # 2. Read from settings file about mapped customers - spreadsheet_id.
        # 3. Instantiate new Template object with the received spreadsheet_id in p.2.
        # 4. Call the function `new_from_template` to duplicate the first tab sheet
        # 5. Cycle through the data frame `df` and load the customer report's data in the new tab sheet created at p.4
        # 6. Feed the status back to the calling procedure
        
        if customer == "":
            raise ValueError("Unidentifiable customer!")
        
        try:

            # ------- step-2 --------- 
            spreadsheet_id = self._get_sprd_id(customer)

            if spreadsheet_id == "":
                raise FileNotFoundError(f"Can not find spreadsheet ID for customer {customer}")

            # ------- step-3 ---------                
            target_file = Template(template_id=spreadsheet_id)
            month_year = datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')

            # -------- step-4 --------
            resp = target_file.new_from_template(self.creds, spreadsheet_id, month_year)
            sheetAttributes = self._parse_new_sheet_id(resp)
            if sheetAttributes[0] == 0 or sheetAttributes[1] == "":
                raise ValueError("Unable to identify the report's taget tab sheet id.")

            # -------- step-5 --------
            # Load the panda Data Frames into the Google's Sheet
            
            values = []
            
            for key, val in df.iterrows():
                tmp_val = []
                for i, v in val.items():
                    tmp_val.append(v)
                values.append(tmp_val)

            data = {
                "majorDimension": "ROWS",
                "range": f"{sheetAttributes[1]}!A2:Z999",
                "values": values,
            }
                        
            result = target_file.write_report_values(creds=self.creds, data=data)
            if result is None:
                raise RuntimeError({"module": f"{self.__name__}", "Message": f"Unsuccessful import from df"})

            return result

        except FileNotFoundError as err:
            print(err)
            return None
        except ValueError as verr:
            print(verr)
            return None
        except ReportCreationError as rerr:
            print(rerr)
            return None


    def load_report(self, customer: str, data: any) -> object:
        """
        This will load a report using the new concept of having 1 customer's Google Sheets File with many
        different reports within it split in tab sheets per YYYY-MM. That should involve as well `Reports Catalog`
        tab sheet from the Customers_mapping file.

        Args:
            customer: the name (or ID) of a customer to which the report data will be loaded. It must be one of the known customers in the list
            data: one of the types:
                - <str> as file name of a CSV file (will be used to determine the report name as well) or 
                - <object> as pandas Data Frame object

        Returns:
            object: An object as returned by the Google's Sheets API with the result of the updated values.

        Raises:
            ValueError:
            FileNotFoundError:

        """

        # TODO [dev] plan:
            # 1. Identify customer (name, id?) self.customers_map
            # 2. Read from settings file about mapped customers - spreadsheet_id.
            # 3. Read the report name (panda DF.index or CSV file name) from Reports Catalog and get the report ID.
            #   3.1 Identify the data source:
            #       - [pandas Data Frame]:
            #       - TODO [dev]: [customer's folder with CSV file] 
            #       - [single CSV file]
            # 4. Instantiate new Template object with the received spreadsheet_id in p.2
            # 5. Call the function `new_from_template` to duplicate the first tab sheet and name it after the pattern:
            #    (name pattern: `<ReportID>-<YYYY-MM><DD-HHMMSS>`)
            # 6. 
            # 7. Cycle through the data source(s) `df` and load the customer report's data in the new tab sheet
            # 8. Feed the status back to the calling procedure

        if customer == "":
            raise ValueError("Unidentifiable customer!")
        
        try:

            # ------- step-2 --------- 
            spreadsheet_id = self._get_sprd_id(customer)

            if spreadsheet_id == "":
                raise FileNotFoundError(f"Can not find spreadsheet ID for customer: {customer}")

            # ------- step-3 ---------
            self.report_name = ""
            self.report_id = 0
            data_type = ""

            if type(data) is str:
                path_fragments = data.split("/")
                fn = path_fragments[len(path_fragments)-1]
                self.report_name = fn.lower().split(".csv")[0]
                data_type = "csv"
                print(f"expect to be str: {type(data).__name__} \n report name: {self.report_name}")

            elif type(data) is pd.DataFrame:
                idx = data.index
                self.report_name = idx.name.lower().replace(" ", "_")
                data_type = "df" 
                print(f"expect to be pd.DataFrame: {type(data).__name__} \n report name: {self.report_name}")

            else:
                print(f"unsupported data type: {type(data).__name__}")
                raise TypeError({"Error": TypeError, "Message": f"Unsupported data type: {type(data).__name__}"})

            if self.report_name == "" or data_type == "":
                raise ValueError({"Message": "Missing report name or type!"})

            for report in self.reports_catalog:
                if report[1] == self.report_name:
                    self.report_id = report[0]

            if self.report_id == 0:
                raise ResourceWarning({"Message": f"Report {self.report_name} not found in Reports Catalog"})
            
            # -------- step-4 ----------
            target_file = Template(template_id=spreadsheet_id)
            month_year = datetime.datetime.now().strftime('%Y-%m <%d-%H%M%S>')
            tab_name = f"{self.report_id}-{month_year}"

            # -------- step-5 ----------
            resp = target_file.new_from_template(self.creds, spreadsheet_id, tab_name)
            sheetAttributes = self._parse_new_sheet_id(resp)
            if sheetAttributes[0] == 0 or sheetAttributes[1] == "":
                raise ValueError({"Message": f"Unable to identify the report's target tab sheet id for {tab_name}!"})

            # -------- step-6 ----------
            # Call the importer method for the respective data type provided
            if data_type == "csv":
                result = self._import_from_csv(target=target_file, sheetAttributes=sheetAttributes, file_name=data)

            elif data_type == "df":
                result = self._import_from_df(target_file, sheetAttributes, df=data)

            if result == None:
                raise RuntimeError({"Module":f" {self.__name__}", "Message":"Error while importing data"})

        except FileNotFoundError as err:
            print(f"error: {err}")




    def _get_sprd_id(self, cstm: str) -> str:
        """ 
        *_get_sprd_id* will look for preconfigured mapping spreadsheet from where to
        extract the spreadsheet for the given in the argument customer.

        Args:
            cstm: the customer name or id string
        
        Returns:
            str: the spreadsheet's ID as string
        """
        
        spreadsheetId = ""

        for row in self.customers_map:
            if cstm == row[0] or cstm == [1]:
                spreadsheetId = row[2]
                break
        
        return spreadsheetId

    def _read_map_file(self, creds: object, mapid: str) -> None:
        """ 
        *_read_map_file* This method will assign values to the object's properties
        `customers_map` - the customers to spreadsheets map and the `reports_catalog` - 
        the id and report name matrix.

        This method will be executed at object instantiation time and will hold the 
        map and the reports catalog during the object life-cycle time.

        Args:
            creds: Credentials of the current user with permissions to read the file
            mapid: The unique Google Sheets file id with the customers' mapping info

        Returns:
            None:

        Raises:
            EmptyMapFileError: in case the method read_map return empty list
                    
        """

        map_file = Template(mapid)

        try:
            self.customers_map = map_file.read_map(creds=creds, readrange="Map!A1:F100")
            if len(self.customers_map) < 1:
                raise EmptyMapFileError("Can not read or an empty map is returned!")

            self.reports_catalog = map_file.read_map(creds=creds, readrange="Reports Catalog!A1:B100")
            if len(self.reports_catalog) < 1:
                raise EmptyMapFileError("Can not read or an empty map is returned!")

            print(f"customer map: {self.customers_map}\n\n")
            print(f"reports catalog: {self.reports_catalog}\n\n")

        except ReadingMapFileError as err:
            print(err)

    def _parse_new_sheet_id(self, resp: dict) -> list:
        """ 
        *_parse_new_sheet_id* - get the new sheet id from the response
            
        This internal method will parse the response of the template duplication 
        and will extract the new sheet id and return it as string.        
        """
        
        # sample of the rsponse.
        # { 
        #     'spreadsheetId': '1w2tToHjQI7S8cH9neu1rCG6768IWrylF2rYtvLCSkcA', 
        #     'replies': [
        #         {'duplicateSheet': 
        #             {'properties': 
        #                 {
        #                     'sheetId': 1500007005, 
        #                     'title': '2022-12', 
        #                     'index': 1, 
        #                     'sheetType': 'GRID', 
        #                     'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}}]}
        

        try:
            # List of attributes (id, name) of the new created tab sheet
            response = [0, ""]
            response[0] = resp['replies'][0]['duplicateSheet']['properties']['sheetId']
            response[1] = resp['replies'][0]['duplicateSheet']['properties']['title'] 
       
        except:
            Exception("Failed to extract the new sheetId!")
        
        return response

    def _import_from_df(self, target: object, sheetAttributes: list, df: object) -> object:
        """
        This internal method will import data from pandas data frame into the customer's 
        spreadsheet (target)

        Args:
            target: the customer's spreadsheet
            sheetAttributes: a list of attributes of the spreadsheet
            df: the pandas Data Frame with the import data

        """

        # TODO [dev]: implement the import of column names as well for the reports data
        # TODO [dev]: import the report name in the cell B1 or the range B1:E1
          
        values = []
        columns = []
        report_name = []

        try:
            
            report_name.append([self.report_name])

            for col in df.columns:
                columns.append(col)
            values.append(columns)

            for key, val in df.iterrows():
                tmp_val = []
                for i, v in val.items():
                    tmp_val.append(v)
                values.append(tmp_val)

            data = [
                {
                    "majorDimension": "ROWS",
                    "range": f"{sheetAttributes[1]}!B1",
                    "values": report_name, 
                },
                {
                    "majorDimension": "ROWS",
                    "range": f"{sheetAttributes[1]}!B2:Z999",
                    "values": values,
                },
            ]        
            result = target.write_report_values(creds=self.creds, data=data)
            if result is None:
                raise RuntimeError({"module": f"{__name__}", "Message": f"Unsuccessful import from df"})

            print(f"successful import as: {result}")
            return result

        except Exception as impdferr:
            print(f"Error while importing form pandas data frame: {impdferr}!")


    def _import_from_csv(self, target: object, sheetAttributes: list, file_name: str) -> object:
        """
        imort csv file into pandas data frame and then invoke `_import_from_df` with the new df object
        
        Args:
            target: the customer's spreadsheet
            sheetAttributes: a list of attributes of the spreadsheet
            file_name: the CSV file name including the reference path to the it
        
        """
        try: 
            # TODO [dev]: For reacher functionality of the import from CSV, the read_csv function needs
            # to be configured with additional config object in extended implementation 
            data = pd.read_csv(file_name, index_col=False, keep_default_na=False, na_filter=False)

            idx = data.index
            idx.name = self.report_name

            result = self._import_from_df(target=target, sheetAttributes=sheetAttributes, df=data)

            if result is None:
                raise RuntimeError({"module": f"{__name__}", "Message": f"Unsuccessful import from df"})

            print(f"successful import as: {result}")
            return result
        
        except Exception as errimpcsv:
            print({"module": "_import_from_csv", "Message":f"while importing CSV file: {errimpcsv}"})
