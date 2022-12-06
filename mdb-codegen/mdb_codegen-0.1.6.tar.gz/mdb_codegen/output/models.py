from django.db import models

class ActivityBlackListed(models.Model):
    """
    Originally sourced from Activity_BlackListed in /home/josh/PNDS_Interim_MIS-Data.accdb (13 records)
    """

    class Meta:
        db_table = "activity_blacklisted"

    blacklistid = models.IntegerField(primary_key=True)
    sectorid = models.IntegerField(null=True, blank=True)
    activityid = models.IntegerField(null=True, blank=True)
    outputid = models.IntegerField(null=True, blank=True)
    date_blacklisted = models.DateTimeField(null=True, blank=True)
    reason_blacklisted = models.CharField(max_length=1024, null=True, blank=True)
    source = models.CharField(max_length=1024, null=True, blank=True)


class DataSyncLogTemp(models.Model):
    """
    Originally sourced from Data_Sync_Log_Temp in /home/josh/PNDS_Interim_MIS-Data.accdb (14 records)
    """

    class Meta:
        db_table = "data_sync_log_temp"

    id = models.IntegerField(primary_key=True)
    districtid = models.IntegerField(null=True, blank=True)
    data_imported = models.IntegerField(null=True, blank=True)
    data_updated = models.IntegerField(null=True, blank=True)
    data_imported_priorities = models.IntegerField(null=True, blank=True)
    data_updated_priorities = models.IntegerField(null=True, blank=True)
    data_imported_progress = models.IntegerField(null=True, blank=True)
    data_updated_progress = models.IntegerField(null=True, blank=True)
    data_imported_project = models.IntegerField(null=True, blank=True)
    data_updated_project = models.IntegerField(null=True, blank=True)
    data_updated_project_dates = models.IntegerField(null=True, blank=True)
    data_imported_mrops = models.IntegerField(null=True, blank=True)
    data_imported_opsrep = models.IntegerField(null=True, blank=True)
    data_updated_opsrep = models.IntegerField(null=True, blank=True)
    data_imported_opsbudget = models.IntegerField(null=True, blank=True)
    data_updated_opsbudget = models.IntegerField(null=True, blank=True)
    data_imported_fininfo = models.IntegerField(null=True, blank=True)
    data_updated_fininfo = models.IntegerField(null=True, blank=True)
    data_imported_mrinf = models.IntegerField(null=True, blank=True)
    data_updated_mrinf = models.IntegerField(null=True, blank=True)
    data_imported_infrep = models.IntegerField(null=True, blank=True)
    data_updated_infrep = models.IntegerField(null=True, blank=True)
    data_imported_sucocycle = models.IntegerField(null=True, blank=True)
    data_updated_sucocycle = models.IntegerField(null=True, blank=True)
    data_imported_projoutput = models.IntegerField(null=True, blank=True)
    data_updated_projoutput = models.IntegerField(null=True, blank=True)
    date_imported = models.DateTimeField(null=True, blank=True)
    date_exported = models.DateTimeField(null=True, blank=True)
    r_import = models.BooleanField()
    data_inserted_district = models.IntegerField(null=True, blank=True)
    data_updated_district = models.IntegerField(null=True, blank=True)
    data_inserted_cmt = models.IntegerField(null=True, blank=True)
    data_updated_cmt = models.IntegerField(null=True, blank=True)


class Documentsandpictures(models.Model):
    """
    Originally sourced from Documents_and_pictures in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "documents_and_pictures"

    id = models.CharField(max_length=1024, primary_key=True)
    document_file_type_id = models.IntegerField(null=True, blank=True)
    document_type_id = models.IntegerField(null=True, blank=True)
    document_upload_date = models.DateTimeField(null=True, blank=True)
    fk_reference = models.CharField(max_length=1024, null=True, blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    system_post_id = models.CharField(max_length=1024, null=True, blank=True)
    file_creation_date = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField()
    deactivated_date = models.DateTimeField(null=True, blank=True)
    transmission_id = models.CharField(max_length=1024, null=True, blank=True)
    gps_coords = models.CharField(max_length=1024, null=True, blank=True)
    gps_direction = models.CharField(max_length=1024, null=True, blank=True)
    table_name = models.CharField(max_length=1024, null=True, blank=True)


class FinanceMonitoring(models.Model):
    """
    Originally sourced from Finance_Monitoring in /home/josh/PNDS_Interim_MIS-Data.accdb (906 records)
    """

    class Meta:
        db_table = "finance_monitoring"

    fm_id = models.CharField(max_length=1024, primary_key=True)
    suco_id = models.IntegerField(null=True, blank=True)
    date_of_assessment = models.DateTimeField(null=True, blank=True)
    criteria_1 = models.IntegerField(null=True, blank=True)
    criteria_2 = models.IntegerField(null=True, blank=True)
    criteria_3 = models.IntegerField(null=True, blank=True)
    criteria_4 = models.IntegerField(null=True, blank=True)
    criteria_5 = models.IntegerField(null=True, blank=True)
    criteria_6 = models.IntegerField(null=True, blank=True)
    criteria_7 = models.IntegerField(null=True, blank=True)
    criteria_8 = models.IntegerField(null=True, blank=True)
    criteria_9 = models.IntegerField(null=True, blank=True)
    criteria_10 = models.IntegerField(null=True, blank=True)
    f_mon_id = models.IntegerField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    system_post_id = models.IntegerField(null=True, blank=True)
    active = models.BooleanField()
    comments = models.CharField(max_length=1024, null=True, blank=True)


class Freebalancetranslationcodes(models.Model):
    """
    Originally sourced from Freebalance_translation_codes in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    class Meta:
        db_table = "freebalance_translation_codes"

    id = models.IntegerField(primary_key=True)
    pnds_budget_code = models.CharField(max_length=1024, null=True, blank=True)
    freebalance_budget_code = models.CharField(max_length=1024, null=True, blank=True)
    active = models.BooleanField()
    deactivated_date = models.DateTimeField(null=True, blank=True)


