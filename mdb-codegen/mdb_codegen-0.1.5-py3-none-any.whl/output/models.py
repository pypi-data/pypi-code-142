from django.db import models

class ActivityBlackListed(models.Model):
    """
    Originally sourced from Activity_BlackListed in /home/josh/PNDS_Interim_MIS-Data.accdb (13 records)
    """

    class Meta:
        db_table = "activity_blacklisted"

    blacklistid = models.IntegerField(primary_key=True, db_column="BlacklistID")
    sectorid = models.IntegerField(null=True, blank=True, db_column="SectorID")
    activityid = models.IntegerField(null=True, blank=True, db_column="ActivityID")
    outputid = models.IntegerField(null=True, blank=True, db_column="OutputID")
    date_blacklisted = models.DateTimeField(null=True, blank=True, db_column="Date_Blacklisted")
    reason_blacklisted = models.CharField(max_length=1024, null=True, blank=True, db_column="Reason_Blacklisted")
    source = models.CharField(max_length=1024, null=True, blank=True, db_column="Source")


class DataSyncLogTemp(models.Model):
    """
    Originally sourced from Data_Sync_Log_Temp in /home/josh/PNDS_Interim_MIS-Data.accdb (14 records)
    """

    class Meta:
        db_table = "data_sync_log_temp"

    id = models.IntegerField(primary_key=True, db_column="ID")
    districtid = models.IntegerField(null=True, blank=True, db_column="DistrictID")
    data_imported = models.IntegerField(null=True, blank=True, db_column="Data_Imported")
    data_updated = models.IntegerField(null=True, blank=True, db_column="Data_Updated")
    data_imported_priorities = models.IntegerField(null=True, blank=True, db_column="Data_Imported_Priorities")
    data_updated_priorities = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Priorities")
    data_imported_progress = models.IntegerField(null=True, blank=True, db_column="Data_Imported_Progress")
    data_updated_progress = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Progress")
    data_imported_project = models.IntegerField(null=True, blank=True, db_column="Data_Imported_Project")
    data_updated_project = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Project")
    data_updated_project_dates = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Project_Dates")
    data_imported_mrops = models.IntegerField(null=True, blank=True, db_column="Data_Imported_MROPS")
    data_imported_opsrep = models.IntegerField(null=True, blank=True, db_column="Data_Imported_OPSRep")
    data_updated_opsrep = models.IntegerField(null=True, blank=True, db_column="Data_Updated_OPSRep")
    data_imported_opsbudget = models.IntegerField(null=True, blank=True, db_column="Data_Imported_OPSBudget")
    data_updated_opsbudget = models.IntegerField(null=True, blank=True, db_column="Data_Updated_OPSBudget")
    data_imported_fininfo = models.IntegerField(null=True, blank=True, db_column="Data_Imported_FinInfo")
    data_updated_fininfo = models.IntegerField(null=True, blank=True, db_column="Data_Updated_FinInfo")
    data_imported_mrinf = models.IntegerField(null=True, blank=True, db_column="Data_Imported_MRINF")
    data_updated_mrinf = models.IntegerField(null=True, blank=True, db_column="Data_Updated_MRINF")
    data_imported_infrep = models.IntegerField(null=True, blank=True, db_column="Data_Imported_INFRep")
    data_updated_infrep = models.IntegerField(null=True, blank=True, db_column="Data_Updated_INFRep")
    data_imported_sucocycle = models.IntegerField(null=True, blank=True, db_column="Data_Imported_SucoCycle")
    data_updated_sucocycle = models.IntegerField(null=True, blank=True, db_column="Data_Updated_SucoCycle")
    data_imported_projoutput = models.IntegerField(null=True, blank=True, db_column="Data_Imported_ProjOutput")
    data_updated_projoutput = models.IntegerField(null=True, blank=True, db_column="Data_Updated_ProjOutput")
    date_imported = models.DateTimeField(null=True, blank=True, db_column="Date_Imported")
    date_exported = models.DateTimeField(null=True, blank=True, db_column="Date_Exported")
    r_import = models.BooleanField(db_column="Import")
    data_inserted_district = models.IntegerField(null=True, blank=True, db_column="Data_Inserted_District")
    data_updated_district = models.IntegerField(null=True, blank=True, db_column="Data_Updated_District")
    data_inserted_cmt = models.IntegerField(null=True, blank=True, db_column="Data_Inserted_CMT")
    data_updated_cmt = models.IntegerField(null=True, blank=True, db_column="Data_Updated_CMT")


class Documentsandpictures(models.Model):
    """
    Originally sourced from Documents_and_pictures in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "documents_and_pictures"

    id = models.CharField(max_length=1024, primary_key=True, db_column="ID")
    document_file_type_id = models.IntegerField(null=True, blank=True, db_column="Document_file_type_id")
    document_type_id = models.IntegerField(null=True, blank=True, db_column="Document_type_id")
    document_upload_date = models.DateTimeField(null=True, blank=True)
    fk_reference = models.CharField(max_length=1024, null=True, blank=True, db_column="FK_reference")
    page_number = models.IntegerField(null=True, blank=True, db_column="Page_number")
    system_post_id = models.CharField(max_length=1024, null=True, blank=True, db_column="System_Post_ID")
    file_creation_date = models.DateTimeField(null=True, blank=True, db_column="File_creation_date")
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(db_column="Active")
    deactivated_date = models.DateTimeField(null=True, blank=True)
    transmission_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Transmission_ID")
    gps_coords = models.CharField(max_length=1024, null=True, blank=True)
    gps_direction = models.CharField(max_length=1024, null=True, blank=True)
    table_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Table_name")


class FinanceMonitoring(models.Model):
    """
    Originally sourced from Finance_Monitoring in /home/josh/PNDS_Interim_MIS-Data.accdb (906 records)
    """

    class Meta:
        db_table = "finance_monitoring"

    fm_id = models.CharField(max_length=1024, primary_key=True, db_column="FM_ID")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_id")
    date_of_assessment = models.DateTimeField(null=True, blank=True, db_column="Date_of_assessment")
    criteria_1 = models.IntegerField(null=True, blank=True, db_column="Criteria_1")
    criteria_2 = models.IntegerField(null=True, blank=True, db_column="Criteria_2")
    criteria_3 = models.IntegerField(null=True, blank=True, db_column="Criteria_3")
    criteria_4 = models.IntegerField(null=True, blank=True, db_column="Criteria_4")
    criteria_5 = models.IntegerField(null=True, blank=True, db_column="Criteria_5")
    criteria_6 = models.IntegerField(null=True, blank=True, db_column="Criteria_6")
    criteria_7 = models.IntegerField(null=True, blank=True, db_column="Criteria_7")
    criteria_8 = models.IntegerField(null=True, blank=True, db_column="Criteria_8")
    criteria_9 = models.IntegerField(null=True, blank=True, db_column="Criteria_9")
    criteria_10 = models.IntegerField(null=True, blank=True, db_column="Criteria_10")
    f_mon_id = models.IntegerField(null=True, blank=True, db_column="F_Mon_ID")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)
    system_post_id = models.IntegerField(null=True, blank=True, db_column="System_post_id")
    active = models.BooleanField(db_column="Active")
    comments = models.CharField(max_length=1024, null=True, blank=True, db_column="Comments")


class Freebalancetranslationcodes(models.Model):
    """
    Originally sourced from Freebalance_translation_codes in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    class Meta:
        db_table = "freebalance_translation_codes"

    id = models.IntegerField(primary_key=True, db_column="ID")
    pnds_budget_code = models.CharField(max_length=1024, null=True, blank=True, db_column="PNDS_budget_code")
    freebalance_budget_code = models.CharField(max_length=1024, null=True, blank=True, db_column="FreeBalance_budget_code")
    active = models.BooleanField(db_column="Active")
    deactivated_date = models.DateTimeField(null=True, blank=True, db_column="Deactivated_date")


