# Analysis of the 2025 Democratic Mayoral Primary Election in New York
This project focuses on identifying analytic insights from the 2025 Democratic Mayoral primary election that are lacking from the many analyses that exist elsewhere on the Internet. 

## value added

**Congressional, State Senate, State Assembly, and City Council district results** - This analysis provides tabulations from the mayoral race across the various constituent districts across the city at the congressional, state senate, state assembly, and city council district level (results that are not widely available). This data could be helpful for determining the ideological lean of the many NYC component districts. 

**Simplified ranked choice voting (RCV) sequence dataset** - Split over 2 files (1M+ rows total - NYC_2025_RCV_allvotes_sequences_1_of_2.xlsx and NYC_2025_RCV_allvotes_sequences_2_of_2.xlsx), a simplified dataset of every RCV sequence submitted by voters in the Democratic mayoral primary is provided. The following optimizations were made to what is currently available online: isolating Dem mayoral primary results from other races, converting candidate ID codes to candidate names for accessibility, and filtering out non-participant votes. 

## sources
Election data was downloaded from [the New York City Board of Elections website](https://vote.nyc/page/election-results-summary), specifically the PRIMARY - JUNE 24, 2025 - Cast Vote Record (CVR). Notably, data was pulled before finalization and certification of the election data was completed. 

Registration data was requested via FOIL from the New York State Board of Elections website. To do so for NYC specifically, requests were made for voter lists in the five New York City counties: New York, Kings, Queens, Bronx, and Richmond.

These two sources provide ample information about the electorate that can be leveraged for key insights about the results. 
