import scipy.stats as stats

#*************************************************************************************************************#
#1: Newton's Approximation Method for finding Implied Volatility
#*************************************************************************************************************#

n = stats.norm.pdf
N = stats.norm.cdf


def bs_price(cp_flag,S,K,T,r,v,q=0.0):
    d1 = (stats.log(S/K)+(r+v*v/2.)*T)/(v*stats.sqrt(T))
    d2 = d1-v*stats.sqrt(T)
    if cp_flag == 'c':
        price = S*stats.exp(-q*T)*N(d1)-K*stats.exp(-r*T)*N(d2)
    else:
        price = K*stats.exp(-r*T)*N(-d2)-S*stats.exp(-q*T)*N(-d1)
    return price


def bs_vega(cp_flag,S,K,T,r,v,q=0.0):
    d1 = (stats.log(S/K)+(r+v*v/2.)*T)/(v*stats.sqrt(T))
    return S * stats.sqrt(T)*n(d1)


def find_vol(target_value, call_put, S, K, T, r):
    max_iterations = 100
    precision = 1.0e-5

    sigma = 0.5
    for i in range(0, max_iterations):
        price = bs_price(call_put, S, K, T, r, sigma)
        vega = bs_vega(call_put, S, K, T, r, sigma)

        price = price
        diff = target_value - price  # our root

        print(i, sigma, diff)

        if abs(diff) < precision:
            return sigma
        sigma = sigma + diff/vega # f(x) / f'(x)

    # value wasn't found, return best guess so far
    return sigma