class GoogleTransfers(models.Model):
    """
    Originally sourced from Google_Transfers in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "google_transfers"

    transmission_id = models.IntegerField(primary_key=True, db_column="Transmission_ID")
    post_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Post_id")
    unique_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Unique_ID")
    transfer_date_time = models.DateTimeField(null=True, blank=True, db_column="Transfer_date_time")
    transfer_direction = models.CharField(max_length=1024, null=True, blank=True, db_column="Transfer_direction")
    transfer_filename = models.CharField(max_length=1024, null=True, blank=True, db_column="Transfer_filename")


class Monthlyreports(models.Model):
    """
    Originally sourced from Monthly_reports in /home/josh/PNDS_Interim_MIS-Data.accdb (41928 records)
    """

    class Meta:
        db_table = "monthly_reports"

    monthly_report_id = models.CharField(max_length=1024, primary_key=True, db_column="Monthly_Report_ID")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    system_post_id = models.IntegerField(null=True, blank=True, db_column="System_post_id")
    reporting_period = models.DateTimeField(null=True, blank=True, db_column="Reporting_Period")
    fin_ops_report_complete = models.BooleanField(db_column="Fin_ops_report_complete")
    fin_inf_reports_complete = models.BooleanField(db_column="Fin_inf_reports_complete")
    tecnical_report_complete = models.BooleanField(db_column="Tecnical_report_complete")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)
    incoming_funding_inf = models.IntegerField(null=True, blank=True, db_column="Incoming_funding_inf")
    cash_on_hand_inf = models.IntegerField(null=True, blank=True, db_column="Cash_on_hand_inf")
    bank_balance_inf = models.IntegerField(null=True, blank=True, db_column="Bank_Balance_inf")
    verified_inf = models.BooleanField(db_column="Verified_inf")
    active = models.BooleanField(db_column="Active")
    deactivated_date = models.DateTimeField(null=True, blank=True, db_column="Deactivated_Date")
    report_date = models.DateTimeField(null=True, blank=True, db_column="Report_date")
    verified = models.BooleanField(db_column="Verified")
    transmitted = models.BooleanField(db_column="Transmitted")
    transmission_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Transmission_ID")
    locked = models.BooleanField(db_column="Locked")
    operationbudgetid = models.IntegerField(null=True, blank=True, db_column="OperationBudgetID")
    suco_cycleid = models.IntegerField(null=True, blank=True, db_column="Suco_CycleID")


class MonthlyreportsInfrastructure(models.Model):
    """
    Originally sourced from Monthly_reports_Infrastructure in /home/josh/PNDS_Interim_MIS-Data.accdb (29260 records)
    """

    class Meta:
        db_table = "monthly_reports_infrastructure"

    monthly_report_id = models.CharField(max_length=1024, primary_key=True, db_column="Monthly_Report_ID")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    system_post_id = models.IntegerField(null=True, blank=True, db_column="System_post_id")
    reporting_period = models.DateTimeField(null=True, blank=True, db_column="Reporting_Period")
    fin_ops_report_complete = models.BooleanField(db_column="Fin_ops_report_complete")
    fin_inf_reports_complete = models.BooleanField(db_column="Fin_inf_reports_complete")
    tecnical_report_complete = models.BooleanField(db_column="Tecnical_report_complete")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)
    incoming_funding_inf = models.IntegerField(null=True, blank=True, db_column="Incoming_funding_inf")
    cash_on_hand_inf = models.IntegerField(null=True, blank=True, db_column="Cash_on_hand_inf")
    bank_balance_inf = models.IntegerField(null=True, blank=True, db_column="Bank_Balance_inf")
    verified_inf = models.BooleanField(db_column="Verified_inf")
    active = models.BooleanField(db_column="Active")
    deactivated_date = models.DateTimeField(null=True, blank=True, db_column="Deactivated_Date")
    report_date = models.DateTimeField(null=True, blank=True, db_column="Report_date")
    verified = models.BooleanField(db_column="Verified")
    transmitted = models.BooleanField(db_column="Transmitted")
    transmission_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Transmission_ID")
    locked = models.BooleanField(db_column="Locked")
    operationbudgetid = models.IntegerField(null=True, blank=True, db_column="OperationBudgetID")
    suco_cycleid = models.IntegerField(null=True, blank=True, db_column="Suco_CycleID")
    brought_forward = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Brought_Forward")


class zCMTPositions(models.Model):
    """
    Originally sourced from zCMTPositions in /home/josh/PNDS_Interim_MIS-Data.accdb (12 records)
    """

    class Meta:
        db_table = "zcmtpositions"

    cmtpositionid = models.IntegerField(primary_key=True, db_column="CMTPositionID")
    cmtposition = models.CharField(max_length=1024, null=True, blank=True, db_column="CMTPosition")
    cmtposition_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="CMTPosition_Tetum")
    recordcreationdate = models.DateTimeField(null=True, blank=True, db_column="RecordCreationDate")
    recordchangedate = models.DateTimeField(null=True, blank=True, db_column="RecordChangeDate")
    positionrank = models.IntegerField(null=True, blank=True, db_column="PositionRank")


class OperationBudget(models.Model):
    """
    Originally sourced from OperationBudget in /home/josh/PNDS_Interim_MIS-Data.accdb (3731 records)
    """

    class Meta:
        db_table = "operationbudget"

    operationbudgetid = models.IntegerField(primary_key=True, db_column="OperationBudgetID")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    grant_year = models.CharField(max_length=1024, null=True, blank=True, db_column="Grant_Year")
    grant_amount = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Grant_Amount")
    expenditure = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Expenditure")
    carry_forward = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Carry_Forward")
    brought_forward_bank = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Brought_Forward_Bank")
    brought_forward_cash = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Brought_Forward_Cash")
    grant_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Grant_Ceiling")
    operationbudget_statusid = models.IntegerField(null=True, blank=True, db_column="OperationBudget_StatusID")
    record_creationdate = models.DateTimeField(null=True, blank=True, db_column="Record_CreationDate")
    record_changedate = models.DateTimeField(null=True, blank=True, db_column="Record_ChangeDate")


class PhaseCycle(models.Model):
    """
    Originally sourced from PhaseCycle in /home/josh/PNDS_Interim_MIS-Data.accdb (38 records)
    """

    class Meta:
        db_table = "phasecycle"

    phasecycleid = models.IntegerField(primary_key=True, db_column="PhaseCycleID")
    phaseid = models.IntegerField(null=True, blank=True, db_column="PhaseID")
    cycleid = models.IntegerField(null=True, blank=True, db_column="CycleID")
    targetdate = models.DateTimeField(null=True, blank=True, db_column="TargetDate")
    targetvalue = models.CharField(max_length=1024, null=True, blank=True, db_column="TargetValue")
    remarks = models.CharField(max_length=1024, null=True, blank=True, db_column="Remarks")


class SubprojectOutputs(models.Model):
    """
    Originally sourced from SubpojectOutputs in /home/josh/PNDS_Interim_MIS-Data.accdb (7995 records)
    """

    class Meta:
        db_table = "SubprojectOutputs"

    subprojectoutputid = models.CharField(max_length=1024, primary_key=True, db_column="SubprojectOutputID")
    sectorid = models.IntegerField(null=True, blank=True, db_column="SectorID")
    outputid = models.IntegerField(null=True, blank=True, db_column="OutputID")
    activityid = models.IntegerField(null=True, blank=True, db_column="ActivityID")
    unitid = models.IntegerField(null=True, blank=True, db_column="UnitID")
    value1 = models.FloatField(null=True, blank=True, db_column="Value1")
    value1_actual = models.FloatField(null=True, blank=True, db_column="Value1_Actual")
    unitid2 = models.IntegerField(null=True, blank=True, db_column="UnitID2")
    value2 = models.IntegerField(null=True, blank=True, db_column="Value2")
    value2_actual = models.IntegerField(null=True, blank=True, db_column="Value2_Actual")
    suco_subproject_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_SubProject_ID")
    ismain = models.BooleanField(db_column="IsMain")
    sub_sectorid = models.IntegerField(null=True, blank=True, db_column="Sub_SectorID")
    record_creationdate = models.DateTimeField(null=True, blank=True, db_column="Record_CreationDate")
    record_changedate = models.DateTimeField(null=True, blank=True, db_column="Record_ChangeDate")


class SucoActvities(models.Model):
    """
    Originally sourced from Suco_Actvities in /home/josh/PNDS_Interim_MIS-Data.accdb (37104 records)
    """

    class Meta:
        db_table = "suco_actvities"

    id = models.CharField(max_length=1024, primary_key=True, db_column="ID")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    system_post_id = models.IntegerField(null=True, blank=True, db_column="System_post_id")
    attendance_male = models.IntegerField(null=True, blank=True, db_column="Attendance_Male")
    attendance_female = models.IntegerField(null=True, blank=True, db_column="Attendance_Female")
    date_completed = models.DateTimeField(null=True, blank=True, db_column="Date_completed")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)
    zproject_activity_id = models.IntegerField(null=True, blank=True, db_column="zProject_Activity_id")
    fd_type_id = models.IntegerField(null=True, blank=True, db_column="FD_type_ID")
    active = models.BooleanField(db_column="Active")
    kpa_male = models.IntegerField(null=True, blank=True, db_column="KPA_Male")
    kpa_female = models.IntegerField(null=True, blank=True, db_column="KPA_Female")
    aldea_id = models.IntegerField(null=True, blank=True, db_column="Aldea_ID")
    district_id = models.IntegerField(null=True, blank=True, db_column="District_ID")
    sd_id = models.IntegerField(null=True, blank=True, db_column="SD_ID")
    subdistrictphaseid = models.IntegerField(null=True, blank=True, db_column="SubdistrictPhaseID")
    suco_cycleid = models.IntegerField(null=True, blank=True, db_column="Suco_CycleID")
    districtphaseid = models.IntegerField(null=True, blank=True, db_column="DistrictPhaseID")
    disable_male = models.IntegerField(null=True, blank=True, db_column="Disable_Male")
    disable_female = models.IntegerField(null=True, blank=True, db_column="Disable_Female")
    disable_kpa_male = models.IntegerField(null=True, blank=True, db_column="Disable_KPA_Male")
    disable_kpa_female = models.IntegerField(null=True, blank=True, db_column="Disable_KPA_Female")
    community_member_male = models.IntegerField(null=True, blank=True, db_column="Community_Member_Male")
    community_member_female = models.IntegerField(null=True, blank=True, db_column="Community_Member_Female")


class SucoCycles(models.Model):
    """
    Originally sourced from Suco_Cycles in /home/josh/PNDS_Interim_MIS-Data.accdb (3924 records)
    """

    class Meta:
        db_table = "suco_cycles"

    suco_cycleid = models.IntegerField(primary_key=True, db_column="Suco_CycleID")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    infrastructure_budget_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Infrastructure_budget_ceiling")
    operations_budget_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Operations_budget_ceiling")
    record_creationdate = models.DateTimeField(null=True, blank=True, db_column="Record_CreationDate")
    record_changedate = models.DateTimeField(null=True, blank=True, db_column="Record_ChangeDate")
    cyclestatusid = models.IntegerField(null=True, blank=True, db_column="CycleStatusID")
    cyclestatusdate = models.DateTimeField(null=True, blank=True, db_column="CycleStatusDate")
    expenditure = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Expenditure")
    carry_forward = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Carry_Forward")
    brought_forward_bank = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Brought_Forward_Bank")
    brought_forward_cash = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Brought_Forward_Cash")
    cycleid = models.IntegerField(null=True, blank=True, db_column="CycleID")


class SucoFinancialDisbursements(models.Model):
    """
    Originally sourced from Suco_Financial_Disbursements in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    class Meta:
        db_table = "suco_financial_disbursements"

    sfd_id = models.IntegerField(primary_key=True, db_column="SFD_ID")
    system_post_id = models.IntegerField(null=True, blank=True, db_column="System_post_id")
    suco_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_ID")
    fd_type_id = models.IntegerField(null=True, blank=True, db_column="FD_type_ID")
    program_activity_id = models.IntegerField(null=True, blank=True, db_column="Program_activity_ID")
    date_of_record = models.DateTimeField(null=True, blank=True, db_column="Date_of_record")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(db_column="Active")


