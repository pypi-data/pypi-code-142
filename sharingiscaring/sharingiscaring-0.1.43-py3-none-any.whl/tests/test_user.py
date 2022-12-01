import pytest
from pathlib import Path
import json
from unittest.mock import Mock
from sharingiscaring.transaction import Transaction
from sharingiscaring.node import ConcordiumNode
from sharingiscaring.tooter import Tooter
from sharingiscaring.cns import CNSActions
from sharingiscaring.user import User

# @pytest.fixture
# def tooter():
#     return Tooter('','','','','')


@pytest.fixture
def node():
    return ConcordiumNode(Tooter('','','','',''))

def read_block_information(blockHeight):
    p = Path('tests')
    
    with open(p / 'blocks' / f'{blockHeight}' / 'blockInfo', 'r') as f:   
            blockInfo = json.load(f)
    with open(p / 'blocks' / f'{blockHeight}' / 'blockSummary', 'r') as f:    
            blockSummary = json.load(f)
    
    block = {'blockInfo': blockInfo, 'blockSummary': blockSummary}
    return block

def get_tx_at_index(node, blockHeight, index):
    block = read_block_information (blockHeight)
    if 'transactionSummaries' in block['blockSummary']:
        tx_by_index = {x['index']: x for x in  block['blockSummary']['transactionSummaries']}
        tx_at_index = tx_by_index[index]
        tx_at_index.update({'blockInfo': block['blockInfo']})
        return Transaction(node).init_from_node(tx_at_index)
    else:
        return None

def test_user_1(node: ConcordiumNode):
    user = User()
    user.perform_subscription_logic(node)
    
    assert user.subscription.site_active == False
    assert user.subscription.bot_active == False

def test_user_1(node: ConcordiumNode):
    user = User()
    user.set_count_messages = 100
    user.perform_subscription_logic(node)
    
    assert user.subscription.site_active == False
    assert user.subscription.bot_active == False