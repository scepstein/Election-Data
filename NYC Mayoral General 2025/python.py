import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import os

def scrape_unoffical_precinct_results(help=False):

    if help:
        print("Function: scrape_unoffical_precinct_results")
        print("Purpose: Scrapes NYC BOE website for Unofficial Mayoral General Election Results 2025")
        print("Description: Scrapes all Assembly District (AD) precinct results from the NYC BOE website,")
        print("             combines them into a single DataFrame, and saves to 'unofficial_results.csv'")
        print("Parameters:")
        print("  help (bool): If True, displays this help message and returns None. Default: False")
        print("Returns: None (saves CSV file to current working directory)")
        print("Output: unofficial_results.csv - Combined precinct-level election results with AD and ED columns")
        return None

    
    # Send GET request
    response = requests.get("https://web.enrboenyc.us/CD27286AD0.html")

    # Check if request was successful
    if response.status_code == 200:

        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Search for all <a> tags containing "CD27286"
        links = soup.find_all('a', href=lambda href: href and 'CD27286' in href)
        
        if links:
            print(f"Found {len(links)} links containing 'CD27286':")
            hrefs = [link.get('href') for link in links]
            hrefs = ['https://web.enrboenyc.us/' + href for href in hrefs]
        else:
            raise ValueError("No links containing 'CD27286' found")
        
    else:
        raise Exception(f"Failed to retrieve page. Status code: {response.status_code}")

    # Loop through each href and scrape the page
    for href in hrefs:
        response = requests.get(href)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', class_='underline')
            if table:
                # Convert HTML table to pandas DataFrame
                df = pd.read_html(StringIO(str(table)))[0]
                df = df.dropna(axis=1, how='all')
                # Concatenate first and second rows to create new column headers
                new_headers = []
                for col in df.columns:
                    first_row = str(df.iloc[0][col]) if pd.notna(df.iloc[0][col]) else ''
                    second_row = str(df.iloc[1][col]) if pd.notna(df.iloc[1][col]) else ''
                    new_header = f"{first_row} {second_row}".strip()
                    new_headers.append(new_header)

                df.columns = new_headers
                df = df.drop([0, 1]).reset_index(drop=True)
                df.columns.values[0] = 'ED'
                df['ED'] = df['ED'].str.replace('ED ', '', regex=False)
                ad_value = href.split('AD')[1][:2]
                df['AD'] = ad_value
                df = df[df['ED'] != 'Total']
                if 'combined_df' not in locals():
                    combined_df = df.copy()
                else:
                    combined_df = pd.concat([combined_df, df], ignore_index=True)
                
            else:
                raise ValueError(f"No table found on {href}")
            # Add your scraping logic here
        else:
            raise Exception(f"Failed to retrieve {href}. Status code: {response.status_code}")
    
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.getcwd(), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    output_path = os.path.join(data_dir, 'unofficial_results.csv')
    combined_df.to_csv(output_path, index=False)
    print(f"Unofficial results saved to: {output_path}")


def map_additional_district_attributes(help=False):

    if help:
        print("Function: map_additional_district_attributes")
        print("Purpose: Maps Congressional District (CD) and Senate District (SD) to precinct-level results")
        print("Description: Merges precinct results with district mappings based on AD and ED,")
        print("             adds CD and SD columns, filters out unmatched records, and generates")
        print("             aggregated reports by AD, CD, and SD")
        print("Parameters:")
        print("  help (bool): If True, displays this help message and returns None. Default: False")
        print("Returns: None (saves CSV files to current working directory)")
        print("Output: unofficial_results_with_districts.csv - Precinct results with CD and SD columns")
        print("        AD_summary.csv, CD_summary.csv, SD_summary.csv - Aggregated vote totals by district")
        return None

    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.getcwd(), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    #import datasets
    precinct_results = pd.read_csv(os.path.join(data_dir, 'unofficial_results.csv'))
    ad_ed_mapping = pd.read_csv('/workspaces/Election-Data/NYC Mayoral Dem Primary 2025/ADED_district_mappings.csv')

    # Merge the precinct results with district mappings on AD and ED columns
    precinct_results = precinct_results.merge(
        ad_ed_mapping[['AD', 'ED', 'CD', 'SD']], 
        on=['AD', 'ED'], 
        how='left'
    )
    precinct_results = precinct_results[precinct_results['CD'].notna()]
    
    # Create CSV file with updated precinct results
    output_csv_path = os.path.join(data_dir, 'unofficial_results_with_districts.csv')
    precinct_results.to_csv(output_csv_path, index=False)
    print(f"Precinct results with districts saved to: {output_csv_path}")
    

def generate_district_reports(help=False):
    
    if help:
        print("Function: generate_district_reports")
        print("Purpose: Generates aggregated election reports by district type")
        print("Description: Groups precinct results by AD, CD, and SD, summing all numeric columns")
        print("             (columns with () in header), and creates separate CSV reports for each")
        print("Parameters:")
        print("  help (bool): If True, displays this help message and returns None. Default: False")
        print("Returns: None (saves 3 CSV files to current working directory)")
        print("Output: AD_summary.csv, CD_summary.csv, SD_summary.csv")
        return None
    
    # Get data directory path
    data_dir = os.path.join(os.getcwd(), 'data')
    
    # Read the precinct results with district mappings
    precinct_results = pd.read_csv(os.path.join(data_dir, 'unofficial_results_with_districts.csv'))
    
    # Identify columns with () in header - these are the vote columns to sum
    vote_columns = [col for col in precinct_results.columns if '(' in col]
    
    # Generate report for Assembly Districts (AD)
    ad_report = precinct_results.groupby('AD')[vote_columns].sum().reset_index()
    ad_output_path = os.path.join(data_dir, 'AD_summary.csv')
    ad_report.to_csv(ad_output_path, index=False)
    print(f"Assembly District report saved to: {ad_output_path}")
    
    # Generate report for Congressional Districts (CD)
    cd_report = precinct_results.groupby('CD')[vote_columns].sum().reset_index()
    cd_output_path = os.path.join(data_dir, 'CD_summary.csv')
    cd_report.to_csv(cd_output_path, index=False)
    print(f"Congressional District report saved to: {cd_output_path}")
    
    # Generate report for Senate Districts (SD)
    sd_report = precinct_results.groupby('SD')[vote_columns].sum().reset_index()
    sd_output_path = os.path.join(data_dir, 'SD_summary.csv')
    sd_report.to_csv(sd_output_path, index=False)
    print(f"Senate District report saved to: {sd_output_path}")


def create_data_readme():
    """Create a README.txt file describing all data files in the data directory"""
    data_dir = os.path.join(os.getcwd(), 'data')
    readme_path = os.path.join(data_dir, 'README.txt')
    
    readme_content = """NYC Mayoral General Election 2025 - Data Files
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
"""
    
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    print(f"Data documentation saved to: {readme_path}")


#Function Running Area

#scrape_unoffical_precinct_results(help=True)
#map_additional_district_attributes(help=True)
create_data_readme()
