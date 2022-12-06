from datetime import date, datetime
from decimal import Decimal


from pydantic import BaseModel, Field



class ActivityBlackListedIn(BaseModel):
    """
    Originally sourced from Activity_BlackListed in /home/josh/PNDS_Interim_MIS-Data.accdb (13 records)
    """

    blacklistid: int = Field(None, alias="BlacklistID")
    sectorid: int = Field(None, alias="SectorID")
    activityid: int = Field(None, alias="ActivityID")
    outputid: int = Field(None, alias="OutputID")
    date_blacklisted: datetime = Field(None, alias="Date_Blacklisted")
    reason_blacklisted: str = Field(None, alias="Reason_Blacklisted")
    source: str = Field(None, alias="Source")


class DataSyncLogTempIn(BaseModel):
    """
    Originally sourced from Data_Sync_Log_Temp in /home/josh/PNDS_Interim_MIS-Data.accdb (14 records)
    """

    id: int = Field(None, alias="ID")
    districtid: int = Field(None, alias="DistrictID")
    data_imported: int = Field(None, alias="Data_Imported")
    data_updated: int = Field(None, alias="Data_Updated")
    data_imported_priorities: int = Field(None, alias="Data_Imported_Priorities")
    data_updated_priorities: int = Field(None, alias="Data_Updated_Priorities")
    data_imported_progress: int = Field(None, alias="Data_Imported_Progress")
    data_updated_progress: int = Field(None, alias="Data_Updated_Progress")
    data_imported_project: int = Field(None, alias="Data_Imported_Project")
    data_updated_project: int = Field(None, alias="Data_Updated_Project")
    data_updated_project_dates: int = Field(None, alias="Data_Updated_Project_Dates")
    data_imported_mrops: int = Field(None, alias="Data_Imported_MROPS")
    data_imported_opsrep: int = Field(None, alias="Data_Imported_OPSRep")
    data_updated_opsrep: int = Field(None, alias="Data_Updated_OPSRep")
    data_imported_opsbudget: int = Field(None, alias="Data_Imported_OPSBudget")
    data_updated_opsbudget: int = Field(None, alias="Data_Updated_OPSBudget")
    data_imported_fininfo: int = Field(None, alias="Data_Imported_FinInfo")
    data_updated_fininfo: int = Field(None, alias="Data_Updated_FinInfo")
    data_imported_mrinf: int = Field(None, alias="Data_Imported_MRINF")
    data_updated_mrinf: int = Field(None, alias="Data_Updated_MRINF")
    data_imported_infrep: int = Field(None, alias="Data_Imported_INFRep")
    data_updated_infrep: int = Field(None, alias="Data_Updated_INFRep")
    data_imported_sucocycle: int = Field(None, alias="Data_Imported_SucoCycle")
    data_updated_sucocycle: int = Field(None, alias="Data_Updated_SucoCycle")
    data_imported_projoutput: int = Field(None, alias="Data_Imported_ProjOutput")
    data_updated_projoutput: int = Field(None, alias="Data_Updated_ProjOutput")
    date_imported: datetime = Field(None, alias="Date_Imported")
    date_exported: datetime = Field(None, alias="Date_Exported")
    r_import: bool = Field(alias="Import")
    data_inserted_district: int = Field(None, alias="Data_Inserted_District")
    data_updated_district: int = Field(None, alias="Data_Updated_District")
    data_inserted_cmt: int = Field(None, alias="Data_Inserted_CMT")
    data_updated_cmt: int = Field(None, alias="Data_Updated_CMT")


class DocumentsandpicturesIn(BaseModel):
    """
    Originally sourced from Documents_and_pictures in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    id: str = Field(None, alias="ID")
    document_file_type_id: int = Field(None, alias="Document_file_type_id")
    document_type_id: int = Field(None, alias="Document_type_id")
    document_upload_date: datetime = Field(None)
    fk_reference: str = Field(None, alias="FK_reference")
    page_number: int = Field(None, alias="Page_number")
    system_post_id: str = Field(None, alias="System_Post_ID")
    file_creation_date: datetime = Field(None, alias="File_creation_date")
    record_creation_date: datetime = Field(None)
    record_changed_date: datetime = Field(None)
    active: bool = Field(alias="Active")
    deactivated_date: datetime = Field(None)
    transmission_id: str = Field(None, alias="Transmission_ID")
    gps_coords: str = Field(None)
    gps_direction: str = Field(None)
    table_name: str = Field(None, alias="Table_name")


class FinanceMonitoringIn(BaseModel):
    """
    Originally sourced from Finance_Monitoring in /home/josh/PNDS_Interim_MIS-Data.accdb (906 records)
    """

    fm_id: str = Field(None, alias="FM_ID")
    suco_id: int = Field(None, alias="Suco_id")
    date_of_assessment: datetime = Field(None, alias="Date_of_assessment")
    criteria_1: int = Field(None, alias="Criteria_1")
    criteria_2: int = Field(None, alias="Criteria_2")
    criteria_3: int = Field(None, alias="Criteria_3")
    criteria_4: int = Field(None, alias="Criteria_4")
    criteria_5: int = Field(None, alias="Criteria_5")
    criteria_6: int = Field(None, alias="Criteria_6")
    criteria_7: int = Field(None, alias="Criteria_7")
    criteria_8: int = Field(None, alias="Criteria_8")
    criteria_9: int = Field(None, alias="Criteria_9")
    criteria_10: int = Field(None, alias="Criteria_10")
    f_mon_id: int = Field(None, alias="F_Mon_ID")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)
    system_post_id: int = Field(None, alias="System_post_id")
    active: bool = Field(alias="Active")
    comments: str = Field(None, alias="Comments")


class FreebalancetranslationcodesIn(BaseModel):
    """
    Originally sourced from Freebalance_translation_codes in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    id: int = Field(None, alias="ID")
    pnds_budget_code: str = Field(None, alias="PNDS_budget_code")
    freebalance_budget_code: str = Field(None, alias="FreeBalance_budget_code")
    active: bool = Field(alias="Active")
    deactivated_date: datetime = Field(None, alias="Deactivated_date")


