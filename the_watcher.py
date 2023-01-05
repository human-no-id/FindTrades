from time import time, sleep
from components import scan_by_name, load_config, scan_by_ID, blind_scan
from multiprocessing.dummy import freeze_support


# function to scan exchanges for a potential trade using one of three methods
def scan_exchanges():
    BLOCKCHAIN = "binance"
    BASETOKEN = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
    BASE_TOKEN = "wbnb"
    SMALL_CAP_THRESHOLD = 200  # 100000
    EXCHANGES = "sushiswapB_biswap"
    EXCHANGE_NAMES = [
        "biswap",
        "pancakeswap",
    ]  # ["sushiswapB", "pancakeswap"]
    SCANBY = "blind"
    NAP = 300

    config = load_config()
    PAIR_NAMES = config[BLOCKCHAIN][EXCHANGES]["selected_names"]
    SELECTED_IDS = config[BLOCKCHAIN][EXCHANGES]["selected_ids"]

    if SCANBY == "name":
        scan_by_name(
            pair_names=PAIR_NAMES,
            xch_names=EXCHANGE_NAMES,
            blockchain=BLOCKCHAIN,
            base_token=BASE_TOKEN,
        )

    elif SCANBY == "id":
        scan_by_ID(
            primary_dex=EXCHANGE_NAMES[0],
            secondary_dex=EXCHANGE_NAMES[1],
            blockchain=BLOCKCHAIN,
            selected_ids=SELECTED_IDS,
            save_name="./Outputs/binance_pairs.xlsx",
            base_token=BASETOKEN,
        )

    else:
        for i in range(100):
            blind_scan(
                primary_dex=EXCHANGE_NAMES[0],
                secondary_dex=EXCHANGE_NAMES[1],
                blockchain=BLOCKCHAIN,
                save_name="./Outputs/binance_pairs.xlsx",
                base_token=BASETOKEN,
                small_cap_threshold=SMALL_CAP_THRESHOLD,
                exchange=EXCHANGE_NAMES,
            )
            sleep(NAP)


def main():
    start = time()
    scan_exchanges()
    end = time()
    duration = end - start
    print(f"{duration} seconds")
    print(f"{duration/60} minutes")


if __name__ == "__main__":
    freeze_support()
    main()

# mdex = 1727 pairs
# apeswap = 3584 pairs
# biswap = 1433 pairs
# pancakeswap = a lot
