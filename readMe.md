# Name
Fermat Near Misses

# Description
Fermat Near Misses is a program that takes n values beteen 3 and 12, and k values between 10 and 5000, and locates  
cases where x^n + y^n = z^n is cloesest to being true, starting at instances where the difference is less than 1%.  

# Execution
To use, run the executable file Fermat Near Misses and follow the instructions presented. You may also wish to run the python file
of the same name should you have python installed. If you do not, you may go to https://www.python.org/downloads/ to obtain and begin
installing python

# Use and Adjustment
When entering your n and k values, please note that per the theorem, the equation sets the exponent of each value to that n, going through all possible combinations from a minimum value of 10 to the k maximum. 

The maximum z value in the program is also larger than the k submitted, as it is calculated to be the root of the nearest whole number should both x and y be at the total k value. So, should k be 100, the maximum z value would be the n root of k^n + k^n. 

Should you be interested in working with numbers outside of the current range constraints, you may edit the code in the python file yourself by changing the number range in line 122 for a larger n value to be allowed, or you may edit line 130 for a larger k value to be allowed. Please note that the theorem does not apply to n values less than 3, and larger k values  increase the time for the program to complete exponentially.

# Support
Please reach out to the creator through their email provided in the opening comment of the program, or by leaving a comment on github for assistance.