class GoogleTransfersIn(BaseModel):
    """
    Originally sourced from Google_Transfers in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    transmission_id: int = Field(None, alias="Transmission_ID")
    post_id: str = Field(None, alias="Post_id")
    unique_id: str = Field(None, alias="Unique_ID")
    transfer_date_time: datetime = Field(None, alias="Transfer_date_time")
    transfer_direction: str = Field(None, alias="Transfer_direction")
    transfer_filename: str = Field(None, alias="Transfer_filename")


class MonthlyreportsIn(BaseModel):
    """
    Originally sourced from Monthly_reports in /home/josh/PNDS_Interim_MIS-Data.accdb (41928 records)
    """

    monthly_report_id: str = Field(None, alias="Monthly_Report_ID")
    suco_id: int = Field(None, alias="Suco_ID")
    system_post_id: int = Field(None, alias="System_post_id")
    reporting_period: datetime = Field(None, alias="Reporting_Period")
    fin_ops_report_complete: bool = Field(alias="Fin_ops_report_complete")
    fin_inf_reports_complete: bool = Field(alias="Fin_inf_reports_complete")
    tecnical_report_complete: bool = Field(alias="Tecnical_report_complete")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)
    incoming_funding_inf: int = Field(None, alias="Incoming_funding_inf")
    cash_on_hand_inf: int = Field(None, alias="Cash_on_hand_inf")
    bank_balance_inf: int = Field(None, alias="Bank_Balance_inf")
    verified_inf: bool = Field(alias="Verified_inf")
    active: bool = Field(alias="Active")
    deactivated_date: datetime = Field(None, alias="Deactivated_Date")
    report_date: datetime = Field(None, alias="Report_date")
    verified: bool = Field(alias="Verified")
    transmitted: bool = Field(alias="Transmitted")
    transmission_id: str = Field(None, alias="Transmission_ID")
    locked: bool = Field(alias="Locked")
    operationbudgetid: int = Field(None, alias="OperationBudgetID")
    suco_cycleid: int = Field(None, alias="Suco_CycleID")


class MonthlyreportsInfrastructureIn(BaseModel):
    """
    Originally sourced from Monthly_reports_Infrastructure in /home/josh/PNDS_Interim_MIS-Data.accdb (29260 records)
    """

    monthly_report_id: str = Field(None, alias="Monthly_Report_ID")
    suco_id: int = Field(None, alias="Suco_ID")
    system_post_id: int = Field(None, alias="System_post_id")
    reporting_period: datetime = Field(None, alias="Reporting_Period")
    fin_ops_report_complete: bool = Field(alias="Fin_ops_report_complete")
    fin_inf_reports_complete: bool = Field(alias="Fin_inf_reports_complete")
    tecnical_report_complete: bool = Field(alias="Tecnical_report_complete")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)
    incoming_funding_inf: int = Field(None, alias="Incoming_funding_inf")
    cash_on_hand_inf: int = Field(None, alias="Cash_on_hand_inf")
    bank_balance_inf: int = Field(None, alias="Bank_Balance_inf")
    verified_inf: bool = Field(alias="Verified_inf")
    active: bool = Field(alias="Active")
    deactivated_date: datetime = Field(None, alias="Deactivated_Date")
    report_date: datetime = Field(None, alias="Report_date")
    verified: bool = Field(alias="Verified")
    transmitted: bool = Field(alias="Transmitted")
    transmission_id: str = Field(None, alias="Transmission_ID")
    locked: bool = Field(alias="Locked")
    operationbudgetid: int = Field(None, alias="OperationBudgetID")
    suco_cycleid: int = Field(None, alias="Suco_CycleID")
    brought_forward: Decimal = Field(None, alias="Brought_Forward")


class zCMTPositionsIn(BaseModel):
    """
    Originally sourced from zCMTPositions in /home/josh/PNDS_Interim_MIS-Data.accdb (12 records)
    """

    cmtpositionid: int = Field(None, alias="CMTPositionID")
    cmtposition: str = Field(None, alias="CMTPosition")
    cmtposition_tetum: str = Field(None, alias="CMTPosition_Tetum")
    recordcreationdate: datetime = Field(None, alias="RecordCreationDate")
    recordchangedate: datetime = Field(None, alias="RecordChangeDate")
    positionrank: int = Field(None, alias="PositionRank")


class OperationBudgetIn(BaseModel):
    """
    Originally sourced from OperationBudget in /home/josh/PNDS_Interim_MIS-Data.accdb (3731 records)
    """

    operationbudgetid: int = Field(alias="OperationBudgetID")
    suco_id: int = Field(None, alias="Suco_ID")
    grant_year: str = Field(None, alias="Grant_Year")
    grant_amount: Decimal = Field(None, alias="Grant_Amount")
    expenditure: Decimal = Field(None, alias="Expenditure")
    carry_forward: Decimal = Field(None, alias="Carry_Forward")
    brought_forward_bank: Decimal = Field(None, alias="Brought_Forward_Bank")
    brought_forward_cash: Decimal = Field(None, alias="Brought_Forward_Cash")
    grant_ceiling: Decimal = Field(None, alias="Grant_Ceiling")
    operationbudget_statusid: int = Field(None, alias="OperationBudget_StatusID")
    record_creationdate: datetime = Field(None, alias="Record_CreationDate")
    record_changedate: datetime = Field(None, alias="Record_ChangeDate")


class PhaseCycleIn(BaseModel):
    """
    Originally sourced from PhaseCycle in /home/josh/PNDS_Interim_MIS-Data.accdb (38 records)
    """

    phasecycleid: int = Field(None, alias="PhaseCycleID")
    phaseid: int = Field(None, alias="PhaseID")
    cycleid: int = Field(None, alias="CycleID")
    targetdate: datetime = Field(None, alias="TargetDate")
    targetvalue: str = Field(None, alias="TargetValue")
    remarks: str = Field(None, alias="Remarks")


class SubprojectOutputsIn(BaseModel):
    """
    Originally sourced from SubpojectOutputs in /home/josh/PNDS_Interim_MIS-Data.accdb (7995 records)
    """

    subprojectoutputid: str = Field(None, alias="SubprojectOutputID")
    sectorid: int = Field(None, alias="SectorID")
    outputid: int = Field(None, alias="OutputID")
    activityid: int = Field(None, alias="ActivityID")
    unitid: int = Field(None, alias="UnitID")
    value1: float = Field(None, alias="Value1")
    value1_actual: float = Field(None, alias="Value1_Actual")
    unitid2: int = Field(None, alias="UnitID2")
    value2: int = Field(None, alias="Value2")
    value2_actual: int = Field(None, alias="Value2_Actual")
    suco_subproject_id: str = Field(None, alias="Suco_SubProject_ID")
    ismain: bool = Field(alias="IsMain")
    sub_sectorid: int = Field(None, alias="Sub_SectorID")
    record_creationdate: datetime = Field(None, alias="Record_CreationDate")
    record_changedate: datetime = Field(None, alias="Record_ChangeDate")


class SucoActvitiesIn(BaseModel):
    """
    Originally sourced from Suco_Actvities in /home/josh/PNDS_Interim_MIS-Data.accdb (37104 records)
    """

    id: str = Field(None, alias="ID")
    suco_id: int = Field(None, alias="Suco_ID")
    system_post_id: int = Field(None, alias="System_post_id")
    attendance_male: int = Field(None, alias="Attendance_Male")
    attendance_female: int = Field(None, alias="Attendance_Female")
    date_completed: datetime = Field(None, alias="Date_completed")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)
    zproject_activity_id: int = Field(None, alias="zProject_Activity_id")
    fd_type_id: int = Field(None, alias="FD_type_ID")
    active: bool = Field(alias="Active")
    kpa_male: int = Field(None, alias="KPA_Male")
    kpa_female: int = Field(None, alias="KPA_Female")
    aldea_id: int = Field(None, alias="Aldea_ID")
    district_id: int = Field(None, alias="District_ID")
    sd_id: int = Field(None, alias="SD_ID")
    subdistrictphaseid: int = Field(None, alias="SubdistrictPhaseID")
    suco_cycleid: int = Field(None, alias="Suco_CycleID")
    districtphaseid: int = Field(None, alias="DistrictPhaseID")
    disable_male: int = Field(None, alias="Disable_Male")
    disable_female: int = Field(None, alias="Disable_Female")
    disable_kpa_male: int = Field(None, alias="Disable_KPA_Male")
    disable_kpa_female: int = Field(None, alias="Disable_KPA_Female")
    community_member_male: int = Field(None, alias="Community_Member_Male")
    community_member_female: int = Field(None, alias="Community_Member_Female")


class SucoCyclesIn(BaseModel):
    """
    Originally sourced from Suco_Cycles in /home/josh/PNDS_Interim_MIS-Data.accdb (3924 records)
    """

    suco_cycleid: int = Field(alias="Suco_CycleID")
    suco_id: int = Field(None, alias="Suco_ID")
    infrastructure_budget_ceiling: Decimal = Field(None, alias="Infrastructure_budget_ceiling")
    operations_budget_ceiling: Decimal = Field(None, alias="Operations_budget_ceiling")
    record_creationdate: datetime = Field(None, alias="Record_CreationDate")
    record_changedate: datetime = Field(None, alias="Record_ChangeDate")
    cyclestatusid: int = Field(None, alias="CycleStatusID")
    cyclestatusdate: datetime = Field(None, alias="CycleStatusDate")
    expenditure: Decimal = Field(None, alias="Expenditure")
    carry_forward: Decimal = Field(None, alias="Carry_Forward")
    brought_forward_bank: Decimal = Field(None, alias="Brought_Forward_Bank")
    brought_forward_cash: Decimal = Field(None, alias="Brought_Forward_Cash")
    cycleid: int = Field(None, alias="CycleID")


class SucoFinancialDisbursementsIn(BaseModel):
    """
    Originally sourced from Suco_Financial_Disbursements in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    sfd_id: int = Field(None, alias="SFD_ID")
    system_post_id: int = Field(None, alias="System_post_id")
    suco_id: str = Field(None, alias="Suco_ID")
    fd_type_id: int = Field(None, alias="FD_type_ID")
    program_activity_id: int = Field(None, alias="Program_activity_ID")
    date_of_record: datetime = Field(None, alias="Date_of_record")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)
    active: bool = Field(alias="Active")


