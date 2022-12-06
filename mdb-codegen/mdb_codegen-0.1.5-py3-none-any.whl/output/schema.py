from ninja import Schema, ModelSchema

from . import models


class Error(Schema):
    message: str



class ActivityBlackListedOut(ModelSchema):
    """
    Originally sourced from Activity_BlackListed in /home/josh/PNDS_Interim_MIS-Data.accdb (13 records)
    """
    class Config:
        model = models.ActivityBlackListed
        model_fields = "__all__"



class DataSyncLogTempOut(ModelSchema):
    """
    Originally sourced from Data_Sync_Log_Temp in /home/josh/PNDS_Interim_MIS-Data.accdb (14 records)
    """
    class Config:
        model = models.DataSyncLogTemp
        model_fields = "__all__"



class DocumentsandpicturesOut(ModelSchema):
    """
    Originally sourced from Documents_and_pictures in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.Documentsandpictures
        model_fields = "__all__"



class FinanceMonitoringOut(ModelSchema):
    """
    Originally sourced from Finance_Monitoring in /home/josh/PNDS_Interim_MIS-Data.accdb (906 records)
    """
    class Config:
        model = models.FinanceMonitoring
        model_fields = "__all__"



class FreebalancetranslationcodesOut(ModelSchema):
    """
    Originally sourced from Freebalance_translation_codes in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """
    class Config:
        model = models.Freebalancetranslationcodes
        model_fields = "__all__"



class GoogleTransfersOut(ModelSchema):
    """
    Originally sourced from Google_Transfers in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """
    class Config:
        model = models.GoogleTransfers
        model_fields = "__all__"



class MonthlyreportsOut(ModelSchema):
    """
    Originally sourced from Monthly_reports in /home/josh/PNDS_Interim_MIS-Data.accdb (41928 records)
    """
    class Config:
        model = models.Monthlyreports
        model_fields = "__all__"



class MonthlyreportsInfrastructureOut(ModelSchema):
    """
    Originally sourced from Monthly_reports_Infrastructure in /home/josh/PNDS_Interim_MIS-Data.accdb (29260 records)
    """
    class Config:
        model = models.MonthlyreportsInfrastructure
        model_fields = "__all__"



class zCMTPositionsOut(ModelSchema):
    """
    Originally sourced from zCMTPositions in /home/josh/PNDS_Interim_MIS-Data.accdb (12 records)
    """
    class Config:
        model = models.zCMTPositions
        model_fields = "__all__"



class OperationBudgetOut(ModelSchema):
    """
    Originally sourced from OperationBudget in /home/josh/PNDS_Interim_MIS-Data.accdb (3731 records)
    """
    class Config:
        model = models.OperationBudget
        model_fields = "__all__"



class PhaseCycleOut(ModelSchema):
    """
    Originally sourced from PhaseCycle in /home/josh/PNDS_Interim_MIS-Data.accdb (38 records)
    """
    class Config:
        model = models.PhaseCycle
        model_fields = "__all__"



class SubprojectOutputsOut(ModelSchema):
    """
    Originally sourced from SubpojectOutputs in /home/josh/PNDS_Interim_MIS-Data.accdb (7995 records)
    """
    class Config:
        model = models.SubprojectOutputs
        model_fields = "__all__"



class SucoActvitiesOut(ModelSchema):
    """
    Originally sourced from Suco_Actvities in /home/josh/PNDS_Interim_MIS-Data.accdb (37104 records)
    """
    class Config:
        model = models.SucoActvities
        model_fields = "__all__"



class SucoCyclesOut(ModelSchema):
    """
    Originally sourced from Suco_Cycles in /home/josh/PNDS_Interim_MIS-Data.accdb (3924 records)
    """
    class Config:
        model = models.SucoCycles
        model_fields = "__all__"



class SucoFinancialDisbursementsOut(ModelSchema):
    """
    Originally sourced from Suco_Financial_Disbursements in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """
    class Config:
        model = models.SucoFinancialDisbursements
        model_fields = "__all__"



class SucoFinancialinfoOut(ModelSchema):
    """
    Originally sourced from Suco_Financial_info in /home/josh/PNDS_Interim_MIS-Data.accdb (3948 records)
    """
    class Config:
        model = models.SucoFinancialinfo
        model_fields = "__all__"



class SucoInfrastructureProjectReportOut(ModelSchema):
    """
    Originally sourced from Suco_Infrastructure_Project_Report in /home/josh/PNDS_Interim_MIS-Data.accdb (52064 records)
    """
    class Config:
        model = models.SucoInfrastructureProjectReport
        model_fields = "__all__"



class SucoOperationalReportOut(ModelSchema):
    """
    Originally sourced from Suco_Operational_Report in /home/josh/PNDS_Interim_MIS-Data.accdb (41291 records)
    """
    class Config:
        model = models.SucoOperationalReport
        model_fields = "__all__"



class SucoPrioritiesOut(ModelSchema):
    """
    Originally sourced from Suco_Priorities in /home/josh/PNDS_Interim_MIS-Data.accdb (11012 records)
    """
    class Config:
        model = models.SucoPriorities
        model_fields = "__all__"



class SucoSubProjectOut(ModelSchema):
    """
    Originally sourced from Suco_SubProject in /home/josh/PNDS_Interim_MIS-Data.accdb (5053 records)
    """
    class Config:
        model = models.SucoSubProject
        model_fields = "__all__"



class SucoCMTMembersOut(ModelSchema):
    """
    Originally sourced from SucoCMTMembers in /home/josh/PNDS_Interim_MIS-Data.accdb (4976 records)
    """
    class Config:
        model = models.SucoCMTMembers
        model_fields = "__all__"



class syncImportLogOut(ModelSchema):
    """
    Originally sourced from syncImportLog in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """
    class Config:
        model = models.syncImportLog
        model_fields = "__all__"



class SystemInfoOut(ModelSchema):
    """
    Originally sourced from System_Info in /home/josh/PNDS_Interim_MIS-Data.accdb (1 records)
    """
    class Config:
        model = models.SystemInfo
        model_fields = "__all__"



class SystemlogOut(ModelSchema):
    """
    Originally sourced from System_log in /home/josh/PNDS_Interim_MIS-Data.accdb (12353 records)
    """
    class Config:
        model = models.Systemlog
        model_fields = "__all__"



class TransfersOut(ModelSchema):
    """
    Originally sourced from Transfers in /home/josh/PNDS_Interim_MIS-Data.accdb (0 records)
    """
    class Config:
        model = models.Transfers
        model_fields = "__all__"



class UsersOut(ModelSchema):
    """
    Originally sourced from Users in /home/josh/PNDS_Interim_MIS-Data.accdb (61 records)
    """
    class Config:
        model = models.Users
        model_fields = "__all__"



class UsersoldOut(ModelSchema):
    """
    Originally sourced from Users_old in /home/josh/PNDS_Interim_MIS-Data.accdb (17 records)
    """
    class Config:
        model = models.Usersold
        model_fields = "__all__"



class UserTrackingOut(ModelSchema):
    """
    Originally sourced from UserTracking in /home/josh/PNDS_Interim_MIS-Data.accdb (23556 records)
    """
    class Config:
        model = models.UserTracking
        model_fields = "__all__"



class zActivitiesOut(ModelSchema):
    """
    Originally sourced from zActivities in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """
    class Config:
        model = models.zActivities
        model_fields = "__all__"



class zActivityDocumenttypeOut(ModelSchema):
    """
    Originally sourced from zActivity_Document_type in /home/josh/PNDS_Interim_MIS-Data.accdb (38 records)
    """
    class Config:
        model = models.zActivityDocumenttype
        model_fields = "__all__"



class zActivitytypeOut(ModelSchema):
    """
    Originally sourced from zActivity_type in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """
    class Config:
        model = models.zActivitytype
        model_fields = "__all__"



class zAldeiaOut(ModelSchema):
    """
    Originally sourced from zAldeia in /home/josh/PNDS_Interim_MIS-Data.accdb (2254 records)
    """
    class Config:
        model = models.zAldeia
        model_fields = "__all__"



class zCategoriesOut(ModelSchema):
    """
    Originally sourced from zCategories in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.zCategories
        model_fields = "__all__"