class SucoFinancialinfo(models.Model):
    """
    Originally sourced from Suco_Financial_info in /home/josh/PNDS_Interim_MIS-Data.accdb (3948 records)
    """

    class Meta:
        db_table = "suco_financial_info"

    suco_financial_info_id = models.CharField(max_length=1024, primary_key=True, db_column="Suco_Financial_Info_ID")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    system_post_id = models.IntegerField(null=True, blank=True, db_column="System_post_id")
    project_cycle = models.IntegerField(null=True, blank=True, db_column="Project_cycle")
    suco_finance_code_inf = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_Finance_Code_Inf")
    cvp_number = models.CharField(max_length=1024, null=True, blank=True, db_column="CVP_Number")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(db_column="Active")
    total_community_meeting_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Total_Community_Meeting_budget")
    total_community_training_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Total_Community_Training_budget")
    total_incentive_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Total_Incentive_budget")
    total_admin_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Total_admin_budget")
    total_survey_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Total_survey_budget")
    total_infra_labour_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Total_infra_Labour_budget")
    total_infra_materials_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Total_infra_Materials_budget")
    operationbudgetid = models.IntegerField(null=True, blank=True, db_column="OperationBudgetID")


class SucoInfrastructureProjectReport(models.Model):
    """
    Originally sourced from Suco_Infrastructure_Project_Report in /home/josh/PNDS_Interim_MIS-Data.accdb (52064 records)
    """

    class Meta:
        db_table = "suco_infrastructure_project_report"

    infrastructure_report_id = models.CharField(max_length=1024, primary_key=True, db_column="Infrastructure_Report_ID")
    system_post_id = models.IntegerField(null=True, blank=True, db_column="System_post_id")
    suco_subproject_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_Subproject_ID")
    monthly_report_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Monthly_report_ID")
    report_month = models.DateTimeField(null=True, blank=True, db_column="Report_Month")
    material_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Material_Spend")
    labour_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Labour_Spend")
    percentage_complete = models.IntegerField(null=True, blank=True, db_column="Percentage_complete")
    mandays_male = models.IntegerField(null=True, blank=True, db_column="Mandays_Male")
    mandays_female = models.IntegerField(null=True, blank=True, db_column="Mandays_Female")
    community_contribution = models.IntegerField(null=True, blank=True, db_column="Community_contribution")
    verified = models.BooleanField(db_column="Verified")
    active = models.BooleanField(db_column="Active")
    deactivated_date = models.DateTimeField(null=True, blank=True, db_column="Deactivated_Date")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)
    report_date = models.DateTimeField(null=True, blank=True, db_column="Report_Date")
    subproject_guid = models.CharField(max_length=1024, null=True, blank=True, db_column="Subproject_GUID")


class SucoOperationalReport(models.Model):
    """
    Originally sourced from Suco_Operational_Report in /home/josh/PNDS_Interim_MIS-Data.accdb (41291 records)
    """

    class Meta:
        db_table = "suco_operational_report"

    operational_report_id = models.CharField(max_length=1024, primary_key=True, db_column="Operational_Report_ID")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    system_post_id = models.IntegerField(null=True, blank=True, db_column="System_post_id")
    monthly_report_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Monthly_report_ID")
    report_month = models.DateTimeField(null=True, blank=True, db_column="Report_Month")
    incoming_funding = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Incoming_funding")
    meeting_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Meeting_Spend")
    training_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Training_Spend")
    suco_incentive_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Suco_Incentive_spend")
    administrative_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Administrative_spend")
    survey_design_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Survey_Design_spend")
    cash_on_hand = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Cash_on_hand")
    bank_balance = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Bank_Balance")
    verified = models.BooleanField(db_column="Verified")
    active = models.BooleanField(db_column="Active")
    deactivated_date = models.DateTimeField(null=True, blank=True, db_column="Deactivated_Date")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)
    report_date = models.DateTimeField(null=True, blank=True, db_column="Report_date")
    report_guid = models.CharField(max_length=1024, null=True, blank=True, db_column="Report_GUID")
    finance_approval = models.BooleanField(db_column="Finance_approval")
    operationbudgetid = models.IntegerField(null=True, blank=True, db_column="OperationBudgetID")
    brought_forward = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Brought_Forward")


class SucoPriorities(models.Model):
    """
    Originally sourced from Suco_Priorities in /home/josh/PNDS_Interim_MIS-Data.accdb (11012 records)
    """

    class Meta:
        db_table = "suco_priorities"

    suco_priorityid = models.CharField(max_length=1024, primary_key=True, db_column="Suco_PriorityID")
    suco_cycleid = models.IntegerField(null=True, blank=True, db_column="Suco_CycleID")
    prority = models.IntegerField(null=True, blank=True, db_column="Prority")
    typeof_infra_proposed = models.CharField(max_length=1024, null=True, blank=True, db_column="TypeOf_Infra_Proposed")
    locationid = models.IntegerField(null=True, blank=True, db_column="LocationID")
    volume = models.CharField(max_length=1024, null=True, blank=True, db_column="Volume")
    iswoman_priority = models.BooleanField(db_column="IsWoman_Priority")
    estimatedbudget_boq = models.IntegerField(null=True, blank=True, db_column="EstimatedBudget_BOQ")
    suco_subproject_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_Subproject_ID")
    sectorid = models.IntegerField(null=True, blank=True, db_column="SectorID")
    id = models.IntegerField(null=True, blank=True, db_column="ID")


class SucoSubProject(models.Model):
    """
    Originally sourced from Suco_SubProject in /home/josh/PNDS_Interim_MIS-Data.accdb (5053 records)
    """

    class Meta:
        db_table = "suco_subproject"

    suco_subproject_id = models.CharField(max_length=1024, primary_key=True, db_column="Suco_SubProject_ID")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    system_post_id = models.IntegerField(null=True, blank=True, db_column="System_post_id")
    project_number = models.IntegerField(null=True, blank=True, db_column="Project_Number")
    sector_id = models.IntegerField(null=True, blank=True, db_column="Sector_ID")
    subproject_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Subproject_Name")
    subproject_description = models.CharField(max_length=1024, null=True, blank=True, db_column="Subproject_Description")
    finance_code = models.CharField(max_length=1024, null=True, blank=True, db_column="Finance_code")
    subproject_materials_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Subproject_Materials_budget")
    subproject_labour_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Subproject_Labour_budget")
    subproject_start_date = models.DateTimeField(null=True, blank=True, db_column="Subproject_Start_Date")
    subproject_finish_date = models.DateTimeField(null=True, blank=True, db_column="Subproject_Finish_Date")
    verified = models.BooleanField(db_column="Verified")
    date_of_verification = models.DateTimeField(null=True, blank=True, db_column="Date_of_Verification")
    active = models.BooleanField(db_column="Active")
    subproject_aldea = models.IntegerField(null=True, blank=True, db_column="Subproject_Aldea")
    no_of_women_benefic = models.IntegerField(null=True, blank=True, db_column="No_of_ Women_Benefic")
    no_of_men_benefic = models.IntegerField(null=True, blank=True, db_column="No_of_Men_Benefic")
    no_of_household_benefic = models.IntegerField(null=True, blank=True, db_column="No_of_Household_Benefic")
    subproject_main_activity_id = models.IntegerField(null=True, blank=True, db_column="Subproject_Main_Activity_ID")
    main_activity_units = models.CharField(max_length=1024, null=True, blank=True, db_column="Main_activity_units")
    main_activity_unit_type = models.CharField(max_length=1024, null=True, blank=True, db_column="Main_activity_unit_type")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)
    gps_coords = models.CharField(max_length=1024, null=True, blank=True, db_column="GPS_coords")
    finance_approval = models.BooleanField(db_column="Finance_approval")
    settlement_id = models.IntegerField(null=True, blank=True, db_column="Settlement_id")
    planned_quantity_value = models.IntegerField(null=True, blank=True, db_column="Planned_Quantity_Value")
    actual_quantity_value = models.IntegerField(null=True, blank=True, db_column="Actual_Quantity_Value")
    estimated_subproject_cost = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Estimated_SubProject_Cost")
    actual_subproject_cost = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Actual_SubProject_Cost")
    subproject_community_contribution = models.IntegerField(null=True, blank=True, db_column="Subproject_Community_Contribution")
    subproject_material_budget_actual = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Subproject_Material_Budget_Actual")
    subproject_labour_budget_actual = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Subproject_Labour_Budget_Actual")
    actual_startdate = models.DateTimeField(null=True, blank=True, db_column="Actual_StartDate")
    actual_finishdate = models.DateTimeField(null=True, blank=True, db_column="Actual_FinishDate")
    iswomen_priority = models.BooleanField(db_column="IsWomen_priority")
    subprojectstatus = models.IntegerField(null=True, blank=True, db_column="SubprojectStatus")
    subprojectstatusdate = models.DateTimeField(null=True, blank=True, db_column="SubprojectStatusDate")
    subproject_delays = models.CharField(max_length=1024, null=True, blank=True, db_column="Subproject_Delays")
    subprojectstatusid = models.IntegerField(null=True, blank=True, db_column="SubprojectStatusID")
    suco_cycleid = models.IntegerField(null=True, blank=True, db_column="Suco_CycleID")
    project_picture_before = models.CharField(max_length=1024, null=True, blank=True, db_column="Project_Picture_Before")
    approval_date = models.DateTimeField(null=True, blank=True, db_column="Approval_Date")
    activityid = models.IntegerField(null=True, blank=True, db_column="ActivityID")
    suco_priorityid = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_PriorityID")
    gps_latitude = models.IntegerField(null=True, blank=True, db_column="GPS_Latitude")
    gps_longitude = models.IntegerField(null=True, blank=True, db_column="GPS_Longitude")
    actual_community_contribution = models.IntegerField(null=True, blank=True, db_column="Actual_Community_Contribution")
    statuschange_reason = models.CharField(max_length=1024, null=True, blank=True, db_column="StatusChange_Reason")
    statuschange_date = models.DateTimeField(null=True, blank=True, db_column="StatusChange_Date")
    projecttypeid = models.IntegerField(null=True, blank=True, db_column="ProjectTypeID")
    parentprojectcode = models.CharField(max_length=1024, null=True, blank=True, db_column="ParentProjectCode")


