# Town of Hempstead, New York Election Analysis

| Year | Contest                   | Dem Candidate     | GOP Candidate         | Dem Votes | GOP Votes | Total Votes | Dem Percent   | GOP Percent  | Dem Margin  |
|------|---------------------------|-------------------|-----------------------|-----------|-----------|--------------|--------------|--------------|-------------|
| 2024 | Presidential Election     | Kamala Harris     | Donald Trump          | 195,692   | 197,919   | 398,534      | 49.1%        | 49.7%        | -0.6%       |
| 2022 | Gubernatorial Election    | Kathy Hochul      | Lee Zeldin            | 132,414   | 155,534   | 287,948      | 46.0%        | 54.0%        | -8.0%       |
| 2022 | Attorney General Election | Letitia James     | Michael Henry         | 133,454   | 150,536   | 283,990      | 47.0%        | 53.0%        | -6.0%       |
| 2022 | US Senator Election       | Chuck Schumer     | Joe Pinion            | 140,870   | 144,091   | 285,692      | 49.3%        | 50.4%        | -1.1%       |
| 2021 | TOH Supervisor            | Jason Abelove     | Donald Clavin         | 49,095    | 93,550    | 142,645      | 34.4%        | 65.6%        | -31.2%      |
| 2021 | County Executive          | Laura Curran      | Bruce Blakeman        | 78,416    | 77,903    | 156,412      | 50.1%        | 49.8%        | 0.3%        |
| 2020 | Presidential Election     | Joe Biden         | Donald Trump          | 226,129   | 174,951   | 406,360      | 55.6%        | 43.1%        | 12.6%       |
| 2018 | Gubernatorial Election    | Andrew Cuomo      | Mark Molinaro         | 162,135   | 109,426   | 271,561      | 59.7%        | 40.3%        | 19.4%       |
| 2018 | US Senator Election       | Kirsten Gillibrand| Chele Chiavacci Farley| 168,567   | 109,666   | 278,233      | 60.6%        | 39.4%        | 21.2%       |
| 2017 | TOH Supervisor            | Laura Gillen      | Anthony Santino       | 80,214    | 77,946    | 158,160      | 50.7%        | 49.3%        | 1.4%        |
| 2016 | Presidential Election     | Hillary Clinton   | Donald Trump  | 80,214    | 77,946    | 158,160      | 50.7%        | 49.3%        | 1.4%        |


## Data Sources

2024 Presidential Election data is sourced from [the New York Times presidential-precinct-map-2024 Github repo](https://github.com/nytimes/presidential-precinct-map-2024?tab=readme-ov-file#download-national-data). The New York specific .csv file was pulled. Data can be isolated for Nassau County by looking for precincts that start with 36059 (FIPS code for Nassau County). The precincts corresponding to Town of Hempstead will start with 3605902 (Town code for Town of Hempstead - see below table).

Nassau County townships are encoded with by the following key:
|Code|Abbv.|Township|
|---|---|---|
|1|GC|Glen Cove|
|2|HE|Hempstead|
|3|LB|Long Beach|
|4|NH|North Hempstead|
|5|OB|Oyster Bay|

2022 Gubernatorial results were obtained from [Muckrock](https://www.muckrock.com/foi/nassau-county-316/nassau-county-2022-general-election-precinct-level-results-138779/#file-1076641). I have already prepared them as a shapefile in a [prior project](https://github.com/scepstein/Election-Data/tree/main/Nassau%20County%2C%20NY%20'22). The same was used for the Attorney General race and the U.S. Senator race.

The 2021 Town Supervisor results were pulled from [local news](https://patch.com/new-york/wantagh/hempstead-town-supervisor-clavin-easily-wins-reelection).

2020 Presidential election and 2021 County Executive results were pulled from an old project where I had already isolated them. 

2018 precinct results from the Governor's race and US Senate race were sourced from the [MIT Election Lab](https://dataverse.harvard.edu/file.xhtml?fileId=6692578&version=1.1).

2017 Town Supervisor results were sourced from [local news](https://patch.com/new-york/rockvillecentre/election-2017-town-hempstead-live-results).
