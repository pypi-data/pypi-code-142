# # import unittest
# from src.sdk import Sdk


# sdk = Sdk()
# # print(sdk.login(refresh=True))
# # print(sdk.login(refresh=False))

# # sdk2 = Sdk()

# # print(sdk.login(refresh=True))
# # print(sdk.login(refresh=False))

# # print(sdk.is_bancked(20312528046))
# # print(sdk.is_bancked(20111111112))
# # print(sdk.is_bancked(99999999999))

# # print(sdk.get_views())
# # print(sdk.get_accounts())
# # print(sdk.get_account("21-1-99999-4-6"))
# # from src.querys.account_movements_query import AccountMovementsQuery

# # amq = AccountMovementsQuery(obp_categories="culo")
# # print(amq.get_query())
# # amq = AccountMovementsQuery()
# # print(amq.get_query())
# # print(sdk.get_account_movements("21-1-99999-4-6"))
# # print(sdk.get_account_details_by_alias("aliasDeCbuValido"))
# # print(sdk.get_account_by_details_cbu_cvu("3220001801000020816200"))

# # print(sdk.get_account_by_details_cbu_cvu("0000033802019012400010"))
# from src.options.currency import Currency

# from src.options.concept import Concept

# from src.requests_payload.transfer_payload import TransferPayload
# tpl = TransferPayload("coco1", "ELBARBACVU", Currency.ARS.value, 1000.21, "taest", Concept.ALQ.value, ["coco@gmail.com", "cacho@coco.com"])
# print(tpl.to_json())
# tpl = TransferPayload("coco1", "3220001801000020816200", Currency.ARS.value, 1000.21, "taest", Concept.CUO.value, ["coco@gmail.com", "cacho@coco.com"])
# print(tpl.to_json())

# print(sdk.send_transfer(tpl.to_json(), "21-1-99999-4-6"))
