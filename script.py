# LISTS
# names of the cuts offered at Carly’s Clippers
hairstyles = [
    "bouffant",
    "pixie",
    "dreadlocks",
    "crew",
    "bowl",
    "bob",
    "mohawk",
    "flattop",
]
# price of each hairstyle in the hairstyles list
prices = [30, 25, 40, 20, 20, 35, 50, 35]
# number of purchases for each hairstyle type in the last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]


# AVERAGE PRICE OF A CUT
# sum up all the prices
total_price = 0

for price in prices:
    total_price += price

# average_price => total_price divided by the number of prices
average_price = round(total_price / len(prices), 2)
print(f"Average Haircut Price: ${average_price}")

# CUT ALL PRICES BY $5
# using list comprehension
new_prices = [price - 5 for price in prices]
print(f"New prices: {new_prices}")

# HOW MUCH REVENUE WAS BROUGHT IN LAST WEEK
total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print(f"Total Revenue: ${total_revenue}")

# AVERAGE DAILY REVENUE
average_daily_revenue = total_revenue / 7
print("Average daily revenue: ${:.2f}".format(average_daily_revenue))

# SELECT HAIRCUTS WITH PRICES UNDER $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(f"Haircuts that are under 30 dollars: {cuts_under_30}")
