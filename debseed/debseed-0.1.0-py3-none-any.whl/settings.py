from __future__ import annotations
import configparser
import re, sys, os, json, shlex
from pathlib import Path
from configparser import ConfigParser, SectionProxy
from datetime import datetime
from .utils import check_ssh_public_key, without_j2
from . import __version__

PACKAGE_ASSETS = Path(__file__).parent.joinpath('assets')

config = ConfigParser(converters={
    'json': lambda x: json.loads(x),
})

config.read([
    # System-wide configuration
    f'C:/ProgramData/debseed.conf' if sys.platform == 'win32' else f'/etc/debseed.conf',

    # Global/user configuration
    os.path.expanduser(f'~/.config/debseed.conf'),

    # Current working directory configuration (we do NOT mention the appname because we expect this file to contain configuration for several modules/applications).
    'local.conf',
])

DEFAULT_EDITION = config.get('debseed', 'default_edition', fallback='generic')
DEFAULT_VARIANT = config.get('debseed', 'default_variant', fallback='firmware')
DEFAULT_ARCH = config.get('debseed', 'default_arch', fallback='amd64-i386')

ORIGIN_ISO_DIR = Path(config.get('debseed', 'origin_iso_dir', fallback="iso-debian"))
TARGET_ISO_DIR = Path(config.get('debseed', 'target_iso_dir', fallback="iso-debseed"))
ARCHIVES_ISO_DIR = TARGET_ISO_DIR.joinpath('archives')

if _value := config.get('debseed', 'debian_cd_signing_key', fallback=None):
    DEBIAN_CD_SIGNING_KEY = Path(_value)
else:
    DEBIAN_CD_SIGNING_KEY = PACKAGE_ASSETS.joinpath('debian-cd-signing.gpg')

# Configure proxy and CA certificates
if not ('HTTP_PROXY' in os.environ or 'http_proxy' in os.environ or 'HTTPS_PROXY' in os.environ or 'https_proxy' in os.environ):
    if _value := config.get('debseed', 'proxy', fallback=None):
        os.environ['HTTP_PROXY'] = _value
        os.environ['HTTPS_PROXY'] = _value

if not ('NO_PROXY' in os.environ or 'no_proxy' in os.environ):
    if _value := config.get('debseed', 'no_proxy', fallback=None):
        os.environ['NO_PROXY'] = _value

if not 'REQUESTS_CA_BUNDLE' in os.environ:
    _value = config.get('debseed', 'ca_certificates', fallback='/etc/ssl/certs/ca-certificates.crt')
    if os.path.exists(_value):
        os.environ['REQUESTS_CA_BUNDLE'] = _value


class Edition:
    def __init__(self, name: str, settings: SectionProxy, default_settings: SectionProxy = None):
        self.name = name
        self.settings = settings
        self.default_settings = default_settings

    def _get(self, key: str, fallback: str = None) -> str:
        if key in self.settings:
            return self.settings[key]
        elif self.default_settings and key in self.default_settings:
            return self.default_settings[key]
        else:
            return fallback

    def _getboolean(self, key: str, fallback: bool = None) -> bool:
        if key in self.settings:
            return self.settings.getboolean(key)
        elif self.default_settings and key in self.default_settings:
            return self.default_settings.getboolean(key)
        else:
            return fallback

    def get_context(self, origin_iso_name: str) -> Context:
        return Context(self, origin_iso_name)