class SucoCMTMembers(models.Model):
    """
    Originally sourced from SucoCMTMembers in /home/josh/PNDS_Interim_MIS-Data.accdb (4976 records)
    """

    class Meta:
        db_table = "sucocmtmembers"

    sucocmtid = models.CharField(max_length=1024, primary_key=True, db_column="SucoCMTID")
    cmtmembername = models.CharField(max_length=1024, null=True, blank=True, db_column="CMTMemberName")
    suco_id = models.IntegerField(db_column="Suco_ID")
    telephone = models.CharField(max_length=1024, null=True, blank=True, db_column="Telephone")
    genderid = models.IntegerField(null=True, blank=True, db_column="GenderID")
    disability = models.BooleanField(db_column="Disability")
    cmtpositionid = models.IntegerField(null=True, blank=True, db_column="CMTPositionID")
    isactivemember = models.BooleanField(db_column="IsActiveMember")
    electionroundid = models.IntegerField(null=True, blank=True, db_column="ElectionRoundID")
    electiondate = models.DateTimeField(null=True, blank=True, db_column="ElectionDate")
    cmtexit = models.BooleanField(db_column="CMTExit")
    dateexitcmt = models.DateTimeField(null=True, blank=True, db_column="DateExitCMT")
    comments = models.CharField(max_length=1024, null=True, blank=True, db_column="Comments")
    recordcreationdate = models.DateTimeField(null=True, blank=True, db_column="RecordCreationDate")
    recordchangedate = models.CharField(max_length=1024, null=True, blank=True, db_column="RecordChangeDate")


class syncImportLog(models.Model):
    """
    Originally sourced from syncImportLog in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    class Meta:
        db_table = "syncimportlog"

    id = models.CharField(max_length=1024, primary_key=True, db_column="ID")
    table_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Table_Name")
    type = models.CharField(max_length=1024, null=True, blank=True, db_column="Type")
    importdate = models.DateTimeField(null=True, blank=True, db_column="ImportDate")


class SystemInfo(models.Model):
    """
    Originally sourced from System_Info in /home/josh/PNDS_Interim_MIS-Data.accdb (1 records)
    """

    class Meta:
        db_table = "system_info"

    system_role = models.CharField(max_length=1024, primary_key=True, db_column="System_role")
    system_name = models.CharField(max_length=1024, null=True, blank=True, db_column="System_name")
    system_table_version = models.IntegerField(null=True, blank=True, db_column="System_table_version")
    system_last_start_date = models.DateTimeField(null=True, blank=True, db_column="System_last_start_date")
    system_post_id_number = models.CharField(max_length=1024, null=True, blank=True, db_column="System_post_ID_number")
    system_district_id = models.IntegerField(null=True, blank=True, db_column="System_district_id")
    system_output_path = models.CharField(max_length=1024, null=True, blank=True, db_column="System_output_path")
    system_input_path = models.CharField(max_length=1024, null=True, blank=True, db_column="System_input_path")
    system_update_path = models.CharField(max_length=1024, null=True, blank=True, db_column="System_update_path")
    system_document_path = models.CharField(max_length=1024, null=True, blank=True, db_column="System_document_path")
    system_data_version = models.IntegerField(null=True, blank=True, db_column="System_data_version")
    system_forms_version = models.IntegerField(null=True, blank=True, db_column="System_forms_version")
    system_forms_path = models.CharField(max_length=1024, null=True, blank=True, db_column="System_forms_path")
    system_log_path = models.CharField(max_length=1024, null=True, blank=True, db_column="System_log_path")
    system_backup_script = models.CharField(max_length=1024, null=True, blank=True, db_column="System_backup_script")
    system_bit_length = models.CharField(max_length=1024, null=True, blank=True, db_column="System_bit_length")
    system_run_once_version = models.IntegerField(null=True, blank=True, db_column="System_run_once_version")


class Systemlog(models.Model):
    """
    Originally sourced from System_log in /home/josh/PNDS_Interim_MIS-Data.accdb (12353 records)
    """

    class Meta:
        db_table = "system_log"

    id = models.IntegerField(primary_key=True, db_column="ID")
    event_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Event_id")
    system_post_id = models.CharField(max_length=1024, null=True, blank=True, db_column="System_Post_id")
    event_class = models.CharField(max_length=1024, null=True, blank=True, db_column="Event_class")
    event_description = models.CharField(max_length=1024, null=True, blank=True, db_column="Event_description")
    event_data = models.CharField(max_length=1024, null=True, blank=True, db_column="Event_data")
    user_id = models.CharField(max_length=1024, null=True, blank=True)
    event_date_time = models.DateTimeField(null=True, blank=True, db_column="event_Date_time")
    transmission_date_time = models.DateTimeField(null=True, blank=True)


class Transfers(models.Model):
    """
    Originally sourced from Transfers in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    class Meta:
        db_table = "transfers"

    transmission_id = models.IntegerField(primary_key=True, db_column="Transmission_ID")
    post_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Post_id")
    unique_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Unique_ID")
    transfer_date_time = models.DateTimeField(null=True, blank=True, db_column="Transfer_date_time")
    transfer_direction = models.CharField(max_length=1024, null=True, blank=True, db_column="Transfer_direction")
    transfer_filename = models.CharField(max_length=1024, null=True, blank=True, db_column="Transfer_filename")


class Users(models.Model):
    """
    Originally sourced from Users in /home/josh/PNDS_Interim_MIS-Data.accdb (61 records)
    """

    class Meta:
        db_table = "users"

    id = models.IntegerField(primary_key=True, db_column="ID")
    email = models.CharField(max_length=1024, null=True, blank=True, db_column="Email")
    fullname = models.CharField(max_length=1024, null=True, blank=True, db_column="FullName")
    login = models.CharField(max_length=1024, null=True, blank=True, db_column="Login")
    password = models.CharField(max_length=1024, null=True, blank=True, db_column="Password")
    language = models.IntegerField(null=True, blank=True, db_column="Language")
    group_id = models.IntegerField(null=True, blank=True, db_column="Group_id")
    email_notifications = models.BooleanField(db_column="Email_notifications")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_change_date = models.DateTimeField(null=True, blank=True, db_column="Record_change_date")
    last_transmission_number = models.IntegerField(null=True, blank=True, db_column="Last_transmission_number")
    district_id = models.IntegerField(null=True, blank=True, db_column="District_ID")


class Usersold(models.Model):
    """
    Originally sourced from Users_old in /home/josh/PNDS_Interim_MIS-Data.accdb (17 records)
    """

    class Meta:
        db_table = "users_old"

    id = models.IntegerField(primary_key=True, db_column="ID")
    email = models.CharField(max_length=1024, null=True, blank=True, db_column="Email")
    fullname = models.CharField(max_length=1024, null=True, blank=True, db_column="FullName")
    login = models.CharField(max_length=1024, null=True, blank=True, db_column="Login")
    password = models.CharField(max_length=1024, null=True, blank=True, db_column="Password")
    language = models.IntegerField(null=True, blank=True, db_column="Language")
    group_id = models.IntegerField(null=True, blank=True, db_column="Group_id")
    email_notifications = models.BooleanField(db_column="Email_notifications")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_change_date = models.DateTimeField(null=True, blank=True, db_column="Record_change_date")
    last_transmission_number = models.IntegerField(null=True, blank=True, db_column="Last_transmission_number")
    district_id = models.IntegerField(null=True, blank=True, db_column="District_ID")


class UserTracking(models.Model):
    """
    Originally sourced from UserTracking in /home/josh/PNDS_Interim_MIS-Data.accdb (23556 records)
    """

    class Meta:
        db_table = "usertracking"

    usertrackingid = models.CharField(max_length=1024, primary_key=True, db_column="UserTrackingID")
    userid = models.IntegerField(null=True, blank=True, db_column="UserID")
    datetime_loggedin = models.DateTimeField(null=True, blank=True, db_column="DateTime_LoggedIn")
    datetime_loggedout = models.DateTimeField(null=True, blank=True, db_column="DateTime_LoggedOut")
    application = models.CharField(max_length=1024, null=True, blank=True, db_column="Application")
    versionnumber = models.CharField(max_length=1024, null=True, blank=True, db_column="VersionNumber")


class zActivities(models.Model):
    """
    Originally sourced from zActivities in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """

    class Meta:
        db_table = "zactivities"

    activityid = models.IntegerField(primary_key=True, db_column="ActivityID")
    activity = models.CharField(max_length=1024, null=True, blank=True, db_column="Activity")
    activity_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Activity_Tetum")
    outputid = models.IntegerField(null=True, blank=True, db_column="OutputID")


class zActivityDocumenttype(models.Model):
    """
    Originally sourced from zActivity_Document_type in /home/josh/PNDS_Interim_MIS-Data.accdb (38 records)
    """

    class Meta:
        db_table = "zactivity_document_type"

    id = models.IntegerField(primary_key=True, db_column="ID")
    zprogram_activity_id = models.IntegerField(null=True, blank=True, db_column="zProgram_Activity_ID")
    zdocument_type_id = models.IntegerField(null=True, blank=True, db_column="zDocument_type_ID")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zActivitytype(models.Model):
    """
    Originally sourced from zActivity_type in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """

    class Meta:
        db_table = "zactivity_type"

    activity_type_id = models.IntegerField(primary_key=True, db_column="Activity_type_ID")
    activity_type_description = models.CharField(max_length=1024, null=True, blank=True, db_column="Activity_type_description")
    units = models.CharField(max_length=1024, null=True, blank=True, db_column="Units")
    range = models.CharField(max_length=1024, null=True, blank=True, db_column="Range")
    can_be_main = models.BooleanField(db_column="Can_be_main")
    can_be_secondary = models.BooleanField(db_column="Can_be_secondary")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zAldeia(models.Model):
    """
    Originally sourced from zAldeia in /home/josh/PNDS_Interim_MIS-Data.accdb (2254 records)
    """

    class Meta:
        db_table = "zaldeia"

    id = models.IntegerField(primary_key=True, db_column="ID")
    aldeia_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Aldeia_name")
    aldeia_pcode = models.CharField(max_length=1024, null=True, blank=True, db_column="Aldeia_PCODE")
    suco_pcode = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_PCODE")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    gps_coords = models.CharField(max_length=1024, null=True, blank=True, db_column="GPS_coords")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    aldea_population_total = models.IntegerField(null=True, blank=True, db_column="Aldea_population_total")
    aldea_population_households = models.IntegerField(null=True, blank=True, db_column="Aldea_population_households")
    aldea_population_women = models.IntegerField(null=True, blank=True, db_column="Aldea_population_women")
    aldea_population_men = models.IntegerField(null=True, blank=True, db_column="Aldea_population_men")
    aldea_population_children = models.IntegerField(null=True, blank=True, db_column="Aldea_population_children")


