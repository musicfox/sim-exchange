# Implementation of Limit Orders Market Model - Parlour (1998) 

*By: Yiwei Zhao and Rita Koulikova* 

## 1.1 Abstract

Christine A. Parlour’s one tick dynamic model of a limit order market (discussed in her 1998 paper, *Price Dynamics in Limit Order Markets*, is examined and expanded to create a foundation of a design system for a simulated exchange between two parties. Specifically this model will be extended to a two-sided market matching music artists and investors. 

## 1.2 Related Works
A similar approach to modeling limit order books can be found in Foucault 1999, *Order Flow Composition and Trading Costs in a Dynamic Limit Order Market*.


## 1.3 Describing the Algorithm

Price dynamics within a limit order market are modeled with an underlying premise that every participating trader makes a probabilistic decision based on the current state of the order book and the effect that his/her order will have on orders to follow. The tradeoff that the algorithm will attempt to solve and examine is that between the best price a trader can obtain and the execution probability of an order placed at time, t,  during its lifetime, T-t. 

Given bid price (B) and ask price (A) for the single product, $\beta$ (randomly initialized from a function), the “patience” of each trader, will determine the trader’s choice of placing a market/limit/no order. The side is randomly initialized in the model. Then, the probability of limit order execution, as well as the bounds for $\beta$, can be found in equilibrium. 

Therefore, the following algorithm may be applicable: for the same product, use an exogenous model to determine its true value V, and then determine its fixed bid and ask prices B and A based on costs for either party. In this way, traders are price takers, and choose the type of order based on their preferences (in this model, this refers to preferences between consuming today and tomorrow). Thus, we can devise an algorithm that sets bid and ask prices, B and A, dynamically through observing traders’ behaviours, optimizing over the aggregate utilities of all traders. 

Our idea is to devise an online learning model that is able to learn A and B that optimize over the aggregate utilities. From the model presented in the paper, the calculation of aggregate utilities involves some other parameters: p, the probability of a limit order being executed; $\beta$, the preferences of traders, and V, the asset value. To obtain these parameters, p can be extracted directly from the transaction record, and beta can be determined from a theoretical range calculated based on trader’s behavior, and V is determined exogenously. 
 

## 1.4 Algorithm Assumptions

We will assume that a trader has only one opportunity to trade at time t when they arrive at the market. The order submitted must be a limit or market order at a fixed price of a bid B or ask A. Orders of a fixed price and quantity can only be submitted. Furthermore, once places, a limit order cannot be cancelled or modified. 

## 1.5 Pseudocode

Each book at time t can be represented as $b_t$ or ($b_t^B, b_t^A$) where $b_t^B \geq  0$ and represents that total buy orders in the book at time $t$ and $b_t^A \leq 0$ represents the total sell orders in the book at time t. Let $p_t^S$ be the probability that a sell order placed at time $t$ is executed by time $T$.   Let $p_t^b$ be the probability that a buy order placed at time $t$ is executed by time $T$.   
 
 Define parameters:
```
V = asset_value 
p_b = 1/2
p_s = 1/2
```


<blockquote>

**def** utility_gain(side,utility,order_type): <br/>
&nbsp; **if** side == SELL:<br/>
&nbsp;&nbsp;&nbsp; **if** order_type == LIMIT:<br/>
&nbsp;&nbsp;&nbsp; gain = p_s(A - $\beta*V$)<br/>
&nbsp;&nbsp;&nbsp; **else:**<br/>
&nbsp;&nbsp;&nbsp; gain = (B - $\beta*V$)

&nbsp; **else**:<br/>
&nbsp;&nbsp;&nbsp; **if** order_type == LIMIT:<br/>
&nbsp;&nbsp;&nbsp; gain = p_b($\beta*V$ - B)<br/>
&nbsp;&nbsp;&nbsp; **else:**<br/>
&nbsp;&nbsp;&nbsp; gain = ($\beta*V$ - A)

</blockquote>

<blockquote>

**def** update_book(order, Book1):<br/>

&nbsp;&nbsp;&nbsp; B = Book1.bids <br/>
&nbsp;&nbsp;&nbsp; A = Book1.asks <br/>
&nbsp;&nbsp;&nbsp; **if** order == market_sell:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; B=-1<br/>
&nbsp;&nbsp;&nbsp; **elif** order == limit_sell:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A=-1<br/>
&nbsp;&nbsp;&nbsp; **elif** order == limit_BUY:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; B+=1<br/>
&nbsp;&nbsp;&nbsp; **elif** order == market_BUY:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A+=1<br/>
&nbsp;&nbsp;&nbsp; **else** <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue<br/>
**return** (B, A)



</blockquote>
<blockquote>

**Class** Book:   
&nbsp;&nbsp;&nbsp; bids = 0<br/>
&nbsp;&nbsp;&nbsp; asks = 0<br/>

&nbsp;&nbsp;&nbsp; update= updatebook()<br/>

</blockquote>

 <blockquote>

**class** Trader:   
&nbsp;&nbsp;&nbsp; $\beta$= tradeoff<br/>
&nbsp;&nbsp;&nbsp; position= tradeoff<br/>
&nbsp;&nbsp;&nbsp; side= " "<br/>


&nbsp;&nbsp;&nbsp; gain = utility_gain()<br/>
</blockquote>



## 1.6 Conclusion/Recommendations

For building the trading exchange, the main caveat of this model is that it assumes that bid and ask prices are exogenous and traders are price takers. It contrasts the fact that in most trading platforms, traders are able to set execution prices for limit orders, and it also excludes the possibilities for negotiation between the buy and sell sides. Moreover, it almost certainly creates friction by having a machine learning algorithm to learn, instead of allowing the market to generate the prices directly. While in Parlour's paper this setting helps simplify the model and helps focus the study on order placing strategies, it may need modifications in implementation. 
