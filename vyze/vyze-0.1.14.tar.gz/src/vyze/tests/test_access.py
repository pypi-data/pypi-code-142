from src.vyze import read_layer_token, AccessGroup, read_access_group, read_layer_profile


def test_read_layer_token__1():
    token = read_layer_token('1994c52ca0d97c82a992277a77362c94b369c56ebba89d8bd84f8744e69f15be01ffffff0000000000000000000000006376b8097ffffffe001692900d88a8df58de060b3d5a383520ede9a1c4')
    assert token.user_id == '1994c52ca0d97c82a992277a77362c94'
    assert token.layer_id == 'b369c56ebba89d8bd84f8744e69f15be'
    assert token.granted == 33554431
    # assert token._created.timestamp() == 1656063581
    # assert token._expiry.seconds == 86399
    assert token.expires.timestamp() == 3816208391
    assert token.signature.hex() == '0d88a8df58de060b3d5a383520ede9a1'
    assert token.token == '1994c52ca0d97c82a992277a77362c94b369c56ebba89d8bd84f8744e69f15be01ffffff0000000000000000000000006376b8097ffffffe001692900d88a8df58de060b3d5a383520ede9a1c4'


def test_access_group():
    ag = AccessGroup('ag1', 0)
    tk1 = read_layer_token('1994c52ca0d97c82a992277a77362c94b369c56ebba89d8bd84f8744e69f15be01ffffff0000000000000000000000006376b8097ffffffe001692900d88a8df58de060b3d5a383520ede9a1c4')
    tk2 = read_layer_token('1994c52ca0d97c82a992277a77362c94c95f6399b88ee7893ed44371dc96deed01ffffff0000000000000000000000006376b8097ffffffe0004713ebed68cad89738aeaf08294c14fc676917b')
    ag.register_layer_token(tk1)
    ag.register_layer_token(tk2)
    assert len(ag.layer_tokens) == 2
    ag.unregister_layer_token(tk2.token)
    assert len(ag.layer_tokens) == 1


def test_access_group_string():
    ags = 'test:1ffffff:1994c52ca0d97c82a992277a77362c94b369c56ebba89d8bd84f8744e69f15be01ffffff0000000000000000000000006376b8097ffffffe001692900d88a8df58de060b3d5a383520ede9a1c4,' \
          '1994c52ca0d97c82a992277a77362c94c95f6399b88ee7893ed44371dc96deed01ffffff0000000000000000000000006376b8097ffffffe0004713ebed68cad89738aeaf08294c14fc676917b'
    ag = read_access_group(ags)
    assert str(ag) == ags


def test_layer_profile_string():
    lps = 'model_full:1ffffff:1994c52ca0d97c82a992277a77362c94b369c56ebba89d8bd84f8744e69f15be01ffffff0000000000000000000000006376b8097ffffffe001692900d88a8df58de060b3d5a383520ede9a1c4;' \
          'main_full:1ffffff:1994c52ca0d97c82a992277a77362c94c95f6399b88ee7893ed44371dc96deed01ffffff0000000000000000000000006376b8097ffffffe0004713ebed68cad89738aeaf08294c14fc676917b'
    lp = read_layer_profile(lps)
    assert lp._access_groups['model_full']
    assert lp._access_groups['main_full']
