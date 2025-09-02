# Analysis of the 2025 Democratic Mayoral Primary Election in New York
This project focuses on identifying analytic insights from the 2025 Democratic Mayoral primary election that are lacking from the many analyses that exist elsewhere on the Internet. 

## value added

**Constituent district analysis** - One element of analysis that is largely lacking from what I've been able to find elsewhere online is calculating the performance of the mayoral candidates across the various constituent districts across the city, meaning each congressional, state senate, and state assembly district. This data could be helpful for determining the ideologically lean of the many NYC component districts. 
**Simplified ranked choice voting (RCV) sequence dataset** - Split over 2 files (1M+ rows total - NYC_2025_RCV_allvotes_sequences_1_of_2.xlsx and NYC_2025_RCV_allvotes_sequences_2_of_2.xlsx), a simplified dataset of every RCV sequence submitted by voters in the Democratic mayoral primary is provided. Optimizations include: isolating Dem mayoral primary results, converting main candidate ID codes to candidate names, and filtering out non-participants. 

## sources
Election data was downloaded from [the New York City Board of Elections website](https://vote.nyc/page/election-results-summary), specifically the PRIMARY - JUNE 24, 2025 - Cast Vote Record (CVR). Notably, data was pulled before finalization and certification of the election data was completed. 

Registration data was requested via FOIL from the New York State Board of Elections website. To do so for NYC specifically, requests were made for voter lists in the five New York City counties: New York, Kings, Queens, Bronx, and Richmond.

These two sources provide ample information about the electorate that can be leveraged for key insights about the results. 