class SucoFinancialinfoIn(BaseModel):
    """
    Originally sourced from Suco_Financial_info in /home/josh/PNDS_Interim_MIS-Data.accdb (3948 records)
    """

    suco_financial_info_id: str = Field(None, alias="Suco_Financial_Info_ID")
    suco_id: int = Field(None, alias="Suco_ID")
    system_post_id: int = Field(None, alias="System_post_id")
    project_cycle: int = Field(None, alias="Project_cycle")
    suco_finance_code_inf: str = Field(None, alias="Suco_Finance_Code_Inf")
    cvp_number: str = Field(None, alias="CVP_Number")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)
    active: bool = Field(alias="Active")
    total_community_meeting_budget: Decimal = Field(None, alias="Total_Community_Meeting_budget")
    total_community_training_budget: Decimal = Field(None, alias="Total_Community_Training_budget")
    total_incentive_budget: Decimal = Field(None, alias="Total_Incentive_budget")
    total_admin_budget: Decimal = Field(None, alias="Total_admin_budget")
    total_survey_budget: Decimal = Field(None, alias="Total_survey_budget")
    total_infra_labour_budget: Decimal = Field(None, alias="Total_infra_Labour_budget")
    total_infra_materials_budget: Decimal = Field(None, alias="Total_infra_Materials_budget")
    operationbudgetid: int = Field(None, alias="OperationBudgetID")


class SucoInfrastructureProjectReportIn(BaseModel):
    """
    Originally sourced from Suco_Infrastructure_Project_Report in /home/josh/PNDS_Interim_MIS-Data.accdb (52064 records)
    """

    infrastructure_report_id: str = Field(None, alias="Infrastructure_Report_ID")
    system_post_id: int = Field(None, alias="System_post_id")
    suco_subproject_id: str = Field(None, alias="Suco_Subproject_ID")
    monthly_report_id: str = Field(None, alias="Monthly_report_ID")
    report_month: datetime = Field(None, alias="Report_Month")
    material_spend: Decimal = Field(None, alias="Material_Spend")
    labour_spend: Decimal = Field(None, alias="Labour_Spend")
    percentage_complete: int = Field(None, alias="Percentage_complete")
    mandays_male: int = Field(None, alias="Mandays_Male")
    mandays_female: int = Field(None, alias="Mandays_Female")
    community_contribution: int = Field(None, alias="Community_contribution")
    verified: bool = Field(alias="Verified")
    active: bool = Field(alias="Active")
    deactivated_date: datetime = Field(None, alias="Deactivated_Date")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)
    report_date: datetime = Field(None, alias="Report_Date")
    subproject_guid: str = Field(None, alias="Subproject_GUID")


class SucoOperationalReportIn(BaseModel):
    """
    Originally sourced from Suco_Operational_Report in /home/josh/PNDS_Interim_MIS-Data.accdb (41291 records)
    """

    operational_report_id: str = Field(None, alias="Operational_Report_ID")
    suco_id: int = Field(None, alias="Suco_ID")
    system_post_id: int = Field(None, alias="System_post_id")
    monthly_report_id: str = Field(None, alias="Monthly_report_ID")
    report_month: datetime = Field(None, alias="Report_Month")
    incoming_funding: Decimal = Field(None, alias="Incoming_funding")
    meeting_spend: Decimal = Field(None, alias="Meeting_Spend")
    training_spend: Decimal = Field(None, alias="Training_Spend")
    suco_incentive_spend: Decimal = Field(None, alias="Suco_Incentive_spend")
    administrative_spend: Decimal = Field(None, alias="Administrative_spend")
    survey_design_spend: Decimal = Field(None, alias="Survey_Design_spend")
    cash_on_hand: Decimal = Field(None, alias="Cash_on_hand")
    bank_balance: Decimal = Field(None, alias="Bank_Balance")
    verified: bool = Field(alias="Verified")
    active: bool = Field(alias="Active")
    deactivated_date: datetime = Field(None, alias="Deactivated_Date")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)
    report_date: datetime = Field(None, alias="Report_date")
    report_guid: str = Field(None, alias="Report_GUID")
    finance_approval: bool = Field(alias="Finance_approval")
    operationbudgetid: int = Field(None, alias="OperationBudgetID")
    brought_forward: Decimal = Field(None, alias="Brought_Forward")


class SucoPrioritiesIn(BaseModel):
    """
    Originally sourced from Suco_Priorities in /home/josh/PNDS_Interim_MIS-Data.accdb (11012 records)
    """

    suco_priorityid: str = Field(None, alias="Suco_PriorityID")
    suco_cycleid: int = Field(None, alias="Suco_CycleID")
    prority: int = Field(None, alias="Prority")
    typeof_infra_proposed: str = Field(None, alias="TypeOf_Infra_Proposed")
    locationid: int = Field(None, alias="LocationID")
    volume: str = Field(None, alias="Volume")
    iswoman_priority: bool = Field(alias="IsWoman_Priority")
    estimatedbudget_boq: int = Field(None, alias="EstimatedBudget_BOQ")
    suco_subproject_id: str = Field(None, alias="Suco_Subproject_ID")
    sectorid: int = Field(None, alias="SectorID")
    id: int = Field(None, alias="ID")


class SucoSubProjectIn(BaseModel):
    """
    Originally sourced from Suco_SubProject in /home/josh/PNDS_Interim_MIS-Data.accdb (5053 records)
    """

    suco_subproject_id: str = Field(None, alias="Suco_SubProject_ID")
    suco_id: int = Field(None, alias="Suco_ID")
    system_post_id: int = Field(None, alias="System_post_id")
    project_number: int = Field(None, alias="Project_Number")
    sector_id: int = Field(None, alias="Sector_ID")
    subproject_name: str = Field(None, alias="Subproject_Name")
    subproject_description: str = Field(None, alias="Subproject_Description")
    finance_code: str = Field(None, alias="Finance_code")
    subproject_materials_budget: Decimal = Field(None, alias="Subproject_Materials_budget")
    subproject_labour_budget: Decimal = Field(None, alias="Subproject_Labour_budget")
    subproject_start_date: datetime = Field(None, alias="Subproject_Start_Date")
    subproject_finish_date: datetime = Field(None, alias="Subproject_Finish_Date")
    verified: bool = Field(alias="Verified")
    date_of_verification: datetime = Field(None, alias="Date_of_Verification")
    active: bool = Field(alias="Active")
    subproject_aldea: int = Field(None, alias="Subproject_Aldea")
    no_of_women_benefic: int = Field(None, alias="No_of_ Women_Benefic")
    no_of_men_benefic: int = Field(None, alias="No_of_Men_Benefic")
    no_of_household_benefic: int = Field(None, alias="No_of_Household_Benefic")
    subproject_main_activity_id: int = Field(None, alias="Subproject_Main_Activity_ID")
    main_activity_units: str = Field(None, alias="Main_activity_units")
    main_activity_unit_type: str = Field(None, alias="Main_activity_unit_type")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)
    gps_coords: str = Field(None, alias="GPS_coords")
    finance_approval: bool = Field(alias="Finance_approval")
    settlement_id: int = Field(None, alias="Settlement_id")
    planned_quantity_value: int = Field(None, alias="Planned_Quantity_Value")
    actual_quantity_value: int = Field(None, alias="Actual_Quantity_Value")
    estimated_subproject_cost: Decimal = Field(None, alias="Estimated_SubProject_Cost")
    actual_subproject_cost: Decimal = Field(None, alias="Actual_SubProject_Cost")
    subproject_community_contribution: int = Field(None, alias="Subproject_Community_Contribution")
    subproject_material_budget_actual: Decimal = Field(None, alias="Subproject_Material_Budget_Actual")
    subproject_labour_budget_actual: Decimal = Field(None, alias="Subproject_Labour_Budget_Actual")
    actual_startdate: datetime = Field(None, alias="Actual_StartDate")
    actual_finishdate: datetime = Field(None, alias="Actual_FinishDate")
    iswomen_priority: bool = Field(alias="IsWomen_priority")
    subprojectstatus: int = Field(None, alias="SubprojectStatus")
    subprojectstatusdate: datetime = Field(None, alias="SubprojectStatusDate")
    subproject_delays: str = Field(None, alias="Subproject_Delays")
    subprojectstatusid: int = Field(None, alias="SubprojectStatusID")
    suco_cycleid: int = Field(None, alias="Suco_CycleID")
    project_picture_before: str = Field(None, alias="Project_Picture_Before")
    approval_date: datetime = Field(None, alias="Approval_Date")
    activityid: int = Field(None, alias="ActivityID")
    suco_priorityid: str = Field(None, alias="Suco_PriorityID")
    gps_latitude: int = Field(None, alias="GPS_Latitude")
    gps_longitude: int = Field(None, alias="GPS_Longitude")
    actual_community_contribution: int = Field(None, alias="Actual_Community_Contribution")
    statuschange_reason: str = Field(None, alias="StatusChange_Reason")
    statuschange_date: datetime = Field(None, alias="StatusChange_Date")
    projecttypeid: int = Field(None, alias="ProjectTypeID")
    parentprojectcode: str = Field(None, alias="ParentProjectCode")


