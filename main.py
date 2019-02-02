from src.blockchain import EthereumMiddleware


SETTINGS = {
    'COMPILED_CONTRACT': open('./build/')
}


if __name__ == "__main__":
    eth = EthereumMiddleware()