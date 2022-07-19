# Election Analysis

## Overview of Election Audit

The purpose of this analysis is to perform an election audit of tabulated results for a U.S. congressional precinct in Colorado. While audits in the past have been done with Microsoft Excel, this successfully generated vote count report using Python 3.7 will serve to automate the process of auditing future elections in other congressional districts, senatorial districts, and local elections.


## Results

* 369,711 votes were cast in this congressional election. 

* Of these, 82.8% were cast in Denver County (306,055 votes), 10.5% were cast in Jefferson County (38,855 votes), and 6.7% were cast in Arapahoe County (24,801 votes).

* Denver County had the largest turnout with 306,055 votes cast.

* Charles Casper Stockham received 23.0% of the votes (85,213 votes), Diana DeGette received 73.8% (272,892 votes), and Raymon Anthony Doane received 3.1% (11,606 votes).

* Diana DeGette won the election with 73.8% of the vote (272,892 votes).


## Election Audit Summary

This analysis performed an automated election audit for a U.S. congressional precinct in Colorado and could easily be used in any election, with some small modification. For ballots with a large number of items, it is simple to add another variable to track tabulated data under the statement `for row in reader`, such as yes or no choices on ballot propositions. It is also a simple matter to change out variables to fit, such as changing `county_votes[county_name]` to `school_district_votes[school_district_name]`.