class SucoCMTMembersIn(BaseModel):
    """
    Originally sourced from SucoCMTMembers in /home/josh/PNDS_Interim_MIS-Data.accdb (4976 records)
    """

    sucocmtid: str = Field(None, alias="SucoCMTID")
    cmtmembername: str = Field(None, alias="CMTMemberName")
    suco_id: int = Field(alias="Suco_ID")
    telephone: str = Field(None, alias="Telephone")
    genderid: int = Field(None, alias="GenderID")
    disability: bool = Field(alias="Disability")
    cmtpositionid: int = Field(None, alias="CMTPositionID")
    isactivemember: bool = Field(alias="IsActiveMember")
    electionroundid: int = Field(None, alias="ElectionRoundID")
    electiondate: datetime = Field(None, alias="ElectionDate")
    cmtexit: bool = Field(alias="CMTExit")
    dateexitcmt: datetime = Field(None, alias="DateExitCMT")
    comments: str = Field(None, alias="Comments")
    recordcreationdate: datetime = Field(None, alias="RecordCreationDate")
    recordchangedate: str = Field(None, alias="RecordChangeDate")


class syncImportLogIn(BaseModel):
    """
    Originally sourced from syncImportLog in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    id: str = Field(None, alias="ID")
    table_name: str = Field(None, alias="Table_Name")
    type: str = Field(None, alias="Type")
    importdate: datetime = Field(None, alias="ImportDate")


class SystemInfoIn(BaseModel):
    """
    Originally sourced from System_Info in /home/josh/PNDS_Interim_MIS-Data.accdb (1 records)
    """

    system_role: str = Field(None, alias="System_role")
    system_name: str = Field(None, alias="System_name")
    system_table_version: int = Field(None, alias="System_table_version")
    system_last_start_date: datetime = Field(None, alias="System_last_start_date")
    system_post_id_number: str = Field(None, alias="System_post_ID_number")
    system_district_id: int = Field(None, alias="System_district_id")
    system_output_path: str = Field(None, alias="System_output_path")
    system_input_path: str = Field(None, alias="System_input_path")
    system_update_path: str = Field(None, alias="System_update_path")
    system_document_path: str = Field(None, alias="System_document_path")
    system_data_version: int = Field(None, alias="System_data_version")
    system_forms_version: int = Field(None, alias="System_forms_version")
    system_forms_path: str = Field(None, alias="System_forms_path")
    system_log_path: str = Field(None, alias="System_log_path")
    system_backup_script: str = Field(None, alias="System_backup_script")
    system_bit_length: str = Field(None, alias="System_bit_length")
    system_run_once_version: int = Field(None, alias="System_run_once_version")


class SystemlogIn(BaseModel):
    """
    Originally sourced from System_log in /home/josh/PNDS_Interim_MIS-Data.accdb (12353 records)
    """

    id: int = Field(None, alias="ID")
    event_id: str = Field(None, alias="Event_id")
    system_post_id: str = Field(None, alias="System_Post_id")
    event_class: str = Field(None, alias="Event_class")
    event_description: str = Field(None, alias="Event_description")
    event_data: str = Field(None, alias="Event_data")
    user_id: str = Field(None)
    event_date_time: datetime = Field(None, alias="event_Date_time")
    transmission_date_time: datetime = Field(None)


class TransfersIn(BaseModel):
    """
    Originally sourced from Transfers in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    transmission_id: int = Field(None, alias="Transmission_ID")
    post_id: str = Field(None, alias="Post_id")
    unique_id: str = Field(None, alias="Unique_ID")
    transfer_date_time: datetime = Field(None, alias="Transfer_date_time")
    transfer_direction: str = Field(None, alias="Transfer_direction")
    transfer_filename: str = Field(None, alias="Transfer_filename")


class UsersIn(BaseModel):
    """
    Originally sourced from Users in /home/josh/PNDS_Interim_MIS-Data.accdb (61 records)
    """

    id: int = Field(alias="ID")
    email: str = Field(None, alias="Email")
    fullname: str = Field(None, alias="FullName")
    login: str = Field(None, alias="Login")
    password: str = Field(None, alias="Password")
    language: int = Field(None, alias="Language")
    group_id: int = Field(None, alias="Group_id")
    email_notifications: bool = Field(alias="Email_notifications")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_change_date: datetime = Field(None, alias="Record_change_date")
    last_transmission_number: int = Field(None, alias="Last_transmission_number")
    district_id: int = Field(None, alias="District_ID")


class UsersoldIn(BaseModel):
    """
    Originally sourced from Users_old in /home/josh/PNDS_Interim_MIS-Data.accdb (17 records)
    """

    id: int = Field(alias="ID")
    email: str = Field(None, alias="Email")
    fullname: str = Field(None, alias="FullName")
    login: str = Field(None, alias="Login")
    password: str = Field(None, alias="Password")
    language: int = Field(None, alias="Language")
    group_id: int = Field(None, alias="Group_id")
    email_notifications: bool = Field(alias="Email_notifications")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_change_date: datetime = Field(None, alias="Record_change_date")
    last_transmission_number: int = Field(None, alias="Last_transmission_number")
    district_id: int = Field(None, alias="District_ID")


class UserTrackingIn(BaseModel):
    """
    Originally sourced from UserTracking in /home/josh/PNDS_Interim_MIS-Data.accdb (23556 records)
    """

    usertrackingid: str = Field(None, alias="UserTrackingID")
    userid: int = Field(None, alias="UserID")
    datetime_loggedin: datetime = Field(None, alias="DateTime_LoggedIn")
    datetime_loggedout: datetime = Field(None, alias="DateTime_LoggedOut")
    application: str = Field(None, alias="Application")
    versionnumber: str = Field(None, alias="VersionNumber")


class zActivitiesIn(BaseModel):
    """
    Originally sourced from zActivities in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """

    activityid: int = Field(alias="ActivityID")
    activity: str = Field(None, alias="Activity")
    activity_tetum: str = Field(None, alias="Activity_Tetum")
    outputid: int = Field(None, alias="OutputID")


class zActivityDocumenttypeIn(BaseModel):
    """
    Originally sourced from zActivity_Document_type in /home/josh/PNDS_Interim_MIS-Data.accdb (38 records)
    """

    id: int = Field(alias="ID")
    zprogram_activity_id: int = Field(None, alias="zProgram_Activity_ID")
    zdocument_type_id: int = Field(None, alias="zDocument_type_ID")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zActivitytypeIn(BaseModel):
    """
    Originally sourced from zActivity_type in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """

    activity_type_id: int = Field(None, alias="Activity_type_ID")
    activity_type_description: str = Field(None, alias="Activity_type_description")
    units: str = Field(None, alias="Units")
    range: str = Field(None, alias="Range")
    can_be_main: bool = Field(alias="Can_be_main")
    can_be_secondary: bool = Field(alias="Can_be_secondary")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zAldeiaIn(BaseModel):
    """
    Originally sourced from zAldeia in /home/josh/PNDS_Interim_MIS-Data.accdb (2254 records)
    """

    id: int = Field(None, alias="ID")
    aldeia_name: str = Field(None, alias="Aldeia_name")
    aldeia_pcode: str = Field(None, alias="Aldeia_PCODE")
    suco_pcode: str = Field(None, alias="Suco_PCODE")
    suco_id: int = Field(None, alias="Suco_ID")
    gps_coords: str = Field(None, alias="GPS_coords")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    aldea_population_total: int = Field(None, alias="Aldea_population_total")
    aldea_population_households: int = Field(None, alias="Aldea_population_households")
    aldea_population_women: int = Field(None, alias="Aldea_population_women")
    aldea_population_men: int = Field(None, alias="Aldea_population_men")
    aldea_population_children: int = Field(None, alias="Aldea_population_children")