class zCMTPositions1Out(ModelSchema):
    """
    Originally sourced from zCMT_Positions in /home/josh/PNDS_Interim_MIS-Data.accdb (11 records)
    """
    class Config:
        model = models.zCMTPositions1
        model_fields = "__all__"



class zCyclesOut(ModelSchema):
    """
    Originally sourced from zCycles in /home/josh/PNDS_Interim_MIS-Data.accdb (13 records)
    """
    class Config:
        model = models.zCycles
        model_fields = "__all__"



class zCycleStatusOut(ModelSchema):
    """
    Originally sourced from zCycleStatus in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """
    class Config:
        model = models.zCycleStatus
        model_fields = "__all__"



class zDistrictPhaseOut(ModelSchema):
    """
    Originally sourced from zDistrict_Phase in /home/josh/PNDS_Interim_MIS-Data.accdb (56 records)
    """
    class Config:
        model = models.zDistrictPhase
        model_fields = "__all__"



class zDocumentfiletypeOut(ModelSchema):
    """
    Originally sourced from zDocument_file_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.zDocumentfiletype
        model_fields = "__all__"



class zDocumenttypeOut(ModelSchema):
    """
    Originally sourced from zDocument_type in /home/josh/PNDS_Interim_MIS-Data.accdb (99 records)
    """
    class Config:
        model = models.zDocumenttype
        model_fields = "__all__"



class zElectionRoundOut(ModelSchema):
    """
    Originally sourced from zElectionRound in /home/josh/PNDS_Interim_MIS-Data.accdb (5 records)
    """
    class Config:
        model = models.zElectionRound
        model_fields = "__all__"



class zFinancedisbursementrulesOut(ModelSchema):
    """
    Originally sourced from zFinance_disbursement_rules in /home/josh/PNDS_Interim_MIS-Data.accdb (23 records)
    """
    class Config:
        model = models.zFinancedisbursementrules
        model_fields = "__all__"



class zFinancedisbursementtypeOut(ModelSchema):
    """
    Originally sourced from zFinance_disbursement_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.zFinancedisbursementtype
        model_fields = "__all__"



