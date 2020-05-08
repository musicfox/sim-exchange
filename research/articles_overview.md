# Overview of Articles - 05/28 

## Parlour 1998 - Price Dynamics in Limit Order Markets

Assumptions:
trades on the exchange are processed individually
market with only 2 prices, a bid B and an ask A
cannot cancel an order
don’t use multiple units (if multiple units are used, we have to take into account optimal order splitting)

one tick dynamic model of a limit order book
Each trader knows that her order will affect the order placement strategies of those who follow
the probability of execution depends both on the state of the book when the trader submits her order, and how many market orders trader believes will arrive until T (end of day)
observe nonrandom patterns in the transactions data and order placement strategies	
If the possible orders that can be observed are a market sell, a limit sell, a market buy, and a limit buy, then:
The probability that the next transaction is at the ask is larger after a transaction at the ask (than at the bid)
The probability of observing a limit buy order given that the last order was a limit buy order is smaller than the probability of observing a limit buy order after any other order or transaction
The probability of observing a limit sell order after a transaction at the ask is greater than the probability of observing a limit sell order after any other transaction or order.
 The probability of observing a limit sell order after a limit sell order is smaller than the probability of observing a limit sell order after a transaction at the bid which is smaller than the probability of observing a limit sell order after a limit buy order
			
To determine if she wants to submit a market order or a limit order, a trader compares the expected utility gain she gets if she submits a limit sell order
use parameter B as a degree of patience for trade (high Bs -> want to trade immediately (can be interpreted as a subjective valuation of the asset)
payoff to each trader depends on the actions of subsequent traders in the market
to characterize an agent’s optimal order submission strategy for a given limit order book, the probability that an additional limit order will execute by the end of the day is taken as given
 
Lemma 1: To determine if she wants to submit a market order or a limit order, a trader compares the expected utility gain she gets if she submits a limit sell order with the utility gain that she receives if she submits a market order
Lemma 2: The higher the probability of execution of a limit  order, the more trader types prefer to submit limit orders over market orders.

## Foucault 1999: Order Flow Composition and Trading Costs in a Dynamic Limit Order Market
 
Assumptions:
1. 	Single risky asset, whose underlying value is random walk
2. 	discrete multi period model that stops randomly with a parameter (captures execution risk for limit orders)
3. 	limit order expire after one period, and orders cannot be modified/ canceled
4. 	reservation price has trader-specific component (high and low type, +/-fixed amount L)
5. 	it follows that volatility is linear in L
6. 	Trading cost is the difference asset value and the price at which market order is executed at nth period
 
Methodology:
Subgame perfect equilibrium. Solve for competitive equilibrium by setting expected profit to 0.
 
Conclusion:
Several theoretical phenomena under the settings:
1. 	proportion of limit orders chosen in each period is positively related to asset volatility
2. 	The fill rate of limit orders is negatively related to asset volatility
3. 	The proportion of limit order is positively related to the average size of the spread
4. 	The increase in trading cost at the end of the trading day is negatively related to the level of competition between limit order traders
5. 	The total trading cost of all orders is maximized when the ratio of buy-to-sell orders is equal to 1.


## Thomas Ho & Hans Stoll
Assumptions:
Stationary stochastics jump as in Garman 
Poisson Jump for order arrival
Dealer is trading in passive way
single dealer in the market
No foreign information ahead of dealer about true price of underlying

Dynamic Programming Three Component in multiperiod process in order to maximize the wealth utility during the periods: 
Cash
Inventory
Base Wealth

Optimal Spread:



Need Calibration and Measure for:
Supply Demand Model
True Price Believed by Trader
True Price Believed by Market Maker
Risk Aversion Coefficient
Expected Return For Underlying

Possible Violation for Music Investing Market:
Not Stationary Stochastics Jump for the price of underlying portfolio if it is not diversified or traded thinly across times
The model needs a lot industry data to calibrate some statistics and does not quite answer the matching algorithm problem in the project lab
