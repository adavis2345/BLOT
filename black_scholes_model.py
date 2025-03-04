from math import log, sqrt, exp
import datetime
from scipy.stats import norm

# *************************************************************************************************************#
# 1: Newton's Approximation Method for finding Implied Volatility
# *************************************************************************************************************#

vocabulary = {"call": "c",
              "put": "p"}

cp = input("Is this a call or put option: ").lower()

if len(cp) > 1:
    words = cp.split()
    for word in words:
        if word in vocabulary:
            cp = vocabulary[word]
            break

# Price of the option
V_market = float(input("Please enter the price of the option: "))

# #Strike Price
K = int(input("Please enter the strike price: "))

# Amount of days until option expires
d = datetime.datetime.now()
e = input("Please enter the date that the option is set to expire (mm/dd/yyyy): ")
e = datetime.datetime.strptime(e, '%m/%d/%Y')
T = (datetime.date(e.year, e.month, e.day) - datetime.date(d.year, d.month, d.day)).days / 365

# Actual Stock Price
S = float(input("Please enter the current stock price of the option's company: "))

# Risk-free rate
r = float(input("Please enter the risk-free rate, approximate the risk-free rate by finding the Treasury bill rate "
                "that matures near when the option expires: "))

# Test Case
# V_market = 17.5
# print(type(V_market))
# K = 585
# T = (datetime.date(2014,10,18) - datetime.date(2014,9,8)).days / 365.
# S = 586.08
# r = 0.0002
# cp = 'c' # call option
# Answer: 21.92%

n = norm.pdf
N = norm.cdf


# *************************************************************************************************************#
# 2: Black Scholes Model
# *************************************************************************************************************#

def bs_price(cp_flag, S, K, T, r, v, q=0.0):
    d1 = (log(S / K) + (r + v * v / 2.) * T) / (v * sqrt(T))
    d2 = d1 - v * sqrt(T)
    if cp_flag == 'c':
        price = S * exp(-q * T) * N(d1) - K * exp(-r * T) * N(d2)
    else:
        price = K * exp(-r * T) * N(-d2) - S * exp(-q * T) * N(-d1)
    return price


def bs_vega(cp_flag, S, K, T, r, v, q=0.0):
    d1 = (log(S / K) + (r + v * v / 2.) * T) / (v * sqrt(T))
    return S * sqrt(T) * n(d1)


def find_vol(target_value, call_put, S, K, T, r):
    max_iterations = 100
    precision = 1.0e-5

    sigma = 0.5
    for i in range(0, max_iterations):
        price = bs_price(call_put, S, K, T, r, sigma)
        vega = bs_vega(call_put, S, K, T, r, sigma)

        price = price
        diff = target_value - price  # our root

        # print(i, sigma, diff)

        if abs(diff) < precision:
            return sigma
        sigma = sigma + diff / vega  # f(x) / f'(x)

    # value wasn't found, return best guess so far
    return sigma


implied_vol = find_vol(V_market, cp, S, K, T, r)
black_scholes_price = bs_price(cp, S, K, T, r, implied_vol)

print("Implied Volatility: {}%".format(implied_vol * 100))
print("Current Option's Price: {}".format(V_market))
print("Black Scholes Model Price: {}".format(black_scholes_price))

if V_market > black_scholes_price:
    print("This option is currently over priced.")
elif V_market == black_scholes_price:
    print("This option is priced correctly.")
else:
    print("This option is currently under priced.")