class Context:
    def __init__(self, edition: Edition, origin_iso_name: str):
        from .debian import extract_debian_full_version, get_debian_major_version, get_debian_version_name

        self.edition = edition
        self.origin_iso_name = origin_iso_name

        self.debian_full_version = extract_debian_full_version(origin_iso_name)
        self.debian_major_version = get_debian_major_version(self.debian_full_version)
        self.debian_version_name = get_debian_version_name(self.debian_full_version)

        value = self._get('assets')
        self.assets = Path(value) if value else None
        self.preseed_template = self._get_asset('preseed_template', "preseed.cfg.j2")
        self.late_command = self._get_asset('late_command', "late-command.sh")
        self.late_command_assets = self._get_late_command_assets(self.edition.settings, self.edition.default_settings)

        self.target_iso = TARGET_ISO_DIR.joinpath(edition.name + '-' + origin_iso_name)
        self.target_iso_volid = self._get('target_iso_volid', "{edition_name}")
        self.target_iso_volset = self._get('target_iso_volset', "Created by Debseed (edition {edition_name}) from {origin_iso_name}")
        self.target_iso_preparer = self._get('target_iso_preparer', "Debseed")
        self.target_iso_publisher = self._get('target_iso_publisher')

        # Network
        self.ip_gateway = self._get('ip_gateway')
        self.ip_netmask = self._get('ip_netmask')
        self.dns_servers = self._get('dns_servers')
        self.dns_domain = self._get('dns_domain')
        self.dhcp = self._getboolean('dhcp', fallback=None)
        if self.dhcp is None and (self.ip_gateway or self.ip_netmask or self.dns_servers):
            self.dhcp = True

        # User
        self.username = self._get('username')
        self.password_crypted = self._get('password_crypted')  # password encrypted using `mkpasswd -s -m sha-512` from package `whois`
        self.ssh_public_key = self._get_ssh_public_key(self.edition.settings, self.edition.default_settings)
        self.locale = self._get('locale')  # example: fr_FR
        self.keyboard = self._get('keyboard')  # example: fr(latin9)

        if self.ssh_public_key:
            self._add_to_packages('openssh-server')

        # Packages
        self.repository_host = self._get('repository_host')
        self.repository_path = self._get('repository_path')
        self.packages = self._get('packages') # example: curl wget netcat-traditional iputils-ping bind9-host git python3-venv python3-pip

        if self.packages:
            if not self.packages.startswith(' '):
                self.packages = ' ' + self.packages
            if not self.packages.endswith(' '):
                self.packages = self.packages + ' '

        # Add packages depending on late command assets
        for lca in self.late_command_assets:
            if lca.joinpath('target/etc/ssh/sshd_config.j2').exists() or lca.joinpath('target/etc/ssh/sshd_config').exists():
                self._add_to_packages('openssh-server')
            if lca.joinpath('target/usr/local/share/ca-certificates').exists():
                self._add_to_packages('ca-certificates')
            if lca.joinpath('target/etc/vim').exists():
                self._add_to_packages('vim')

        # Time
        self.timezone = self._get('timezone')  # example: Europe/Paris
        self.localtime_clock = self.edition._getboolean('localtime_clock')
        self.ntp_servers = self._get('ntp_servers')

        # Files
        self.auto_partitioning = self._get('auto_partitioning')
        self.srv_group = self._get('srv_group')

        if self.srv_group:
            self._add_to_packages('acl')

        # Additional
        self.additional_context = self._get_additional_context()


    def format(self, fmt: str):
        if not isinstance(fmt, str):
            return fmt
        return fmt.format(edition_name=self.edition.name, origin_iso_name=self.origin_iso_name, debian_full_version=self.debian_full_version, debian_major_version=self.debian_major_version, debian_version_name=self.debian_version_name)

    def _get(self, key: str, fallback: str = None) -> str:
        return self.format(self.edition._get(key, fallback=fallback))

    def _getboolean(self, key: str, fallback: bool = None) -> bool:
        return self.edition._getboolean(key, fallback=fallback)
    
    def _get_asset(self, key: str, default_name: str) -> Path:
        if key in self.edition.settings:
            value = self.edition.settings[key]
            if not value:
                return None
            return Path(self.format(value))
        elif self.assets and (path := self.assets.joinpath(default_name)).exists():
            return path
        elif self.edition.default_settings and key in self.edition.default_settings:
            value = self.edition.default_settings[key]
            if not value:
                return None
            return Path(self.format(value))
        else:
            return PACKAGE_ASSETS.joinpath(default_name)

    def _get_late_command_assets(self, settings: SectionProxy, previous_settings: SectionProxy = None) -> list[Path]:
        key = "late_command_assets"
        default_name = "late-command-assets"


        def append_previous(paths: list[Path]):
            if previous_settings:
                paths += self._get_late_command_assets(previous_settings)
            else:
                paths.append(PACKAGE_ASSETS.joinpath(default_name))

        paths = []

        if key in settings:
            value = settings[key]
            if not value:
                return None

            value = value.strip()
            if value.startswith('+'):
                append_previous(paths)
                paths.append(Path(self.format(value[1:].strip())))
            else:
                paths.append(Path(self.format(value.strip())))

        elif self.assets and (path := self.assets.joinpath(default_name)).exists():
            append_previous(paths)
            paths.append(path)

        else:
            append_previous(paths)

        return paths


    def _get_ssh_public_key(self, settings: SectionProxy, default_settings: SectionProxy = None):
        if 'ssh_public_key' in settings and 'ssh_public_keyfile' in settings:
            raise ValueError(f"please provide only one of 'ssh_public_key' and 'ssh_public_keyfile'")

        if 'ssh_public_key' in settings:
            ssh_public_key = settings.get('ssh_public_key')
            check_ssh_public_key(ssh_public_key)
            return ssh_public_key

        elif 'ssh_public_keyfile' in settings:
            keyfile = Path(self.format(settings.get('ssh_public_keyfile')))
            if not keyfile.exists():
                raise ValueError(f"ssh_public_keyfile does not exist: {keyfile}")
            ssh_public_key = keyfile.read_text()
            check_ssh_public_key(ssh_public_key)
            return ssh_public_key

        elif default_settings:
            return self._get_ssh_public_key(default_settings)

        else:
            return None

    def _get_additional_context(self):
        context = {}

        for section in [self.edition.default_settings, self.edition.settings]:
            try:
                if section:
                    for key in section:
                        if not key.startswith('_') and not key in self.__dict__ and not key in self.edition.__dict__:
                            context[key] = self.format(section.get(key))
            except configparser.NoSectionError:
                pass

        return context

    @property
    def template_data(self) -> dict[str,str|bool|int]:
        try:
            return self._template_data
        except AttributeError:

            self._template_data = {
                'edition_name': self.edition.name,
                'origin_iso_name': self.origin_iso_name,
                'debian_full_version': self.debian_full_version,
                'debian_major_version': self.debian_major_version,
                'debian_version_name': self.debian_version_name,
                'debseed_version': __version__,
                'debseed_generated': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                # Network
                'dhcp': self.dhcp,
                'ip_gateway': self.ip_gateway,
                'ip_netmask': self.ip_netmask,
                'dns_servers': self.dns_servers,
                'dns_domain': self.dns_domain,
                # User
                'username': self.username,
                'password_crypted': self.password_crypted,
                'locale': self.locale,
                'keyboard': self.keyboard,
                'ssh_public_key': self.ssh_public_key,
                # Packages
                'repository_host': self.repository_host,
                'repository_path': self.repository_path,
                'packages': self.packages,
                # Time
                'timezone': self.timezone,
                'localtime_clock': self.localtime_clock,
                'ntp_servers': self.ntp_servers,
                'first_ntp_server': self._get_first_ntp_server(),
                # Files
                'auto_partitioning': self.auto_partitioning,
                'srv_group': self.srv_group,
                # Additional
                **self.additional_context,
            }

            arguments = ""
            comments = ""
            for key, value in self._template_data.items():
                if not (value is None or value is False or value == ''):
                    arguments += f" \\\n    {shlex.quote('--' + key)} {shlex.quote(str(value) if value is not None else None)}"
                comments += ("\n" if comments else "") + f"# {key}: {value}"

            self._template_data['late_command'] = self._get_late_command_template_data(arguments)
            self._template_data['context_comments'] = comments
            return self._template_data


    def _get_first_ntp_server(self):
        if not self.ntp_servers:
            return None

        servers = self.ntp_servers.strip()
        pos = servers.find(' ')
        if pos >= 0:
            return servers[:pos]
        else:
            return servers

    def _get_late_command_template_data(self, arguments: str):
        if not self.late_command:
            return None

        script = without_j2(self.late_command.name)
        return "sh " + shlex.quote(script) + arguments

    def _add_to_packages(self, name: str):
        if not self.packages:
            self.packages = f' {name} '
        elif not f' {name} ' in self.packages:
            self.packages += (' ' if not self.packages.endswith(' ') else '') + f'{name} '


_cache = {}

def get_editions() -> dict[str,Edition]:
    if not 'editions' in _cache:
        editions = {}
        
        # Add default section
        default_settings = SectionProxy(config, f'debseed:{DEFAULT_EDITION}')
        editions[DEFAULT_EDITION] = Edition(DEFAULT_EDITION, settings=default_settings)
        
        # Add generic section (if default != generic):
        if DEFAULT_EDITION != 'generic':
            generic_settings = SectionProxy(config, f'debseed:generic')
            editions['generic'] = Edition('generic', settings=generic_settings)

        # Find other sections
        for section_name in config.sections():
            if not (m := re.match(r'\s*debseed\s*\:\s*(.+)\s*', section_name)):
                continue

            edition_name = m.group(1).strip()
            if edition_name != DEFAULT_EDITION and edition_name != 'generic':
                editions[edition_name] = Edition(edition_name, settings=config[section_name], default_settings=default_settings)
        
        # Register in cache
        _cache['editions'] = editions

    return _cache['editions']


def get_edition(name: str) -> Edition:
    editions = get_editions()
    return editions[name]
