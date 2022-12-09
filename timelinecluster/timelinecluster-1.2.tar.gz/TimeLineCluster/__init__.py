import TimeLineCluster.GenericController as GenericController
import TimeLineCluster.UtilsController as UtilsController
import TimeLineCluster.DBConnector as DBConnector
from datetime import datetime
class TimeLineClusterClass:
    def __init__(self, data_for_time_line_cluster) :
        self.app_name = data_for_time_line_cluster["app_name"]
        self.status = True
        self.generic = GenericController.GenericControllerClass(data_for_time_line_cluster)
        self.connect_db_output = DBConnector.ConnectDB(self.generic.data_app_config["output_db"]["host"] , self.generic.data_app_config["output_db"]["database"] , self.generic.data_app_config["output_db"]["user"] ,self.generic.data_app_config["output_db"]["password"])
        self.connect_db_output.connect_to_db(1,1)  # connect db output 
        self.flag_data = UtilsController.getFlagData()
        self.sql_data = UtilsController.getSql()
        self.source_data = ""
        self.source_detail_data = ""

        self.store_for_time_line_cluster = data_for_time_line_cluster
        self.model_app = self.store_for_time_line_cluster["model"]

        # self.data_for_time_line_cluster = data_for_time_line_cluster

        self.pk_report_name = self.generic.data_app_config["report"]["field_pk"]
        self.pk_report_start_date = self.generic.data_app_config["report"]["field_start_date"]

        self.pk_member_name = ""
        if("field_pk" in self.generic.data_app_config["member"]):
            self.pk_member_name = self.generic.data_app_config["member"]["field_pk"]

        self.pk_member_detail_start_date = ""
        if("member_details" in self.generic.data_app_config): 
            if("field_start_date" in self.generic.data_app_config["member_details"]):          
                self.pk_member_detail_start_date = self.generic.data_app_config["member_details"]["field_start_date"]

    def setSource(self, source_data, source_detail_data):
        self.source_data = source_data
        self.source_detail_data = source_detail_data


    def run(self):
        try:
            if(self.generic.data_app_config == "" or self.generic.data_app_config == False or self.generic.data_app_config == None):
                self.status = False
                return 
            if(self.status):

                source_data = self.source_data
                source_data_no_detail = []
                
                if(len(source_data) > 0): # check source data for process

                    self.flag_data = UtilsController.getFlagData()
                        
                    if(self.connect_db_output.conn == False or self.connect_db_output.conn == None): # connect db output 
                        print("Connect database output")
                        self.connect_db_output.connect_to_db(1,1)

                    last_update_source = UtilsController.readFileJson(self.store_for_time_line_cluster["last_update_path"]) # get last update timestamp

                    if(last_update_source == False): # Check last update not found or Error readFileJson function ??
                        self.connect_db_output.closeAllConnection("output")
                        self.status = False
                        self.generic.log.text_long += "last update not found or Error readFileJson function."
                        # self.generic.log.genLog(self.generic.log.text_long, "error")
                        return False    
                    last_update_source = source_data.iloc[len(source_data)-1] # store max update timestamp

                    # sort data by pk, start_date
                    for_drop = []
                    ascending_list = []
                    for pk in self.generic.data_app_config["report"]["field_pk"]:
                        for_drop.append(pk)
                        ascending_list.append(True)
                    for_drop.append(self.generic.data_app_config["report"]["field_start_date"])
                    ascending_list.append(True)
                    source_data = source_data.sort_values(for_drop, ascending=ascending_list)
                     # end sort data by pk, start_date

                    for_drop = []
                    for pk in self.pk_report_name:
                        for_drop.append(pk)
                    for_drop.append(self.pk_report_start_date)
                    unique_source_data = source_data.drop_duplicates(for_drop) # duplicates source data for process
                    if(len(self.source_detail_data) > 0):
                        source_detail_data = self.source_detail_data
                        unique_source_detail_data = source_detail_data.drop_duplicates([self.pk_member_name]) # duplicates source data detail for process
                        if(len(source_data) != len(unique_source_detail_data)): # check source data no detail
                            source_data_no_detail = source_data[~source_data[self.pk_member_name].isin(unique_source_detail_data[self.pk_member_name])]
                    self.model_app["report"] = self.store_for_time_line_cluster["model"]["report"]
                    data_explore_cluster = []
                    for i , source in enumerate(unique_source_data.iloc): # self.pk_report_name, self.pk_report_start_date
                        self.generic.data_app_config = self.store_for_time_line_cluster["data_app_config"]
                        self.generic.log.text_long = "Process start time : " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " "
                        
                        self.model_app["summary"] = self.store_for_time_line_cluster["model"]["summary"]
                        self.model_app["summary"].summary_date = source[self.pk_report_start_date]
                        
                        self.flag_data["sql_for_insert_cluster_execute"]["flag_insert_for_summary_details"] = False
                        source_by_create_date = source_data.loc[(source_data[self.pk_report_start_date] == source[self.pk_report_start_date])] # member source 
                        for pk in self.pk_report_name:
                            source_by_create_date = source_by_create_date.loc[(source_by_create_date[pk]  == source[pk])] # member source 

                        if(self.pk_member_detail_start_date != ""):
                            source_detail_by_create_date = source_detail_data.loc[(source_detail_data[self.pk_member_detail_start_date] == source[self.pk_report_start_date])] # member detail source
                            for pk in self.pk_report_name:
                                source_detail_by_create_date = source_detail_by_create_date.loc[(source_detail_by_create_date[pk]  == source[pk])] # member detail source
                        else:
                            source_detail_by_create_date = []

                        data_cluster_representative = self.generic.getClusterRepresentative(self.connect_db_output, self.generic.data_app_config, source) # get cluster
                        data_explore_cluster = self.generic.exploreCluster(self.connect_db_output, source, unique_source_data, i, source_by_create_date, data_cluster_representative, self.flag_data, self.generic) # check cluster
                        
                        for pk in self.pk_report_name:
                            self.generic.log.text_long += pk + " : " + str(source[pk]) + " "

                        if(self.pk_member_name != ""):
                            self.generic.log.text_long += self.generic.log.convertDf2StringForLog(source_by_create_date, self.pk_member_name) + " "

                        self.generic.handleProcessMember(self.connect_db_output, source, source_by_create_date, source_detail_by_create_date, source_data_no_detail, self.model_app, self.flag_data, self.sql_data, data_cluster_representative, data_explore_cluster, self.generic)
                        self.generic.handleProcessSummary(self.connect_db_output, source, source_by_create_date, source_detail_by_create_date, self.model_app, self.flag_data, self.sql_data, data_cluster_representative, self.generic)

                        data_process_report = self.generic.handleProcessReport(source, self.model_app, self.flag_data, self.sql_data, data_cluster_representative, self.generic)
                        # self.model_app["report"] = data_process_report[0] # data model report
                        # self.flag_data = data_process_report[1] # self.flag_data
                        
                        if(self.generic.data_app_config["execute_status"] == 1):
                            self.generic.executeSQLForProcess(self.connect_db_output, self.flag_data, self.sql_data, self.generic)
                        else:
                            self.generic.controller_app["report"].executeSQLForProcess(self.connect_db_output, self.flag_data, self.generic)
                            
                        self.generic.log.text_long += "Process end time : " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " "
                    
                    if("field_last_update_timestamp" in self.generic.data_app_config):
                        UtilsController.writeLastUpdateSurveyJson(self.store_for_time_line_cluster["last_update_path"] , last_update_source[self.generic.data_app_config["field_last_update_timestamp"]])
                
            self.connect_db_output.closeAllConnection("output")
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            print("Stop !!")
            self.generic.log.text_long += "Oops! An exception has occured : " + str(error) + " Exception TYPE : " + str(type(error))
            # self.generic.log.genLog(self.generic.log.text_long, "error")
            self.status = False
            self.connect_db_output.closeAllConnection("output")