class zCategoriesIn(BaseModel):
    """
    Originally sourced from zCategories in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    categoryid: int = Field(alias="CategoryID")
    category: str = Field(None, alias="Category")
    category_tetum: str = Field(None, alias="Category_Tetum")


class zCMTPositions1In(BaseModel):
    """
    Originally sourced from zCMT_Positions in /home/josh/PNDS_Interim_MIS-Data.accdb (11 records)
    """

    cmt_position_id: int = Field(None, alias="CMT_Position_ID")
    cmt_position_name: str = Field(None, alias="CMT_Position_name")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zCyclesIn(BaseModel):
    """
    Originally sourced from zCycles in /home/josh/PNDS_Interim_MIS-Data.accdb (13 records)
    """

    cycle_id: int = Field(alias="Cycle_ID")
    cycle_name: str = Field(None, alias="Cycle_name")
    cycle_start_date: datetime = Field(None, alias="Cycle_start_date")
    cycle_finish_date: datetime = Field(None, alias="Cycle_finish_date")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zCycleStatusIn(BaseModel):
    """
    Originally sourced from zCycleStatus in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    cyclestatusid: int = Field(alias="CycleStatusID")
    cyclestatus: str = Field(None, alias="CycleStatus")
    cyclestatus_tetum: str = Field(None, alias="CycleStatus_Tetum")


class zDistrictPhaseIn(BaseModel):
    """
    Originally sourced from zDistrict_Phase in /home/josh/PNDS_Interim_MIS-Data.accdb (56 records)
    """

    districtphaseid: int = Field(None, alias="DistrictPhaseID")
    districtid: int = Field(None, alias="DistrictID")
    phaseid: int = Field(None, alias="PhaseID")
    cycleid: int = Field(None, alias="CycleID")


class zDocumentfiletypeIn(BaseModel):
    """
    Originally sourced from zDocument_file_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    id: int = Field(alias="ID")
    document_type: str = Field(None, alias="Document_type")
    valid_extension: str = Field(None, alias="Valid_extension")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zDocumenttypeIn(BaseModel):
    """
    Originally sourced from zDocument_type in /home/josh/PNDS_Interim_MIS-Data.accdb (99 records)
    """

    id: int = Field(alias="ID")
    document_type_name: str = Field(None, alias="Document_type_name")
    monthly_reports: bool = Field(alias="Monthly_reports")
    social_activities: bool = Field()
    finance_activites: bool = Field()
    verification: bool = Field(alias="Verification")
    r_50_report: bool = Field(alias="50%_report")
    completion_report: bool = Field(alias="Completion_report")
    active: bool = Field(alias="Active")
    deacticated_date: datetime = Field(None)
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zElectionRoundIn(BaseModel):
    """
    Originally sourced from zElectionRound in /home/josh/PNDS_Interim_MIS-Data.accdb (5 records)
    """

    electionroundid: int = Field(None, alias="ElectionRoundID")
    electionroundtype: str = Field(None, alias="ElectionRoundType")
    electionround_tetum: str = Field(None, alias="ElectionRound_Tetum")
    recordcreationdate: datetime = Field(None, alias="RecordCreationDate")
    recordchangedate: datetime = Field(None, alias="RecordChangeDate")


class zFinancedisbursementrulesIn(BaseModel):
    """
    Originally sourced from zFinance_disbursement_rules in /home/josh/PNDS_Interim_MIS-Data.accdb (23 records)
    """

    id: int = Field(alias="ID")
    fd_type_id: int = Field(None, alias="FD_type_id")
    program_activity_id: int = Field(None, alias="Program_activity_id")
    order: int = Field(None, alias="Order")
    active: bool = Field(alias="Active")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None)


class zFinancedisbursementtypeIn(BaseModel):
    """
    Originally sourced from zFinance_disbursement_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    fbt_id: int = Field(alias="FBT_ID")
    fbd_type: str = Field(None, alias="FBD_type")
    active: bool = Field()
    fdb_order_number: int = Field(None, alias="FDB_order_number")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zFinancialdisbursementactitvitesIn(BaseModel):
    """
    Originally sourced from zFinancial_disbursement_actitvites in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """

    fda_id: int = Field(None, alias="FDA_ID")
    activity_order: int = Field(None, alias="Activity_order")
    activity_name: str = Field(None, alias="Activity_Name")
    active: bool = Field()
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zFreebalanceBudgetextractIn(BaseModel):
    """
    Originally sourced from zFreebalance_Budget_extract in /home/josh/PNDS_Interim_MIS-Data.accdb (3666 records)
    """

    id: int = Field(None, alias="ID")
    import_id: str = Field(None)
    allocateddomestic: str = Field(None, alias="allocatedDomestic")
    allocatedforeign: str = Field(None, alias="allocatedForeign")
    allowtoexceed: str = Field(None, alias="allowToExceed")
    annualforecastdomestic: str = Field(None, alias="annualForecastDomestic")
    annualforecastforeign: str = Field(None, alias="annualForecastForeign")
    approvaldate: str = Field(None, alias="approvalDate")
    checkcontrolamount: str = Field(None, alias="checkControlAmount")
    checkcontrolpercentage: str = Field(None, alias="checkControlPercentage")
    commitmentsdomestic: str = Field(None, alias="commitmentsDomestic")
    commitmentsforeign: str = Field(None, alias="commitmentsForeign")
    creationdate: str = Field(None, alias="creationDate")
    currentamountdomestic: str = Field(None, alias="currentAmountDomestic")
    currentamountforeign: str = Field(None, alias="currentAmountForeign")
    exchangerate: str = Field(None, alias="exchangeRate")
    freebalancedomestic: str = Field(None, alias="freeBalanceDomestic")
    freebalanceforeign: str = Field(None, alias="freeBalanceForeign")
    indicativecommitmentsdomestic: str = Field(None, alias="indicativeCommitmentsDomestic")
    indicativecommitmentsforeign: str = Field(None, alias="indicativeCommitmentsForeign")
    isactive: str = Field(None, alias="isActive")
    isbasedonaccumulatedperiodamount: str = Field(None, alias="isBasedOnAccumulatedPeriodAmount")
    isbudgetdistributioncontrol: str = Field(None, alias="isBudgetDistributionControl")
    isvalidatedbyforeigncurrency: str = Field(None, alias="isValidatedByForeignCurrency")
    obligationsdomestic: str = Field(None, alias="obligationsDomestic")
    obligationsforeign: str = Field(None, alias="obligationsForeign")
    origin: str = Field(None)
    originalamountdomestic: int = Field(None, alias="originalAmountDomestic")
    originalamountforeign: str = Field(None, alias="originalAmountForeign")
    paiddomestic: str = Field(None, alias="paidDomestic")
    paidforeign: str = Field(None, alias="paidForeign")
    surplusdeficitdomestic: str = Field(None, alias="surplusDeficitDomestic")
    surplusdeficitforeign: str = Field(None, alias="surplusDeficitForeign")
    toleranceamount: str = Field(None, alias="toleranceAmount")
    tolerancepercentage: str = Field(None, alias="tolerancePercentage")
    transfersdomestic: str = Field(None, alias="transfersDomestic")
    transfersforeign: str = Field(None, alias="transfersForeign")
    unallocateddomestic: str = Field(None, alias="unallocatedDomestic")
    unallocatedforeign: str = Field(None, alias="unallocatedForeign")
    updatesdomestic: str = Field(None, alias="updatesDomestic")
    updatesforeign: str = Field(None, alias="updatesForeign")
    ytdactualdomestic: str = Field(None, alias="ytdActualDomestic")
    ytdactualforeign: str = Field(None, alias="ytdActualForeign")
    approvedbyapplicationid: str = Field(None, alias="approvedByapplicationId")
    budgetcontroltypeapplicationid: str = Field(None, alias="budgetControlTypeapplicationId")
    budgetofficeapplicationid: str = Field(None, alias="budgetOfficeapplicationId")
    codingblockstringcode: str = Field(None, alias="codingBlockstringCode")
    codingblockcoagroupcoaapplicationid: str = Field(None, alias="codingBlockcoaGroupcoaapplicationId")
    codingblockcoagroupcode: str = Field(None, alias="codingBlockcoaGroupcode")
    createdbyapplicationid: str = Field(None, alias="createdByapplicationId")
    currencyapplicationid: str = Field(None, alias="currencyapplicationId")
    fiscalyearapplicationid: str = Field(None, alias="fiscalYearapplicationId")
    record_creation_date: datetime = Field(None)
    record_export_date: datetime = Field(None)
    export_number: int = Field(None)
    suco_id: int = Field(None, alias="Suco_ID")
    order: int = Field(None)
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zGenderIn(BaseModel):
    """
    Originally sourced from zGender in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    genderid: int = Field(alias="GenderID")
    gender_english: str = Field(None, alias="Gender_English")
    gender_tetum: str = Field(None, alias="Gender_Tetum")


class zGroupsIn(BaseModel):
    """
    Originally sourced from zGroups in /home/josh/PNDS_Interim_MIS-Data.accdb (8 records)
    """

    id: int = Field(alias="ID")
    group_name: str = Field(None, alias="Group_name")
    finance_functions: bool = Field(alias="Finance_functions")
    admin_functions: bool = Field(alias="Admin_functions")
    reporting_functions: bool = Field(alias="Reporting_functions")
    mis_functions: bool = Field(alias="MIS_functions")
    complaints_functions: bool = Field(alias="Complaints_functions")
    data_fix_functions: bool = Field(alias="Data_fix_functions")
    social_functions: bool = Field(alias="Social_functions")
    field_team_data: bool = Field(alias="Field_team_data")
    field_team_approval: bool = Field(alias="Field_team_approval")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_change_date: datetime = Field(None, alias="Record_change_date")
    last_transmission_number: int = Field(None, alias="Last_transmission_number")
    finance_edit: bool = Field(alias="Finance_edit")
    social_edit: bool = Field(alias="Social_edit")
    subproject_edit: bool = Field(alias="Subproject_edit")
    suco_budgeting_edit: bool = Field(alias="Suco_budgeting_edit")
    finance_monitoring_edit: bool = Field(alias="Finance_monitoring_edit")
    complaints_edit: bool = Field(alias="Complaints_edit")
    reports_edit: bool = Field(alias="Reports_edit")
    unverify_report: bool = Field(alias="Unverify_report")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    district_admin: bool = Field(alias="District_admin")


class zIndicatorsIn(BaseModel):
    """
    Originally sourced from zIndicators in /home/josh/PNDS_Interim_MIS-Data.accdb (10 records)
    """

    indicatorid: int = Field(None, alias="IndicatorID")
    categoryid: int = Field(None, alias="CategoryID")
    indicator: str = Field(None, alias="Indicator")
    indicator_tetum: str = Field(None, alias="Indicator_Tetum")


class zLanguageIn(BaseModel):
    """
    Originally sourced from zLanguage in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    id: int = Field(alias="ID")
    language_name: str = Field(None, alias="Language_Name")
    language_default: bool = Field(alias="Language_default")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zLastIDIn(BaseModel):
    """
    Originally sourced from zLastID in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    tablename: str = Field(None, alias="TableName")
    lastid: int = Field(None, alias="LastID")


class zOutputsIn(BaseModel):
    """
    Originally sourced from zOutputs in /home/josh/PNDS_Interim_MIS-Data.accdb (123 records)
    """

    outputid: int = Field(alias="OutputID")
    output: str = Field(None, alias="Output")
    output_tetum: str = Field(None, alias="Output_Tetum")
    sectorid: int = Field(None, alias="SectorID")
    sub_sectorid: int = Field(None, alias="Sub_SectorID")


class zOutputUnitIn(BaseModel):
    """
    Originally sourced from zOutputUnit in /home/josh/PNDS_Interim_MIS-Data.accdb (117 records)
    """

    outputunitid: int = Field(None, alias="OutputUnitID")
    outputid: int = Field(None, alias="OutputID")
    unitid: int = Field(None, alias="UnitID")
    minimum_value: int = Field(None, alias="Minimum_Value")
    maximum_value: int = Field(None, alias="Maximum_Value")


class zPNDSFreebalancetranslationIn(BaseModel):
    """
    Originally sourced from zPNDS_Freebalance_translation in /home/josh/PNDS_Interim_MIS-Data.accdb (9 records)
    """

    id: int = Field(None, alias="ID")
    acct_no: int = Field(None, alias="Acct_No")
    description: str = Field(None, alias="Description")
    freebalance_line_item_budget: int = Field(None, alias="FreeBalance_Line_Item_budget")
    freebalance_line_item_monthly_exp: int = Field(None, alias="Freebalance_line_item_monthly_exp")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zPrioritiesIn(BaseModel):
    """
    Originally sourced from zPriorities in /home/josh/PNDS_Interim_MIS-Data.accdb (50 records)
    """

    priorityid: int = Field(None, alias="PriorityID")
    priority: int = Field(None, alias="Priority")


class zProgramActivityIn(BaseModel):
    """
    Originally sourced from zProgram_Activity in /home/josh/PNDS_Interim_MIS-Data.accdb (39 records)
    """

    program_activity_id: int = Field(alias="Program_activity_ID")
    activity_name: str = Field(None, alias="Activity_Name")
    social_activity_number: int = Field(None, alias="Social_Activity_number")
    finance_activity_number: int = Field(None, alias="Finance_Activity_number")
    program_activity_number: int = Field(None, alias="Program_activity_number")
    finance_activity: bool = Field(alias="Finance_activity")
    social_activity: bool = Field(alias="Social_activity")
    program_activity: bool = Field(alias="Program_activity")
    technical_activity: bool = Field(alias="Technical_Activity")
    active: bool = Field(alias="Active")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    aldea_activity: bool = Field(alias="Aldea_activity")
    zprogram_activity_level_id: int = Field(None, alias="zProgram_Activity_level_ID")
    zprogram_activity_type_id: int = Field(None, alias="zProgram_Activity_type_ID")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zProgramActivitylevelIn(BaseModel):
    """
    Originally sourced from zProgram_Activity_level in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    program_activity_level_id: int = Field(alias="Program_Activity_level_ID")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_change_date: datetime = Field(None, alias="Record_change_date")


