from django.core.management import call_command


def test_command_log():
    call_command("log", "root")


def test_command_log_level():
    call_command("log", "root", "--level=INFO")


def test_command_log_propagate():
    call_command("log", "root", "--propagate=on")


def test_command_log_one_handler():
    call_command("log", "root", "--handler=console")


def test_command_log_multi_handlers():
    call_command("log", "root", "--handler=console", "--handler=console1")
