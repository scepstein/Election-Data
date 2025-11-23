NYC Mayoral General Election 2025 - Data Files
=================================================

Generated: November 22, 2025
Source: NYC Board of Elections (https://web.enrboenyc.us/)

This directory contains unofficial election results for the NYC Mayoral General Election 2025,
organized at various geographic levels.

FILES:
------

1. unofficial_results.csv
   - Raw precinct-level election results scraped from NYC BOE website
   - Contains vote counts for all candidates by Election District (ED) and Assembly District (AD)
   - Each row represents one precinct (ED within an AD)
   - Columns: ED, AD, and candidate vote columns (format: "Candidate Name Party (Votes)")
   - Does NOT include Congressional District (CD) or Senate District (SD) mappings

2. unofficial_results_with_districts.csv
   - Enhanced precinct-level results with additional district mappings
   - Same data as unofficial_results.csv PLUS Congressional District (CD) and Senate District (SD)
   - Merged with historical district mapping data
   - Only includes precincts that could be successfully mapped to CD/SD
   - Use this file for geographic analysis across different district types

3. AD_summary.csv
   - Aggregated vote totals by Assembly District (AD)
   - Each row represents one Assembly District
   - Vote columns summed across all precincts within each AD
   - Useful for Assembly District-level analysis

4. CD_summary.csv
   - Aggregated vote totals by Congressional District (CD)
   - Each row represents one Congressional District
   - Vote columns summed across all precincts within each CD
   - Useful for Congressional District-level analysis

5. SD_summary.csv
   - Aggregated vote totals by Senate District (SD)
   - Each row represents one State Senate District
   - Vote columns summed across all precincts within each SD
   - Useful for State Senate District-level analysis

DATA STRUCTURE:
--------------

Geographic Hierarchy:
- Election District (ED): Smallest unit, corresponds to a precinct/polling place
- Assembly District (AD): State Assembly district, contains multiple EDs
- Congressional District (CD): U.S. House district, contains multiple EDs from various ADs
- Senate District (SD): State Senate district, contains multiple EDs from various ADs

Vote Columns:
- All vote-related columns contain "()" in their headers
- Format: "Candidate Name (Party)" (Votes)
- Example: "JOHN SMITH (Democratic)" (Votes)

NOTES:
------
- These are UNOFFICIAL results scraped from the NYC BOE website
- Some precincts in unofficial_results.csv may not appear in files with district mappings
  if the AD/ED combination could not be matched to historical district data
- Summary files (AD, CD, SD) only include vote columns, not other metadata
- All vote totals are integers representing the number of votes cast

DATA PROCESSING PIPELINE:
------------------------
1. scrape_unoffical_precinct_results() → unofficial_results.csv
   - Scrapes NYC BOE website for all Assembly District pages
   - Extracts HTML tables containing precinct-level vote counts
   - Parses candidate names, party affiliations, and vote totals
   - Combines multi-row headers into single column names
   - Adds AD column and cleans ED formatting
   - Removes "Total" rows to keep only individual precinct data
   - Outputs: ED, AD, and all candidate vote columns

2. map_additional_district_attributes() → unofficial_results_with_districts.csv
   - Reads unofficial_results.csv and district mapping reference file
   - Performs left join on AD and ED columns
   - Adds CD (Congressional District) and SD (Senate District) columns
   - Filters out precincts with no matching district mapping (removes null CD/SD)
   - Outputs: All columns from step 1 plus CD and SD columns

3. generate_district_reports() → AD_summary.csv, CD_summary.csv, SD_summary.csv
   - Reads unofficial_results_with_districts.csv
   - Identifies vote columns (those containing parentheses)
   - Groups by district type (AD, CD, or SD)
   - Sums all numeric vote columns within each district
   - Outputs: District ID column plus aggregated vote totals for all candidates
