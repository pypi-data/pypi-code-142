from .test_system import service_url, system_url
from ..client import Client, Pipe
from ..system import SystemClient, read_layer_profile
from ..service import ServiceClient


profile_token = 'model_extend:492cea:1994c52ca0d97c82a992277a77362c94cab7d6702beadf64018dc0c4dc41351c00492cea000000000000000000000000638bd8fa7ffffffe00b0897f9785744cccec7fbd367b79f6996b384e8a;main_full:1ffffff:1994c52ca0d97c82a992277a77362c94aa264f4deab2f2295dedd2ab69cd8fe101ffffff000000000000000000000000638bd8fa7ffffffe0068a84df39a458818c7bf5b5515353cbeef7482e5;main_read:4924ea:1994c52ca0d97c82a992277a77362c9436f8c3fb16e9ea09f723a0c8df48530c004924ea000000000000000000000000638bd8fa7ffffffe00fd9f0156850f3f3f94b0a51d52bf680167492284,1994c52ca0d97c82a992277a77362c94aa264f4deab2f2295dedd2ab69cd8fe1004924ea000000000000000000000000638bd8fa7ffffffe00701005aa230c693d84d6dd62a0bd86261157ed99'
service_token = 'GZTFLKDZfIKpkid6dzYslPrYi2MAAAAA____fwABAAUAAAAFKi8qLyozmlWh2hYt8SYRpUtZMjdsRtdfUg'

service_url_loc = service_url
system_url_loc = system_url


def test_client__load_universe():
    client = Client(ServiceClient(service_url_loc), SystemClient(system_url_loc))
    client.service_client.set_token(service_token)
    client.system_client.set_layer_profile(read_layer_profile(profile_token))
    univ = client.service_client.load_universe('my_universe_1')

    pipe = Pipe('on base.object -> @id')
    app = client.get_objects(pipe)
    print(app)

    # client.system_client.delete_object();

    # pipe = Pipe('$getItem')
    # items = client.get_objects(pipe)
    # for item in items:
    #     print(item)
    #
    # print()
    #
    # pipe = Pipe('$getItem').order('name')
    # items = client.get_objects(pipe)
    # for item in items:
    #     print(item)
    #
    # print()
    #
    # pipe = Pipe('$getItem').order('id')
    # items = client.get_objects(pipe)
    # for item in items:
    #     print(item)
    #
    # print()
    #
    # pipe = Pipe('$getItem').order('itemId')
    # items = client.get_objects(pipe)
    # for item in items:
    #     print(item)

    # items = get_item_pipe.model('item').filter('itemId', 'eq', '7743023').get_objects()
    # print(items)

    # print()
    #
    # pipe = Pipe('$getItem').filter('itemId', 'eq', '7743023')
    # items = client.get_objects(pipe)
    # for item in items:
    #     print(item)

    # print()
    #
    # pipe = Pipe('$putCrawljob')
    # crawljob = client.put_object(pipe, {'running': True})
    # print(crawljob)

    # items = get_item_pipe.model('item').filter('itemId', 'eq', '7743023').get_objects()
    # print(items)


    # Pipe(client, 'on item [name = %name] -> %node').params(name="Test", node=Pipe())