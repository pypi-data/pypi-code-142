# Net Income 
def net_income(total_revenues:float,total_cost:float):
    '''
    Returns the net income or total profit gained/loss occured.
        Parameters:
            total_revenues (float): Total revenue generated
            total_revenues (float): Total costs incurred 
        Returns:
            net_income (float): Value of the net income
    '''
    net_income = ( total_revenues - total_cost ) 
    return net_income

# Simple Interest 
def simple_interest(principal:float,interest_rate:float,num_of_years:int):
    '''
    Returns the total value of simple interest
        Parameters:
            principle (float): Present value of the investment
            interest_rate (float): Interest rate per period, e.g. year
            num_of_years (int): Term of the investment
        Returns:
            simple_interest (float): Value of the simple interest after the term
    '''
    simple_interest = ( principal * interest_rate * num_of_years )  
    return simple_interest

# Compound Interest 
def compound_interest(principal:float,interest_rate:float,num_of_years:int,times_compounded:int=1):
    '''
    Returns the total value of compound interest
        Parameters:
            principle (float): Present value of the investment
            interest_rate (float): Interest rate per period, e.g. year
            num_of_years (int): Term of the investment
            times_compounded (int): Number of compoundings per period( or year), default 1 ( annually ) 
                Example : For half yearly compounding frequency : 2
        Returns:
            compound_interest (float): Value of the compounded interest after the term
    '''
    compounded_amount = principal * ( pow((1+interest_rate/times_compounded),(times_compounded * num_of_years)))
    compound_interest = compounded_amount - principal 
    return compound_interest
    
# Inflation Adjusted Value 
def inflation_adjusted_value(principle:float,inflation_rate:float,num_of_years:int=1):
    '''
    Returns the future value of principal adjusted for inflation at the end of the period.
        Parameters:
            principle (float): Present value of the investment
            inflation_rate (float): Inflation rate per period, e.g. year
            num_of_years (int): Term of the investment 
            times_compounded (int): Number of compoundings per period( or year), default 1(annually) 
                Example : For half yearly compounding frequency : 6
        Returns:
            future_value (float): Value of the inflation adjusted value after the term
    '''
    future_value = principle * ( (1+inflation_rate) ** num_of_years )
    return future_value

# Purchasing Power
def purchasing_power(principle:float,inflation_rate:float,num_of_years:int=1):
    '''
    Returns the purchasing power of the principal at the end of the period.
        Parameters:
            principle (float): Present value of the investment
            inflation_rate (float): Inflation rate per period, e.g. year
            num_of_years (int): Term of the investment 
        Returns:
            future_value (float): Future value of the principal after the term
    '''
    future_amount = principle / ( (1+inflation_rate) ** num_of_years )
    return future_amount

# Compounded Annual Growth Rate 
def compounded_annual_growth_rate(future_value:float,current_value:float,num_of_years:int=1):
    '''
    Returns the return on an investment over a period
        Parameters:
            future_value (float): Expected Future value of the investment
            current_value (float): Present value of the investment
            num_of_years (int): Term of the investment 
        Returns:
            cagr (float): compounded annual growth rate after the term
    '''
    cagr = ( pow((future_value/current_value) , (1.0/num_of_years) ) ) - 1 
    return cagr

