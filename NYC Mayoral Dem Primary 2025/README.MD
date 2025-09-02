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
 
 *Insights:* 

* **CD-8** represented by the national Democratic leader **Hakeem Jeffries** (who through now has refused to endorse Mamdani for mayor) went to Mamdani by +12%, indicating that a strong progressive challenger to Jeffries has considerable opportunity to upset. 

* **CD-12** represented by newly-announced retiring **Jerry Nadler** was a tie between Mamdani and Cuomo, indicating the potential for the progressive House member to be replaced by a more moderate figure. 
* **CD-11** represented by NYC's sole Republican **Nicole Malliotakis** actually went to Mamdani by 3%. 
* **Dan Goldman** of **CD-10** was a moderate figure who beat out a field of progressive candidates (non-ranked choice) when the seat was open. The seat went for Mamdani by a strong 36%, indicating that it's a great upset opportunity by a strong progressive challenger.

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

*Insights:* 

* **SD-13** - **Jessica Ramos** ran for mayor as well and ended up dropping out early to endorse Andrew Cuomo over Zohran Mamdani. Her district went to Mamdani by a strong +21% margin, indicating an opportunity for her to be replaced by a Mamdani-aligned candidate. 


## NYC Mayoral Primary Final Vote by State Assembly District 

|AD |Mamdani Percentage (Final Vote)|Cuomo Percentage (Final Vote)|Mamdani Margin (Final Vote)|Member                    |Member Party|
|---|-------------------------------|-----------------------------|---------------------------|--------------------------|------------|
|23 |37%                            |63%                          |-27%                       |Stacey Pheffer Amato      |Democratic  |
|24 |53%                            |47%                          |+6%                        |David Weprin              |Democratic  |
|25 |48%                            |52%                          |-5%                        |Nily Rozic                |Democratic  |
|26 |42%                            |58%                          |-15%                       |Edward Braunstein         |Democratic  |
|27 |38%                            |62%                          |-25%                       |Sam Berger                |Democratic  |
|28 |52%                            |48%                          |+4%                        |Andrew Hevesi             |Democratic  |
|29 |40%                            |60%                          |-20%                       |Alicia Hyndman            |Democratic  |
|30 |68%                            |32%                          |+36%                       |Steven Raga               |Democratic  |
|31 |37%                            |63%                          |-25%                       |Khaleel Anderson          |Democratic  |
|32 |36%                            |64%                          |-28%                       |Vivian E. Cook            |Democratic  |
|33 |42%                            |58%                          |-15%                       |Clyde Vanel               |Democratic  |
|34 |71%                            |29%                          |+41%                       |Jessica González-Rojas    |Democratic  |
|35 |47%                            |53%                          |-7%                        |Larinda Hooks             |Democratic  |
|36 |81%                            |19%                          |+62%                       |Zohran Mamdani            |Democratic  |
|37 |77%                            |23%                          |+54%                       |Claire Valdez             |Democratic  |
|38 |70%                            |30%                          |+41%                       |Jenifer Rajkumar          |Democratic  |
|39 |64%                            |36%                          |+28%                       |Catalina Cruz             |Democratic  |
|40 |52%                            |48%                          |+4%                        |Ron Kim                   |Democratic  |
|41 |31%                            |69%                          |-39%                       |Kalman Yeger              |Democratic  |
|42 |55%                            |45%                          |+9%                        |Rodneyse Bichotte Hermelyn|Democratic  |
|43 |61%                            |39%                          |+23%                       |Brian A. Cunningham       |Democratic  |
|44 |79%                            |21%                          |+58%                       |Robert Carroll            |Democratic  |
|45 |28%                            |72%                          |-43%                       |Michael Novakhov          |Republican  |
|46 |56%                            |44%                          |+12%                       |Alec Brook-Krasny         |Republican  |
|47 |54%                            |46%                          |+7%                        |William Colton            |Democratic  |
|48 |16%                            |87%                          |-71%                       |Simcha Eichenstein        |Democratic  |
|49 |58%                            |42%                          |+17%                       |Lester Chang              |Republican  |
|50 |74%                            |26%                          |+48%                       |Emily Gallagher           |Democratic  |
|51 |77%                            |23%                          |+53%                       |Marcela Mitaynes          |Democratic  |
|52 |74%                            |26%                          |+48%                       |Jo Anne Simon             |Democratic  |
|53 |83%                            |17%                          |+67%                       |Maritza Davila            |Democratic  |
|54 |71%                            |29%                          |+42%                       |Erik Martin Dilan         |Democratic  |
|55 |48%                            |52%                          |-3%                        |Latrice Walker            |Democratic  |
|56 |75%                            |25%                          |+51%                       |Stefani Zinerman          |Democratic  |
|57 |78%                            |22%                          |+57%                       |Phara Souffrant Forrest   |Democratic  |
|58 |31%                            |69%                          |-38%                       |Monique Chandler-Waterman |Democratic  |
|59 |31%                            |69%                          |-38%                       |Jaime Williams            |Democratic  |
|60 |31%                            |69%                          |-37%                       |Nikki Lucas               |Democratic  |
|61 |50%                            |51%                          |-1%                        |Charles Fall              |Democratic  |
|62 |40%                            |60%                          |-20%                       |Michael Reilly            |Republican  |
|63 |46%                            |54%                          |-7%                        |Sam Pirozzolo             |Republican  |
|64 |56%                            |44%                          |+12%                       |Michael Tannousis         |Republican  |
|65 |65%                            |35%                          |+30%                       |Grace Lee                 |Democratic  |
|66 |57%                            |43%                          |+14%                       |Deborah J. Glick          |Democratic  |
|67 |49%                            |51%                          |-3%                        |Linda Rosenthal           |Democratic  |
|68 |56%                            |44%                          |+11%                       |Eddie Gibbs               |Democratic  |
|69 |59%                            |41%                          |+17%                       |Micah Lasher              |Democratic  |
|70 |63%                            |37%                          |+26%                       |Jordan Wright             |Democratic  |
|71 |66%                            |34%                          |+32%                       |Al Taylor                 |Democratic  |
|72 |58%                            |42%                          |+17%                       |Manny De Los Santos       |Democratic  |
|73 |37%                            |63%                          |-27%                       |Alex Bores                |Democratic  |
|74 |62%                            |38%                          |+24%                       |Harvey Epstein            |Democratic  |
|75 |57%                            |43%                          |+15%                       |Tony Simone               |Democratic  |
|76 |48%                            |52%                          |-5%                        |Rebecca Seawright         |Democratic  |
|77 |38%                            |62%                          |-24%                       |Landon Dais               |Democratic  |
|78 |44%                            |56%                          |-11%                       |George Alvarez            |Democratic  |
|79 |36%                            |64%                          |-27%                       |Chantel Jackson           |Democratic  |
|80 |49%                            |51%                          |-1%                        |John Zaccaro Jr.          |Democratic  |
|81 |46%                            |54%                          |-9%                        |Jeffrey Dinowitz          |Democratic  |
|82 |38%                            |62%                          |-25%                       |Michael Benedetto         |Democratic  |
|83 |29%                            |71%                          |-43%                       |Carl Heastie              |Democratic  |
|84 |45%                            |55%                          |-10%                       |Amanda Septimo            |Democratic  |
|85 |37%                            |63%                          |-26%                       |Emerita Torres            |Democratic  |
|86 |37%                            |63%                          |-26%                       |Yudelka Tapia             |Democratic  |
|87 |49%                            |51%                          |-2%                        |Karines Reyes             |Democratic  |


## sources
Election data was downloaded from [the New York City Board of Elections website](https://vote.nyc/page/election-results-summary), specifically the PRIMARY - JUNE 24, 2025 - Cast Vote Record (CVR). Notably, data was pulled before finalization and certification of the election data was completed. 

Registration data was requested via FOIL from the New York State Board of Elections website. To do so for NYC specifically, requests were made for voter lists in the five New York City counties: New York, Kings, Queens, Bronx, and Richmond.

These two sources provide ample information about the electorate that can be leveraged for key insights about the results. 

[Helpful tool for generating tables from csv files](https://www.convertcsv.com/csv-to-markdown.htm)
