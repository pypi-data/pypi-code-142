import pytest

from py_cover_letters.config import ConfigurationManager
from py_cover_letters.exceptions import ConfigurationError
from tests.factories import TestingConfigurationManager


def test_write(output_folder):
    config_file = output_folder / 'configuration.toml'
    config_file.unlink(missing_ok=True)

    config_manager = ConfigurationManager(output_folder)
    assert config_manager.config_file.exists()

    config = config_manager.get_sample_config()
    config_manager.write_configuration(config, over_write=True)

    assert config_manager.config_file.exists()


def test_export_json(output_folder):
    json_file = output_folder / 'configuration.json'
    json_file.unlink(missing_ok=True)

    config_manager = ConfigurationManager()
    config_manager.export_to_json(json_file)


def test_is_valid(fixtures_folder):
    config_file = fixtures_folder / 'configuration_missing_key.toml'

    config_manager = TestingConfigurationManager(config_file)
    with pytest.raises(ConfigurationError) as e:
        config_manager.is_valid(raise_error=True)

    clean_error = str(e.value).replace('\n', ' ')
    assert clean_error == 'Configuration error. Type: ValidationError Error: 1 validation error for Configuration' \
                          ' database -> backup_folder   field required (type=value_error.missing)'
