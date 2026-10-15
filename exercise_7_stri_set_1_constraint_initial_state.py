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


import utilities_nl_set

def build_model(stockcodes, returns, num_stocks_to_buy):
    """
    Requirements:
        Objective: Maximize returns
        Constraints:
            - Choose exactly num_stocks_to_buy stocks
            
    Args:
        stockcodes (list): List of stocks under consideration
        returns (list): List of average monthly returns for each stock in 'stockcodes'
        num_stocks_to_buy (int): Number of stocks to purchase
        
    Returns:
        model 
        selected_stocks
    """
    
    # TODO: Initialize the nonlinear model called 'model'
    ## Hint: Remember to import the required package at the top of the file 


    # TODO: Define the set variable and store it in 'selected_stocks'
    # Hint: Use len() to specify the total number of elements
    

    # TODO: Add the constants to the model object
    # Hint: Add the constant 'returns' to the model object and name it 'ret'


    # TODO: Set the objective function: maximize returns


    return selected_stocks, model

if __name__ == '__main__':
    # 10 stocks used in this program
    stockcodes=["T", "SFL", "PFE", "XOM", "MO", "VZ", "IBM", "TSLA", "GILD", "GE"]

    # Compute relevant statistics like price, average returns, and covariance
    price, returns, variance = utilities_nl_set.get_stock_info()

    # Number of stocks to buy
    num_stocks_to_buy = 2

    # Build NL
    selected_stocks, model = build_model(stockcodes, returns, num_stocks_to_buy)
    
    # TODO: Lock the model to prevent changes


    # Process and print solution
    print("\nPart 7 solution: Test the initial state with one constraint using set variables\n")
    """Read in initial state returned using .state(0) and display solution."""

    # TODO: Define the number of states: only 1 state will be tested 


    # TODO: Provide the following initial state: [3,4]
    # Hint: Use the `set_state()` method to assign the specifcied state to its index. 


    # TODO: Return the initial state for the set variable symbol and store it 'stocks_state'


    # TODO: Return the objective value of the initial state and store it 'objective_value'


    selected_indices = sorted(int(i) for i in stocks_state)
    selected_stocks = [stockcodes[i] for i in selected_indices]

    print(f"Objective Value of the initial state: {objective_value:.6f}")
    print(f"Stocks (at state 0): {stocks_state}")
    print(f"Selected indices: {selected_indices}")
    print(f"Selected stocks: {selected_stocks}")