class GoogleTransfers(models.Model):
    """
    Originally sourced from Google_Transfers in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "google_transfers"

    transmission_id = models.IntegerField(primary_key=True)
    post_id = models.CharField(max_length=1024, null=True, blank=True)
    unique_id = models.CharField(max_length=1024, null=True, blank=True)
    transfer_date_time = models.DateTimeField(null=True, blank=True)
    transfer_direction = models.CharField(max_length=1024, null=True, blank=True)
    transfer_filename = models.CharField(max_length=1024, null=True, blank=True)


class Monthlyreports(models.Model):
    """
    Originally sourced from Monthly_reports in /home/josh/PNDS_Interim_MIS-Data.accdb (41928 records)
    """

    class Meta:
        db_table = "monthly_reports"

    monthly_report_id = models.CharField(max_length=1024, primary_key=True)
    suco_id = models.IntegerField(null=True, blank=True)
    system_post_id = models.IntegerField(null=True, blank=True)
    reporting_period = models.DateTimeField(null=True, blank=True)
    fin_ops_report_complete = models.BooleanField()
    fin_inf_reports_complete = models.BooleanField()
    tecnical_report_complete = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    incoming_funding_inf = models.IntegerField(null=True, blank=True)
    cash_on_hand_inf = models.IntegerField(null=True, blank=True)
    bank_balance_inf = models.IntegerField(null=True, blank=True)
    verified_inf = models.BooleanField()
    active = models.BooleanField()
    deactivated_date = models.DateTimeField(null=True, blank=True)
    report_date = models.DateTimeField(null=True, blank=True)
    verified = models.BooleanField()
    transmitted = models.BooleanField()
    transmission_id = models.CharField(max_length=1024, null=True, blank=True)
    locked = models.BooleanField()
    operationbudgetid = models.IntegerField(null=True, blank=True)
    suco_cycleid = models.IntegerField(null=True, blank=True)


class MonthlyreportsInfrastructure(models.Model):
    """
    Originally sourced from Monthly_reports_Infrastructure in /home/josh/PNDS_Interim_MIS-Data.accdb (29260 records)
    """

    class Meta:
        db_table = "monthly_reports_infrastructure"

    monthly_report_id = models.CharField(max_length=1024, primary_key=True)
    suco_id = models.IntegerField(null=True, blank=True)
    system_post_id = models.IntegerField(null=True, blank=True)
    reporting_period = models.DateTimeField(null=True, blank=True)
    fin_ops_report_complete = models.BooleanField()
    fin_inf_reports_complete = models.BooleanField()
    tecnical_report_complete = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    incoming_funding_inf = models.IntegerField(null=True, blank=True)
    cash_on_hand_inf = models.IntegerField(null=True, blank=True)
    bank_balance_inf = models.IntegerField(null=True, blank=True)
    verified_inf = models.BooleanField()
    active = models.BooleanField()
    deactivated_date = models.DateTimeField(null=True, blank=True)
    report_date = models.DateTimeField(null=True, blank=True)
    verified = models.BooleanField()
    transmitted = models.BooleanField()
    transmission_id = models.CharField(max_length=1024, null=True, blank=True)
    locked = models.BooleanField()
    operationbudgetid = models.IntegerField(null=True, blank=True)
    suco_cycleid = models.IntegerField(null=True, blank=True)
    brought_forward = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)


class zCMTPositions(models.Model):
    """
    Originally sourced from zCMTPositions in /home/josh/PNDS_Interim_MIS-Data.accdb (12 records)
    """

    class Meta:
        db_table = "zcmtpositions"

    cmtpositionid = models.IntegerField(primary_key=True)
    cmtposition = models.CharField(max_length=1024, null=True, blank=True)
    cmtposition_tetum = models.CharField(max_length=1024, null=True, blank=True)
    recordcreationdate = models.DateTimeField(null=True, blank=True)
    recordchangedate = models.DateTimeField(null=True, blank=True)
    positionrank = models.IntegerField(null=True, blank=True)


class OperationBudget(models.Model):
    """
    Originally sourced from OperationBudget in /home/josh/PNDS_Interim_MIS-Data.accdb (3731 records)
    """

    class Meta:
        db_table = "operationbudget"

    operationbudgetid = models.IntegerField(primary_key=True)
    suco_id = models.IntegerField(null=True, blank=True)
    grant_year = models.CharField(max_length=1024, null=True, blank=True)
    grant_amount = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    expenditure = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    carry_forward = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    brought_forward_bank = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    brought_forward_cash = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    grant_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    operationbudget_statusid = models.IntegerField(null=True, blank=True)
    record_creationdate = models.DateTimeField(null=True, blank=True)
    record_changedate = models.DateTimeField(null=True, blank=True)


class PhaseCycle(models.Model):
    """
    Originally sourced from PhaseCycle in /home/josh/PNDS_Interim_MIS-Data.accdb (38 records)
    """

    class Meta:
        db_table = "phasecycle"

    phasecycleid = models.IntegerField(primary_key=True)
    phaseid = models.IntegerField(null=True, blank=True)
    cycleid = models.IntegerField(null=True, blank=True)
    targetdate = models.DateTimeField(null=True, blank=True)
    targetvalue = models.CharField(max_length=1024, null=True, blank=True)
    remarks = models.CharField(max_length=1024, null=True, blank=True)


class SubprojectOutputs(models.Model):
    """
    Originally sourced from SubpojectOutputs in /home/josh/PNDS_Interim_MIS-Data.accdb (7995 records)
    """

    class Meta:
        db_table = "SubprojectOutputs"

    subprojectoutputid = models.CharField(max_length=1024, primary_key=True)
    sectorid = models.IntegerField(null=True, blank=True)
    outputid = models.IntegerField(null=True, blank=True)
    activityid = models.IntegerField(null=True, blank=True)
    unitid = models.IntegerField(null=True, blank=True)
    value1 = models.FloatField(null=True, blank=True)
    value1_actual = models.FloatField(null=True, blank=True)
    unitid2 = models.IntegerField(null=True, blank=True)
    value2 = models.IntegerField(null=True, blank=True)
    value2_actual = models.IntegerField(null=True, blank=True)
    suco_subproject_id = models.CharField(max_length=1024, null=True, blank=True)
    ismain = models.BooleanField()
    sub_sectorid = models.IntegerField(null=True, blank=True)
    record_creationdate = models.DateTimeField(null=True, blank=True)
    record_changedate = models.DateTimeField(null=True, blank=True)


class SucoActvities(models.Model):
    """
    Originally sourced from Suco_Actvities in /home/josh/PNDS_Interim_MIS-Data.accdb (37104 records)
    """

    class Meta:
        db_table = "suco_actvities"

    id = models.CharField(max_length=1024, primary_key=True)
    suco_id = models.IntegerField(null=True, blank=True)
    system_post_id = models.IntegerField(null=True, blank=True)
    attendance_male = models.IntegerField(null=True, blank=True)
    attendance_female = models.IntegerField(null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    zproject_activity_id = models.IntegerField(null=True, blank=True)
    fd_type_id = models.IntegerField(null=True, blank=True)
    active = models.BooleanField()
    kpa_male = models.IntegerField(null=True, blank=True)
    kpa_female = models.IntegerField(null=True, blank=True)
    aldea_id = models.IntegerField(null=True, blank=True)
    district_id = models.IntegerField(null=True, blank=True)
    sd_id = models.IntegerField(null=True, blank=True)
    subdistrictphaseid = models.IntegerField(null=True, blank=True)
    suco_cycleid = models.IntegerField(null=True, blank=True)
    districtphaseid = models.IntegerField(null=True, blank=True)
    disable_male = models.IntegerField(null=True, blank=True)
    disable_female = models.IntegerField(null=True, blank=True)
    disable_kpa_male = models.IntegerField(null=True, blank=True)
    disable_kpa_female = models.IntegerField(null=True, blank=True)
    community_member_male = models.IntegerField(null=True, blank=True)
    community_member_female = models.IntegerField(null=True, blank=True)


class SucoCycles(models.Model):
    """
    Originally sourced from Suco_Cycles in /home/josh/PNDS_Interim_MIS-Data.accdb (3924 records)
    """

    class Meta:
        db_table = "suco_cycles"

    suco_cycleid = models.IntegerField(primary_key=True)
    suco_id = models.IntegerField(null=True, blank=True)
    infrastructure_budget_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    operations_budget_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    record_creationdate = models.DateTimeField(null=True, blank=True)
    record_changedate = models.DateTimeField(null=True, blank=True)
    cyclestatusid = models.IntegerField(null=True, blank=True)
    cyclestatusdate = models.DateTimeField(null=True, blank=True)
    expenditure = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    carry_forward = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    brought_forward_bank = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    brought_forward_cash = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    cycleid = models.IntegerField(null=True, blank=True)


class SucoFinancialDisbursements(models.Model):
    """
    Originally sourced from Suco_Financial_Disbursements in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    class Meta:
        db_table = "suco_financial_disbursements"

    sfd_id = models.IntegerField(primary_key=True)
    system_post_id = models.IntegerField(null=True, blank=True)
    suco_id = models.CharField(max_length=1024, null=True, blank=True)
    fd_type_id = models.IntegerField(null=True, blank=True)
    program_activity_id = models.IntegerField(null=True, blank=True)
    date_of_record = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField()


class SucoFinancialinfo(models.Model):
    """
    Originally sourced from Suco_Financial_info in /home/josh/PNDS_Interim_MIS-Data.accdb (3948 records)
    """

    class Meta:
        db_table = "suco_financial_info"

    suco_financial_info_id = models.CharField(max_length=1024, primary_key=True)
    suco_id = models.IntegerField(null=True, blank=True)
    system_post_id = models.IntegerField(null=True, blank=True)
    project_cycle = models.IntegerField(null=True, blank=True)
    suco_finance_code_inf = models.CharField(max_length=1024, null=True, blank=True)
    cvp_number = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField()
    total_community_meeting_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_community_training_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_incentive_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_admin_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_survey_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_infra_labour_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    total_infra_materials_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    operationbudgetid = models.IntegerField(null=True, blank=True)