class zCategories(models.Model):
    """
    Originally sourced from zCategories in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zcategories"

    categoryid = models.IntegerField(primary_key=True, db_column="CategoryID")
    category = models.CharField(max_length=1024, null=True, blank=True, db_column="Category")
    category_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Category_Tetum")


class zCMTPositions1(models.Model):
    """
    Originally sourced from zCMT_Positions in /home/josh/PNDS_Interim_MIS-Data.accdb (11 records)
    """

    class Meta:
        db_table = "zcmt_positions"

    cmt_position_id = models.IntegerField(primary_key=True, db_column="CMT_Position_ID")
    cmt_position_name = models.CharField(max_length=1024, null=True, blank=True, db_column="CMT_Position_name")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zCycles(models.Model):
    """
    Originally sourced from zCycles in /home/josh/PNDS_Interim_MIS-Data.accdb (13 records)
    """

    class Meta:
        db_table = "zcycles"

    cycle_id = models.IntegerField(primary_key=True, db_column="Cycle_ID")
    cycle_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Cycle_name")
    cycle_start_date = models.DateTimeField(null=True, blank=True, db_column="Cycle_start_date")
    cycle_finish_date = models.DateTimeField(null=True, blank=True, db_column="Cycle_finish_date")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zCycleStatus(models.Model):
    """
    Originally sourced from zCycleStatus in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zcyclestatus"

    cyclestatusid = models.IntegerField(primary_key=True, db_column="CycleStatusID")
    cyclestatus = models.CharField(max_length=1024, null=True, blank=True, db_column="CycleStatus")
    cyclestatus_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="CycleStatus_Tetum")


class zDistrictPhase(models.Model):
    """
    Originally sourced from zDistrict_Phase in /home/josh/PNDS_Interim_MIS-Data.accdb (56 records)
    """

    class Meta:
        db_table = "zdistrict_phase"

    districtphaseid = models.IntegerField(primary_key=True, db_column="DistrictPhaseID")
    districtid = models.IntegerField(null=True, blank=True, db_column="DistrictID")
    phaseid = models.IntegerField(null=True, blank=True, db_column="PhaseID")
    cycleid = models.IntegerField(null=True, blank=True, db_column="CycleID")


class zDocumentfiletype(models.Model):
    """
    Originally sourced from zDocument_file_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zdocument_file_type"

    id = models.IntegerField(primary_key=True, db_column="ID")
    document_type = models.CharField(max_length=1024, null=True, blank=True, db_column="Document_type")
    valid_extension = models.CharField(max_length=1024, null=True, blank=True, db_column="Valid_extension")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zDocumenttype(models.Model):
    """
    Originally sourced from zDocument_type in /home/josh/PNDS_Interim_MIS-Data.accdb (99 records)
    """

    class Meta:
        db_table = "zdocument_type"

    id = models.IntegerField(primary_key=True, db_column="ID")
    document_type_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Document_type_name")
    monthly_reports = models.BooleanField(db_column="Monthly_reports")
    social_activities = models.BooleanField()
    finance_activites = models.BooleanField()
    verification = models.BooleanField(db_column="Verification")
    r_50_report = models.BooleanField(db_column="50_report")
    completion_report = models.BooleanField(db_column="Completion_report")
    active = models.BooleanField(db_column="Active")
    deacticated_date = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zElectionRound(models.Model):
    """
    Originally sourced from zElectionRound in /home/josh/PNDS_Interim_MIS-Data.accdb (5 records)
    """

    class Meta:
        db_table = "zelectionround"

    electionroundid = models.IntegerField(primary_key=True, db_column="ElectionRoundID")
    electionroundtype = models.CharField(max_length=1024, null=True, blank=True, db_column="ElectionRoundType")
    electionround_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="ElectionRound_Tetum")
    recordcreationdate = models.DateTimeField(null=True, blank=True, db_column="RecordCreationDate")
    recordchangedate = models.DateTimeField(null=True, blank=True, db_column="RecordChangeDate")


class zFinancedisbursementrules(models.Model):
    """
    Originally sourced from zFinance_disbursement_rules in /home/josh/PNDS_Interim_MIS-Data.accdb (23 records)
    """

    class Meta:
        db_table = "zfinance_disbursement_rules"

    id = models.IntegerField(primary_key=True, db_column="ID")
    fd_type_id = models.IntegerField(null=True, blank=True, db_column="FD_type_id")
    program_activity_id = models.IntegerField(null=True, blank=True, db_column="Program_activity_id")
    order = models.IntegerField(null=True, blank=True, db_column="Order")
    active = models.BooleanField(db_column="Active")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zFinancedisbursementtype(models.Model):
    """
    Originally sourced from zFinance_disbursement_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zfinance_disbursement_type"

    fbt_id = models.IntegerField(primary_key=True, db_column="FBT_ID")
    fbd_type = models.CharField(max_length=1024, null=True, blank=True, db_column="FBD_type")
    active = models.BooleanField()
    fdb_order_number = models.IntegerField(null=True, blank=True, db_column="FDB_order_number")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zFinancialdisbursementactitvites(models.Model):
    """
    Originally sourced from zFinancial_disbursement_actitvites in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """

    class Meta:
        db_table = "zfinancial_disbursement_actitvites"

    fda_id = models.IntegerField(primary_key=True, db_column="FDA_ID")
    activity_order = models.IntegerField(null=True, blank=True, db_column="Activity_order")
    activity_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Activity_Name")
    active = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zFreebalanceBudgetextract(models.Model):
    """
    Originally sourced from zFreebalance_Budget_extract in /home/josh/PNDS_Interim_MIS-Data.accdb (3666 records)
    """

    class Meta:
        db_table = "zfreebalance_budget_extract"

    id = models.IntegerField(primary_key=True, db_column="ID")
    import_id = models.CharField(max_length=1024, null=True, blank=True)
    allocateddomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="allocatedDomestic")
    allocatedforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="allocatedForeign")
    allowtoexceed = models.CharField(max_length=1024, null=True, blank=True, db_column="allowToExceed")
    annualforecastdomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="annualForecastDomestic")
    annualforecastforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="annualForecastForeign")
    approvaldate = models.CharField(max_length=1024, null=True, blank=True, db_column="approvalDate")
    checkcontrolamount = models.CharField(max_length=1024, null=True, blank=True, db_column="checkControlAmount")
    checkcontrolpercentage = models.CharField(max_length=1024, null=True, blank=True, db_column="checkControlPercentage")
    commitmentsdomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="commitmentsDomestic")
    commitmentsforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="commitmentsForeign")
    creationdate = models.CharField(max_length=1024, null=True, blank=True, db_column="creationDate")
    currentamountdomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="currentAmountDomestic")
    currentamountforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="currentAmountForeign")
    exchangerate = models.CharField(max_length=1024, null=True, blank=True, db_column="exchangeRate")
    freebalancedomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="freeBalanceDomestic")
    freebalanceforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="freeBalanceForeign")
    indicativecommitmentsdomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="indicativeCommitmentsDomestic")
    indicativecommitmentsforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="indicativeCommitmentsForeign")
    isactive = models.CharField(max_length=1024, null=True, blank=True, db_column="isActive")
    isbasedonaccumulatedperiodamount = models.CharField(max_length=1024, null=True, blank=True, db_column="isBasedOnAccumulatedPeriodAmount")
    isbudgetdistributioncontrol = models.CharField(max_length=1024, null=True, blank=True, db_column="isBudgetDistributionControl")
    isvalidatedbyforeigncurrency = models.CharField(max_length=1024, null=True, blank=True, db_column="isValidatedByForeignCurrency")
    obligationsdomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="obligationsDomestic")
    obligationsforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="obligationsForeign")
    origin = models.CharField(max_length=1024, null=True, blank=True)
    originalamountdomestic = models.IntegerField(null=True, blank=True, db_column="originalAmountDomestic")
    originalamountforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="originalAmountForeign")
    paiddomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="paidDomestic")
    paidforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="paidForeign")
    surplusdeficitdomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="surplusDeficitDomestic")
    surplusdeficitforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="surplusDeficitForeign")
    toleranceamount = models.CharField(max_length=1024, null=True, blank=True, db_column="toleranceAmount")
    tolerancepercentage = models.CharField(max_length=1024, null=True, blank=True, db_column="tolerancePercentage")
    transfersdomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="transfersDomestic")
    transfersforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="transfersForeign")
    unallocateddomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="unallocatedDomestic")
    unallocatedforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="unallocatedForeign")
    updatesdomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="updatesDomestic")
    updatesforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="updatesForeign")
    ytdactualdomestic = models.CharField(max_length=1024, null=True, blank=True, db_column="ytdActualDomestic")
    ytdactualforeign = models.CharField(max_length=1024, null=True, blank=True, db_column="ytdActualForeign")
    approvedbyapplicationid = models.CharField(max_length=1024, null=True, blank=True, db_column="approvedByapplicationId")
    budgetcontroltypeapplicationid = models.CharField(max_length=1024, null=True, blank=True, db_column="budgetControlTypeapplicationId")
    budgetofficeapplicationid = models.CharField(max_length=1024, null=True, blank=True, db_column="budgetOfficeapplicationId")
    codingblockstringcode = models.CharField(max_length=1024, null=True, blank=True, db_column="codingBlockstringCode")
    codingblockcoagroupcoaapplicationid = models.CharField(max_length=1024, null=True, blank=True, db_column="codingBlockcoaGroupcoaapplicationId")
    codingblockcoagroupcode = models.CharField(max_length=1024, null=True, blank=True, db_column="codingBlockcoaGroupcode")
    createdbyapplicationid = models.CharField(max_length=1024, null=True, blank=True, db_column="createdByapplicationId")
    currencyapplicationid = models.CharField(max_length=1024, null=True, blank=True, db_column="currencyapplicationId")
    fiscalyearapplicationid = models.CharField(max_length=1024, null=True, blank=True, db_column="fiscalYearapplicationId")
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_export_date = models.DateTimeField(null=True, blank=True)
    export_number = models.IntegerField(null=True, blank=True)
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    order = models.IntegerField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zGender(models.Model):
    """
    Originally sourced from zGender in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zgender"

    genderid = models.IntegerField(primary_key=True, db_column="GenderID")
    gender_english = models.CharField(max_length=1024, null=True, blank=True, db_column="Gender_English")
    gender_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Gender_Tetum")


class zGroups(models.Model):
    """
    Originally sourced from zGroups in /home/josh/PNDS_Interim_MIS-Data.accdb (8 records)
    """

    class Meta:
        db_table = "zgroups"

    id = models.IntegerField(primary_key=True, db_column="ID")
    group_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Group_name")
    finance_functions = models.BooleanField(db_column="Finance_functions")
    admin_functions = models.BooleanField(db_column="Admin_functions")
    reporting_functions = models.BooleanField(db_column="Reporting_functions")
    mis_functions = models.BooleanField(db_column="MIS_functions")
    complaints_functions = models.BooleanField(db_column="Complaints_functions")
    data_fix_functions = models.BooleanField(db_column="Data_fix_functions")
    social_functions = models.BooleanField(db_column="Social_functions")
    field_team_data = models.BooleanField(db_column="Field_team_data")
    field_team_approval = models.BooleanField(db_column="Field_team_approval")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_change_date = models.DateTimeField(null=True, blank=True, db_column="Record_change_date")
    last_transmission_number = models.IntegerField(null=True, blank=True, db_column="Last_transmission_number")
    finance_edit = models.BooleanField(db_column="Finance_edit")
    social_edit = models.BooleanField(db_column="Social_edit")
    subproject_edit = models.BooleanField(db_column="Subproject_edit")
    suco_budgeting_edit = models.BooleanField(db_column="Suco_budgeting_edit")
    finance_monitoring_edit = models.BooleanField(db_column="Finance_monitoring_edit")
    complaints_edit = models.BooleanField(db_column="Complaints_edit")
    reports_edit = models.BooleanField(db_column="Reports_edit")
    unverify_report = models.BooleanField(db_column="Unverify_report")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    district_admin = models.BooleanField(db_column="District_admin")


class zIndicators(models.Model):
    """
    Originally sourced from zIndicators in /home/josh/PNDS_Interim_MIS-Data.accdb (10 records)
    """

    class Meta:
        db_table = "zindicators"

    indicatorid = models.IntegerField(primary_key=True, db_column="IndicatorID")
    categoryid = models.IntegerField(null=True, blank=True, db_column="CategoryID")
    indicator = models.CharField(max_length=1024, null=True, blank=True, db_column="Indicator")
    indicator_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Indicator_Tetum")


class zLanguage(models.Model):
    """
    Originally sourced from zLanguage in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    class Meta:
        db_table = "zlanguage"

    id = models.IntegerField(primary_key=True, db_column="ID")
    language_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Language_Name")
    language_default = models.BooleanField(db_column="Language_default")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zLastID(models.Model):
    """
    Originally sourced from zLastID in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zlastid"

    tablename = models.CharField(max_length=1024, primary_key=True, db_column="TableName")
    lastid = models.IntegerField(null=True, blank=True, db_column="LastID")


class zOutputs(models.Model):
    """
    Originally sourced from zOutputs in /home/josh/PNDS_Interim_MIS-Data.accdb (123 records)
    """

    class Meta:
        db_table = "zoutputs"

    outputid = models.IntegerField(primary_key=True, db_column="OutputID")
    output = models.CharField(max_length=1024, null=True, blank=True, db_column="Output")
    output_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Output_Tetum")
    sectorid = models.IntegerField(null=True, blank=True, db_column="SectorID")
    sub_sectorid = models.IntegerField(null=True, blank=True, db_column="Sub_SectorID")


class zOutputUnit(models.Model):
    """
    Originally sourced from zOutputUnit in /home/josh/PNDS_Interim_MIS-Data.accdb (117 records)
    """

    class Meta:
        db_table = "zoutputunit"

    outputunitid = models.IntegerField(primary_key=True, db_column="OutputUnitID")
    outputid = models.IntegerField(null=True, blank=True, db_column="OutputID")
    unitid = models.IntegerField(null=True, blank=True, db_column="UnitID")
    minimum_value = models.IntegerField(null=True, blank=True, db_column="Minimum_Value")
    maximum_value = models.IntegerField(null=True, blank=True, db_column="Maximum_Value")


class zPNDSFreebalancetranslation(models.Model):
    """
    Originally sourced from zPNDS_Freebalance_translation in /home/josh/PNDS_Interim_MIS-Data.accdb (9 records)
    """

    class Meta:
        db_table = "zpnds_freebalance_translation"

    id = models.IntegerField(primary_key=True, db_column="ID")
    acct_no = models.IntegerField(null=True, blank=True, db_column="Acct_No")
    description = models.CharField(max_length=1024, null=True, blank=True, db_column="Description")
    freebalance_line_item_budget = models.IntegerField(null=True, blank=True, db_column="FreeBalance_Line_Item_budget")
    freebalance_line_item_monthly_exp = models.IntegerField(null=True, blank=True, db_column="Freebalance_line_item_monthly_exp")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zPriorities(models.Model):
    """
    Originally sourced from zPriorities in /home/josh/PNDS_Interim_MIS-Data.accdb (50 records)
    """

    class Meta:
        db_table = "zpriorities"

    priorityid = models.IntegerField(primary_key=True, db_column="PriorityID")
    priority = models.IntegerField(null=True, blank=True, db_column="Priority")


class zProgramActivity(models.Model):
    """
    Originally sourced from zProgram_Activity in /home/josh/PNDS_Interim_MIS-Data.accdb (39 records)
    """

    class Meta:
        db_table = "zprogram_activity"

    program_activity_id = models.IntegerField(primary_key=True, db_column="Program_activity_ID")
    activity_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Activity_Name")
    social_activity_number = models.IntegerField(null=True, blank=True, db_column="Social_Activity_number")
    finance_activity_number = models.IntegerField(null=True, blank=True, db_column="Finance_Activity_number")
    program_activity_number = models.IntegerField(null=True, blank=True, db_column="Program_activity_number")
    finance_activity = models.BooleanField(db_column="Finance_activity")
    social_activity = models.BooleanField(db_column="Social_activity")
    program_activity = models.BooleanField(db_column="Program_activity")
    technical_activity = models.BooleanField(db_column="Technical_Activity")
    active = models.BooleanField(db_column="Active")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    aldea_activity = models.BooleanField(db_column="Aldea_activity")
    zprogram_activity_level_id = models.IntegerField(null=True, blank=True, db_column="zProgram_Activity_level_ID")
    zprogram_activity_type_id = models.IntegerField(null=True, blank=True, db_column="zProgram_Activity_type_ID")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zProgramActivitylevel(models.Model):
    """
    Originally sourced from zProgram_Activity_level in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zprogram_activity_level"

    program_activity_level_id = models.IntegerField(primary_key=True, db_column="Program_Activity_level_ID")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_change_date = models.DateTimeField(null=True, blank=True, db_column="Record_change_date")