class zFinancialdisbursementactitvitesOut(ModelSchema):
    """
    Originally sourced from zFinancial_disbursement_actitvites in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """
    class Config:
        model = models.zFinancialdisbursementactitvites
        model_fields = "__all__"



class zFreebalanceBudgetextractOut(ModelSchema):
    """
    Originally sourced from zFreebalance_Budget_extract in /home/josh/PNDS_Interim_MIS-Data.accdb (3666 records)
    """
    class Config:
        model = models.zFreebalanceBudgetextract
        model_fields = "__all__"



class zGenderOut(ModelSchema):
    """
    Originally sourced from zGender in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """
    class Config:
        model = models.zGender
        model_fields = "__all__"



class zGroupsOut(ModelSchema):
    """
    Originally sourced from zGroups in /home/josh/PNDS_Interim_MIS-Data.accdb (8 records)
    """
    class Config:
        model = models.zGroups
        model_fields = "__all__"



class zIndicatorsOut(ModelSchema):
    """
    Originally sourced from zIndicators in /home/josh/PNDS_Interim_MIS-Data.accdb (10 records)
    """
    class Config:
        model = models.zIndicators
        model_fields = "__all__"



class zLanguageOut(ModelSchema):
    """
    Originally sourced from zLanguage in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """
    class Config:
        model = models.zLanguage
        model_fields = "__all__"



class zLastIDOut(ModelSchema):
    """
    Originally sourced from zLastID in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """
    class Config:
        model = models.zLastID
        model_fields = "__all__"



class zOutputsOut(ModelSchema):
    """
    Originally sourced from zOutputs in /home/josh/PNDS_Interim_MIS-Data.accdb (123 records)
    """
    class Config:
        model = models.zOutputs
        model_fields = "__all__"



class zOutputUnitOut(ModelSchema):
    """
    Originally sourced from zOutputUnit in /home/josh/PNDS_Interim_MIS-Data.accdb (117 records)
    """
    class Config:
        model = models.zOutputUnit
        model_fields = "__all__"



