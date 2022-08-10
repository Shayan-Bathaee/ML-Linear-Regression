# ML-Linear-Regression
This Python program implements Linear Regression using Gradient Descent on any data from a .xlsx file. 

## Files
- linear-regression.py: The python program that implements Linear Regression and Gradient Descent.
- US_GDP_example.xlsx: The default data used if no input file is provided. This data contains the U.S. GDP from 1999-2022 ([source](https://www.kaggle.com/datasets/alejopaullier/-gdp-by-country-1999-2022)).

## Usage
To run linear-regression.py, open a command prompt and navigate to the location of the file. Next, run the following command:

`python linear-regression.py -l <iterations-limit> -lr <learning-rate> -i <input-file>`

There are a few different flags in this command. Here is what they mean:
- `-l` specifies a limit to the number of iterations the program performs.
  - If no limit is provided, the program will continuously perform the linear regression until the window is closed or the program is killed.
- `-lr` specifies a learning rate.
  - The right learning rate differs for each dataset.
  - If your learning rate is too high, the slope, y-intercept, and loss will grow to very high values, and the program will yield an error.
  - If your learning rate is too low, the program will take longer to reach the line of best fit. 
  - If no learning rate is provided, the program defaults to 0.000001.
- `-i` specifies an input file.
  - The program takes in .xlsx files containing a column of Y values and a column of X values. 
  - US_GDP_example.xlsx is an example of a properly formatted input file.
  - If no input file is provided, the default file is US_GDP_example.xlsx.

To quickly review the usage from the command prompt, enter the following command:

`python linear-regression.py -help`

## Implementation
To implement this program, I used [this article](https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931) as a conceptual explanation of how linear regression and gradient descent works. After understanding the process, I developed my implementation away from the example code. In the end, I found that my program focused more on OOP and visualization than the article's example.
