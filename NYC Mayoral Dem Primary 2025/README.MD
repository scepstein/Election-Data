# Analysis of the 2025 Democratic Mayoral Primary Election in New York
This project focuses on identifying analytic insights from the 2025 Democratic Mayoral primary election that are lacking from the many analyses that exist elsewhere on the Internet. 

## value added

**Congressional, State Senate, State Assembly, and City Council district results** - This analysis provides tabulations from the mayoral race across the various constituent districts across the city at the congressional, state senate, state assembly, and city council district level (results that are not widely available). This data could be helpful for determining the ideological lean of the many NYC component districts. 

**Simplified ranked choice voting (RCV) sequence dataset** - Split over 2 files (1M+ rows total - NYC_2025_RCV_allvotes_sequences_1_of_2.xlsx and NYC_2025_RCV_allvotes_sequences_2_of_2.xlsx), a simplified dataset of every RCV sequence submitted by voters in the Democratic mayoral primary is provided. The following optimizations were made to what is currently available online: isolating Dem mayoral primary results from other races, converting candidate ID codes to candidate names for accessibility, and filtering out non-participant votes. 

## NYC Mayoral Primary Final Vote by Congressional District 

|CD |Mamdani Percentage (Final Vote)|Cuomo Percentage (Final Vote)|Mamdani Margin  (Final Vote)|Member                  |Member Party|
|---|-------------------------------|-----------------------------|----------------------------|------------------------|------------|
|3  |46%                            |54%                          |-8%                         |Tom Suozzi              |DEM         |
|5  |40%                            |60%                          |-20%                        |Gregory Meeks           |DEM         |
|6  |51%                            |49%                          |+3%                         |Grace Meng              |DEM         |
|7  |76%                            |24%                          |+52%                        |Nydia Velazquez         |DEM         |
|8  |56%                            |44%                          |+12%                        |Hakeem Jeffries         |DEM         |
|9  |52%                            |48%                          |+4%                         |Yvette Clarke           |DEM         |
|10 |68%                            |32%                          |+36%                        |Dan Goldman             |DEM         |
|11 |52%                            |48%                          |+3%                         |Nicole Malliotakis      |GOP         |
|12 |50%                            |50%                          |+0.1%                       |Jerry Nadler            |DEM         |
|13 |60%                            |40%                          |+20%                        |Adriano Espaillat       |DEM         |
|14 |62%                            |38%                          |+24%                        |Alexandria Ocasio-Cortez|DEM         |
|15 |40%                            |60%                          |-19%                        |Ritchie Torres          |DEM         |
|16 |27%                            |73%                          |-47%                        |George Latimer          |DEM         |





## sources
Election data was downloaded from [the New York City Board of Elections website](https://vote.nyc/page/election-results-summary), specifically the PRIMARY - JUNE 24, 2025 - Cast Vote Record (CVR). Notably, data was pulled before finalization and certification of the election data was completed. 

Registration data was requested via FOIL from the New York State Board of Elections website. To do so for NYC specifically, requests were made for voter lists in the five New York City counties: New York, Kings, Queens, Bronx, and Richmond.

These two sources provide ample information about the electorate that can be leveraged for key insights about the results. 
