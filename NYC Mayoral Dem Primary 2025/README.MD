# Analysis of the 2025 Democratic Mayoral Primary Election in New York
This project focuses on identifying analytic insights from the 2025 Democratic Mayoral primary election that are lacking from the many analyses that exist elsewhere on the Internet. 

## value added

**Congressional, State Senate, State Assembly, and City Council district results** - This analysis provides tabulations from the mayoral race across the various constituent districts across the city at the congressional, state senate, state assembly, and city council district level (results that are not widely available). This data could be helpful for determining the ideological lean of the many NYC component districts. 

**Simplified ranked choice voting (RCV) sequence dataset** - Split over 2 files (1M+ rows total - NYC_2025_RCV_allvotes_sequences_1_of_2.xlsx and NYC_2025_RCV_allvotes_sequences_2_of_2.xlsx), a simplified dataset of every RCV sequence submitted by voters in the Democratic mayoral primary is provided. The following optimizations were made to what is currently available online: isolating Dem mayoral primary results from other races, converting candidate ID codes to candidate names for accessibility, and filtering out non-participant votes. 

## NYC Mayoral Primary Final Vote by Congressional District 

|SD |Mamdani Percentage (Final Vote)|Cuomo Percentage (Final Vote)|Mamdani Margin  (Final Vote)|Member                  |Member Party|
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

## NYC Mayoral Primary Final Vote by State Senate District 

|SD |Mamdani Percentage (Final Vote)|Cuomo Percentage (Final Vote)|Mamdani Margin (Final Vote)|Member                   |Member Party|
|---|-------------------------------|-----------------------------|---------------------------|-------------------------|------------|
|10 |32%                            |68%                          |-37%                       |James Sanders Jr.        |Democratic  |
|11 |52%                            |48%                          |+4%                        |Toby Ann Stavisky        |Democratic  |
|12 |75%                            |25%                          |+51%                       |Michael Gianaris         |Democratic  |
|13 |60%                            |40%                          |+21%                       |Jessica Ramos            |Democratic  |
|14 |39%                            |61%                          |-21%                       |Leroy Comrie             |Democratic  |
|15 |54%                            |46%                          |+8%                        |Joseph Addabbo Jr.       |Democratic  |
|16 |48%                            |52%                          |-5%                        |John Liu                 |Democratic  |
|17 |63%                            |37%                          |+26%                       |Stephen T. Chan          |Republican  |
|18 |76%                            |24%                          |+52%                       |Julia Salazar            |Democratic  |
|19 |32%                            |68%                          |-36%                       |Roxanne Persaud          |Democratic  |
|20 |70%                            |30%                          |+40%                       |Zellnor Myrie            |Democratic  |
|21 |50%                            |50%                          |+1%                        |Kevin Parker             |Democratic  |
|22 |21%                            |80%                          |-59%                       |Sam Sutton               |Democratic  |
|23 |46%                            |54%                          |-9%                        |Jessica Scarcella-Spanton|Democratic  |
|24 |44%                            |56%                          |-13%                       |Andrew Lanza             |Republican  |
|25 |74%                            |26%                          |+48%                       |Jabari Brisport          |Democratic  |
|26 |73%                            |27%                          |+47%                       |Andrew Gounardes         |Democratic  |
|27 |62%                            |38%                          |+25%                       |Brian P. Kavanagh        |Democratic  |
|28 |42%                            |58%                          |-15%                       |Liz Krueger              |Democratic  |
|29 |50%                            |50%                          |-0.2%                      |José M. Serrano          |Democratic  |
|30 |63%                            |37%                          |+26%                       |Cordell Cleare           |Democratic  |
|31 |58%                            |42%                          |+17%                       |Robert Jackson           |Democratic  |
|32 |38%                            |62%                          |-24%                       |Luis R. Sepúlveda        |Democratic  |
|33 |46%                            |54%                          |-9%                        |Gustavo Rivera           |Democratic  |
|34 |49%                            |51%                          |-2%                        |Nathalia Fernandez       |Democratic  |
|36 |31%                            |69%                          |-38%                       |Jamaal Bailey            |Democratic  |
|47 |53%                            |47%                          |+5%                        |Brad Hoylman-Sigal       |Democratic  |
|59 |74%                            |26%                          |+49%                       |Kristen Gonzalez         |Democratic  |


## sources
Election data was downloaded from [the New York City Board of Elections website](https://vote.nyc/page/election-results-summary), specifically the PRIMARY - JUNE 24, 2025 - Cast Vote Record (CVR). Notably, data was pulled before finalization and certification of the election data was completed. 

Registration data was requested via FOIL from the New York State Board of Elections website. To do so for NYC specifically, requests were made for voter lists in the five New York City counties: New York, Kings, Queens, Bronx, and Richmond.

These two sources provide ample information about the electorate that can be leveraged for key insights about the results. 