class zProgramactivtytypeIn(BaseModel):
    """
    Originally sourced from zProgram_activty_type in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    program_activtiy_type_id: int = Field(alias="Program_activtiy_type_ID")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_change_date: datetime = Field(None, alias="Record_change_date")


class zReporttypeIn(BaseModel):
    """
    Originally sourced from zReport_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    report_type_id: int = Field(alias="Report_type_ID")
    report_type_name: str = Field(None, alias="Report_type_name")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zSectorIn(BaseModel):
    """
    Originally sourced from zSector in /home/josh/PNDS_Interim_MIS-Data.accdb (8 records)
    """

    sector_id: int = Field(alias="Sector_ID")
    sector_name: str = Field(None, alias="Sector_Name")
    icon_name: str = Field(None)
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zSectorActvityIn(BaseModel):
    """
    Originally sourced from zSector_Actvity in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """

    id: int = Field(alias="ID")
    active: bool = Field(alias="Active")
    sector_id: int = Field(None, alias="Sector_ID")
    activity_type_id: int = Field(None, alias="Activity_Type_ID")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zSettlementsIn(BaseModel):
    """
    Originally sourced from zSettlements in /home/josh/PNDS_Interim_MIS-Data.accdb (2829 records)
    """

    id: int = Field(None, alias="ID")
    set_name: str = Field(None, alias="Set_Name")
    suco_pcode: str = Field(None, alias="Suco_PCODE")
    suco_id: int = Field(None, alias="Suco_ID")
    gps_coords: str = Field(None, alias="GPS_Coords")
    set_pcode: str = Field(None, alias="Set_PCODE")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zSubSectorIn(BaseModel):
    """
    Originally sourced from zSub_Sector in /home/josh/PNDS_Interim_MIS-Data.accdb (23 records)
    """

    sub_sectorid: int = Field(alias="Sub_SectorID")
    sub_sector: str = Field(None, alias="Sub_Sector")
    sub_sector_tetum: str = Field(None, alias="Sub_Sector_Tetum")
    sector_id: int = Field(None, alias="Sector_ID")