class SucoInfrastructureProjectReport(models.Model):
    """
    Originally sourced from Suco_Infrastructure_Project_Report in /home/josh/PNDS_Interim_MIS-Data.accdb (52064 records)
    """

    class Meta:
        db_table = "suco_infrastructure_project_report"

    infrastructure_report_id = models.CharField(max_length=1024, primary_key=True)
    system_post_id = models.IntegerField(null=True, blank=True)
    suco_subproject_id = models.CharField(max_length=1024, null=True, blank=True)
    monthly_report_id = models.CharField(max_length=1024, null=True, blank=True)
    report_month = models.DateTimeField(null=True, blank=True)
    material_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    labour_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    percentage_complete = models.IntegerField(null=True, blank=True)
    mandays_male = models.IntegerField(null=True, blank=True)
    mandays_female = models.IntegerField(null=True, blank=True)
    community_contribution = models.IntegerField(null=True, blank=True)
    verified = models.BooleanField()
    active = models.BooleanField()
    deactivated_date = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    report_date = models.DateTimeField(null=True, blank=True)
    subproject_guid = models.CharField(max_length=1024, null=True, blank=True)


class SucoOperationalReport(models.Model):
    """
    Originally sourced from Suco_Operational_Report in /home/josh/PNDS_Interim_MIS-Data.accdb (41291 records)
    """

    class Meta:
        db_table = "suco_operational_report"

    operational_report_id = models.CharField(max_length=1024, primary_key=True)
    suco_id = models.IntegerField(null=True, blank=True)
    system_post_id = models.IntegerField(null=True, blank=True)
    monthly_report_id = models.CharField(max_length=1024, null=True, blank=True)
    report_month = models.DateTimeField(null=True, blank=True)
    incoming_funding = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    meeting_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    training_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    suco_incentive_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    administrative_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    survey_design_spend = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    cash_on_hand = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    bank_balance = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    verified = models.BooleanField()
    active = models.BooleanField()
    deactivated_date = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    report_date = models.DateTimeField(null=True, blank=True)
    report_guid = models.CharField(max_length=1024, null=True, blank=True)
    finance_approval = models.BooleanField()
    operationbudgetid = models.IntegerField(null=True, blank=True)
    brought_forward = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)


class SucoPriorities(models.Model):
    """
    Originally sourced from Suco_Priorities in /home/josh/PNDS_Interim_MIS-Data.accdb (11012 records)
    """

    class Meta:
        db_table = "suco_priorities"

    suco_priorityid = models.CharField(max_length=1024, primary_key=True)
    suco_cycleid = models.IntegerField(null=True, blank=True)
    prority = models.IntegerField(null=True, blank=True)
    typeof_infra_proposed = models.CharField(max_length=1024, null=True, blank=True)
    locationid = models.IntegerField(null=True, blank=True)
    volume = models.CharField(max_length=1024, null=True, blank=True)
    iswoman_priority = models.BooleanField()
    estimatedbudget_boq = models.IntegerField(null=True, blank=True)
    suco_subproject_id = models.CharField(max_length=1024, null=True, blank=True)
    sectorid = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(null=True, blank=True)


class SucoSubProject(models.Model):
    """
    Originally sourced from Suco_SubProject in /home/josh/PNDS_Interim_MIS-Data.accdb (5053 records)
    """

    class Meta:
        db_table = "suco_subproject"

    suco_subproject_id = models.CharField(max_length=1024, primary_key=True)
    suco_id = models.IntegerField(null=True, blank=True)
    system_post_id = models.IntegerField(null=True, blank=True)
    project_number = models.IntegerField(null=True, blank=True)
    sector_id = models.IntegerField(null=True, blank=True)
    subproject_name = models.CharField(max_length=1024, null=True, blank=True)
    subproject_description = models.CharField(max_length=1024, null=True, blank=True)
    finance_code = models.CharField(max_length=1024, null=True, blank=True)
    subproject_materials_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    subproject_labour_budget = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    subproject_start_date = models.DateTimeField(null=True, blank=True)
    subproject_finish_date = models.DateTimeField(null=True, blank=True)
    verified = models.BooleanField()
    date_of_verification = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField()
    subproject_aldea = models.IntegerField(null=True, blank=True)
    no_of_women_benefic = models.IntegerField(null=True, blank=True)
    no_of_men_benefic = models.IntegerField(null=True, blank=True)
    no_of_household_benefic = models.IntegerField(null=True, blank=True)
    subproject_main_activity_id = models.IntegerField(null=True, blank=True)
    main_activity_units = models.CharField(max_length=1024, null=True, blank=True)
    main_activity_unit_type = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    gps_coords = models.CharField(max_length=1024, null=True, blank=True)
    finance_approval = models.BooleanField()
    settlement_id = models.IntegerField(null=True, blank=True)
    planned_quantity_value = models.IntegerField(null=True, blank=True)
    actual_quantity_value = models.IntegerField(null=True, blank=True)
    estimated_subproject_cost = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    actual_subproject_cost = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    subproject_community_contribution = models.IntegerField(null=True, blank=True)
    subproject_material_budget_actual = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    subproject_labour_budget_actual = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    actual_startdate = models.DateTimeField(null=True, blank=True)
    actual_finishdate = models.DateTimeField(null=True, blank=True)
    iswomen_priority = models.BooleanField()
    subprojectstatus = models.IntegerField(null=True, blank=True)
    subprojectstatusdate = models.DateTimeField(null=True, blank=True)
    subproject_delays = models.CharField(max_length=1024, null=True, blank=True)
    subprojectstatusid = models.IntegerField(null=True, blank=True)
    suco_cycleid = models.IntegerField(null=True, blank=True)
    project_picture_before = models.CharField(max_length=1024, null=True, blank=True)
    approval_date = models.DateTimeField(null=True, blank=True)
    activityid = models.IntegerField(null=True, blank=True)
    suco_priorityid = models.CharField(max_length=1024, null=True, blank=True)
    gps_latitude = models.IntegerField(null=True, blank=True)
    gps_longitude = models.IntegerField(null=True, blank=True)
    actual_community_contribution = models.IntegerField(null=True, blank=True)
    statuschange_reason = models.CharField(max_length=1024, null=True, blank=True)
    statuschange_date = models.DateTimeField(null=True, blank=True)
    projecttypeid = models.IntegerField(null=True, blank=True)
    parentprojectcode = models.CharField(max_length=1024, null=True, blank=True)


class SucoCMTMembers(models.Model):
    """
    Originally sourced from SucoCMTMembers in /home/josh/PNDS_Interim_MIS-Data.accdb (4976 records)
    """

    class Meta:
        db_table = "sucocmtmembers"

    sucocmtid = models.CharField(max_length=1024, primary_key=True)
    cmtmembername = models.CharField(max_length=1024, null=True, blank=True)
    suco_id = models.IntegerField()
    telephone = models.CharField(max_length=1024, null=True, blank=True)
    genderid = models.IntegerField(null=True, blank=True)
    disability = models.BooleanField()
    cmtpositionid = models.IntegerField(null=True, blank=True)
    isactivemember = models.BooleanField()
    electionroundid = models.IntegerField(null=True, blank=True)
    electiondate = models.DateTimeField(null=True, blank=True)
    cmtexit = models.BooleanField()
    dateexitcmt = models.DateTimeField(null=True, blank=True)
    comments = models.CharField(max_length=1024, null=True, blank=True)
    recordcreationdate = models.DateTimeField(null=True, blank=True)
    recordchangedate = models.CharField(max_length=1024, null=True, blank=True)


