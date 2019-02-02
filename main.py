from src.blockchain import EthereumMiddleware


CONTRACT_NAME = 'Lyricsify'


SETTINGS = {
    'CONTRACT_NAME': CONTRACT_NAME,
    'COMPILED_CONTRACT':
        open('./build/contracts/{}.json'.format(CONTRACT_NAME), 'r'),
}


if __name__ == "__main__":
    eth = EthereumMiddleware(contract_build_file=SETTINGS['COMPILED_CONTRACT'])
    eth.store_new_lyric('This is my new song!')
