from typing import List, Optional, Type
from http import HTTPStatus
from ninja import ModelSchema, NinjaAPI

from . import models
from . import base_models
from . import schema


api = NinjaAPI()

def _get_pk(model: Type[models.Model]) -> models.Field:
    for field in model._meta.fields:
        if getattr(field, "primary_key", False) is True:
            return field
    raise KeyError("No primary key?")



@api.post("/ActivityBlackListed", response={HTTPStatus.CREATED: schema.ActivityBlackListedOut, HTTPStatus.OK: schema.ActivityBlackListedOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_ActivityBlackListed(request, data: base_models.ActivityBlackListedIn):
    model = models.ActivityBlackListed
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/DataSyncLogTemp", response={HTTPStatus.CREATED: schema.DataSyncLogTempOut, HTTPStatus.OK: schema.DataSyncLogTempOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_DataSyncLogTemp(request, data: base_models.DataSyncLogTempIn):
    model = models.DataSyncLogTemp
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/Documentsandpictures", response={HTTPStatus.CREATED: schema.DocumentsandpicturesOut, HTTPStatus.OK: schema.DocumentsandpicturesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_Documentsandpictures(request, data: base_models.DocumentsandpicturesIn):
    model = models.Documentsandpictures
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/FinanceMonitoring", response={HTTPStatus.CREATED: schema.FinanceMonitoringOut, HTTPStatus.OK: schema.FinanceMonitoringOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_FinanceMonitoring(request, data: base_models.FinanceMonitoringIn):
    model = models.FinanceMonitoring
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/Freebalancetranslationcodes", response={HTTPStatus.CREATED: schema.FreebalancetranslationcodesOut, HTTPStatus.OK: schema.FreebalancetranslationcodesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_Freebalancetranslationcodes(request, data: base_models.FreebalancetranslationcodesIn):
    model = models.Freebalancetranslationcodes
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/GoogleTransfers", response={HTTPStatus.CREATED: schema.GoogleTransfersOut, HTTPStatus.OK: schema.GoogleTransfersOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_GoogleTransfers(request, data: base_models.GoogleTransfersIn):
    model = models.GoogleTransfers
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/Monthlyreports", response={HTTPStatus.CREATED: schema.MonthlyreportsOut, HTTPStatus.OK: schema.MonthlyreportsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_Monthlyreports(request, data: base_models.MonthlyreportsIn):
    model = models.Monthlyreports
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/MonthlyreportsInfrastructure", response={HTTPStatus.CREATED: schema.MonthlyreportsInfrastructureOut, HTTPStatus.OK: schema.MonthlyreportsInfrastructureOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_MonthlyreportsInfrastructure(request, data: base_models.MonthlyreportsInfrastructureIn):
    model = models.MonthlyreportsInfrastructure
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zCMTPositions", response={HTTPStatus.CREATED: schema.zCMTPositionsOut, HTTPStatus.OK: schema.zCMTPositionsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zCMTPositions(request, data: base_models.zCMTPositionsIn):
    model = models.zCMTPositions
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/OperationBudget", response={HTTPStatus.CREATED: schema.OperationBudgetOut, HTTPStatus.OK: schema.OperationBudgetOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_OperationBudget(request, data: base_models.OperationBudgetIn):
    model = models.OperationBudget
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/PhaseCycle", response={HTTPStatus.CREATED: schema.PhaseCycleOut, HTTPStatus.OK: schema.PhaseCycleOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_PhaseCycle(request, data: base_models.PhaseCycleIn):
    model = models.PhaseCycle
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SubprojectOutputs", response={HTTPStatus.CREATED: schema.SubprojectOutputsOut, HTTPStatus.OK: schema.SubprojectOutputsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SubprojectOutputs(request, data: base_models.SubprojectOutputsIn):
    model = models.SubprojectOutputs
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoActvities", response={HTTPStatus.CREATED: schema.SucoActvitiesOut, HTTPStatus.OK: schema.SucoActvitiesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoActvities(request, data: base_models.SucoActvitiesIn):
    model = models.SucoActvities
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoCycles", response={HTTPStatus.CREATED: schema.SucoCyclesOut, HTTPStatus.OK: schema.SucoCyclesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoCycles(request, data: base_models.SucoCyclesIn):
    model = models.SucoCycles
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoFinancialDisbursements", response={HTTPStatus.CREATED: schema.SucoFinancialDisbursementsOut, HTTPStatus.OK: schema.SucoFinancialDisbursementsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoFinancialDisbursements(request, data: base_models.SucoFinancialDisbursementsIn):
    model = models.SucoFinancialDisbursements
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoFinancialinfo", response={HTTPStatus.CREATED: schema.SucoFinancialinfoOut, HTTPStatus.OK: schema.SucoFinancialinfoOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoFinancialinfo(request, data: base_models.SucoFinancialinfoIn):
    model = models.SucoFinancialinfo
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoInfrastructureProjectReport", response={HTTPStatus.CREATED: schema.SucoInfrastructureProjectReportOut, HTTPStatus.OK: schema.SucoInfrastructureProjectReportOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoInfrastructureProjectReport(request, data: base_models.SucoInfrastructureProjectReportIn):
    model = models.SucoInfrastructureProjectReport
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoOperationalReport", response={HTTPStatus.CREATED: schema.SucoOperationalReportOut, HTTPStatus.OK: schema.SucoOperationalReportOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoOperationalReport(request, data: base_models.SucoOperationalReportIn):
    model = models.SucoOperationalReport
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoPriorities", response={HTTPStatus.CREATED: schema.SucoPrioritiesOut, HTTPStatus.OK: schema.SucoPrioritiesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoPriorities(request, data: base_models.SucoPrioritiesIn):
    model = models.SucoPriorities
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoSubProject", response={HTTPStatus.CREATED: schema.SucoSubProjectOut, HTTPStatus.OK: schema.SucoSubProjectOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoSubProject(request, data: base_models.SucoSubProjectIn):
    model = models.SucoSubProject
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoCMTMembers", response={HTTPStatus.CREATED: schema.SucoCMTMembersOut, HTTPStatus.OK: schema.SucoCMTMembersOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoCMTMembers(request, data: base_models.SucoCMTMembersIn):
    model = models.SucoCMTMembers
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/syncImportLog", response={HTTPStatus.CREATED: schema.syncImportLogOut, HTTPStatus.OK: schema.syncImportLogOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_syncImportLog(request, data: base_models.syncImportLogIn):
    model = models.syncImportLog
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SystemInfo", response={HTTPStatus.CREATED: schema.SystemInfoOut, HTTPStatus.OK: schema.SystemInfoOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SystemInfo(request, data: base_models.SystemInfoIn):
    model = models.SystemInfo
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/Systemlog", response={HTTPStatus.CREATED: schema.SystemlogOut, HTTPStatus.OK: schema.SystemlogOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_Systemlog(request, data: base_models.SystemlogIn):
    model = models.Systemlog
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/Transfers", response={HTTPStatus.CREATED: schema.TransfersOut, HTTPStatus.OK: schema.TransfersOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_Transfers(request, data: base_models.TransfersIn):
    model = models.Transfers
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/Users", response={HTTPStatus.CREATED: schema.UsersOut, HTTPStatus.OK: schema.UsersOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_Users(request, data: base_models.UsersIn):
    model = models.Users
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/Usersold", response={HTTPStatus.CREATED: schema.UsersoldOut, HTTPStatus.OK: schema.UsersoldOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_Usersold(request, data: base_models.UsersoldIn):
    model = models.Usersold
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/UserTracking", response={HTTPStatus.CREATED: schema.UserTrackingOut, HTTPStatus.OK: schema.UserTrackingOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_UserTracking(request, data: base_models.UserTrackingIn):
    model = models.UserTracking
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zActivities", response={HTTPStatus.CREATED: schema.zActivitiesOut, HTTPStatus.OK: schema.zActivitiesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zActivities(request, data: base_models.zActivitiesIn):
    model = models.zActivities
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zActivityDocumenttype", response={HTTPStatus.CREATED: schema.zActivityDocumenttypeOut, HTTPStatus.OK: schema.zActivityDocumenttypeOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zActivityDocumenttype(request, data: base_models.zActivityDocumenttypeIn):
    model = models.zActivityDocumenttype
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zActivitytype", response={HTTPStatus.CREATED: schema.zActivitytypeOut, HTTPStatus.OK: schema.zActivitytypeOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zActivitytype(request, data: base_models.zActivitytypeIn):
    model = models.zActivitytype
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zAldeia", response={HTTPStatus.CREATED: schema.zAldeiaOut, HTTPStatus.OK: schema.zAldeiaOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zAldeia(request, data: base_models.zAldeiaIn):
    model = models.zAldeia
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zCategories", response={HTTPStatus.CREATED: schema.zCategoriesOut, HTTPStatus.OK: schema.zCategoriesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zCategories(request, data: base_models.zCategoriesIn):
    model = models.zCategories
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zCMTPositions1", response={HTTPStatus.CREATED: schema.zCMTPositions1Out, HTTPStatus.OK: schema.zCMTPositions1Out, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zCMTPositions1(request, data: base_models.zCMTPositions1In):
    model = models.zCMTPositions1
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zCycles", response={HTTPStatus.CREATED: schema.zCyclesOut, HTTPStatus.OK: schema.zCyclesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zCycles(request, data: base_models.zCyclesIn):
    model = models.zCycles
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zCycleStatus", response={HTTPStatus.CREATED: schema.zCycleStatusOut, HTTPStatus.OK: schema.zCycleStatusOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zCycleStatus(request, data: base_models.zCycleStatusIn):
    model = models.zCycleStatus
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zDistrictPhase", response={HTTPStatus.CREATED: schema.zDistrictPhaseOut, HTTPStatus.OK: schema.zDistrictPhaseOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zDistrictPhase(request, data: base_models.zDistrictPhaseIn):
    model = models.zDistrictPhase
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zDocumentfiletype", response={HTTPStatus.CREATED: schema.zDocumentfiletypeOut, HTTPStatus.OK: schema.zDocumentfiletypeOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zDocumentfiletype(request, data: base_models.zDocumentfiletypeIn):
    model = models.zDocumentfiletype
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zDocumenttype", response={HTTPStatus.CREATED: schema.zDocumenttypeOut, HTTPStatus.OK: schema.zDocumenttypeOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zDocumenttype(request, data: base_models.zDocumenttypeIn):
    model = models.zDocumenttype
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zElectionRound", response={HTTPStatus.CREATED: schema.zElectionRoundOut, HTTPStatus.OK: schema.zElectionRoundOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zElectionRound(request, data: base_models.zElectionRoundIn):
    model = models.zElectionRound
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zFinancedisbursementrules", response={HTTPStatus.CREATED: schema.zFinancedisbursementrulesOut, HTTPStatus.OK: schema.zFinancedisbursementrulesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zFinancedisbursementrules(request, data: base_models.zFinancedisbursementrulesIn):
    model = models.zFinancedisbursementrules
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zFinancedisbursementtype", response={HTTPStatus.CREATED: schema.zFinancedisbursementtypeOut, HTTPStatus.OK: schema.zFinancedisbursementtypeOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zFinancedisbursementtype(request, data: base_models.zFinancedisbursementtypeIn):
    model = models.zFinancedisbursementtype
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zFinancialdisbursementactitvites", response={HTTPStatus.CREATED: schema.zFinancialdisbursementactitvitesOut, HTTPStatus.OK: schema.zFinancialdisbursementactitvitesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zFinancialdisbursementactitvites(request, data: base_models.zFinancialdisbursementactitvitesIn):
    model = models.zFinancialdisbursementactitvites
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zFreebalanceBudgetextract", response={HTTPStatus.CREATED: schema.zFreebalanceBudgetextractOut, HTTPStatus.OK: schema.zFreebalanceBudgetextractOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zFreebalanceBudgetextract(request, data: base_models.zFreebalanceBudgetextractIn):
    model = models.zFreebalanceBudgetextract
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zGender", response={HTTPStatus.CREATED: schema.zGenderOut, HTTPStatus.OK: schema.zGenderOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zGender(request, data: base_models.zGenderIn):
    model = models.zGender
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zGroups", response={HTTPStatus.CREATED: schema.zGroupsOut, HTTPStatus.OK: schema.zGroupsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zGroups(request, data: base_models.zGroupsIn):
    model = models.zGroups
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zIndicators", response={HTTPStatus.CREATED: schema.zIndicatorsOut, HTTPStatus.OK: schema.zIndicatorsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zIndicators(request, data: base_models.zIndicatorsIn):
    model = models.zIndicators
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zLanguage", response={HTTPStatus.CREATED: schema.zLanguageOut, HTTPStatus.OK: schema.zLanguageOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zLanguage(request, data: base_models.zLanguageIn):
    model = models.zLanguage
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zLastID", response={HTTPStatus.CREATED: schema.zLastIDOut, HTTPStatus.OK: schema.zLastIDOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zLastID(request, data: base_models.zLastIDIn):
    model = models.zLastID
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zOutputs", response={HTTPStatus.CREATED: schema.zOutputsOut, HTTPStatus.OK: schema.zOutputsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zOutputs(request, data: base_models.zOutputsIn):
    model = models.zOutputs
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zOutputUnit", response={HTTPStatus.CREATED: schema.zOutputUnitOut, HTTPStatus.OK: schema.zOutputUnitOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zOutputUnit(request, data: base_models.zOutputUnitIn):
    model = models.zOutputUnit
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zPNDSFreebalancetranslation", response={HTTPStatus.CREATED: schema.zPNDSFreebalancetranslationOut, HTTPStatus.OK: schema.zPNDSFreebalancetranslationOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zPNDSFreebalancetranslation(request, data: base_models.zPNDSFreebalancetranslationIn):
    model = models.zPNDSFreebalancetranslation
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zPriorities", response={HTTPStatus.CREATED: schema.zPrioritiesOut, HTTPStatus.OK: schema.zPrioritiesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zPriorities(request, data: base_models.zPrioritiesIn):
    model = models.zPriorities
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zProgramActivity", response={HTTPStatus.CREATED: schema.zProgramActivityOut, HTTPStatus.OK: schema.zProgramActivityOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zProgramActivity(request, data: base_models.zProgramActivityIn):
    model = models.zProgramActivity
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zProgramActivitylevel", response={HTTPStatus.CREATED: schema.zProgramActivitylevelOut, HTTPStatus.OK: schema.zProgramActivitylevelOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zProgramActivitylevel(request, data: base_models.zProgramActivitylevelIn):
    model = models.zProgramActivitylevel
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zProgramactivtytype", response={HTTPStatus.CREATED: schema.zProgramactivtytypeOut, HTTPStatus.OK: schema.zProgramactivtytypeOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zProgramactivtytype(request, data: base_models.zProgramactivtytypeIn):
    model = models.zProgramactivtytype
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zReporttype", response={HTTPStatus.CREATED: schema.zReporttypeOut, HTTPStatus.OK: schema.zReporttypeOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zReporttype(request, data: base_models.zReporttypeIn):
    model = models.zReporttype
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSector", response={HTTPStatus.CREATED: schema.zSectorOut, HTTPStatus.OK: schema.zSectorOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSector(request, data: base_models.zSectorIn):
    model = models.zSector
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSectorActvity", response={HTTPStatus.CREATED: schema.zSectorActvityOut, HTTPStatus.OK: schema.zSectorActvityOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSectorActvity(request, data: base_models.zSectorActvityIn):
    model = models.zSectorActvity
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSettlements", response={HTTPStatus.CREATED: schema.zSettlementsOut, HTTPStatus.OK: schema.zSettlementsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSettlements(request, data: base_models.zSettlementsIn):
    model = models.zSettlements
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSubSector", response={HTTPStatus.CREATED: schema.zSubSectorOut, HTTPStatus.OK: schema.zSubSectorOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSubSector(request, data: base_models.zSubSectorIn):
    model = models.zSubSector
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSubprojectStatus", response={HTTPStatus.CREATED: schema.zSubprojectStatusOut, HTTPStatus.OK: schema.zSubprojectStatusOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSubprojectStatus(request, data: base_models.zSubprojectStatusIn):
    model = models.zSubprojectStatus
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSubprojectStatus1", response={HTTPStatus.CREATED: schema.zSubprojectStatus1Out, HTTPStatus.OK: schema.zSubprojectStatus1Out, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSubprojectStatus1(request, data: base_models.zSubprojectStatus1In):
    model = models.zSubprojectStatus1
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSucophase", response={HTTPStatus.CREATED: schema.zSucophaseOut, HTTPStatus.OK: schema.zSucophaseOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSucophase(request, data: base_models.zSucophaseIn):
    model = models.zSucophase
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSucoStatus", response={HTTPStatus.CREATED: schema.zSucoStatusOut, HTTPStatus.OK: schema.zSucoStatusOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSucoStatus(request, data: base_models.zSucoStatusIn):
    model = models.zSucoStatus
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zTetumtranslation", response={HTTPStatus.CREATED: schema.zTetumtranslationOut, HTTPStatus.OK: schema.zTetumtranslationOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zTetumtranslation(request, data: base_models.zTetumtranslationIn):
    model = models.zTetumtranslation
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zTetumtranslationOLD", response={HTTPStatus.CREATED: schema.zTetumtranslationOLDOut, HTTPStatus.OK: schema.zTetumtranslationOLDOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zTetumtranslationOLD(request, data: base_models.zTetumtranslationOLDIn):
    model = models.zTetumtranslationOLD
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zTransMetatables", response={HTTPStatus.CREATED: schema.zTransMetatablesOut, HTTPStatus.OK: schema.zTransMetatablesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zTransMetatables(request, data: base_models.zTransMetatablesIn):
    model = models.zTransMetatables
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zUnits", response={HTTPStatus.CREATED: schema.zUnitsOut, HTTPStatus.OK: schema.zUnitsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zUnits(request, data: base_models.zUnitsIn):
    model = models.zUnits
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zYears", response={HTTPStatus.CREATED: schema.zYearsOut, HTTPStatus.OK: schema.zYearsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zYears(request, data: base_models.zYearsIn):
    model = models.zYears
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/DataSyncLog", response={HTTPStatus.CREATED: schema.DataSyncLogOut, HTTPStatus.OK: schema.DataSyncLogOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_DataSyncLog(request, data: base_models.DataSyncLogIn):
    model = models.DataSyncLog
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/ImportToSQL", response={HTTPStatus.CREATED: schema.ImportToSQLOut, HTTPStatus.OK: schema.ImportToSQLOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_ImportToSQL(request, data: base_models.ImportToSQLIn):
    model = models.ImportToSQL
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SubprojectPhysicalProgress", response={HTTPStatus.CREATED: schema.SubprojectPhysicalProgressOut, HTTPStatus.OK: schema.SubprojectPhysicalProgressOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SubprojectPhysicalProgress(request, data: base_models.SubprojectPhysicalProgressIn):
    model = models.SubprojectPhysicalProgress
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/Sucosubprojectadditonalinfo", response={HTTPStatus.CREATED: schema.SucosubprojectadditonalinfoOut, HTTPStatus.OK: schema.SucosubprojectadditonalinfoOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_Sucosubprojectadditonalinfo(request, data: base_models.SucosubprojectadditonalinfoIn):
    model = models.Sucosubprojectadditonalinfo
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/Validmonthlyreports", response={HTTPStatus.CREATED: schema.ValidmonthlyreportsOut, HTTPStatus.OK: schema.ValidmonthlyreportsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_Validmonthlyreports(request, data: base_models.ValidmonthlyreportsIn):
    model = models.Validmonthlyreports
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zFinanceMonitors", response={HTTPStatus.CREATED: schema.zFinanceMonitorsOut, HTTPStatus.OK: schema.zFinanceMonitorsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zFinanceMonitors(request, data: base_models.zFinanceMonitorsIn):
    model = models.zFinanceMonitors
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zOperationBudgetStatus", response={HTTPStatus.CREATED: schema.zOperationBudgetStatusOut, HTTPStatus.OK: schema.zOperationBudgetStatusOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zOperationBudgetStatus(request, data: base_models.zOperationBudgetStatusIn):
    model = models.zOperationBudgetStatus
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zReportformat", response={HTTPStatus.CREATED: schema.zReportformatOut, HTTPStatus.OK: schema.zReportformatOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zReportformat(request, data: base_models.zReportformatIn):
    model = models.zReportformat
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSubdistrictPhase", response={HTTPStatus.CREATED: schema.zSubdistrictPhaseOut, HTTPStatus.OK: schema.zSubdistrictPhaseOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSubdistrictPhase(request, data: base_models.zSubdistrictPhaseIn):
    model = models.zSubdistrictPhase
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zTransmetafields", response={HTTPStatus.CREATED: schema.zTransmetafieldsOut, HTTPStatus.OK: schema.zTransmetafieldsOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zTransmetafields(request, data: base_models.zTransmetafieldsIn):
    model = models.zTransmetafields
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zDistrict", response={HTTPStatus.CREATED: schema.zDistrictOut, HTTPStatus.OK: schema.zDistrictOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zDistrict(request, data: base_models.zDistrictIn):
    model = models.zDistrict
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSubdistrict", response={HTTPStatus.CREATED: schema.zSubdistrictOut, HTTPStatus.OK: schema.zSubdistrictOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSubdistrict(request, data: base_models.zSubdistrictIn):
    model = models.zSubdistrict
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zSuco", response={HTTPStatus.CREATED: schema.zSucoOut, HTTPStatus.OK: schema.zSucoOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zSuco(request, data: base_models.zSucoIn):
    model = models.zSuco
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/SucoFundingSources", response={HTTPStatus.CREATED: schema.SucoFundingSourcesOut, HTTPStatus.OK: schema.SucoFundingSourcesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_SucoFundingSources(request, data: base_models.SucoFundingSourcesIn):
    model = models.SucoFundingSources
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance



@api.post("/zFundingSources", response={HTTPStatus.CREATED: schema.zFundingSourcesOut, HTTPStatus.OK: schema.zFundingSourcesOut, HTTPStatus.BAD_REQUEST: schema.Error})
async def add_zFundingSources(request, data: base_models.zFundingSourcesIn):
    model = models.zFundingSources
    objects = model.objects
    pk_field =  _get_pk(model).name # This is the name of the "primary key" field
    data_for_update = data.dict()
    data_for_update.pop(pk_field)

    instance, created = await objects.aupdate_or_create(
        pk = pk_field,
        defaults=data_for_update
    )

    return instance


