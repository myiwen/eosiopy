import json
import requests

from eosiopy.config import eosio_config


def requests_post(url, json_data):
    headers = {
        'Content-Type': 'application/json',
    }
    data = json.dumps(json_data, ensure_ascii=False).encode('utf8')
    return requests.post(url, data=data, headers=headers)


class NodeNetwork(object):
    @staticmethod
    def get_info():
        res = requests.get(eosio_config.url_port + eosio_config.get_info)
        return res.json()

    @staticmethod
    def node_post_base(url, json_data):
        res = requests_post(eosio_config.url_port + url, json_data=json_data)
        return res.json()

    @staticmethod
    def get_block(block_num_or_id):
        res = requests.post(eosio_config.url_port + eosio_config.get_block,
                            json={"block_num_or_id": block_num_or_id})
        return res.json()

    @staticmethod
    def get_info_block():
        res = NodeNetwork.get_info()
        res.update(NodeNetwork.get_block(res["last_irreversible_block_num"]))
        return res

    @staticmethod
    def push_transaction(json_data):
        res = requests_post(eosio_config.url_port + eosio_config.push_transaction, json_data=json_data)
        return res.json()

    @staticmethod
    def json_to_abi(json_data):
        res = requests_post(eosio_config.url_port + eosio_config.abi_json_to_bin, json_data=json_data)
        return res.json()

    @staticmethod
    def get_account(json_data):
        res = requests_post(eosio_config.url_port + eosio_config.get_account, json_data=json_data)
        return res.json()

    @staticmethod
    def get_accounts(json_data):
        res = requests_post(eosio_config.url_port + eosio_config.get_accounts, json_data=json_data)
        return res.json()

    @staticmethod
    def get_currency_balance(json_data):
        res = requests_post(eosio_config.url_port + eosio_config.get_currency_balance, json_data=json_data)
        return res.json()
