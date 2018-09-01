from setuptools import setup

setup(
    name="electrum-sum-server",
    version="1.0",
    scripts=['run_electrum_sum_server.py','electrum-sum-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumsumserver':'src'
        },
    py_modules=[
        'electrumsumserver.__init__',
        'electrumsumserver.utils',
        'electrumsumserver.storage',
        'electrumsumserver.deserialize',
        'electrumsumserver.networks',
        'electrumsumserver.blockchain_processor',
        'electrumsumserver.server_processor',
        'electrumsumserver.processor',
        'electrumsumserver.version',
        'electrumsumserver.ircthread',
        'electrumsumserver.stratum_tcp'
    ],
    description="Sumcoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/pooler/electrum-sum-server/",
    long_description="""Server for the Electrum Lightweight Sumcoin Wallet"""
)
