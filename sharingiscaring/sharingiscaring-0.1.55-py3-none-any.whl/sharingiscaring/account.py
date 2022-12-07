from pydantic import BaseModel, Extra
from sharingiscaring.pool import PoolInfo, APY

class AccountBakerPool(BaseModel):
    delegatorCount: int
    delegatedStake: int
    totalStake: int
    apy_30: APY
    apy_7: APY
class AccountBakerState(BaseModel):
    pool: AccountBakerPool = None
class AccountBakerFromCCDScan(BaseModel):
    state: AccountBakerState
    
class AccountBaker(BaseModel):
    bakerAggregationVerifyKey: str
    bakerElectionVerifyKey: str
    bakerId: int
    bakerPoolInfo: PoolInfo
    bakerSignatureVerifyKey: str
    restakeEarnings: bool
    stakedAmount: str
    
class AccountReleaseScheduleNodes(BaseModel):
    nodes: list

class AccountReleaseScheduleFromCCDScan(BaseModel):
    schedule: AccountReleaseScheduleNodes
    totalAmount: int
class AccountReleaseSchedule(BaseModel):
    schedule: list
    total: str
    
    
class DelegationTarget(BaseModel, extra=Extra.ignore):
    bakerId: int = None
    delegateType: str = None
    
class AccountDelegation(BaseModel):
    delegationTarget: DelegationTarget
    delegatorId: int = None
    restakeEarnings: bool
    stakedAmount: str

class ConcordiumAccountFromClient(BaseModel, extra=Extra.ignore):
    accountAddress: str
    accountAmount: str
    accountBaker: AccountBaker = None
    accountDelegation: AccountDelegation = None
    accountEncryptionKey: str
    accountIndex: int
    accountNonce: int
    accountReleaseSchedule: AccountReleaseSchedule
    accountThreshold: int

class Address(BaseModel):
    asString: str
class ConcordiumAccountFromCCDScan(BaseModel):
    createdAt: str
    id: str
    transactionCount: int
    amount: int
    address: Address
    delegation: AccountDelegation = None
    baker: AccountBakerFromCCDScan = None
    releaseSchedule: AccountReleaseScheduleFromCCDScan

class RewardAmount(BaseModel):
    sumRewardAmount: int
class ConcordiumAccountRewards(BaseModel):
    LAST24_HOURS: RewardAmount
    LAST7_DAYS: RewardAmount
    LAST30_DAYS: RewardAmount

class ConcordiumAccount(BaseModel):
    via_client:     ConcordiumAccountFromClient    = None
    via_ccdscan:    ConcordiumAccountFromCCDScan   = None
    rewards:        ConcordiumAccountRewards       = None
# TODO: config extra ignore