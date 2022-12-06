from django.contrib import admin
from . import models


@admin.register(models.ActivityBlackListed)
class ActivityBlackListedAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.ActivityBlackListed._meta.fields]


@admin.register(models.DataSyncLogTemp)
class DataSyncLogTempAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.DataSyncLogTemp._meta.fields]


@admin.register(models.Documentsandpictures)
class DocumentsandpicturesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.Documentsandpictures._meta.fields]


@admin.register(models.FinanceMonitoring)
class FinanceMonitoringAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.FinanceMonitoring._meta.fields]


@admin.register(models.Freebalancetranslationcodes)
class FreebalancetranslationcodesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.Freebalancetranslationcodes._meta.fields]


@admin.register(models.GoogleTransfers)
class GoogleTransfersAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.GoogleTransfers._meta.fields]


@admin.register(models.Monthlyreports)
class MonthlyreportsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.Monthlyreports._meta.fields]


@admin.register(models.MonthlyreportsInfrastructure)
class MonthlyreportsInfrastructureAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.MonthlyreportsInfrastructure._meta.fields]


@admin.register(models.zCMTPositions)
class zCMTPositionsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zCMTPositions._meta.fields]


@admin.register(models.OperationBudget)
class OperationBudgetAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.OperationBudget._meta.fields]


@admin.register(models.PhaseCycle)
class PhaseCycleAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.PhaseCycle._meta.fields]


@admin.register(models.SubprojectOutputs)
class SubprojectOutputsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SubprojectOutputs._meta.fields]


@admin.register(models.SucoActvities)
class SucoActvitiesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoActvities._meta.fields]


@admin.register(models.SucoCycles)
class SucoCyclesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoCycles._meta.fields]


@admin.register(models.SucoFinancialDisbursements)
class SucoFinancialDisbursementsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoFinancialDisbursements._meta.fields]


@admin.register(models.SucoFinancialinfo)
class SucoFinancialinfoAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoFinancialinfo._meta.fields]


@admin.register(models.SucoInfrastructureProjectReport)
class SucoInfrastructureProjectReportAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoInfrastructureProjectReport._meta.fields]


@admin.register(models.SucoOperationalReport)
class SucoOperationalReportAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoOperationalReport._meta.fields]


@admin.register(models.SucoPriorities)
class SucoPrioritiesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoPriorities._meta.fields]


@admin.register(models.SucoSubProject)
class SucoSubProjectAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoSubProject._meta.fields]


@admin.register(models.SucoCMTMembers)
class SucoCMTMembersAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoCMTMembers._meta.fields]


@admin.register(models.syncImportLog)
class syncImportLogAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.syncImportLog._meta.fields]


@admin.register(models.SystemInfo)
class SystemInfoAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SystemInfo._meta.fields]


@admin.register(models.Systemlog)
class SystemlogAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.Systemlog._meta.fields]


@admin.register(models.Transfers)
class TransfersAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.Transfers._meta.fields]


@admin.register(models.Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.Users._meta.fields]


@admin.register(models.Usersold)
class UsersoldAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.Usersold._meta.fields]


@admin.register(models.UserTracking)
class UserTrackingAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.UserTracking._meta.fields]


@admin.register(models.zActivities)
class zActivitiesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zActivities._meta.fields]


@admin.register(models.zActivityDocumenttype)
class zActivityDocumenttypeAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zActivityDocumenttype._meta.fields]


@admin.register(models.zActivitytype)
class zActivitytypeAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zActivitytype._meta.fields]


@admin.register(models.zAldeia)
class zAldeiaAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zAldeia._meta.fields]


@admin.register(models.zCategories)
class zCategoriesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zCategories._meta.fields]


@admin.register(models.zCMTPositions1)
class zCMTPositions1Admin(admin.ModelAdmin):
    list_display = [n.name for n in models.zCMTPositions1._meta.fields]


@admin.register(models.zCycles)
class zCyclesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zCycles._meta.fields]


@admin.register(models.zCycleStatus)
class zCycleStatusAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zCycleStatus._meta.fields]


@admin.register(models.zDistrictPhase)
class zDistrictPhaseAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zDistrictPhase._meta.fields]


@admin.register(models.zDocumentfiletype)
class zDocumentfiletypeAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zDocumentfiletype._meta.fields]


@admin.register(models.zDocumenttype)
class zDocumenttypeAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zDocumenttype._meta.fields]


@admin.register(models.zElectionRound)
class zElectionRoundAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zElectionRound._meta.fields]


@admin.register(models.zFinancedisbursementrules)
class zFinancedisbursementrulesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zFinancedisbursementrules._meta.fields]


@admin.register(models.zFinancedisbursementtype)
class zFinancedisbursementtypeAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zFinancedisbursementtype._meta.fields]