class zProgramactivtytype(models.Model):
    """
    Originally sourced from zProgram_activty_type in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zprogram_activty_type"

    program_activtiy_type_id = models.IntegerField(primary_key=True, db_column="Program_activtiy_type_ID")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_change_date = models.DateTimeField(null=True, blank=True, db_column="Record_change_date")


class zReporttype(models.Model):
    """
    Originally sourced from zReport_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zreport_type"

    report_type_id = models.IntegerField(primary_key=True, db_column="Report_type_ID")
    report_type_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Report_type_name")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zSector(models.Model):
    """
    Originally sourced from zSector in /home/josh/PNDS_Interim_MIS-Data.accdb (8 records)
    """

    class Meta:
        db_table = "zsector"

    sector_id = models.IntegerField(primary_key=True, db_column="Sector_ID")
    sector_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Sector_Name")
    icon_name = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zSectorActvity(models.Model):
    """
    Originally sourced from zSector_Actvity in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """

    class Meta:
        db_table = "zsector_actvity"

    id = models.IntegerField(primary_key=True, db_column="ID")
    active = models.BooleanField(db_column="Active")
    sector_id = models.IntegerField(null=True, blank=True, db_column="Sector_ID")
    activity_type_id = models.IntegerField(null=True, blank=True, db_column="Activity_Type_ID")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zSettlements(models.Model):
    """
    Originally sourced from zSettlements in /home/josh/PNDS_Interim_MIS-Data.accdb (2829 records)
    """

    class Meta:
        db_table = "zsettlements"

    id = models.IntegerField(primary_key=True, db_column="ID")
    set_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Set_Name")
    suco_pcode = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_PCODE")
    suco_id = models.IntegerField(null=True, blank=True, db_column="Suco_ID")
    gps_coords = models.CharField(max_length=1024, null=True, blank=True, db_column="GPS_Coords")
    set_pcode = models.CharField(max_length=1024, null=True, blank=True, db_column="Set_PCODE")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zSubSector(models.Model):
    """
    Originally sourced from zSub_Sector in /home/josh/PNDS_Interim_MIS-Data.accdb (23 records)
    """

    class Meta:
        db_table = "zsub_sector"

    sub_sectorid = models.IntegerField(primary_key=True, db_column="Sub_SectorID")
    sub_sector = models.CharField(max_length=1024, null=True, blank=True, db_column="Sub_Sector")
    sub_sector_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Sub_Sector_Tetum")
    sector_id = models.IntegerField(null=True, blank=True, db_column="Sector_ID")