class zPNDSFreebalancetranslationOut(ModelSchema):
    """
    Originally sourced from zPNDS_Freebalance_translation in /home/josh/PNDS_Interim_MIS-Data.accdb (9 records)
    """
    class Config:
        model = models.zPNDSFreebalancetranslation
        model_fields = "__all__"



class zPrioritiesOut(ModelSchema):
    """
    Originally sourced from zPriorities in /home/josh/PNDS_Interim_MIS-Data.accdb (50 records)
    """
    class Config:
        model = models.zPriorities
        model_fields = "__all__"



class zProgramActivityOut(ModelSchema):
    """
    Originally sourced from zProgram_Activity in /home/josh/PNDS_Interim_MIS-Data.accdb (39 records)
    """
    class Config:
        model = models.zProgramActivity
        model_fields = "__all__"



class zProgramActivitylevelOut(ModelSchema):
    """
    Originally sourced from zProgram_Activity_level in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.zProgramActivitylevel
        model_fields = "__all__"



class zProgramactivtytypeOut(ModelSchema):
    """
    Originally sourced from zProgram_activty_type in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """
    class Config:
        model = models.zProgramactivtytype
        model_fields = "__all__"



class zReporttypeOut(ModelSchema):
    """
    Originally sourced from zReport_type in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.zReporttype
        model_fields = "__all__"



class zSectorOut(ModelSchema):
    """
    Originally sourced from zSector in /home/josh/PNDS_Interim_MIS-Data.accdb (8 records)
    """
    class Config:
        model = models.zSector
        model_fields = "__all__"



class zSectorActvityOut(ModelSchema):
    """
    Originally sourced from zSector_Actvity in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """
    class Config:
        model = models.zSectorActvity
        model_fields = "__all__"



class zSettlementsOut(ModelSchema):
    """
    Originally sourced from zSettlements in /home/josh/PNDS_Interim_MIS-Data.accdb (2829 records)
    """
    class Config:
        model = models.zSettlements
        model_fields = "__all__"



class zSubSectorOut(ModelSchema):
    """
    Originally sourced from zSub_Sector in /home/josh/PNDS_Interim_MIS-Data.accdb (23 records)
    """
    class Config:
        model = models.zSubSector
        model_fields = "__all__"



class zSubprojectStatusOut(ModelSchema):
    """
    Originally sourced from zSubproject_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.zSubprojectStatus
        model_fields = "__all__"



class zSubprojectStatus1Out(ModelSchema):
    """
    Originally sourced from zSubprojectStatus in /home/josh/PNDS_Interim_MIS-Data.accdb (7 records)
    """
    class Config:
        model = models.zSubprojectStatus1
        model_fields = "__all__"



class zSucophaseOut(ModelSchema):
    """
    Originally sourced from zSuco_phase in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.zSucophase
        model_fields = "__all__"



class zSucoStatusOut(ModelSchema):
    """
    Originally sourced from zSuco_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """
    class Config:
        model = models.zSucoStatus
        model_fields = "__all__"



class zTetumtranslationOut(ModelSchema):
    """
    Originally sourced from zTetum_translation in /home/josh/PNDS_Interim_MIS-Data.accdb (606 records)
    """
    class Config:
        model = models.zTetumtranslation
        model_fields = "__all__"



class zTetumtranslationOLDOut(ModelSchema):
    """
    Originally sourced from zTetum_translation_OLD in /home/josh/PNDS_Interim_MIS-Data.accdb (569 records)
    """
    class Config:
        model = models.zTetumtranslationOLD
        model_fields = "__all__"



class zTransMetatablesOut(ModelSchema):
    """
    Originally sourced from zTrans_Meta_tables in /home/josh/PNDS_Interim_MIS-Data.accdb (50 records)
    """
    class Config:
        model = models.zTransMetatables
        model_fields = "__all__"



class zUnitsOut(ModelSchema):
    """
    Originally sourced from zUnits in /home/josh/PNDS_Interim_MIS-Data.accdb (9 records)
    """
    class Config:
        model = models.zUnits
        model_fields = "__all__"