@admin.register(models.zFinancialdisbursementactitvites)
class zFinancialdisbursementactitvitesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zFinancialdisbursementactitvites._meta.fields]


@admin.register(models.zFreebalanceBudgetextract)
class zFreebalanceBudgetextractAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zFreebalanceBudgetextract._meta.fields]


@admin.register(models.zGender)
class zGenderAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zGender._meta.fields]


@admin.register(models.zGroups)
class zGroupsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zGroups._meta.fields]


@admin.register(models.zIndicators)
class zIndicatorsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zIndicators._meta.fields]


@admin.register(models.zLanguage)
class zLanguageAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zLanguage._meta.fields]


@admin.register(models.zLastID)
class zLastIDAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zLastID._meta.fields]


@admin.register(models.zOutputs)
class zOutputsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zOutputs._meta.fields]


@admin.register(models.zOutputUnit)
class zOutputUnitAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zOutputUnit._meta.fields]


@admin.register(models.zPNDSFreebalancetranslation)
class zPNDSFreebalancetranslationAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zPNDSFreebalancetranslation._meta.fields]


@admin.register(models.zPriorities)
class zPrioritiesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zPriorities._meta.fields]


@admin.register(models.zProgramActivity)
class zProgramActivityAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zProgramActivity._meta.fields]


@admin.register(models.zProgramActivitylevel)
class zProgramActivitylevelAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zProgramActivitylevel._meta.fields]


@admin.register(models.zProgramactivtytype)
class zProgramactivtytypeAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zProgramactivtytype._meta.fields]


@admin.register(models.zReporttype)
class zReporttypeAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zReporttype._meta.fields]


@admin.register(models.zSector)
class zSectorAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSector._meta.fields]


@admin.register(models.zSectorActvity)
class zSectorActvityAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSectorActvity._meta.fields]


@admin.register(models.zSettlements)
class zSettlementsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSettlements._meta.fields]


@admin.register(models.zSubSector)
class zSubSectorAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSubSector._meta.fields]


@admin.register(models.zSubprojectStatus)
class zSubprojectStatusAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSubprojectStatus._meta.fields]


@admin.register(models.zSubprojectStatus1)
class zSubprojectStatus1Admin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSubprojectStatus1._meta.fields]


@admin.register(models.zSucophase)
class zSucophaseAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSucophase._meta.fields]


@admin.register(models.zSucoStatus)
class zSucoStatusAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSucoStatus._meta.fields]


@admin.register(models.zTetumtranslation)
class zTetumtranslationAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zTetumtranslation._meta.fields]


@admin.register(models.zTetumtranslationOLD)
class zTetumtranslationOLDAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zTetumtranslationOLD._meta.fields]


@admin.register(models.zTransMetatables)
class zTransMetatablesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zTransMetatables._meta.fields]


@admin.register(models.zUnits)
class zUnitsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zUnits._meta.fields]


@admin.register(models.zYears)
class zYearsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zYears._meta.fields]


@admin.register(models.DataSyncLog)
class DataSyncLogAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.DataSyncLog._meta.fields]


@admin.register(models.ImportToSQL)
class ImportToSQLAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.ImportToSQL._meta.fields]


@admin.register(models.SubprojectPhysicalProgress)
class SubprojectPhysicalProgressAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SubprojectPhysicalProgress._meta.fields]


@admin.register(models.Sucosubprojectadditonalinfo)
class SucosubprojectadditonalinfoAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.Sucosubprojectadditonalinfo._meta.fields]


@admin.register(models.Validmonthlyreports)
class ValidmonthlyreportsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.Validmonthlyreports._meta.fields]


@admin.register(models.zFinanceMonitors)
class zFinanceMonitorsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zFinanceMonitors._meta.fields]


@admin.register(models.zOperationBudgetStatus)
class zOperationBudgetStatusAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zOperationBudgetStatus._meta.fields]


@admin.register(models.zReportformat)
class zReportformatAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zReportformat._meta.fields]


@admin.register(models.zSubdistrictPhase)
class zSubdistrictPhaseAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSubdistrictPhase._meta.fields]


@admin.register(models.zTransmetafields)
class zTransmetafieldsAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zTransmetafields._meta.fields]


@admin.register(models.zDistrict)
class zDistrictAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zDistrict._meta.fields]


@admin.register(models.zSubdistrict)
class zSubdistrictAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSubdistrict._meta.fields]


@admin.register(models.zSuco)
class zSucoAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zSuco._meta.fields]


@admin.register(models.SucoFundingSources)
class SucoFundingSourcesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.SucoFundingSources._meta.fields]


@admin.register(models.zFundingSources)
class zFundingSourcesAdmin(admin.ModelAdmin):
    list_display = [n.name for n in models.zFundingSources._meta.fields]

