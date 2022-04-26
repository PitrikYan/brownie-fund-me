from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()

    # kdyz jsem na testnetu, beru z configu adresu aktualniho testnetu
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:  # kdyz nejsem na testnetu
        deploy_mocks()
        # pouziju funkci z helpful_scripts

        price_feed_address = MockV3Aggregator[-1].address
        # [-1] znamena ze pouzije most recently deployed MockV3Aggregator

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
        # get verify je tam kdybysme nahodou zapomneli nastavit v configu verify
    )  # funkce meni blockchain, takze tu musi byt "from"
    print(f"Contract je deployed na {fund_me.address}")

    return fund_me

    # print("Fundme", FundMe)            test na dotaz z netu..
    # print("fund_me", fund_me)


def main():
    deploy_fund_me()
