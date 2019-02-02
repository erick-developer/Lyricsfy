import json

from web3 import Web3

from .exceptions import ContractBuildFileNotDefined
from .utils import get_address_from_compiled_json


class EthereumMiddleware:
    web3 = None

    def __init__(self, *args, **kwargs):
        contract_build_file = kwargs.get('contract_build_file', None)
        if contract_build_file is None:
            raise ContractBuildFileNotDefined('Contract Build File needs to be valid')

        web3_http_provider_url = kwargs.get('web3_http_provider_url', 'http://127.0.0.1:8545')
        self.w3 = Web3(Web3.HTTPProvider(web3_http_provider_url))
        with contract_build_file as f:
            datastore = json.load(f)
            abi = datastore["abi"]
            contract_address = get_address_from_compiled_json(datastore)

    def store_new_lyric(self, lyric, *args, **kwargs):
        pass
