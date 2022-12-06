"""generate by foyou-pypi"""
__version__ = '0.0.1'

import subprocess
import uuid


def keytool():
    print('hello from foyou-sign', __version__)

    import argparse
    parser = argparse.ArgumentParser(
        description='生成 APK 签名证书的小工具',
        epilog=f'pysign({__version__}) by foyou(https://github.com/foyoux)'
    )
    parser.add_argument('-v', '--version', dest='version', help='show pypi version', action='store_true')

    parser.add_argument('-p', '--password', dest='password', type=str, default=uuid.uuid4().hex)
    parser.add_argument('-a', '--alias', dest='alias', type=str, default='key0')
    parser.add_argument('-y', '--year', dest='year', type=int, default=25, help='证书有效期多少年')
    parser.add_argument('-n', '--name', dest='name', type=str, default='foyou', help='名字')
    parser.add_argument('--org', dest='org', type=str, default='', help='组织')
    parser.add_argument('--org-unit', dest='org_unit', type=str, default='', help='组织单位')
    parser.add_argument('--city', dest='city', type=str, default='', help='城市或地区')
    parser.add_argument('--state-or-province', dest='sop', type=str, default='', help='州或省')
    parser.add_argument('--country-code', dest='code', type=str, default='', help='州或省')

    parser.add_argument('-o', '--output', dest='output', type=str, default=None,
                        help='optional, pypi project output path')

    args = parser.parse_args()

    if args.version:
        print('pysign version', __version__)
        return

    if args.output is None:
        args.output = f'{args.alias}-{args.password}'

    subprocess.run(
        [
            'keytool', '-genkey', '-alias', args.alias, '-keyalg', 'RSA', '-dname',
            f'CN={args.name},OU={args.org_unit},O={args.org},L={args.city},ST={args.sop},C={args.code}',
            '-validity', str(args.year * 365), '-keypass', args.password, '-keystore', args.output, '-storepass',
            args.password
        ], capture_output=True
    )

    print(f"""signingConfigs {{
    debug {{
        storeFile file("{args.output}")
        storePassword '{args.password}'
        keyAlias '{args.alias}'
        keyPassword '{args.password}'
    }}
    release {{
        storeFile file("{args.output}")
        storePassword '{args.password}'
        keyAlias '{args.alias}'
        keyPassword '{args.password}'
    }}
}}
Generated successfully""")
