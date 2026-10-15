# Copyright 2021 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TODO: Import the relevant packages


import utilities_nl_binary

def build_model(stockcodes, returns, num_stocks_to_buy, price, budget,variance):
    """
    Requirements:
        Objective: Maximize returns
        Constraints:
            - Choose exactly num_stocks_to_buy stocks
            - The cost of the purchased stocks should be under a certain budget.
            
    Args:
        stockcodes (list): List of stocks under consideration
        returns (list): List of average monthly returns for each stock in 'stockcodes'
        num_stocks_to_buy (int): Number of stocks to purchase
        price (list): List of current daily prices for each stock in 'stockcodes'
        budget (float): Budget for purchase
        variance (2D numpy array): Entry [i][j] is the variance between stocks i and j
        
    Returns:
        model 
        stocks
    """
    
    # TODO: Initialize the nonlinear model called 'model'
    ## Hint: Remember to import the required package at the top of the file 


    # TODO: Define the binary variable and call it 'stocks'
    # Hint: Use len() to determine the total number of binary variables


    # TODO: Add the constants to the model object
    # Hint: Add the constant 'returns' to the model object and name it 'ret'
    # Hint: Add the constant 'num_stocks_to_buy' to the model object and name it 'capacity'


    # TODO: Add the constants to the model object
    # Hint: Add the constant 'price' to the model object and name it 'pri'
    # Hint: Add the constant 'budget' to the model object and name it 'bud'
    # Hint: Add the constant 'variance' to the model object and name it 'var'


    # TODO: Set the objective function: maximize returns and minimize variance
    ## Hint: Determine each objective separately, then add them together
    ## Hint: Variance is computed as a quadratic term: var[i][j]*stocks[i]*stocks[j]


    # TODO: Add a constraint to choose exactly num_stocks_to_buy stocks


    # TODO: Add a constraint that the cost of the purchased stocks is less than or equal to the budget


    return stocks, model

def sample_nl(model):

    # TODO: Instantiate the sampler, and name it 'sampler' 
    ## Hint: Remember to import the required package at the top of the file 


    # TODO: Submit the model to the NL sampler
    ## Important: Use the label 'Portfolio_Stride_Binary', this label is case sensitive and uses an underscore


if __name__ == '__main__':
    # 10 stocks used in this program
    stockcodes=["T", "SFL", "PFE", "XOM", "MO", "VZ", "IBM", "TSLA", "GILD", "GE"]

    # Compute relevant statistics like price, average returns, and covariance
    price, returns, variance = utilities_nl_binary.get_stock_info()

    # Number of stocks to buy
    num_stocks_to_buy = 2

    # Set the budget for the purchase
    budget = 40

    # Build NL
    stocks, model = build_model(stockcodes, returns, num_stocks_to_buy, price, budget,variance)

    # Run NL on hybrid solver
    sample_nl(model)
    
    # TODO: Lock the model to prevent changes


    # Process and print solution
    print("\nPart 6 solution: Submit the problem to the Stride hybrid solver with a quadratic objective using binary variables \n")
    """Read the solution returned using .state(0) and display the solution."""

    # TODO: Return the optimal solution for the binary variable symbol and store it in 'stocks_state'


    # TODO: Return the objective value of the optimal solution and store it in 'objective_value'


    selected_indices = [i for i, val in enumerate(stocks_state) if round(val) == 1]
    selected_stockcodes = [stockcodes[i] for i in selected_indices]

    print(f"Objective Value of the optimal solution: {objective_value:.6f}")
    print(f"Stocks (at state 0): {stocks_state}")
    print(f"Selected indices: {selected_indices}")
    print(f"Selected stocks: {selected_stockcodes}")
