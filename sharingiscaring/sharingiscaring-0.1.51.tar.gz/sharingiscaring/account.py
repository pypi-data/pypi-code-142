# from pydantic import BaseModel
# from sharingiscaring.pool import PoolInfo

# class AccountBaker(BaseModel):
#     bakerAggregationVerifyKey: str
#     bakerElectionVerifyKey: int
#     bakerId: int
#     bakerPoolInfo: PoolInfo
#     bakerSignatureVerifyKey: str
#     restakeEarnings: bool
#     stakedAmount: str
    

# class AccountReleaseSchedule(BaseModel):
#     scehdule: list
#     total: str
    
# class ConcordiumAccount(BaseModel):
#     accountAddress: str
#     accountAmount: str
#     accountBaker: 
#     accountEncryptionKey: str
#     accountIndex: int
#     accountNonce: int
#     accountReleaseSchedule: AccountReleaseSchedule
#     accountThreshold: int

# TODO: config extra ignore