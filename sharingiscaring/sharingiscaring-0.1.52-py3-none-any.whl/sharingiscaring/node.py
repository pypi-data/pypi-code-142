from pydantic import BaseModel, Extra

class ConcordiumNodeFromDashboard(BaseModel):
    nodeName: str
    nodeId: str
    peerType: str
    uptime: int
    client: str
    averagePing: float
    peersCount: int
    peersList: list
    bestBlock: str
    bestBlockHeight: int
    bestBlockBakerId: int
    bestArrivedTime: str
    blockArrivePeriodEMA: float
    blockArrivePeriodEMSD: float
    blockArriveLatencyEMA: float
    blockArriveLatencyEMSD: float
    blockReceivePeriodEMA: float
    blockReceivePeriodEMSD: float
    blockReceiveLatencyEMA: float
    blockReceiveLatencyEMSD: float
    finalizedBlock: str
    finalizedBlockHeight: int
    finalizedTime: str
    finalizationPeriodEMA: float
    finalizationPeriodEMSD: float
    packetsSent: int
    packetsReceived: int
    consensusRunning: bool
    bakingCommitteeMember: str
    consensusBakerId: int
    finalizationCommitteeMember: bool
    transactionsPerBlockEMA: float
    transactionsPerBlockEMSD: float
    bestBlockTransactionsSize: int
    bestBlockTotalEncryptedAmount: str = None
    bestBlockTotalAmount: str = None
    bestBlockTransactionCount: int = None
    bestBlockTransactionEnergyCost: int = None
    bestBlockExecutionCost: float = None
    bestBlockCentralBankAmount: str = None
    blocksReceivedCount: int
    blocksVerifiedCount: int
    genesisBlock: str
    finalizationCount: int
    finalizedBlockParent: str
    averageBytesPerSecondIn: int
    averageBytesPerSecondOut: int
  