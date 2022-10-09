money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

# month = 0 

def count_month(spend, salary, money_capital, increase):
    current_spend = spend
    current_capital = money_capital
    month = 0
    while current_capital > current_spend - salary:
        current_capital = current_capital - (current_spend - salary)
        current_spend = current_spend * (1 + increase)
        month = month + 1
    return month

print(count_month(spend, salary, money_capital, increase))