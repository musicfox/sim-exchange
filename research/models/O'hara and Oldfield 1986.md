# Brief Notes on O'hara & Oldfield (1986)

## Basics

- Paper name: The Microeconomics of Market Making
- Source: Journal of Finance and Quantitative Analysis, VOL21,NO.4
- Author: O'hara and Oldfield
- Publish time: DEC 1986
- Tags: Microeconomics, Dynamic Programming

## Algorithm discription

### Summary

With supply and demand analysis, this paper found an equilibrium for bid and ask price selection for the market makers, and gave insights to the market making process.

1. First, the spread can be decomposed into three parts:

    - known orders
    - expectation of future orders
    - risk adjustment for inventory value uncertainty

2. Risk averse lead to smaller spread, thus cannot be driven out by risk neutral specialists

3. Inventory affect both placement and size of the spread

### Assumptions

- Linear supply-demand functions
- Von-Neumann Morganstern utility function (increasing, concave, bounded, twice differentiable)
- Market orders are related to market maker quotes, limit orders don't
- Approximation continuous aution market with a decretized autions
  - bid-ask price is set at the beginning of periods, executes at the period's end

### Settings

- each day has n trading periods
- begin: know limit orders, have expectation of coming market orders
- end: compute inventory, get limit orders for next interval

## Order flow

- As stated above, the orders come in with a linear supply-demand function
- Asks: $A_t=\alpha-a_t\gamma+w_t$
- Bids: $B_t=\beta-b_t\phi+\epsilon_t$
  - Both of these have included both market and limit orders. Then randomness comes from market orders. Some details omitted.
- Simplification: doesn't consider interaction between dealer's current price with limit orders.

## Market maker behavior

- First note that above behavior may lead to an inventory.
- market maker target: $max{E(U(\sum_{t=1}^n \pi_t)+V(I_n))}$
  - $V$: Derived value of the inventory, concave, increasing, twice differentiable
    - Effect of current actions on future expected utility, given future actions chosen optimally
  - Now overall utility is a combination of cash flow and inventory in the future.
  - In this article, author used "constant absolute risk aversion", which is: $max{E(-exp(-\sum_{t=1}^n \pi_t)-exp(-I_n))}$

## Overnight market

- The market maker can lend or borrow positions overnight.
- Overnight market has price $\tilde{p}$ and interest rate $r$, both exogenous

## Find the optimal bid/ask

- All above combined, we have a constrained optimization problem
  $$\max_{a_n,b_n} E[U(\sum_{t=1}^{n-1} \pi_t+a_n(\alpha-a_n\gamma+\tilde{w}_n)-b_n(\beta+b_n\phi+\tilde{\epsilon}_n)\\
  +r\tilde{p}(I_{n-1}+(\beta+b_n\phi+\tilde{\epsilon}_n)-(\alpha-a_n\gamma-\tilde{w}_n))\\
  +V(I_{n-1}+(\beta+b_n\phi+\tilde{\epsilon}_n)-(\alpha-a_n\gamma-\tilde{w}_n))$$
  - constraints are omitted here
  - The terms related to $\alpha, a_n, \beta, b_n$ represent concepts like $\pi_n, (I_n-I_{n-1})$

- Take first derivative and we have
  $$a_n=\alpha/{2\gamma}+E(U'\tilde{w}_n)/E(U')2\gamma\\
  +rE(U'\tilde{p})/{2E(U')}+E(V')/{2E(U')}$$
  and
  $$b_n=-\beta/{2\phi}-E(U'\tilde{\epsilon}_n)/E(U')2\phi\\
  +rE(U'\tilde{p})/{2E(U')}+E(V')/{2E(U')}$$
  - This is not explicit expression because $U$ contains $a_n,b_n$

- We can interpret each part, though
  - first terms: known limit orders and expected market orders
  - second terms: risk adjustments for variability in market orders
    - covariance, $Cov(U',\tilde{w}_n)<0, Cov(U',\tilde{\epsilon}_n)>0$
    - shifts both $a_n,b_n$ down
  - third/fourth:inventory's effects

