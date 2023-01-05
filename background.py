from components import store_new_abi, get_pairs_from_factory, load_config

# this uses the functions from the components to build the background data
def main():
    FILE_NAME = "biswap_factory"
    BLOCKCHAIN = "binance"
    SECONDARY_DEX = "pancakeswap_factory"
    EXCHANGES = "biswap_pancakeswap"

    # uncomment and to get ABIs for selected Binance DEXes
    ABI_to_load = [
        "sushiswapB_router",
        "sushiswapB_factory",
        "sushiswapB_factory_pool",
        "pancakeswap_router",
        "pancakeswap_factory",
        "pancakeswap_factory_pool",
        "biswap_router",
        "biswap_factory",
        "biswap_factory_pool",
        "mdex_router",
        "mdex_factory",
        "mdex_factory_pool",
        "apeswap_router",
        "apeswap_factory",
        "apeswap_factory_pool",
    ]
    for i in ABI_to_load:
        # if the abi doesn't exist then store it as a json file
        store_new_abi(blockchain=BLOCKCHAIN, file_name=i)

    # uncomment/comment as needed
    # this function gets all pairs that are common to both exchanges based on a ref exchange defined in filename
    # this is useful for discovery to find pairs to target on a given pair of exchanges
    SELECTED_IDS = load_config()[BLOCKCHAIN][EXCHANGES]["selected_ids"]
    get_pairs_from_factory(
        blockchain=BLOCKCHAIN,
        file_name=FILE_NAME,
        secondary_dex=SECONDARY_DEX,
        save_name="./Outputs/binance_pairs.xlsx",
        selected_ids=SELECTED_IDS,
        base_token="0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
    )


if __name__ == "__main__":
    main()