class zSubprojectStatus(models.Model):
    """
    Originally sourced from zSubproject_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zsubproject_status"

    status_id = models.IntegerField(primary_key=True, db_column="Status_ID")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_change_date = models.DateTimeField(null=True, blank=True, db_column="Record_change_date")


class zSubprojectStatus1(models.Model):
    """
    Originally sourced from zSubprojectStatus in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """

    class Meta:
        db_table = "zsubprojectstatus"

    subprojectstatusid = models.IntegerField(primary_key=True, db_column="SubprojectStatusID")
    subprojectstatus = models.CharField(max_length=1024, null=True, blank=True, db_column="SubprojectStatus")
    subprojectstatus_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="SubprojectStatus_Tetum")


class zSucophase(models.Model):
    """
    Originally sourced from zSuco_phase in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zsuco_phase"

    id = models.IntegerField(primary_key=True, db_column="ID")
    phase = models.CharField(max_length=1024, null=True, blank=True, db_column="Phase")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zSucoStatus(models.Model):
    """
    Originally sourced from zSuco_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    class Meta:
        db_table = "zsuco_status"

    suco_status_id = models.IntegerField(primary_key=True, db_column="Suco_Status_ID")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_change_date = models.DateTimeField(null=True, blank=True, db_column="Record_change_date")


class zTetumtranslation(models.Model):
    """
    Originally sourced from zTetum_translation in /home/josh/PNDS_Interim_MIS-Data.accdb (606 records)
    """

    class Meta:
        db_table = "ztetum_translation"

    id = models.IntegerField(primary_key=True, db_column="ID")
    type_data = models.BooleanField(db_column="Type_Data")
    type_label = models.BooleanField(db_column="Type_Label")
    type_error = models.BooleanField(db_column="Type_error")
    english_word = models.CharField(max_length=1024, null=True, blank=True, db_column="English_word")
    tetum_word = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum_word")
    indonesian_word = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian_word")
    long_number = models.IntegerField(null=True, blank=True, db_column="Long_number")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zTetumtranslationOLD(models.Model):
    """
    Originally sourced from zTetum_translation_OLD in /home/josh/PNDS_Interim_MIS-Data.accdb (569 records)
    """

    class Meta:
        db_table = "ztetum_translation_old"

    id = models.IntegerField(primary_key=True, db_column="ID")
    type_data = models.BooleanField(db_column="Type_Data")
    type_label = models.BooleanField(db_column="Type_Label")
    type_error = models.BooleanField(db_column="Type_error")
    english_word = models.CharField(max_length=1024, null=True, blank=True, db_column="English_word")
    tetum_word = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum_word")
    indonesian_word = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian_word")
    long_number = models.IntegerField(null=True, blank=True, db_column="Long_number")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zTransMetatables(models.Model):
    """
    Originally sourced from zTrans_Meta_tables in /home/josh/PNDS_Interim_MIS-Data.accdb (50 records)
    """

    class Meta:
        db_table = "ztrans_meta_tables"

    id = models.IntegerField(primary_key=True, db_column="ID")
    table_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Table_name")
    transfer_table_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Transfer_table_name")
    audit_table_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Audit_table_name")
    trans_dili_to_district = models.BooleanField(db_column="Trans_DILI_to_District")
    trans_district_to_dili = models.BooleanField(db_column="Trans_DISTRICT_to_DILI")
    requires_verified = models.BooleanField(db_column="Requires_verified")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zUnits(models.Model):
    """
    Originally sourced from zUnits in /home/josh/PNDS_Interim_MIS-Data.accdb (9 records)
    """

    class Meta:
        db_table = "zunits"

    unitid = models.IntegerField(primary_key=True, db_column="UnitID")
    unit_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Unit_Tetum")
    description = models.CharField(max_length=1024, null=True, blank=True, db_column="Description")
    unit = models.CharField(max_length=1024, null=True, blank=True, db_column="Unit")


class zYears(models.Model):
    """
    Originally sourced from zYears in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zyears"

    id = models.IntegerField(primary_key=True, db_column="ID")
    year_of_operation = models.CharField(max_length=1024, null=True, blank=True, db_column="Year_of_operation")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class DataSyncLog(models.Model):
    """
    Originally sourced from Data_Sync_Log in /home/josh/PNDS_Interim_MIS-Data.accdb (4375 records)
    """

    class Meta:
        db_table = "data_sync_log"

    id = models.IntegerField(primary_key=True, db_column="ID")
    districtid = models.IntegerField(null=True, blank=True, db_column="DistrictID")
    data_imported = models.IntegerField(null=True, blank=True, db_column="Data_Imported")
    data_updated = models.IntegerField(null=True, blank=True, db_column="Data_Updated")
    data_imported_priorities = models.IntegerField(null=True, blank=True, db_column="Data_Imported_Priorities")
    data_updated_priorities = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Priorities")
    data_imported_progress = models.IntegerField(null=True, blank=True, db_column="Data_Imported_Progress")
    data_updated_progress = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Progress")
    data_imported_project = models.IntegerField(null=True, blank=True, db_column="Data_Imported_Project")
    data_updated_project = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Project")
    data_updated_project_dates = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Project_Dates")
    date_imported = models.DateTimeField(null=True, blank=True, db_column="Date_Imported")
    date_exported = models.DateTimeField(null=True, blank=True, db_column="Date_Exported")
    r_import = models.BooleanField(db_column="Import")
    data_imported_monthlyrep = models.IntegerField(null=True, blank=True, db_column="Data_Imported_MonthlyRep")
    data_imported_opsrep = models.IntegerField(null=True, blank=True, db_column="Data_Imported_OpsRep")
    data_updated_opsrep = models.IntegerField(null=True, blank=True, db_column="Data_Updated_OpsRep")
    data_imported_opsbudget = models.IntegerField(null=True, blank=True, db_column="Data_Imported_OpsBudget")
    data_updated_opsbudget = models.IntegerField(null=True, blank=True, db_column="Data_Updated_OpsBudget")
    data_imported_fininfo = models.IntegerField(null=True, blank=True, db_column="Data_Imported_FinInfo")
    data_updated_fininfo = models.IntegerField(null=True, blank=True, db_column="Data_Updated_FinInfo")
    data_imported_monthlyrepinf = models.IntegerField(null=True, blank=True, db_column="Data_Imported_MonthlyRepInf")
    data_updated_monthlyrepinf = models.IntegerField(null=True, blank=True, db_column="Data_Updated_MonthlyRepInf")
    data_imported_inf_exp = models.IntegerField(null=True, blank=True, db_column="Data_Imported_Inf_Exp")
    data_updated_inf_exp = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Inf_Exp")
    data_imported_sucocycle = models.IntegerField(null=True, blank=True, db_column="Data_Imported_SucoCycle")
    data_updated_suco_cycle = models.IntegerField(null=True, blank=True, db_column="Data_Updated_Suco_Cycle")
    data_imported_projoutput = models.IntegerField(null=True, blank=True, db_column="Data_Imported_ProjOutput")
    data_updated_projoutput = models.IntegerField(null=True, blank=True, db_column="Data_Updated_ProjOutput")


class ImportToSQL(models.Model):
    """
    Originally sourced from ImportToSQL in /home/josh/PNDS_Interim_MIS-Data.accdb (1 records)
    """

    class Meta:
        db_table = "importtosql"

    id = models.IntegerField(primary_key=True, db_column="ID")
    importtosql = models.BooleanField(db_column="ImportToSQL")


class SubprojectPhysicalProgress(models.Model):
    """
    Originally sourced from Subproject_Physical_Progress in /home/josh/PNDS_Interim_MIS-Data.accdb (25395 records)
    """

    class Meta:
        db_table = "subproject_physical_progress"

    id = models.IntegerField(primary_key=True, db_column="ID")
    subprojectid = models.CharField(max_length=1024, null=True, blank=True, db_column="SubprojectID")
    progress_period = models.DateTimeField(null=True, blank=True, db_column="Progress_Period")
    progress_date = models.DateTimeField(null=True, blank=True, db_column="Progress_Date")
    physical_progress = models.FloatField(db_column="Physical_Progress")
    numberofdaysworked = models.IntegerField(null=True, blank=True, db_column="NumberOfDaysWorked")
    labour_female = models.IntegerField(null=True, blank=True, db_column="Labour_Female")
    labour_male = models.IntegerField(null=True, blank=True, db_column="Labour_Male")
    labour_poor = models.IntegerField(null=True, blank=True, db_column="Labour_Poor")
    labour_disabled = models.IntegerField(null=True, blank=True, db_column="Labour_Disabled")
    picture_path = models.CharField(max_length=1024, null=True, blank=True, db_column="Picture_Path")
    remarks = models.CharField(max_length=1024, null=True, blank=True, db_column="Remarks")
    record_creationdate = models.DateTimeField(null=True, blank=True, db_column="Record_CreationDate")
    record_changedate = models.DateTimeField(null=True, blank=True, db_column="Record_ChangeDate")
    physical_progress_id = models.CharField(max_length=1024, null=True, blank=True, db_column="Physical_Progress_ID")


class Sucosubprojectadditonalinfo(models.Model):
    """
    Originally sourced from Suco_subproject_additonal_info in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """

    class Meta:
        db_table = "suco_subproject_additonal_info"

    id = models.IntegerField(primary_key=True, db_column="ID")
    district_name = models.CharField(max_length=1024, null=True, blank=True, db_column="District_name")
    subdistrict_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Subdistrict_name")
    suco_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_Name")
    project_number = models.IntegerField(null=True, blank=True, db_column="Project_Number")
    sector = models.CharField(max_length=1024, null=True, blank=True, db_column="Sector")
    subproject_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Subproject_Name")
    subproject_description = models.CharField(max_length=1024, null=True, blank=True, db_column="Subproject_Description")
    mof_finance_code = models.CharField(max_length=1024, null=True, blank=True, db_column="MOF_Finance_code")
    subproject_materials_budget = models.IntegerField(null=True, blank=True, db_column="Subproject_Materials_budget")
    subproject_labour_budget = models.IntegerField(null=True, blank=True, db_column="Subproject_Labour_budget")
    subproject_start_date = models.CharField(max_length=1024, null=True, blank=True, db_column="Subproject_Start_Date")
    subproject_finish_date = models.CharField(max_length=1024, null=True, blank=True, db_column="Subproject_Finish_Date")
    verified_y_n = models.CharField(max_length=1024, null=True, blank=True, db_column="Verified (Y/N)")
    date_of_verification = models.CharField(max_length=1024, null=True, blank=True, db_column="Date_of_Verification")
    subproject_aldea = models.CharField(max_length=1024, null=True, blank=True, db_column="Subproject_Aldea")
    no_of_women_benefic = models.CharField(max_length=1024, null=True, blank=True, db_column="No_of_ Women_Benefic")
    no_of_men_benefic = models.CharField(max_length=1024, null=True, blank=True, db_column="No_of_Men_Benefic")
    no_of_household_benefic = models.CharField(max_length=1024, null=True, blank=True, db_column="No_of_Household_Benefic")
    main_activity_units = models.CharField(max_length=1024, null=True, blank=True, db_column="Main_activity_units")
    main_activity_unit_type = models.CharField(max_length=1024, null=True, blank=True, db_column="Main_activity_unit_type")
    uniqueval = models.CharField(max_length=1024, null=True, blank=True)


