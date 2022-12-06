
from fore_cloudreach.errors import ReadingMapFileError, ReportCreationError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Template:
    """
        The `Template` class will represent Google Sheets spreadsheet (template) used to create and feed GS report file with 
        prepared data data.
    """

    def __init__(self, template_id:str) -> None:
        if template_id == "":
            raise Exception("The template id is required")
        self.id = template_id


    def new_from_template(self, creds: object, spreadsheet_id: str, report_name: str) -> object:
        """ 
        **Duplicates** the first tab sheet of the given template object (file)
            
        This must be called before ingesting the monthly report data for each customer.
        It will return the new tab sheet id the is required for the ingestion process.

        Args:
            creds: the current user credentials that has permissions to edit the file
            spreadsheet_id: the Google Sheets global unique id of the file that will get the duplcated tab sheet
            report_name: the name of the duplicated sheet

        Returns:
            object: the feedback from the Google's Sheets API

        Raises:
            
        """

        requests = []
        requests.append({
            # Duplicates the contents of a sheet. # Duplicates a sheet.
            "duplicateSheet": { 
                # The zero-based index where the new sheet should be inserted. The index of all sheets after this are incremented.
                "insertSheetIndex": 1,
                # If set, the ID of the new sheet. If not set, an ID is chosen. If set, the ID must not conflict with any existing sheet ID. If set, it must be non-negative. 
                "newSheetId": None, 
                # The name of the new sheet. If empty, a new name is chosen for you.
                "newSheetName": report_name, 
                # The sheet to duplicate. If the source sheet is of DATA_SOURCE type, its backing DataSource is also duplicated and associated with the new copy of the sheet. No data execution is triggered, the grid data of this sheet is also copied over but only available after the batch request completes.
                "sourceSheetId": 0,
            } 
        })

        # API docs: https://googleapis.github.io/google-api-python-client/docs/dyn/sheets_v4.spreadsheets.html#batchUpdate
        try:

            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API for duplicating the first sheet (index=0) of the spreadsheet
            response = service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id, 
                body={'requests':requests}
                ).execute()
            
            # TODO[dev]: extract the sheetId from the response object!

            # The `response` object sample:
            # {'spreadsheetId': '1Ni5B7zolPKD2J0CXQSaLec31AXw8HpcdM_xPJKPILRw', 
            #  'replies': [
            #     {'duplicateSheet': 
            #        {'properties': {'sheetId': 431392078, 'title': '11-2022', 'index': 1, 'sheetType': 'GRID', 'gridProperties': {'rowCount': 1000, 'columnCount': 26}}}}]}
            return response

        except HttpError as err:
            print("new_from_template threw an error:", format(err))
            return


    def read_map(self, creds, readrange) -> list:
        """ 
        *read_map* will read the provided range from the mapping file

        Args:
            creds     -- authentication credentials
            readrange -- the range where the mapping is stored
        """
    
        try:
            service = build('sheets', 'v4', credentials=creds)
            
            # Call the Sheets API
            sheet = service.spreadsheets()

            result = sheet.values().get(spreadsheetId=self.id,
                                        range=readrange).execute()

            values = result.get('values', [])

            if not values:
                print('No data found.')
                return None

            range_width = len(values[0])
            map_titles = []
            cstmmap = []

            for idx, row in enumerate(values):
                
                if idx == 0:
                    for i in range(range_width):
                        map_titles.append(row[i])
                    continue
                
                map_row = []
                for j in range(range_width):
                    map_row.append(row[j])

                cstmmap.append(map_row)
            
            return cstmmap

        except HttpError as err:
            print(f"HTTP error: {err}", err)
            raise ReadingMapFileError(str(err.content))

    def write_report_values(self, creds: object, data: list) -> object:
        """ 
            *write_repost_values* write the report in the object's spreadsheet

            source: https://googleapis.github.io/google-api-python-client/docs/dyn/sheets_v4.spreadsheets.values.html#batchUpdate

            keyword arguments:

            * creds -- is the credentials object with permissions to the spreadsheet
            * data  -- is a list of objects; Each object is of the type below:

        ```
        .. highlight:: python
        .. code-block:: python

            { #### Data within a range of the spreadsheet.
                ##### The major dimension of the values. For output, if the spreadsheet data is:
                ##### `A1=1,B1=2,A2=3,B2=4`, then requesting `range=A1:B2,majorDimension=ROWS` will return `[[1,2],[3,4]]`, 
                ##### whereas requesting `range=A1:B2,majorDimension=COLUMNS` will return `[[1,3],[2,4]]`. 
                ##### For input, with `range=A1:B2,majorDimension=ROWS` then `[[1,2],[3,4]]` will set `A1=1,B1=2,A2=3,B2=4`. 
                ##### With `range=A1:B2,majorDimension=COLUMNS` then `[[1,2],[3,4]]` will set `A1=1,B1=3,A2=2,B2=4`. 
                ##### When writing, if this field is not set, it defaults to ROWS.

                "majorDimension": "A String",

                ##### The range the values cover, in [A1 notation](/sheets/api/guides/concepts#cell). 
                ##### For output, this range indicates the entire requested range, even though the values will exclude 
                ##### trailing rows and columns. When appending values, this field represents the range to search for a table, 
                ##### after which values will be appended.

                "range": "A String",

                ##### The data that was read or to be written. This is an array of arrays, the outer array representing all 
                ##### the data and each inner array representing a major dimension. Each item in the inner array corresponds 
                ##### with one cell. 
                ##### For output, empty trailing rows and columns will not be included. 
                ##### For input, supported value types are: bool, string, and double. Null values will be skipped. 
                ##### To set a cell to an empty value, set the string value to an empty string.
                
                "values": [ 
                    [
                        "",
                    ],
                ],
            },
        ```
        """

        try:

            service = build('sheets', 'v4', credentials=creds)

            request =   { # The request for updating more than one range of values in a spreadsheet.
                            # The new values to apply to the spreadsheet.
                            "data": data,

                            # Determines if the update response should include the values of the cells that were updated. 
                            # By default, responses do not include the updated values. The `updatedData` field within each of 
                            # the BatchUpdateValuesResponse.responses contains the updated values. 
                            # If the range to write was larger than the range actually written, the response includes all values 
                            # in the requested range (excluding trailing empty rows and columns).
                            "includeValuesInResponse": False,

                            # Determines how dates, times, and durations in the response should be rendered. This is ignored 
                            # if response_value_render_option is FORMATTED_VALUE. The default dateTime render 
                            # option is SERIAL_NUMBER.
                            "responseDateTimeRenderOption": None,

                            # Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE.
                            "responseValueRenderOption": "FORMATTED_VALUE",

                            # How the input data should be interpreted. The values `USER_ENTERED` is seen in an [example](https://developers.google.com/sheets/api/guides/values#writing_to_a_single_range)
                            "valueInputOption": "USER_ENTERED", 
                        } 

            response = None

            # Call the Sheets API for duplicating the first sheet (index=0) of the spreadsheet
            response = service.spreadsheets().values().batchUpdate(
                spreadsheetId=self.id,
                body=request,
                x__xgafv=None,
            ).execute()

        except Exception as err:
            raise ReportCreationError(f"Failed to update the spreadsheet! Error {err}")

        return response
