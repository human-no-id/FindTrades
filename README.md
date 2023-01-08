# Searching DEXes for potentially viable trading pairs

This project includes functions written in Python to interact with an EVM blockchain to:

1. build ABIs for the factory, router and pool of uniswap style DEXes; and
2. search two DEXes for token pairs that might be worth considering for an arbitrage trade.

Note that in the process of determining whether a trade might be worth considering, the search does not take pool size or transaction fees into account. However, these and other factors are likely to affect the profitability of an arbitrage trade. The code presented employs a very simple strategy, better results may be obtained using more advanced trading strategies.
