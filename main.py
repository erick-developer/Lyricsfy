from src.blockchain import EthereumMiddleware


CONTRACT_NAME = 'Lyricsify'


SETTINGS = {
    'CONTRACT_NAME': CONTRACT_NAME,
    'COMPILED_CONTRACT':
        open('./build/contracts/{}.json'.format(CONTRACT_NAME)),
}


if __name__ == "__main__":
    eth = EthereumMiddleware()