class syncImportLog(models.Model):
    """
    Originally sourced from syncImportLog in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    class Meta:
        db_table = "syncimportlog"

    id = models.CharField(max_length=1024, primary_key=True)
    table_name = models.CharField(max_length=1024, null=True, blank=True)
    type = models.CharField(max_length=1024, null=True, blank=True)
    importdate = models.DateTimeField(null=True, blank=True)


class SystemInfo(models.Model):
    """
    Originally sourced from System_Info in /home/josh/PNDS_Interim_MIS-Data.accdb (1 records)
    """

    class Meta:
        db_table = "system_info"

    system_role = models.CharField(max_length=1024, primary_key=True)
    system_name = models.CharField(max_length=1024, null=True, blank=True)
    system_table_version = models.IntegerField(null=True, blank=True)
    system_last_start_date = models.DateTimeField(null=True, blank=True)
    system_post_id_number = models.CharField(max_length=1024, null=True, blank=True)
    system_district_id = models.IntegerField(null=True, blank=True)
    system_output_path = models.CharField(max_length=1024, null=True, blank=True)
    system_input_path = models.CharField(max_length=1024, null=True, blank=True)
    system_update_path = models.CharField(max_length=1024, null=True, blank=True)
    system_document_path = models.CharField(max_length=1024, null=True, blank=True)
    system_data_version = models.IntegerField(null=True, blank=True)
    system_forms_version = models.IntegerField(null=True, blank=True)
    system_forms_path = models.CharField(max_length=1024, null=True, blank=True)
    system_log_path = models.CharField(max_length=1024, null=True, blank=True)
    system_backup_script = models.CharField(max_length=1024, null=True, blank=True)
    system_bit_length = models.CharField(max_length=1024, null=True, blank=True)
    system_run_once_version = models.IntegerField(null=True, blank=True)


class Systemlog(models.Model):
    """
    Originally sourced from System_log in /home/josh/PNDS_Interim_MIS-Data.accdb (12353 records)
    """

    class Meta:
        db_table = "system_log"

    id = models.IntegerField(primary_key=True)
    event_id = models.CharField(max_length=1024, null=True, blank=True)
    system_post_id = models.CharField(max_length=1024, null=True, blank=True)
    event_class = models.CharField(max_length=1024, null=True, blank=True)
    event_description = models.CharField(max_length=1024, null=True, blank=True)
    event_data = models.CharField(max_length=1024, null=True, blank=True)
    user_id = models.CharField(max_length=1024, null=True, blank=True)
    event_date_time = models.DateTimeField(null=True, blank=True)
    transmission_date_time = models.DateTimeField(null=True, blank=True)


class Transfers(models.Model):
    """
    Originally sourced from Transfers in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """

    class Meta:
        db_table = "transfers"

    transmission_id = models.IntegerField(primary_key=True)
    post_id = models.CharField(max_length=1024, null=True, blank=True)
    unique_id = models.CharField(max_length=1024, null=True, blank=True)
    transfer_date_time = models.DateTimeField(null=True, blank=True)
    transfer_direction = models.CharField(max_length=1024, null=True, blank=True)
    transfer_filename = models.CharField(max_length=1024, null=True, blank=True)


class Users(models.Model):
    """
    Originally sourced from Users in /home/josh/PNDS_Interim_MIS-Data.accdb (61 records)
    """

    class Meta:
        db_table = "users"

    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=1024, null=True, blank=True)
    fullname = models.CharField(max_length=1024, null=True, blank=True)
    login = models.CharField(max_length=1024, null=True, blank=True)
    password = models.CharField(max_length=1024, null=True, blank=True)
    language = models.IntegerField(null=True, blank=True)
    group_id = models.IntegerField(null=True, blank=True)
    email_notifications = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)
    last_transmission_number = models.IntegerField(null=True, blank=True)
    district_id = models.IntegerField(null=True, blank=True)


class Usersold(models.Model):
    """
    Originally sourced from Users_old in /home/josh/PNDS_Interim_MIS-Data.accdb (17 records)
    """

    class Meta:
        db_table = "users_old"

    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=1024, null=True, blank=True)
    fullname = models.CharField(max_length=1024, null=True, blank=True)
    login = models.CharField(max_length=1024, null=True, blank=True)
    password = models.CharField(max_length=1024, null=True, blank=True)
    language = models.IntegerField(null=True, blank=True)
    group_id = models.IntegerField(null=True, blank=True)
    email_notifications = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)
    last_transmission_number = models.IntegerField(null=True, blank=True)
    district_id = models.IntegerField(null=True, blank=True)


class UserTracking(models.Model):
    """
    Originally sourced from UserTracking in /home/josh/PNDS_Interim_MIS-Data.accdb (23556 records)
    """

    class Meta:
        db_table = "usertracking"

    usertrackingid = models.CharField(max_length=1024, primary_key=True)
    userid = models.IntegerField(null=True, blank=True)
    datetime_loggedin = models.DateTimeField(null=True, blank=True)
    datetime_loggedout = models.DateTimeField(null=True, blank=True)
    application = models.CharField(max_length=1024, null=True, blank=True)
    versionnumber = models.CharField(max_length=1024, null=True, blank=True)


class zActivities(models.Model):
    """
    Originally sourced from zActivities in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """

    class Meta:
        db_table = "zactivities"

    activityid = models.IntegerField(primary_key=True)
    activity = models.CharField(max_length=1024, null=True, blank=True)
    activity_tetum = models.CharField(max_length=1024, null=True, blank=True)
    outputid = models.IntegerField(null=True, blank=True)


class zActivityDocumenttype(models.Model):
    """
    Originally sourced from zActivity_Document_type in /home/josh/PNDS_Interim_MIS-Data.accdb (38 records)
    """

    class Meta:
        db_table = "zactivity_document_type"

    id = models.IntegerField(primary_key=True)
    zprogram_activity_id = models.IntegerField(null=True, blank=True)
    zdocument_type_id = models.IntegerField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zActivitytype(models.Model):
    """
    Originally sourced from zActivity_type in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """

    class Meta:
        db_table = "zactivity_type"

    activity_type_id = models.IntegerField(primary_key=True)
    activity_type_description = models.CharField(max_length=1024, null=True, blank=True)
    units = models.CharField(max_length=1024, null=True, blank=True)
    range = models.CharField(max_length=1024, null=True, blank=True)
    can_be_main = models.BooleanField()
    can_be_secondary = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zAldeia(models.Model):
    """
    Originally sourced from zAldeia in /home/josh/PNDS_Interim_MIS-Data.accdb (2254 records)
    """

    class Meta:
        db_table = "zaldeia"

    id = models.IntegerField(primary_key=True)
    aldeia_name = models.CharField(max_length=1024, null=True, blank=True)
    aldeia_pcode = models.CharField(max_length=1024, null=True, blank=True)
    suco_pcode = models.CharField(max_length=1024, null=True, blank=True)
    suco_id = models.IntegerField(null=True, blank=True)
    gps_coords = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    aldea_population_total = models.IntegerField(null=True, blank=True)
    aldea_population_households = models.IntegerField(null=True, blank=True)
    aldea_population_women = models.IntegerField(null=True, blank=True)
    aldea_population_men = models.IntegerField(null=True, blank=True)
    aldea_population_children = models.IntegerField(null=True, blank=True)


class zCategories(models.Model):
    """
    Originally sourced from zCategories in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zcategories"

    categoryid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=1024, null=True, blank=True)
    category_tetum = models.CharField(max_length=1024, null=True, blank=True)