class zSubprojectStatusIn(BaseModel):
    """
    Originally sourced from zSubproject_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    status_id: int = Field(alias="Status_ID")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_change_date: datetime = Field(None, alias="Record_change_date")


class zSubprojectStatus1In(BaseModel):
    """
    Originally sourced from zSubprojectStatus in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """

    subprojectstatusid: int = Field(alias="SubprojectStatusID")
    subprojectstatus: str = Field(None, alias="SubprojectStatus")
    subprojectstatus_tetum: str = Field(None, alias="SubprojectStatus_Tetum")


class zSucophaseIn(BaseModel):
    """
    Originally sourced from zSuco_phase in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    id: int = Field(alias="ID")
    phase: str = Field(None, alias="Phase")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zSucoStatusIn(BaseModel):
    """
    Originally sourced from zSuco_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    suco_status_id: int = Field(alias="Suco_Status_ID")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_change_date: datetime = Field(None, alias="Record_change_date")


class zTetumtranslationIn(BaseModel):
    """
    Originally sourced from zTetum_translation in /home/josh/PNDS_Interim_MIS-Data.accdb (606 records)
    """

    id: int = Field(None, alias="ID")
    type_data: bool = Field(alias="Type_Data")
    type_label: bool = Field(alias="Type_Label")
    type_error: bool = Field(alias="Type_error")
    english_word: str = Field(None, alias="English_word")
    tetum_word: str = Field(None, alias="Tetum_word")
    indonesian_word: str = Field(None, alias="Indonesian_word")
    long_number: int = Field(None, alias="Long_number")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zTetumtranslationOLDIn(BaseModel):
    """
    Originally sourced from zTetum_translation_OLD in /home/josh/PNDS_Interim_MIS-Data.accdb (569 records)
    """

    id: int = Field(None, alias="ID")
    type_data: bool = Field(alias="Type_Data")
    type_label: bool = Field(alias="Type_Label")
    type_error: bool = Field(alias="Type_error")
    english_word: str = Field(None, alias="English_word")
    tetum_word: str = Field(None, alias="Tetum_word")
    indonesian_word: str = Field(None, alias="Indonesian_word")
    long_number: int = Field(None, alias="Long_number")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zTransMetatablesIn(BaseModel):
    """
    Originally sourced from zTrans_Meta_tables in /home/josh/PNDS_Interim_MIS-Data.accdb (50 records)
    """

    id: int = Field(None, alias="ID")
    table_name: str = Field(None, alias="Table_name")
    transfer_table_name: str = Field(None, alias="Transfer_table_name")
    audit_table_name: str = Field(None, alias="Audit_table_name")
    trans_dili_to_district: bool = Field(alias="Trans_DILI_to_District")
    trans_district_to_dili: bool = Field(alias="Trans_DISTRICT_to_DILI")
    requires_verified: bool = Field(alias="Requires_verified")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zUnitsIn(BaseModel):
    """
    Originally sourced from zUnits in /home/josh/PNDS_Interim_MIS-Data.accdb (9 records)
    """

    unitid: int = Field(alias="UnitID")
    unit_tetum: str = Field(None, alias="Unit_Tetum")
    description: str = Field(None, alias="Description")
    unit: str = Field(None, alias="Unit")


class zYearsIn(BaseModel):
    """
    Originally sourced from zYears in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    id: int = Field(None, alias="ID")
    year_of_operation: str = Field(None, alias="Year_of_operation")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class DataSyncLogIn(BaseModel):
    """
    Originally sourced from Data_Sync_Log in /home/josh/PNDS_Interim_MIS-Data.accdb (4375 records)
    """

    id: int = Field(None, alias="ID")
    districtid: int = Field(None, alias="DistrictID")
    data_imported: int = Field(None, alias="Data_Imported")
    data_updated: int = Field(None, alias="Data_Updated")
    data_imported_priorities: int = Field(None, alias="Data_Imported_Priorities")
    data_updated_priorities: int = Field(None, alias="Data_Updated_Priorities")
    data_imported_progress: int = Field(None, alias="Data_Imported_Progress")
    data_updated_progress: int = Field(None, alias="Data_Updated_Progress")
    data_imported_project: int = Field(None, alias="Data_Imported_Project")
    data_updated_project: int = Field(None, alias="Data_Updated_Project")
    data_updated_project_dates: int = Field(None, alias="Data_Updated_Project_Dates")
    date_imported: datetime = Field(None, alias="Date_Imported")
    date_exported: datetime = Field(None, alias="Date_Exported")
    r_import: bool = Field(alias="Import")
    data_imported_monthlyrep: int = Field(None, alias="Data_Imported_MonthlyRep")
    data_imported_opsrep: int = Field(None, alias="Data_Imported_OpsRep")
    data_updated_opsrep: int = Field(None, alias="Data_Updated_OpsRep")
    data_imported_opsbudget: int = Field(None, alias="Data_Imported_OpsBudget")
    data_updated_opsbudget: int = Field(None, alias="Data_Updated_OpsBudget")
    data_imported_fininfo: int = Field(None, alias="Data_Imported_FinInfo")
    data_updated_fininfo: int = Field(None, alias="Data_Updated_FinInfo")
    data_imported_monthlyrepinf: int = Field(None, alias="Data_Imported_MonthlyRepInf")
    data_updated_monthlyrepinf: int = Field(None, alias="Data_Updated_MonthlyRepInf")
    data_imported_inf_exp: int = Field(None, alias="Data_Imported_Inf_Exp")
    data_updated_inf_exp: int = Field(None, alias="Data_Updated_Inf_Exp")
    data_imported_sucocycle: int = Field(None, alias="Data_Imported_SucoCycle")
    data_updated_suco_cycle: int = Field(None, alias="Data_Updated_Suco_Cycle")
    data_imported_projoutput: int = Field(None, alias="Data_Imported_ProjOutput")
    data_updated_projoutput: int = Field(None, alias="Data_Updated_ProjOutput")


class ImportToSQLIn(BaseModel):
    """
    Originally sourced from ImportToSQL in /home/josh/PNDS_Interim_MIS-Data.accdb (1 records)
    """

    id: int = Field(None, alias="ID")
    importtosql: bool = Field(alias="ImportToSQL")


class SubprojectPhysicalProgressIn(BaseModel):
    """
    Originally sourced from Subproject_Physical_Progress in /home/josh/PNDS_Interim_MIS-Data.accdb (25395 records)
    """

    id: int = Field(None, alias="ID")
    subprojectid: str = Field(None, alias="SubprojectID")
    progress_period: datetime = Field(None, alias="Progress_Period")
    progress_date: datetime = Field(None, alias="Progress_Date")
    physical_progress: float = Field(alias="Physical_Progress")
    numberofdaysworked: int = Field(None, alias="NumberOfDaysWorked")
    labour_female: int = Field(None, alias="Labour_Female")
    labour_male: int = Field(None, alias="Labour_Male")
    labour_poor: int = Field(None, alias="Labour_Poor")
    labour_disabled: int = Field(None, alias="Labour_Disabled")
    picture_path: str = Field(None, alias="Picture_Path")
    remarks: str = Field(None, alias="Remarks")
    record_creationdate: datetime = Field(None, alias="Record_CreationDate")
    record_changedate: datetime = Field(None, alias="Record_ChangeDate")
    physical_progress_id: str = Field(None, alias="Physical_Progress_ID")


class SucosubprojectadditonalinfoIn(BaseModel):
    """
    Originally sourced from Suco_subproject_additonal_info in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """

    id: int = Field(None, alias="ID")
    district_name: str = Field(None, alias="District_name")
    subdistrict_name: str = Field(None, alias="Subdistrict_name")
    suco_name: str = Field(None, alias="Suco_Name")
    project_number: int = Field(None, alias="Project_Number")
    sector: str = Field(None, alias="Sector")
    subproject_name: str = Field(None, alias="Subproject_Name")
    subproject_description: str = Field(None, alias="Subproject_Description")
    mof_finance_code: str = Field(None, alias="MOF_Finance_code")
    subproject_materials_budget: int = Field(None, alias="Subproject_Materials_budget")
    subproject_labour_budget: int = Field(None, alias="Subproject_Labour_budget")
    subproject_start_date: str = Field(None, alias="Subproject_Start_Date")
    subproject_finish_date: str = Field(None, alias="Subproject_Finish_Date")
    verified_y_n: str = Field(None, alias="Verified (Y/N)")
    date_of_verification: str = Field(None, alias="Date_of_Verification")
    subproject_aldea: str = Field(None, alias="Subproject_Aldea")
    no_of_women_benefic: str = Field(None, alias="No_of_ Women_Benefic")
    no_of_men_benefic: str = Field(None, alias="No_of_Men_Benefic")
    no_of_household_benefic: str = Field(None, alias="No_of_Household_Benefic")
    main_activity_units: str = Field(None, alias="Main_activity_units")
    main_activity_unit_type: str = Field(None, alias="Main_activity_unit_type")
    uniqueval: str = Field(None)