class Validmonthlyreports(models.Model):
    """
    Originally sourced from Valid_monthly_reports in /home/josh/PNDS_Interim_MIS-Data.accdb (61 records)
    """

    class Meta:
        db_table = "valid_monthly_reports"

    vmr_id = models.IntegerField(primary_key=True, db_column="VMR_ID")
    vmr_date = models.DateTimeField(null=True, blank=True, db_column="VMR_Date")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_change_date = models.DateTimeField(null=True, blank=True, db_column="Record_change_date")


class zFinanceMonitors(models.Model):
    """
    Originally sourced from zFinance_Monitors in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zfinance_monitors"

    f_mon_id = models.IntegerField(primary_key=True, db_column="F_Mon_ID")
    f_monitor_name = models.CharField(max_length=1024, null=True, blank=True, db_column="F_Monitor_Name")
    active = models.BooleanField(db_column="Active")
    deactivated_date = models.DateTimeField(null=True, blank=True, db_column="Deactivated_date")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    english = models.CharField(max_length=1024, null=True, blank=True, db_column="English")
    tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="Tetum")
    indonesian = models.CharField(max_length=1024, null=True, blank=True, db_column="Indonesian")


class zOperationBudgetStatus(models.Model):
    """
    Originally sourced from zOperationBudget_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    class Meta:
        db_table = "zoperationbudget_status"

    operationbudget_statusid = models.IntegerField(primary_key=True, db_column="OperationBudget_StatusID")
    operationbudget_status = models.CharField(max_length=1024, null=True, blank=True, db_column="OperationBudget_Status")
    operationbudget_status_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="OperationBudget_Status_Tetum")


class zReportformat(models.Model):
    """
    Originally sourced from zReport_format in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    class Meta:
        db_table = "zreport_format"

    id = models.IntegerField(primary_key=True, db_column="ID")
    format_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Format_name")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zSubdistrictPhase(models.Model):
    """
    Originally sourced from zSubdistrict_Phase in /home/josh/PNDS_Interim_MIS-Data.accdb (104 records)
    """

    class Meta:
        db_table = "zsubdistrict_phase"

    subdistrictphaseid = models.IntegerField(primary_key=True, db_column="SubdistrictPhaseID")
    sudistrictid = models.IntegerField(null=True, blank=True, db_column="SudistrictID")
    phaseid = models.IntegerField(null=True, blank=True, db_column="PhaseID")
    cycleid = models.IntegerField(null=True, blank=True, db_column="CycleID")


class zTransmetafields(models.Model):
    """
    Originally sourced from zTrans_meta_fields in /home/josh/PNDS_Interim_MIS-Data.accdb (548 records)
    """

    class Meta:
        db_table = "ztrans_meta_fields"

    id = models.IntegerField(primary_key=True, db_column="ID")
    table_id = models.IntegerField(null=True, blank=True, db_column="Table_ID")
    field_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Field_Name")
    load_at_dili = models.BooleanField(db_column="Load_at_DILI")
    load_at_district = models.BooleanField(db_column="Load_at_DISTRICT")
    extract_at_dili = models.BooleanField(db_column="Extract_at_DILI")
    extract_at_district = models.BooleanField(db_column="Extract_at_district")
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)
    creation = models.BooleanField()
    change = models.BooleanField()
    r_pk = models.BooleanField(db_column="PK")
    fk = models.BooleanField(db_column="FK")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zDistrict(models.Model):
    """
    Originally sourced from zDistrict in /home/josh/PNDS_Interim_MIS-Data.accdb (14 records)
    """

    class Meta:
        db_table = "zdistrict"

    distict_id = models.IntegerField(primary_key=True, db_column="Distict_ID")
    district_name = models.CharField(max_length=1024, null=True, blank=True, db_column="District_name")
    district_code = models.CharField(max_length=1024, null=True, blank=True, db_column="District_Code")
    mof_district_code = models.CharField(max_length=1024, null=True, blank=True, db_column="MOF_District_code")
    pcode = models.CharField(max_length=1024, null=True, blank=True, db_column="PCODE")
    post_id_number = models.CharField(max_length=1024, null=True, blank=True, db_column="POST_ID_number")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")


class zSubdistrict(models.Model):
    """
    Originally sourced from zSubdistrict in /home/josh/PNDS_Interim_MIS-Data.accdb (67 records)
    """

    class Meta:
        db_table = "zsubdistrict"

    subdistrict_id = models.IntegerField(primary_key=True, db_column="Subdistrict_ID")
    subdistrict_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Subdistrict_name")
    subdistrict_name_jdr = models.CharField(max_length=1024, null=True, blank=True, db_column="Subdistrict_Name_JDR")
    subdistrict_name_arch = models.CharField(max_length=1024, null=True, blank=True, db_column="Subdistrict_name_arch")
    subdistrict_code = models.CharField(max_length=1024, null=True, blank=True, db_column="Subdistrict_Code")
    district_id = models.IntegerField(null=True, blank=True, db_column="District_ID")
    mof_subdistrict_code = models.CharField(max_length=1024, null=True, blank=True, db_column="MOF_Subdistrict_code")
    mof_district_code = models.CharField(max_length=1024, null=True, blank=True, db_column="MOF_District_code")
    subdistrict_pcode = models.CharField(max_length=1024, null=True, blank=True, db_column="Subdistrict_PCODE")
    district_pcode = models.CharField(max_length=1024, null=True, blank=True, db_column="District_PCODE")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    sd_population_total = models.IntegerField(null=True, blank=True, db_column="SD_population_total")
    sd_population_households = models.IntegerField(null=True, blank=True, db_column="SD_population_households")
    sd_population_women = models.IntegerField(null=True, blank=True, db_column="SD_population_women")
    sd_population_men = models.IntegerField(null=True, blank=True, db_column="SD_population_men")
    sd_population_children = models.IntegerField(null=True, blank=True, db_column="SD_population_children")


class zSuco(models.Model):
    """
    Originally sourced from zSuco in /home/josh/PNDS_Interim_MIS-Data.accdb (452 records)
    """

    class Meta:
        db_table = "zsuco"

    suco_id = models.IntegerField(primary_key=True, db_column="Suco_ID")
    suco_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_Name")
    suco_name_jdr = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_Name_JDR")
    suco_name_arch = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_name_arch")
    suco_code = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_Code")
    subdistrict_id = models.IntegerField(null=True, blank=True, db_column="SubDistrict_ID")
    suco_mof_finance_code = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_MOF_Finance_Code")
    operational_bank_account_no = models.CharField(max_length=1024, null=True, blank=True, db_column="Operational_Bank_account_no")
    infrastructure_bank_account_no = models.CharField(max_length=1024, null=True, blank=True, db_column="Infrastructure_Bank_account_no")
    mof_suco_code = models.CharField(max_length=1024, null=True, blank=True, db_column="MOF_suco_code")
    mof_subdistrict_code = models.CharField(max_length=1024, null=True, blank=True, db_column="MOF_Subdistrict_code")
    suco_phase = models.IntegerField(null=True, blank=True, db_column="Suco_phase")
    infrastructure_budget_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Infrastructure_budget_ceiling")
    operations_budget_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, db_column="Operations_budget_ceiling")
    suco_pcode = models.CharField(max_length=1024, null=True, blank=True, db_column="Suco_PCODE")
    subdistrict_pcode = models.CharField(max_length=1024, null=True, blank=True, db_column="Subdistrict_PCODE")
    alternate_spelling1 = models.CharField(max_length=1024, null=True, blank=True, db_column="Alternate_spelling1")
    record_creation_date = models.DateTimeField(null=True, blank=True, db_column="Record_creation_date")
    record_changed_date = models.DateTimeField(null=True, blank=True, db_column="Record_changed_date")
    bank_name = models.CharField(max_length=1024, null=True, blank=True, db_column="Bank_Name")
    bank_branch = models.CharField(max_length=1024, null=True, blank=True, db_column="Bank_Branch")
    zsuco_status = models.IntegerField(null=True, blank=True, db_column="zSuco_Status")
    remarks = models.CharField(max_length=1024, null=True, blank=True, db_column="Remarks")
    grant_agreement_startdate = models.DateTimeField(null=True, blank=True, db_column="Grant_Agreement_StartDate")
    grant_agreement_finishdate = models.DateTimeField(null=True, blank=True, db_column="Grant_Agreement_FinishDate")
    suco_population_total = models.IntegerField(null=True, blank=True, db_column="Suco_population_total")
    suco_population_households = models.IntegerField(null=True, blank=True, db_column="Suco_population_households")
    suco_population_women = models.IntegerField(null=True, blank=True, db_column="Suco_population_women")
    suco_population_men = models.IntegerField(null=True, blank=True, db_column="Suco_population_men")
    suco_population_children = models.IntegerField(null=True, blank=True, db_column="Suco_population_children")


class SucoFundingSources(models.Model):
    """
    Originally sourced from SucoFundingSources in /home/josh/PNDS_Interim_MIS-Data.accdb (1524 records)
    """

    class Meta:
        db_table = "sucofundingsources"

    sucofundingsourceid = models.CharField(max_length=1024, primary_key=True, db_column="SucoFundingSourceID")
    suco_cycleid = models.IntegerField(null=True, blank=True, db_column="Suco_CycleID")
    fundingsourceid = models.IntegerField(null=True, blank=True, db_column="FundingSourceID")
    fundingamount = models.IntegerField(null=True, blank=True, db_column="FundingAmount")


class zFundingSources(models.Model):
    """
    Originally sourced from zFundingSources in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zfundingsources"

    fundingsourceid = models.IntegerField(primary_key=True, db_column="FundingSourceID")
    fundingsourceabbreviation = models.CharField(max_length=1024, null=True, blank=True, db_column="FundingSourceAbbreviation")
    fundingsource = models.CharField(max_length=1024, null=True, blank=True, db_column="FundingSource")
    fundingsource_tetum = models.CharField(max_length=1024, null=True, blank=True, db_column="FundingSource_Tetum")


