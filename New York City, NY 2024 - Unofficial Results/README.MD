# New York City Election Results (2024 General Election)
## Data Source
Voting data on the level of Election District was sourced from New York City Board of Elections website ([https://vote.nyc/page/election-results-summary](https://vote.nyc/page/election-results-summary)).
Data was pulled from the site using [Organize Data.R](Organize Data.R) and organized into two tables: (1) Harris '24 and Trump '24 votes by precinct (AD/ED) [ADED24.csv](ADED24.csv) and (2) list of precincts for which results were combined into another precinct [ADEDremap.csv](ADEDremap.csv). 
The download took place on January 14, 2025. The raw data is available as a csv ([00000100000Citywide President Vice President Citywide EDLevel.csv](00000100000Citywide President Vice President Citywide EDLevel.csv)).

Geospatial data on Election Districts was pulled from the New York City Open Data portal on December 1, 2024 ([https://data.cityofnewyork.us/City-Government/nyed/wwxk-38u4/about_data](https://data.cityofnewyork.us/City-Government/nyed/wwxk-38u4/about_data)) and uploaded as [nyed_24c](nyed_24c).