- Analyze the spread
  $$ a_n-b_n=(\alpha\phi+\beta\gamma)/{2\phi\gamma}+(\phi E(\tilde{w}_n)+\gamma E(\tilde{\epsilon}_n))/{2\gamma\phi}\\
  +(\phi Cov(U',\tilde{w}_n)+\gamma Cov(U',\tilde{\epsilon}_n))/{2\phi\gamma E(U')}$$
  - first two terms: total expected supply and demand, charged by risk-neutral market maker
  - third term: market order uncertainty, may expand or narrow according to market order behavior, or magnitude of supply-demand
  - there was a $V$ term, cancelled here. but $U'$ indirectly presents an overnight inventory effect
    - $U'$ is a function of $a_n,b_n,I_{n-1}$ and $a_n,b_n$ are also functions of inventory $I_{n-1}$
- If we can assume normality of $\tilde{\pi}$, then we can utilize the transformation:
  $$E(-exp(\pi))=-exp(E(\pi)-Var(\pi)/2)$$
  when pi is normally distributed.

  Then, we can make a transformation based on this. The maximation transformation above can then be transformed into the following:
  $$\max_{a_n,b_n} E[\sum_{t=1}^{n-1} \pi_t+E(\tilde{\pi}_n)-\frac{c}{2}Var(\tilde{\pi}_n)+E(\tilde{p}\tilde{I}_n)-\frac{d}{2}Var(\tilde{p}\tilde{I}_n)]$$

- With the substitution above, we can reformulate the spread:
  $$a_n-b_n=\frac{\alpha\phi+\beta\gamma}{2\gamma\phi}+\frac{\bar{w}_n\phi+\bar{\epsilon}_n\gamma}{2\gamma\phi}\\
  +\frac{c}{2\gamma\phi}[\gamma Var(\tilde{\epsilon}_n)(\frac{-\beta-\epsilon_n+(1+r)\bar{p}\phi-cr\bar{p}Var(\tilde{\epsilon}_n)}{2\phi+c Var(\tilde{\epsilon}_n)}+r\bar{p}\\
  -\phi Var(\tilde{w}_n)(\frac{\alpha+\bar{w}_n+(1+r)\bar{p}\phi-cr\bar{p}Var(\tilde{w}_n)}{2\gamma+c Var(\tilde{w}_n)}+r\bar{p}]$$
  - Here we can observe the risk adjustments more clearly.
  - The first two terms are risk-neutral spread and the remaining part is the risk adjustment part.
  - We can see that the risk adjustment can be either positive or negative, this depend on the relative magnitudes of the parameters.
    - e.g.: When there's symmetric market order variability and the absolute values of slopes of the total ordr flow are equal (i.e., $\gamma Var(\tilde{\epsilon})=\phi Var(\tilde{w})=H>0$).
      In this case we have 
      $$a_n-b_n=\frac{\alpha\phi+\beta\gamma}{2\gamma\phi+cH}+\frac{\bar{w}_n\phi+\bar{\epsilon}_n\gamma}{2\gamma\phi+cH}$$
      Here, the risk aversion factor c is still in play (This is a risk adjustment factor). As c increases, we can see that the spread narrows. Therefore, the risk averse players cannot always be dominated by a risk-neutral specialist.
  - Also, we can see from the equations above that level of intentory positions $I_n$ does not affect the spread. Note that this hold true if the market makes's inventory position can always be settled at a known price $\bar{p}$.
  - Also it can be shown that inventory affects the placement of bid and offer respectively.
  - Size of the market maker's optimal spread can be determined by Demsetz(1968).
  - If risk neutral prices do prevail, there is an relationship between quoted price and overnight repurchaseing price. Substitute risk-neutral prices $(1+r)\bar{p}$ into the supply/demand equations, we have 
    $$ E(\tilde{A}_t^*)=(\alpha+\bar{w}_t-(1+r)\bar{p}\gamma)/2\\
    E(\tilde{B}_t^*)=(\beta+\bar{\epsilon}_t-(1+r)\bar{p}\phi)/2$$
    Then we have
    $$(1+r)\bar{p}=(\gamma a_t+\phi b_t)/(\gamma+\phi)$$
    This means that the repurchase price is a weighted average of the bid and ask price, weighted by the slope of the two functions.
    - In conclusion, if risk neutral prices are set such that expected inventory change is 0, then overnight speculation is not a trading motive. Because overnight price is bracketed by the bid and ask.

## Todo
- We may include randomness of limit orders as Zabel and Bradfield (1981), then the risk aversion would give a more significant influence. 
