# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given us an election_result.CSV file that listed a recent local congressional election. This project will generate an election audit report that contains:

1. Total number of voter
2. Total number of votes for each county
3. The percentage of votes from each county
4. Determine which county has the highest turnout
5. A complete list of candidates who received votes.
6. Number of votes each candidate received.
7. The percentage of votes each candidate won.
8. The Winner of the election based on popular vote.
9. Print all results from list #1-8 on a text file (election_results.txt)

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code

## Election-Audit Result
The analysis of the election shows that:
- There was a total of 369,711 votes cast in this congressional election.
- The county were:
    - Jefferson
    - Denver
    - Arapahoe
- The county results were:
    - Jefferson has 38,855 votes, and the percentage is 10.5% out of the total votes.
    - Denver has 306,055 votes, and the percentage is 82.2% out of total votes.
    - Arapahoe has 24,801 votes, and the percentage is 6.7% out of total votes. 
- Denver had the largest number of vote

- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.    
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

![](https://github.com/helen3121433/Election_Analysis/blob/main/myDraft/Election_results_terminal.PNG)

## Election-Audit Summary

This script can generate an election report for any election. For example, if the election CSV file has the voting method. We can modify the script by telling how many votes were from the mail-in Ballot, how many were punch cards, and how many were direct recording electronic. We can also determine which voting methods are more popular. If the election CSV file were for nationwide elections, we can also modify the script by adding a total number of votes from each state. Additionally, we can also write a new statement to determine the percentage of different political parties in each state. Overall, this script could help many different elections, as long as we have data in rows and columns.

