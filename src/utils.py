def get_address_from_compiled_json(datastore):
    networks = datastore.get('networks')
    if networks:
        network = networks.get(list(networks.keys())[0])
        if network:
            return network.get('address')
    return None