class zCMTPositions1(models.Model):
    """
    Originally sourced from zCMT_Positions in /home/josh/PNDS_Interim_MIS-Data.accdb (11 records)
    """

    class Meta:
        db_table = "zcmt_positions"

    cmt_position_id = models.IntegerField(primary_key=True)
    cmt_position_name = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zCycles(models.Model):
    """
    Originally sourced from zCycles in /home/josh/PNDS_Interim_MIS-Data.accdb (13 records)
    """

    class Meta:
        db_table = "zcycles"

    cycle_id = models.IntegerField(primary_key=True)
    cycle_name = models.CharField(max_length=1024, null=True, blank=True)
    cycle_start_date = models.DateTimeField(null=True, blank=True)
    cycle_finish_date = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zCycleStatus(models.Model):
    """
    Originally sourced from zCycleStatus in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zcyclestatus"

    cyclestatusid = models.IntegerField(primary_key=True)
    cyclestatus = models.CharField(max_length=1024, null=True, blank=True)
    cyclestatus_tetum = models.CharField(max_length=1024, null=True, blank=True)


class zDistrictPhase(models.Model):
    """
    Originally sourced from zDistrict_Phase in /home/josh/PNDS_Interim_MIS-Data.accdb (56 records)
    """

    class Meta:
        db_table = "zdistrict_phase"

    districtphaseid = models.IntegerField(primary_key=True)
    districtid = models.IntegerField(null=True, blank=True)
    phaseid = models.IntegerField(null=True, blank=True)
    cycleid = models.IntegerField(null=True, blank=True)


class zDocumentfiletype(models.Model):
    """
    Originally sourced from zDocument_file_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zdocument_file_type"

    id = models.IntegerField(primary_key=True)
    document_type = models.CharField(max_length=1024, null=True, blank=True)
    valid_extension = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zDocumenttype(models.Model):
    """
    Originally sourced from zDocument_type in /home/josh/PNDS_Interim_MIS-Data.accdb (99 records)
    """

    class Meta:
        db_table = "zdocument_type"

    id = models.IntegerField(primary_key=True)
    document_type_name = models.CharField(max_length=1024, null=True, blank=True)
    monthly_reports = models.BooleanField()
    social_activities = models.BooleanField()
    finance_activites = models.BooleanField()
    verification = models.BooleanField()
    r_50_report = models.BooleanField()
    completion_report = models.BooleanField()
    active = models.BooleanField()
    deacticated_date = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zElectionRound(models.Model):
    """
    Originally sourced from zElectionRound in /home/josh/PNDS_Interim_MIS-Data.accdb (5 records)
    """

    class Meta:
        db_table = "zelectionround"

    electionroundid = models.IntegerField(primary_key=True)
    electionroundtype = models.CharField(max_length=1024, null=True, blank=True)
    electionround_tetum = models.CharField(max_length=1024, null=True, blank=True)
    recordcreationdate = models.DateTimeField(null=True, blank=True)
    recordchangedate = models.DateTimeField(null=True, blank=True)


class zFinancedisbursementrules(models.Model):
    """
    Originally sourced from zFinance_disbursement_rules in /home/josh/PNDS_Interim_MIS-Data.accdb (23 records)
    """

    class Meta:
        db_table = "zfinance_disbursement_rules"

    id = models.IntegerField(primary_key=True)
    fd_type_id = models.IntegerField(null=True, blank=True)
    program_activity_id = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    active = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zFinancedisbursementtype(models.Model):
    """
    Originally sourced from zFinance_disbursement_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zfinance_disbursement_type"

    fbt_id = models.IntegerField(primary_key=True)
    fbd_type = models.CharField(max_length=1024, null=True, blank=True)
    active = models.BooleanField()
    fdb_order_number = models.IntegerField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zFinancialdisbursementactitvites(models.Model):
    """
    Originally sourced from zFinancial_disbursement_actitvites in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """

    class Meta:
        db_table = "zfinancial_disbursement_actitvites"

    fda_id = models.IntegerField(primary_key=True)
    activity_order = models.IntegerField(null=True, blank=True)
    activity_name = models.CharField(max_length=1024, null=True, blank=True)
    active = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zFreebalanceBudgetextract(models.Model):
    """
    Originally sourced from zFreebalance_Budget_extract in /home/josh/PNDS_Interim_MIS-Data.accdb (3666 records)
    """

    class Meta:
        db_table = "zfreebalance_budget_extract"

    id = models.IntegerField(primary_key=True)
    import_id = models.CharField(max_length=1024, null=True, blank=True)
    allocateddomestic = models.CharField(max_length=1024, null=True, blank=True)
    allocatedforeign = models.CharField(max_length=1024, null=True, blank=True)
    allowtoexceed = models.CharField(max_length=1024, null=True, blank=True)
    annualforecastdomestic = models.CharField(max_length=1024, null=True, blank=True)
    annualforecastforeign = models.CharField(max_length=1024, null=True, blank=True)
    approvaldate = models.CharField(max_length=1024, null=True, blank=True)
    checkcontrolamount = models.CharField(max_length=1024, null=True, blank=True)
    checkcontrolpercentage = models.CharField(max_length=1024, null=True, blank=True)
    commitmentsdomestic = models.CharField(max_length=1024, null=True, blank=True)
    commitmentsforeign = models.CharField(max_length=1024, null=True, blank=True)
    creationdate = models.CharField(max_length=1024, null=True, blank=True)
    currentamountdomestic = models.CharField(max_length=1024, null=True, blank=True)
    currentamountforeign = models.CharField(max_length=1024, null=True, blank=True)
    exchangerate = models.CharField(max_length=1024, null=True, blank=True)
    freebalancedomestic = models.CharField(max_length=1024, null=True, blank=True)
    freebalanceforeign = models.CharField(max_length=1024, null=True, blank=True)
    indicativecommitmentsdomestic = models.CharField(max_length=1024, null=True, blank=True)
    indicativecommitmentsforeign = models.CharField(max_length=1024, null=True, blank=True)
    isactive = models.CharField(max_length=1024, null=True, blank=True)
    isbasedonaccumulatedperiodamount = models.CharField(max_length=1024, null=True, blank=True)
    isbudgetdistributioncontrol = models.CharField(max_length=1024, null=True, blank=True)
    isvalidatedbyforeigncurrency = models.CharField(max_length=1024, null=True, blank=True)
    obligationsdomestic = models.CharField(max_length=1024, null=True, blank=True)
    obligationsforeign = models.CharField(max_length=1024, null=True, blank=True)
    origin = models.CharField(max_length=1024, null=True, blank=True)
    originalamountdomestic = models.IntegerField(null=True, blank=True)
    originalamountforeign = models.CharField(max_length=1024, null=True, blank=True)
    paiddomestic = models.CharField(max_length=1024, null=True, blank=True)
    paidforeign = models.CharField(max_length=1024, null=True, blank=True)
    surplusdeficitdomestic = models.CharField(max_length=1024, null=True, blank=True)
    surplusdeficitforeign = models.CharField(max_length=1024, null=True, blank=True)
    toleranceamount = models.CharField(max_length=1024, null=True, blank=True)
    tolerancepercentage = models.CharField(max_length=1024, null=True, blank=True)
    transfersdomestic = models.CharField(max_length=1024, null=True, blank=True)
    transfersforeign = models.CharField(max_length=1024, null=True, blank=True)
    unallocateddomestic = models.CharField(max_length=1024, null=True, blank=True)
    unallocatedforeign = models.CharField(max_length=1024, null=True, blank=True)
    updatesdomestic = models.CharField(max_length=1024, null=True, blank=True)
    updatesforeign = models.CharField(max_length=1024, null=True, blank=True)
    ytdactualdomestic = models.CharField(max_length=1024, null=True, blank=True)
    ytdactualforeign = models.CharField(max_length=1024, null=True, blank=True)
    approvedbyapplicationid = models.CharField(max_length=1024, null=True, blank=True)
    budgetcontroltypeapplicationid = models.CharField(max_length=1024, null=True, blank=True)
    budgetofficeapplicationid = models.CharField(max_length=1024, null=True, blank=True)
    codingblockstringcode = models.CharField(max_length=1024, null=True, blank=True)
    codingblockcoagroupcoaapplicationid = models.CharField(max_length=1024, null=True, blank=True)
    codingblockcoagroupcode = models.CharField(max_length=1024, null=True, blank=True)
    createdbyapplicationid = models.CharField(max_length=1024, null=True, blank=True)
    currencyapplicationid = models.CharField(max_length=1024, null=True, blank=True)
    fiscalyearapplicationid = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_export_date = models.DateTimeField(null=True, blank=True)
    export_number = models.IntegerField(null=True, blank=True)
    suco_id = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zGender(models.Model):
    """
    Originally sourced from zGender in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zgender"

    genderid = models.IntegerField(primary_key=True)
    gender_english = models.CharField(max_length=1024, null=True, blank=True)
    gender_tetum = models.CharField(max_length=1024, null=True, blank=True)


