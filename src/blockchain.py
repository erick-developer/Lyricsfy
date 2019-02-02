import json

from web3 import Web3

from .exceptions import ContractBuildFileNotDefined
from .utils import get_address_from_compiled_json


class EthereumMiddleware:
    web3 = None
    contract_address = None
    contract_abi = None

    def __init__(self, *args, **kwargs):
        contract_build_file = kwargs.get('contract_build_file', None)
        if contract_build_file is None:
            raise ContractBuildFileNotDefined('Contract Build File needs to be valid')

        web3_http_provider_url = kwargs.get('web3_http_provider_url', 'http://127.0.0.1:8545')
        self.w3 = Web3(Web3.HTTPProvider(web3_http_provider_url))
        with contract_build_file as f:
            datastore = json.load(f)
            self.contract_abi = datastore["abi"]
            self.contract_address = get_address_from_compiled_json(datastore)
        self.w3.eth.defaultAccount = self.w3.eth.accounts[1]

    def store_new_lyric(self, lyric, *args, **kwargs):
        instance = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        tx_hash = instance.functions.setLyricForSender(lyric)
        tx_hash = tx_hash.transact()
        self.w3.eth.waitForTransactionReceipt(tx_hash)
        _lyric = instance.functions.getLyricByIndex(0).call()
        print(_lyric)
        _amount_of_publishers = instance.functions.getUsersCount().call()
        print(_amount_of_publishers)
        return {
            'lyric': _lyric,
            'count': _amount_of_publishers,
        }
