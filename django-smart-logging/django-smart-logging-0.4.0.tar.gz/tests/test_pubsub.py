import time

import pytest
from smart_logging.pubsub import Subscriber
from smart_logging.signals import message_received


def wait_until(condition, *args, timeout=1, interval=1):
    start = time.time()
    while not condition(*args) and (time.time() - start < timeout):
        time.sleep(interval)


@pytest.fixture
def client():
    listener = Subscriber()
    yield listener
    listener.stop()


def test_thread(client: Subscriber):
    client.start()
    assert client.is_alive()
    client.stop(1)
    assert not client.is_alive()


def test_ignore_double_start(client: Subscriber):
    client.start()
    assert client.is_alive()
    client.start()
    assert client.is_alive()


def test_thread_main_thread_terminated(client: Subscriber):
    client.start()
    client.main_thread_terminated()
    assert not client.is_alive()


def test_pub_sub(client: Subscriber):
    message_processed = False
    publisher = Subscriber()

    def on_message(sender, **kwargs):
        nonlocal message_processed
        message_processed = True

    message_received.connect(on_message)

    publisher.notify({"logger": "root"})
    wait_until(lambda: message_processed, timeout=30, interval=5)

    assert message_processed
