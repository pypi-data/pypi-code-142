from fore_cloudreach.errors import AuthenticationError, ReadingMapFileError, EmptyMapFileError, ReportCreationError
from fore_cloudreach.auth import Auth
from fore_cloudreach.template import Template
import pandas as pd
import datetime

class Ingester:
    """ *Ingester* loads data into new customer finance report
        In order to function properlly the object instantiated from this class
        will need to have mapping file (spreadsheet) ID which introduce
        the mapping of the customers' name/id to their spreadsheet file IDs.
        One Ingester object will work with one mapping file always. In case more
        mapping files have to be used, one object per each must be instantiated.
    """

    def __init__(self, mapping_file_id: str) -> None:
        """ \n
            **Keyword arguments**:\n
            mapping_file_id -- the spreadsheet ID of the Google's Sheets file that contains
            mapping data between the customer and the spreadsheet_id of the file used for 
            this customer's finantial reports.  
        """
    
        # Set default value for map_id. Even an empty string is assigned - the user will be prompted to enter one.
        map_id = "1pUmAAcQCU4rNNyAayKNb4RQVv-DkEn4cWwLmEynxCBk"
        customers_map = []
        creds = None

        if mapping_file_id == "" and map_id == "":
            self.map_id = input("Enter the Google Sheet file ID from the URL for the customers' mapping file:\n")

        if mapping_file_id != "":
            map_id = mapping_file_id

        if map_id == "":
            raise FileNotFoundError("There is no defined mapping file id!")

        authet = Auth() 
        
        try:
            self.creds = authet.get()

            self.customers_map = self._read_map_file(self.creds, map_id)

        except AuthenticationError:
            raise Exception("Unable to authenticate current user!")

        except ReadingMapFileError:
            raise Exception("Unable to read the customers to spreadsheets mapping file!")     
        
        except EmptyMapFileError:
            raise Exception("Unable to use customers map!")

    
    def load_from_df(self, customer: str, df: pd.DataFrame) -> object:
        """ *load* will receive a pandas data frame with report's data to load in the customer's data spreadsheet.
            This method is sorta "driver" for the report's data for each customer.
            It will be called from reports data exporter ran in the Jupyter notebook.
            
            Keyword arguments:
            customer -- name or id as string for the customer for which the data is to be loaded
            df -- the pandas dataframe contaning the data to load
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
            #TODO [dev]: Load the panda Data Frames into the Google's Sheet
            
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


    def _get_sprd_id(self, cstm: str) -> str:
        """ 
            *_get_sprd_id* will look for preconfigured mapping spreadsheet from where to
            extract the spreadsheet for the given in the argument customer.

            Keyword arguments:
            cstm -- the customer name or id string
        """
        
        spreadsheetId = ""

        for row in self.customers_map:
            if cstm == row[0] or cstm == [1]:
                spreadsheetId = row[2]
                break
        
        return spreadsheetId


    def _read_map_file(self, creds: object, mapid: str) -> list:
        """ *_read_map_file* will load in the memory the customers to spreadsheets map
            \n\n
            this method will be executed at object instantiation time and will hold the map during 
            the object life-cycle time.
            \n\n        
        """
        map_file = Template(mapid)

        try:
            cstm_map = map_file.read_map(creds=creds, readrange="Map!A1:F100")
            if cstm_map == None or len(cstm_map) < 1:
                raise EmptyMapFileError("Can not read or an empty map is returned!")

            return cstm_map

        except ReadingMapFileError as err:
            print(err)
            return None

    def _parse_new_sheet_id(self, resp: dict) -> list:
        """ *_parse_new_sheet_id* - get the new sheet id from the response
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