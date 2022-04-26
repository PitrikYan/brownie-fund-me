from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"Aktivní network je:{network.show_active()}")
    print("Deploying Mocks....")  # fake network..

    # jen jestli jeste nebyl deploynut zadny MockV3Aggregator
    if len(MockV3Aggregator) <= 0:
        # vola uvnitr funkci z web3 ktera predeve castku v eth na wei
        # pfrom account je tam rotoze je to deploy..
        MockV3Aggregator.deploy(
            # DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}       potom co nahore zmenil promene z 18 a 2000 na 8 a 2000*10**8
            DECIMALS,
            STARTING_PRICE,
            {"from": get_account()},
        )
    print("mock deployed..")