class zGroups(models.Model):
    """
    Originally sourced from zGroups in /home/josh/PNDS_Interim_MIS-Data.accdb (8 records)
    """

    class Meta:
        db_table = "zgroups"

    id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=1024, null=True, blank=True)
    finance_functions = models.BooleanField()
    admin_functions = models.BooleanField()
    reporting_functions = models.BooleanField()
    mis_functions = models.BooleanField()
    complaints_functions = models.BooleanField()
    data_fix_functions = models.BooleanField()
    social_functions = models.BooleanField()
    field_team_data = models.BooleanField()
    field_team_approval = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)
    last_transmission_number = models.IntegerField(null=True, blank=True)
    finance_edit = models.BooleanField()
    social_edit = models.BooleanField()
    subproject_edit = models.BooleanField()
    suco_budgeting_edit = models.BooleanField()
    finance_monitoring_edit = models.BooleanField()
    complaints_edit = models.BooleanField()
    reports_edit = models.BooleanField()
    unverify_report = models.BooleanField()
    record_changed_date = models.DateTimeField(null=True, blank=True)
    district_admin = models.BooleanField()


class zIndicators(models.Model):
    """
    Originally sourced from zIndicators in /home/josh/PNDS_Interim_MIS-Data.accdb (10 records)
    """

    class Meta:
        db_table = "zindicators"

    indicatorid = models.IntegerField(primary_key=True)
    categoryid = models.IntegerField(null=True, blank=True)
    indicator = models.CharField(max_length=1024, null=True, blank=True)
    indicator_tetum = models.CharField(max_length=1024, null=True, blank=True)


class zLanguage(models.Model):
    """
    Originally sourced from zLanguage in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    class Meta:
        db_table = "zlanguage"

    id = models.IntegerField(primary_key=True)
    language_name = models.CharField(max_length=1024, null=True, blank=True)
    language_default = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zLastID(models.Model):
    """
    Originally sourced from zLastID in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zlastid"

    tablename = models.CharField(max_length=1024, primary_key=True)
    lastid = models.IntegerField(null=True, blank=True)


class zOutputs(models.Model):
    """
    Originally sourced from zOutputs in /home/josh/PNDS_Interim_MIS-Data.accdb (123 records)
    """

    class Meta:
        db_table = "zoutputs"

    outputid = models.IntegerField(primary_key=True)
    output = models.CharField(max_length=1024, null=True, blank=True)
    output_tetum = models.CharField(max_length=1024, null=True, blank=True)
    sectorid = models.IntegerField(null=True, blank=True)
    sub_sectorid = models.IntegerField(null=True, blank=True)


class zOutputUnit(models.Model):
    """
    Originally sourced from zOutputUnit in /home/josh/PNDS_Interim_MIS-Data.accdb (117 records)
    """

    class Meta:
        db_table = "zoutputunit"

    outputunitid = models.IntegerField(primary_key=True)
    outputid = models.IntegerField(null=True, blank=True)
    unitid = models.IntegerField(null=True, blank=True)
    minimum_value = models.IntegerField(null=True, blank=True)
    maximum_value = models.IntegerField(null=True, blank=True)


class zPNDSFreebalancetranslation(models.Model):
    """
    Originally sourced from zPNDS_Freebalance_translation in /home/josh/PNDS_Interim_MIS-Data.accdb (9 records)
    """

    class Meta:
        db_table = "zpnds_freebalance_translation"

    id = models.IntegerField(primary_key=True)
    acct_no = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    freebalance_line_item_budget = models.IntegerField(null=True, blank=True)
    freebalance_line_item_monthly_exp = models.IntegerField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zPriorities(models.Model):
    """
    Originally sourced from zPriorities in /home/josh/PNDS_Interim_MIS-Data.accdb (50 records)
    """

    class Meta:
        db_table = "zpriorities"

    priorityid = models.IntegerField(primary_key=True)
    priority = models.IntegerField(null=True, blank=True)


class zProgramActivity(models.Model):
    """
    Originally sourced from zProgram_Activity in /home/josh/PNDS_Interim_MIS-Data.accdb (39 records)
    """

    class Meta:
        db_table = "zprogram_activity"

    program_activity_id = models.IntegerField(primary_key=True)
    activity_name = models.CharField(max_length=1024, null=True, blank=True)
    social_activity_number = models.IntegerField(null=True, blank=True)
    finance_activity_number = models.IntegerField(null=True, blank=True)
    program_activity_number = models.IntegerField(null=True, blank=True)
    finance_activity = models.BooleanField()
    social_activity = models.BooleanField()
    program_activity = models.BooleanField()
    technical_activity = models.BooleanField()
    active = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    aldea_activity = models.BooleanField()
    zprogram_activity_level_id = models.IntegerField(null=True, blank=True)
    zprogram_activity_type_id = models.IntegerField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zProgramActivitylevel(models.Model):
    """
    Originally sourced from zProgram_Activity_level in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zprogram_activity_level"

    program_activity_level_id = models.IntegerField(primary_key=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)


class zProgramactivtytype(models.Model):
    """
    Originally sourced from zProgram_activty_type in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zprogram_activty_type"

    program_activtiy_type_id = models.IntegerField(primary_key=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)


class zReporttype(models.Model):
    """
    Originally sourced from zReport_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zreport_type"

    report_type_id = models.IntegerField(primary_key=True)
    report_type_name = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zSector(models.Model):
    """
    Originally sourced from zSector in /home/josh/PNDS_Interim_MIS-Data.accdb (8 records)
    """

    class Meta:
        db_table = "zsector"

    sector_id = models.IntegerField(primary_key=True)
    sector_name = models.CharField(max_length=1024, null=True, blank=True)
    icon_name = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zSectorActvity(models.Model):
    """
    Originally sourced from zSector_Actvity in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """

    class Meta:
        db_table = "zsector_actvity"

    id = models.IntegerField(primary_key=True)
    active = models.BooleanField()
    sector_id = models.IntegerField(null=True, blank=True)
    activity_type_id = models.IntegerField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zSettlements(models.Model):
    """
    Originally sourced from zSettlements in /home/josh/PNDS_Interim_MIS-Data.accdb (2829 records)
    """

    class Meta:
        db_table = "zsettlements"

    id = models.IntegerField(primary_key=True)
    set_name = models.CharField(max_length=1024, null=True, blank=True)
    suco_pcode = models.CharField(max_length=1024, null=True, blank=True)
    suco_id = models.IntegerField(null=True, blank=True)
    gps_coords = models.CharField(max_length=1024, null=True, blank=True)
    set_pcode = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zSubSector(models.Model):
    """
    Originally sourced from zSub_Sector in /home/josh/PNDS_Interim_MIS-Data.accdb (23 records)
    """

    class Meta:
        db_table = "zsub_sector"

    sub_sectorid = models.IntegerField(primary_key=True)
    sub_sector = models.CharField(max_length=1024, null=True, blank=True)
    sub_sector_tetum = models.CharField(max_length=1024, null=True, blank=True)
    sector_id = models.IntegerField(null=True, blank=True)


class zSubprojectStatus(models.Model):
    """
    Originally sourced from zSubproject_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zsubproject_status"

    status_id = models.IntegerField(primary_key=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)


class zSubprojectStatus1(models.Model):
    """
    Originally sourced from zSubprojectStatus in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """

    class Meta:
        db_table = "zsubprojectstatus"

    subprojectstatusid = models.IntegerField(primary_key=True)
    subprojectstatus = models.CharField(max_length=1024, null=True, blank=True)
    subprojectstatus_tetum = models.CharField(max_length=1024, null=True, blank=True)


class zSucophase(models.Model):
    """
    Originally sourced from zSuco_phase in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zsuco_phase"

    id = models.IntegerField(primary_key=True)
    phase = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zSucoStatus(models.Model):
    """
    Originally sourced from zSuco_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    class Meta:
        db_table = "zsuco_status"

    suco_status_id = models.IntegerField(primary_key=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)


