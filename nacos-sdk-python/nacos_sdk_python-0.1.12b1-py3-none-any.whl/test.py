from nacos import NacosClient

if __name__ == "__main__":
        server_addresses = "12341234"
        endpoint = "http://acm.aliyun.com:8080/diamond-server/diamond"
        namespace = "03708ada-fb86-4f38-91fa-45b4c33dcaaf"
        ak = "LTAI5tP9HQTuX88Ng7NjazTS"
        sk = "aHcQVTtgK6si6rFLVT6hk7Uvt1NFXu"
        nacos_client = NacosClient(server_addresses, endpoint, namespace, ak, sk)
        nacos_client.publish_config("test-sun", "test_group", "test_content")
        content = nacos_client.get_config("test-sun", "test_group")
        print(content)