class ValidmonthlyreportsIn(BaseModel):
    """
    Originally sourced from Valid_monthly_reports in /home/josh/PNDS_Interim_MIS-Data.accdb (61 records)
    """

    vmr_id: int = Field(alias="VMR_ID")
    vmr_date: datetime = Field(None, alias="VMR_Date")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_change_date: datetime = Field(None, alias="Record_change_date")


class zFinanceMonitorsIn(BaseModel):
    """
    Originally sourced from zFinance_Monitors in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    f_mon_id: int = Field(alias="F_Mon_ID")
    f_monitor_name: str = Field(None, alias="F_Monitor_Name")
    active: bool = Field(alias="Active")
    deactivated_date: datetime = Field(None, alias="Deactivated_date")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    english: str = Field(None, alias="English")
    tetum: str = Field(None, alias="Tetum")
    indonesian: str = Field(None, alias="Indonesian")


class zOperationBudgetStatusIn(BaseModel):
    """
    Originally sourced from zOperationBudget_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    operationbudget_statusid: int = Field(alias="OperationBudget_StatusID")
    operationbudget_status: str = Field(None, alias="OperationBudget_Status")
    operationbudget_status_tetum: str = Field(None, alias="OperationBudget_Status_Tetum")


class zReportformatIn(BaseModel):
    """
    Originally sourced from zReport_format in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    id: int = Field(alias="ID")
    format_name: str = Field(None, alias="Format_name")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zSubdistrictPhaseIn(BaseModel):
    """
    Originally sourced from zSubdistrict_Phase in /home/josh/PNDS_Interim_MIS-Data.accdb (104 records)
    """

    subdistrictphaseid: int = Field(None, alias="SubdistrictPhaseID")
    sudistrictid: int = Field(None, alias="SudistrictID")
    phaseid: int = Field(None, alias="PhaseID")
    cycleid: int = Field(None, alias="CycleID")


class zTransmetafieldsIn(BaseModel):
    """
    Originally sourced from zTrans_meta_fields in /home/josh/PNDS_Interim_MIS-Data.accdb (548 records)
    """

    id: int = Field(None, alias="ID")
    table_id: int = Field(None, alias="Table_ID")
    field_name: str = Field(None, alias="Field_Name")
    load_at_dili: bool = Field(alias="Load_at_DILI")
    load_at_district: bool = Field(alias="Load_at_DISTRICT")
    extract_at_dili: bool = Field(alias="Extract_at_DILI")
    extract_at_district: bool = Field(alias="Extract_at_district")
    record_creation_date: datetime = Field(None)
    record_change_date: datetime = Field(None)
    creation: bool = Field()
    change: bool = Field()
    r_pk: bool = Field(alias="PK")
    fk: bool = Field(alias="FK")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zDistrictIn(BaseModel):
    """
    Originally sourced from zDistrict in /home/josh/PNDS_Interim_MIS-Data.accdb (14 records)
    """

    distict_id: int = Field(alias="Distict_ID")
    district_name: str = Field(None, alias="District_name")
    district_code: str = Field(None, alias="District_Code")
    mof_district_code: str = Field(None, alias="MOF_District_code")
    pcode: str = Field(None, alias="PCODE")
    post_id_number: str = Field(None, alias="POST_ID_number")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")


class zSubdistrictIn(BaseModel):
    """
    Originally sourced from zSubdistrict in /home/josh/PNDS_Interim_MIS-Data.accdb (67 records)
    """

    subdistrict_id: int = Field(alias="Subdistrict_ID")
    subdistrict_name: str = Field(None, alias="Subdistrict_name")
    subdistrict_name_jdr: str = Field(None, alias="Subdistrict_Name_JDR")
    subdistrict_name_arch: str = Field(None, alias="Subdistrict_name_arch")
    subdistrict_code: str = Field(None, alias="Subdistrict_Code")
    district_id: int = Field(None, alias="District_ID")
    mof_subdistrict_code: str = Field(None, alias="MOF_Subdistrict_code")
    mof_district_code: str = Field(None, alias="MOF_District_code")
    subdistrict_pcode: str = Field(None, alias="Subdistrict_PCODE")
    district_pcode: str = Field(None, alias="District_PCODE")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    sd_population_total: int = Field(None, alias="SD_population_total")
    sd_population_households: int = Field(None, alias="SD_population_households")
    sd_population_women: int = Field(None, alias="SD_population_women")
    sd_population_men: int = Field(None, alias="SD_population_men")
    sd_population_children: int = Field(None, alias="SD_population_children")


class zSucoIn(BaseModel):
    """
    Originally sourced from zSuco in /home/josh/PNDS_Interim_MIS-Data.accdb (452 records)
    """

    suco_id: int = Field(alias="Suco_ID")
    suco_name: str = Field(None, alias="Suco_Name")
    suco_name_jdr: str = Field(None, alias="Suco_Name_JDR")
    suco_name_arch: str = Field(None, alias="Suco_name_arch")
    suco_code: str = Field(None, alias="Suco_Code")
    subdistrict_id: int = Field(None, alias="SubDistrict_ID")
    suco_mof_finance_code: str = Field(None, alias="Suco_MOF_Finance_Code")
    operational_bank_account_no: str = Field(None, alias="Operational_Bank_account_no")
    infrastructure_bank_account_no: str = Field(None, alias="Infrastructure_Bank_account_no")
    mof_suco_code: str = Field(None, alias="MOF_suco_code")
    mof_subdistrict_code: str = Field(None, alias="MOF_Subdistrict_code")
    suco_phase: int = Field(None, alias="Suco_phase")
    infrastructure_budget_ceiling: Decimal = Field(None, alias="Infrastructure_budget_ceiling")
    operations_budget_ceiling: Decimal = Field(None, alias="Operations_budget_ceiling")
    suco_pcode: str = Field(None, alias="Suco_PCODE")
    subdistrict_pcode: str = Field(None, alias="Subdistrict_PCODE")
    alternate_spelling1: str = Field(None, alias="Alternate_spelling1")
    record_creation_date: datetime = Field(None, alias="Record_creation_date")
    record_changed_date: datetime = Field(None, alias="Record_changed_date")
    bank_name: str = Field(None, alias="Bank_Name")
    bank_branch: str = Field(None, alias="Bank_Branch")
    zsuco_status: int = Field(None, alias="zSuco_Status")
    remarks: str = Field(None, alias="Remarks")
    grant_agreement_startdate: datetime = Field(None, alias="Grant_Agreement_StartDate")
    grant_agreement_finishdate: datetime = Field(None, alias="Grant_Agreement_FinishDate")
    suco_population_total: int = Field(None, alias="Suco_population_total")
    suco_population_households: int = Field(None, alias="Suco_population_households")
    suco_population_women: int = Field(None, alias="Suco_population_women")
    suco_population_men: int = Field(None, alias="Suco_population_men")
    suco_population_children: int = Field(None, alias="Suco_population_children")


class SucoFundingSourcesIn(BaseModel):
    """
    Originally sourced from SucoFundingSources in /home/josh/PNDS_Interim_MIS-Data.accdb (1524 records)
    """

    sucofundingsourceid: str = Field(None, alias="SucoFundingSourceID")
    suco_cycleid: int = Field(None, alias="Suco_CycleID")
    fundingsourceid: int = Field(None, alias="FundingSourceID")
    fundingamount: int = Field(None, alias="FundingAmount")


class zFundingSourcesIn(BaseModel):
    """
    Originally sourced from zFundingSources in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    fundingsourceid: int = Field(alias="FundingSourceID")
    fundingsourceabbreviation: str = Field(None, alias="FundingSourceAbbreviation")
    fundingsource: str = Field(None, alias="FundingSource")
    fundingsource_tetum: str = Field(None, alias="FundingSource_Tetum")