class zYearsOut(ModelSchema):
    """
    Originally sourced from zYears in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.zYears
        model_fields = "__all__"



class DataSyncLogOut(ModelSchema):
    """
    Originally sourced from Data_Sync_Log in /home/josh/PNDS_Interim_MIS-Data.accdb (4375 records)
    """
    class Config:
        model = models.DataSyncLog
        model_fields = "__all__"



class ImportToSQLOut(ModelSchema):
    """
    Originally sourced from ImportToSQL in /home/josh/PNDS_Interim_MIS-Data.accdb (1 records)
    """
    class Config:
        model = models.ImportToSQL
        model_fields = "__all__"



class SubprojectPhysicalProgressOut(ModelSchema):
    """
    Originally sourced from Subproject_Physical_Progress in /home/josh/PNDS_Interim_MIS-Data.accdb (25395 records)
    """
    class Config:
        model = models.SubprojectPhysicalProgress
        model_fields = "__all__"



class SucosubprojectadditonalinfoOut(ModelSchema):
    """
    Originally sourced from Suco_subproject_additonal_info in /home/josh/PNDS_Interim_MIS-Data.accdb (73 records)
    """
    class Config:
        model = models.Sucosubprojectadditonalinfo
        model_fields = "__all__"



class ValidmonthlyreportsOut(ModelSchema):
    """
    Originally sourced from Valid_monthly_reports in /home/josh/PNDS_Interim_MIS-Data.accdb (61 records)
    """
    class Config:
        model = models.Validmonthlyreports
        model_fields = "__all__"



class zFinanceMonitorsOut(ModelSchema):
    """
    Originally sourced from zFinance_Monitors in /home/josh/PNDS_Interim_MIS-Data.accdb (4 records)
    """
    class Config:
        model = models.zFinanceMonitors
        model_fields = "__all__"



class zOperationBudgetStatusOut(ModelSchema):
    """
    Originally sourced from zOperationBudget_Status in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """
    class Config:
        model = models.zOperationBudgetStatus
        model_fields = "__all__"



class zReportformatOut(ModelSchema):
    """
    Originally sourced from zReport_format in /home/josh/PNDS_Interim_MIS-Data.accdb (3 records)
    """
    class Config:
        model = models.zReportformat
        model_fields = "__all__"



class zSubdistrictPhaseOut(ModelSchema):
    """
    Originally sourced from zSubdistrict_Phase in /home/josh/PNDS_Interim_MIS-Data.accdb (104 records)
    """
    class Config:
        model = models.zSubdistrictPhase
        model_fields = "__all__"



class zTransmetafieldsOut(ModelSchema):
    """
    Originally sourced from zTrans_meta_fields in /home/josh/PNDS_Interim_MIS-Data.accdb (548 records)
    """
    class Config:
        model = models.zTransmetafields
        model_fields = "__all__"



class zDistrictOut(ModelSchema):
    """
    Originally sourced from zDistrict in /home/josh/PNDS_Interim_MIS-Data.accdb (14 records)
    """
    class Config:
        model = models.zDistrict
        model_fields = "__all__"



class zSubdistrictOut(ModelSchema):
    """
    Originally sourced from zSubdistrict in /home/josh/PNDS_Interim_MIS-Data.accdb (67 records)
    """
    class Config:
        model = models.zSubdistrict
        model_fields = "__all__"



class zSucoOut(ModelSchema):
    """
    Originally sourced from zSuco in /home/josh/PNDS_Interim_MIS-Data.accdb (452 records)
    """
    class Config:
        model = models.zSuco
        model_fields = "__all__"



class SucoFundingSourcesOut(ModelSchema):
    """
    Originally sourced from SucoFundingSources in /home/josh/PNDS_Interim_MIS-Data.accdb (1524 records)
    """
    class Config:
        model = models.SucoFundingSources
        model_fields = "__all__"



class zFundingSourcesOut(ModelSchema):
    """
    Originally sourced from zFundingSources in /home/josh/PNDS_Interim_MIS-Data.accdb (2 records)
    """
    class Config:
        model = models.zFundingSources
        model_fields = "__all__"

