# Quant_cast_assgn

## This repo consists of Python script to fetch the most active cookie for the day along with the test file

1. This repo also consists of two csv files used for running the main script and test file. Can be be replaced by any other csv file for the main script. But make sure data follows the format "cookie,timestamp". Timestamp should be in UTC time zone. Please note that the python scripts and csv files should be in the same folder before running the scripts. If not, mention the relevant paths for the same before execution.

2. To run the main script, please use the following command:

    python most_active_cookie.py filename -d yyyy-mm-dd
    (example: python most_active_cookie.py Demo_assgn.csv -d 2018-12-08)

4. To run the test file, please use the following command:
     
    python test_most_active_cookie.py

5. To check the coverage, please use the following command:

   coverage run -m unittest test_most_active_cookie.py
   coverage report -m

   (Make sure you have installed the coverage package first before running these commands)