class zTetumtranslation(models.Model):
    """
    Originally sourced from zTetum_translation in /home/josh/PNDS_Interim_MIS-Data.accdb (606 records)
    """

    class Meta:
        db_table = "ztetum_translation"

    id = models.IntegerField(primary_key=True)
    type_data = models.BooleanField()
    type_label = models.BooleanField()
    type_error = models.BooleanField()
    english_word = models.CharField(max_length=1024, null=True, blank=True)
    tetum_word = models.CharField(max_length=1024, null=True, blank=True)
    indonesian_word = models.CharField(max_length=1024, null=True, blank=True)
    long_number = models.IntegerField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zTetumtranslationOLD(models.Model):
    """
    Originally sourced from zTetum_translation_OLD in /home/josh/PNDS_Interim_MIS-Data.accdb (569 records)
    """

    class Meta:
        db_table = "ztetum_translation_old"

    id = models.IntegerField(primary_key=True)
    type_data = models.BooleanField()
    type_label = models.BooleanField()
    type_error = models.BooleanField()
    english_word = models.CharField(max_length=1024, null=True, blank=True)
    tetum_word = models.CharField(max_length=1024, null=True, blank=True)
    indonesian_word = models.CharField(max_length=1024, null=True, blank=True)
    long_number = models.IntegerField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zTransMetatables(models.Model):
    """
    Originally sourced from zTrans_Meta_tables in /home/josh/PNDS_Interim_MIS-Data.accdb (50 records)
    """

    class Meta:
        db_table = "ztrans_meta_tables"

    id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=1024, null=True, blank=True)
    transfer_table_name = models.CharField(max_length=1024, null=True, blank=True)
    audit_table_name = models.CharField(max_length=1024, null=True, blank=True)
    trans_dili_to_district = models.BooleanField()
    trans_district_to_dili = models.BooleanField()
    requires_verified = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zUnits(models.Model):
    """
    Originally sourced from zUnits in /home/josh/PNDS_Interim_MIS-Data.accdb (9 records)
    """

    class Meta:
        db_table = "zunits"

    unitid = models.IntegerField(primary_key=True)
    unit_tetum = models.CharField(max_length=1024, null=True, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)
    unit = models.CharField(max_length=1024, null=True, blank=True)


class zYears(models.Model):
    """
    Originally sourced from zYears in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zyears"

    id = models.IntegerField(primary_key=True)
    year_of_operation = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class DataSyncLog(models.Model):
    """
    Originally sourced from Data_Sync_Log in /home/josh/PNDS_Interim_MIS-Data.accdb (4375 records)
    """

    class Meta:
        db_table = "data_sync_log"

    id = models.IntegerField(primary_key=True)
    districtid = models.IntegerField(null=True, blank=True)
    data_imported = models.IntegerField(null=True, blank=True)
    data_updated = models.IntegerField(null=True, blank=True)
    data_imported_priorities = models.IntegerField(null=True, blank=True)
    data_updated_priorities = models.IntegerField(null=True, blank=True)
    data_imported_progress = models.IntegerField(null=True, blank=True)
    data_updated_progress = models.IntegerField(null=True, blank=True)
    data_imported_project = models.IntegerField(null=True, blank=True)
    data_updated_project = models.IntegerField(null=True, blank=True)
    data_updated_project_dates = models.IntegerField(null=True, blank=True)
    date_imported = models.DateTimeField(null=True, blank=True)
    date_exported = models.DateTimeField(null=True, blank=True)
    r_import = models.BooleanField()
    data_imported_monthlyrep = models.IntegerField(null=True, blank=True)
    data_imported_opsrep = models.IntegerField(null=True, blank=True)
    data_updated_opsrep = models.IntegerField(null=True, blank=True)
    data_imported_opsbudget = models.IntegerField(null=True, blank=True)
    data_updated_opsbudget = models.IntegerField(null=True, blank=True)
    data_imported_fininfo = models.IntegerField(null=True, blank=True)
    data_updated_fininfo = models.IntegerField(null=True, blank=True)
    data_imported_monthlyrepinf = models.IntegerField(null=True, blank=True)
    data_updated_monthlyrepinf = models.IntegerField(null=True, blank=True)
    data_imported_inf_exp = models.IntegerField(null=True, blank=True)
    data_updated_inf_exp = models.IntegerField(null=True, blank=True)
    data_imported_sucocycle = models.IntegerField(null=True, blank=True)
    data_updated_suco_cycle = models.IntegerField(null=True, blank=True)
    data_imported_projoutput = models.IntegerField(null=True, blank=True)
    data_updated_projoutput = models.IntegerField(null=True, blank=True)


class ImportToSQL(models.Model):
    """
    Originally sourced from ImportToSQL in /home/josh/PNDS_Interim_MIS-Data.accdb (1 records)
    """

    class Meta:
        db_table = "importtosql"

    id = models.IntegerField(primary_key=True)
    importtosql = models.BooleanField()


class SubprojectPhysicalProgress(models.Model):
    """
    Originally sourced from Subproject_Physical_Progress in /home/josh/PNDS_Interim_MIS-Data.accdb (25395 records)
    """

    class Meta:
        db_table = "subproject_physical_progress"

    id = models.IntegerField(primary_key=True)
    subprojectid = models.CharField(max_length=1024, null=True, blank=True)
    progress_period = models.DateTimeField(null=True, blank=True)
    progress_date = models.DateTimeField(null=True, blank=True)
    physical_progress = models.FloatField()
    numberofdaysworked = models.IntegerField(null=True, blank=True)
    labour_female = models.IntegerField(null=True, blank=True)
    labour_male = models.IntegerField(null=True, blank=True)
    labour_poor = models.IntegerField(null=True, blank=True)
    labour_disabled = models.IntegerField(null=True, blank=True)
    picture_path = models.CharField(max_length=1024, null=True, blank=True)
    remarks = models.CharField(max_length=1024, null=True, blank=True)
    record_creationdate = models.DateTimeField(null=True, blank=True)
    record_changedate = models.DateTimeField(null=True, blank=True)
    physical_progress_id = models.CharField(max_length=1024, null=True, blank=True)


class Sucosubprojectadditonalinfo(models.Model):
    """
    Originally sourced from Suco_subproject_additonal_info in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """

    class Meta:
        db_table = "suco_subproject_additonal_info"

    id = models.IntegerField(primary_key=True)
    district_name = models.CharField(max_length=1024, null=True, blank=True)
    subdistrict_name = models.CharField(max_length=1024, null=True, blank=True)
    suco_name = models.CharField(max_length=1024, null=True, blank=True)
    project_number = models.IntegerField(null=True, blank=True)
    sector = models.CharField(max_length=1024, null=True, blank=True)
    subproject_name = models.CharField(max_length=1024, null=True, blank=True)
    subproject_description = models.CharField(max_length=1024, null=True, blank=True)
    mof_finance_code = models.CharField(max_length=1024, null=True, blank=True)
    subproject_materials_budget = models.IntegerField(null=True, blank=True)
    subproject_labour_budget = models.IntegerField(null=True, blank=True)
    subproject_start_date = models.CharField(max_length=1024, null=True, blank=True)
    subproject_finish_date = models.CharField(max_length=1024, null=True, blank=True)
    verified_y_n = models.CharField(max_length=1024, null=True, blank=True)
    date_of_verification = models.CharField(max_length=1024, null=True, blank=True)
    subproject_aldea = models.CharField(max_length=1024, null=True, blank=True)
    no_of_women_benefic = models.CharField(max_length=1024, null=True, blank=True)
    no_of_men_benefic = models.CharField(max_length=1024, null=True, blank=True)
    no_of_household_benefic = models.CharField(max_length=1024, null=True, blank=True)
    main_activity_units = models.CharField(max_length=1024, null=True, blank=True)
    main_activity_unit_type = models.CharField(max_length=1024, null=True, blank=True)
    uniqueval = models.CharField(max_length=1024, null=True, blank=True)


class Validmonthlyreports(models.Model):
    """
    Originally sourced from Valid_monthly_reports in /home/josh/PNDS_Interim_MIS-Data.accdb (61 records)
    """

    class Meta:
        db_table = "valid_monthly_reports"

    vmr_id = models.IntegerField(primary_key=True)
    vmr_date = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)


class zFinanceMonitors(models.Model):
    """
    Originally sourced from zFinance_Monitors in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """

    class Meta:
        db_table = "zfinance_monitors"

    f_mon_id = models.IntegerField(primary_key=True)
    f_monitor_name = models.CharField(max_length=1024, null=True, blank=True)
    active = models.BooleanField()
    deactivated_date = models.DateTimeField(null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    english = models.CharField(max_length=1024, null=True, blank=True)
    tetum = models.CharField(max_length=1024, null=True, blank=True)
    indonesian = models.CharField(max_length=1024, null=True, blank=True)


class zOperationBudgetStatus(models.Model):
    """
    Originally sourced from zOperationBudget_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    class Meta:
        db_table = "zoperationbudget_status"

    operationbudget_statusid = models.IntegerField(primary_key=True)
    operationbudget_status = models.CharField(max_length=1024, null=True, blank=True)
    operationbudget_status_tetum = models.CharField(max_length=1024, null=True, blank=True)


