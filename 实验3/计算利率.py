s = input()
money,year,rate = s.split()
money = eval(money)
year = eval(year)
rate = eval(rate)
interest = money*(1+rate)**year-money
print("interest={0:.2f}".format(interest))