class zReportformat(models.Model):
    """
    Originally sourced from zReport_format in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """

    class Meta:
        db_table = "zreport_format"

    id = models.IntegerField(primary_key=True)
    format_name = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zSubdistrictPhase(models.Model):
    """
    Originally sourced from zSubdistrict_Phase in /home/josh/PNDS_Interim_MIS-Data.accdb (104 records)
    """

    class Meta:
        db_table = "zsubdistrict_phase"

    subdistrictphaseid = models.IntegerField(primary_key=True)
    sudistrictid = models.IntegerField(null=True, blank=True)
    phaseid = models.IntegerField(null=True, blank=True)
    cycleid = models.IntegerField(null=True, blank=True)


class zTransmetafields(models.Model):
    """
    Originally sourced from zTrans_meta_fields in /home/josh/PNDS_Interim_MIS-Data.accdb (548 records)
    """

    class Meta:
        db_table = "ztrans_meta_fields"

    id = models.IntegerField(primary_key=True)
    table_id = models.IntegerField(null=True, blank=True)
    field_name = models.CharField(max_length=1024, null=True, blank=True)
    load_at_dili = models.BooleanField()
    load_at_district = models.BooleanField()
    extract_at_dili = models.BooleanField()
    extract_at_district = models.BooleanField()
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_change_date = models.DateTimeField(null=True, blank=True)
    creation = models.BooleanField()
    change = models.BooleanField()
    r_pk = models.BooleanField()
    fk = models.BooleanField()
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zDistrict(models.Model):
    """
    Originally sourced from zDistrict in /home/josh/PNDS_Interim_MIS-Data.accdb (14 records)
    """

    class Meta:
        db_table = "zdistrict"

    distict_id = models.IntegerField(primary_key=True)
    district_name = models.CharField(max_length=1024, null=True, blank=True)
    district_code = models.CharField(max_length=1024, null=True, blank=True)
    mof_district_code = models.CharField(max_length=1024, null=True, blank=True)
    pcode = models.CharField(max_length=1024, null=True, blank=True)
    post_id_number = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)


class zSubdistrict(models.Model):
    """
    Originally sourced from zSubdistrict in /home/josh/PNDS_Interim_MIS-Data.accdb (67 records)
    """

    class Meta:
        db_table = "zsubdistrict"

    subdistrict_id = models.IntegerField(primary_key=True)
    subdistrict_name = models.CharField(max_length=1024, null=True, blank=True)
    subdistrict_name_jdr = models.CharField(max_length=1024, null=True, blank=True)
    subdistrict_name_arch = models.CharField(max_length=1024, null=True, blank=True)
    subdistrict_code = models.CharField(max_length=1024, null=True, blank=True)
    district_id = models.IntegerField(null=True, blank=True)
    mof_subdistrict_code = models.CharField(max_length=1024, null=True, blank=True)
    mof_district_code = models.CharField(max_length=1024, null=True, blank=True)
    subdistrict_pcode = models.CharField(max_length=1024, null=True, blank=True)
    district_pcode = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    sd_population_total = models.IntegerField(null=True, blank=True)
    sd_population_households = models.IntegerField(null=True, blank=True)
    sd_population_women = models.IntegerField(null=True, blank=True)
    sd_population_men = models.IntegerField(null=True, blank=True)
    sd_population_children = models.IntegerField(null=True, blank=True)


class zSuco(models.Model):
    """
    Originally sourced from zSuco in /home/josh/PNDS_Interim_MIS-Data.accdb (452 records)
    """

    class Meta:
        db_table = "zsuco"

    suco_id = models.IntegerField(primary_key=True)
    suco_name = models.CharField(max_length=1024, null=True, blank=True)
    suco_name_jdr = models.CharField(max_length=1024, null=True, blank=True)
    suco_name_arch = models.CharField(max_length=1024, null=True, blank=True)
    suco_code = models.CharField(max_length=1024, null=True, blank=True)
    subdistrict_id = models.IntegerField(null=True, blank=True)
    suco_mof_finance_code = models.CharField(max_length=1024, null=True, blank=True)
    operational_bank_account_no = models.CharField(max_length=1024, null=True, blank=True)
    infrastructure_bank_account_no = models.CharField(max_length=1024, null=True, blank=True)
    mof_suco_code = models.CharField(max_length=1024, null=True, blank=True)
    mof_subdistrict_code = models.CharField(max_length=1024, null=True, blank=True)
    suco_phase = models.IntegerField(null=True, blank=True)
    infrastructure_budget_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    operations_budget_ceiling = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    suco_pcode = models.CharField(max_length=1024, null=True, blank=True)
    subdistrict_pcode = models.CharField(max_length=1024, null=True, blank=True)
    alternate_spelling1 = models.CharField(max_length=1024, null=True, blank=True)
    record_creation_date = models.DateTimeField(null=True, blank=True)
    record_changed_date = models.DateTimeField(null=True, blank=True)
    bank_name = models.CharField(max_length=1024, null=True, blank=True)
    bank_branch = models.CharField(max_length=1024, null=True, blank=True)
    zsuco_status = models.IntegerField(null=True, blank=True)
    remarks = models.CharField(max_length=1024, null=True, blank=True)
    grant_agreement_startdate = models.DateTimeField(null=True, blank=True)
    grant_agreement_finishdate = models.DateTimeField(null=True, blank=True)
    suco_population_total = models.IntegerField(null=True, blank=True)
    suco_population_households = models.IntegerField(null=True, blank=True)
    suco_population_women = models.IntegerField(null=True, blank=True)
    suco_population_men = models.IntegerField(null=True, blank=True)
    suco_population_children = models.IntegerField(null=True, blank=True)


class SucoFundingSources(models.Model):
    """
    Originally sourced from SucoFundingSources in /home/josh/PNDS_Interim_MIS-Data.accdb (1524 records)
    """

    class Meta:
        db_table = "sucofundingsources"

    sucofundingsourceid = models.CharField(max_length=1024, primary_key=True)
    suco_cycleid = models.IntegerField(null=True, blank=True)
    fundingsourceid = models.IntegerField(null=True, blank=True)
    fundingamount = models.IntegerField(null=True, blank=True)


class zFundingSources(models.Model):
    """
    Originally sourced from zFundingSources in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """

    class Meta:
        db_table = "zfundingsources"

    fundingsourceid = models.IntegerField(primary_key=True)
    fundingsourceabbreviation = models.CharField(max_length=1024, null=True, blank=True)
    fundingsource = models.CharField(max_length=1024, null=True, blank=True)
    fundingsource_tetum = models.CharField(max_length=1024, null=True, blank=True)


