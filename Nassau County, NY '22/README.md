
# Nassau County, NY 2022 Elections Results by Precinct

### insert image here

Precinct-level election results and geographic boundaries for the following elections/candidates (Nassau County, NY Nov. 2022) are included in the data set:
Contest Name|Candidate Name|Major Party|
| ------------- |-------------|-------------|
|Governor and Lieutenant Governor |Kathy C. Hochul |DEM|
|Governor and Lieutenant Governor |Lee Zeldin |REP|
|Attorney General |Letitia A. James |DEM|
|Attorney General |Michael Henry |REP|
|United States Senator |Charles E. Schumer |DEM|
|United States Senator |Joe Pinion |REP|
|United States Senator |Diane Sare |THIRD|
|Representative in Congress District 2 |Jackie Gordon |DEM|
|Representative in Congress District 2 |Andrew R. Garbarino |REP|
|Representative in Congress District 3 |Robert P. Zimmerman |DEM|
|Representative in Congress District 3 |George A.D. Santos |REP|
|Representative in Congress District 4 |Laura A. Gillen |DEM|
|Representative in Congress District 4 |Anthony P. D'Esposito |REP|

###### Note: Write-in votes were not included in the data set. 
###### Note: Not every precinct for which there are geographic bounds has corresponding election data.

Data set contains the following information:
* Vote Total by Candidate per Precinct
* Vote Percentage by Candidate per Precinct
* Geographic Bounds per Precinct

## _Nassau_2022_precinctlevel.geojson_

#### File Mapping:
Rows = individual precincts
|Column Name|Contest Name|Candidate Name|Major Party|Metric|
| ------------- |-------------|-------------|-------------|-------------|
|GUB_DEM_votes|Governor and Lieutenant Governor |Kathy C. Hochul |DEM|Votes|
|GUB_REP_votes|Governor and Lieutenant Governor |Lee Zeldin |REP|Votes|
|AG_DEM_votes|Attorney General |Letitia A. James |DEM|Votes|
|AG_REP_votes|Attorney General |Michael Henry |REP|Votes|
|SEN_DEM_votes|United States Senator |Charles E. Schumer |DEM|Votes|
|SEN_REP_votes|United States Senator |Joe Pinion |REP|Votes|
|SEN_3RD_votes|United States Senator |Diane Sare |THIRD|Votes|
|CD2_DEM_votes|Representative in Congress District 2 |Jackie Gordon |DEM|Votes|
|CD2_REP_votes|Representative in Congress District 2 |Andrew R. Garbarino |REP|Votes|
|CD3_DEM_votes|Representative in Congress District 3 |Robert P. Zimmerman |DEM|Votes|
|CD3_REP_votes|Representative in Congress District 3 |George A.D. Santos |REP|Votes|
|CD4_DEM_votes|Representative in Congress District 4 |Laura A. Gillen |DEM|Votes|
|CD4_REP_votes|Representative in Congress District 4 |Anthony P. D'Esposito |REP|Votes|
|GUB_DEM_per|Governor and Lieutenant Governor |Kathy C. Hochul |DEM|Percentage|
|GUB_REP_per|Governor and Lieutenant Governor |Lee Zeldin |REP|Percentage|
|AG_DEM_per|Attorney General |Letitia A. James |DEM|Percentage|
|AG_REP_per|Attorney General |Michael Henry |REP|Percentage|
|SEN_DEM_per|United States Senator |Charles E. Schumer |DEM|Percentage|
|SEN_REP_per|United States Senator |Joe Pinion |REP|Percentage|
|SEN_3RD_per|United States Senator |Diane Sare |THIRD|Percentage|
|CD2_DEM_per|Representative in Congress District 2 |Jackie Gordon |DEM|Percentage|
|CD2_REP_per|Representative in Congress District 2 |Andrew R. Garbarino |REP|Percentage|
|CD3_DEM_per|Representative in Congress District 3 |Robert P. Zimmerman |DEM|Percentage|
|CD3_REP_per|Representative in Congress District 3 |George A.D. Santos |REP|Percentage|
|CD4_DEM_per|Representative in Congress District 4 |Laura A. Gillen |DEM|Percentage|
|CD4_REP_per|Representative in Congress District 4 |Anthony P. D'Esposito |REP|Percentage|
|geometry|N/A|N/A|NA|geometry|

#### Future Usage/How To Import GeoJson File in R:
```
library(sf)
map = as.data.frame(st_read("Nassauprecints.geojson"))
```

## Information on Precincts 
Precint names operate on the following nomenclature in Nassau County, NY:
|Digits|Encodes|
|---|----|
|1|Township*|
|2-3|Assembly District|
|4-6|Election District|
###### All feature leading zeroes when possible
Townships are encoded with by the following key:
|Code|Abbv.|Township|
|---|---|---|
|1|GC|Glen Cove|
|2|HE|Hempstead|
|3|LB|Long Beach|
|4|NH|North Hempstead|
|5|OB|Oyster Bay|

## File Build Information for _Nassau_2022_precinctlevel.geojson_
#### Built with following R Code:
```
data = read.csv("2022_Nassau_PrecinctLeveldata.csv")

#Function delivers a df based on ContestTitle and Candidate Name
PullData = function(df, ContestTitleString, CandidateNameString){
  test = subset(data, ContestTitle == ContestTitleString)
  test2 = subset(test, CandidateName == CandidateNameString)
  library(dplyr)
  result = test2 %>%
    group_by(PrecinctName) %>%
    summarise(Votes = sum(Voters_Votes, na.rm=FALSE))
  return(result)
}

datadict = read.csv("datadict.csv")

for(x in 1:length(datadict$Column.Name)){
  if(datadict$Metric[x]=="Votes"){
    if(x == 1){
      df = PullData(df=data, ContestTitleString=datadict$Contest.Name[1], CandidateNameString=datadict$Candidate.Name[1])
      colnames(df)[2] = datadict$Column.Name[1]
    }
    if (x > 1){
      df2 = PullData(df=data, ContestTitleString=datadict$Contest.Name[x], CandidateNameString=datadict$Candidate.Name[x])
      colnames(df2)[2] = datadict$Column.Name[x]
      df = full_join(df, df2, by = c("PrecinctName" = "PrecinctName"))
      rm(df2)
    }
  }
  if(datadict$Metric[x]=="Percentage"){
    df$New = df[,which(colnames(df)==subset(datadict, Metric=="Votes" & Contest.Name==datadict$Contest.Name[x] & Candidate.Name==datadict$Candidate.Name[x])$Column.Name)] /
      rowSums(df[,subset(datadict, Metric == "Votes")$Column.Name[which(subset(datadict, Metric == "Votes")$Contest.Name == datadict$Contest.Name[x])]])
    df$New = df$New[,1]
    colnames(df)[which(colnames(df)=="New")]=datadict$Column.Name[x]
  }
}
library(sf)
map = as.data.frame(st_read("Nassauprecints.geojson"))
map = subset(map, select = c(3, 8))
map$TADED = as.numeric(map$TADED)
df = full_join(df, map, by = c("PrecinctName" = "TADED"))
st_write(df, "Nassau_2022_precinctlevel.geojson", driver = "GeoJSON")

```

## Supporting File: _GEN2022.ASC_
#### Usage:
Source of all election data. 

#### Source: 
[Muckrock: Nassau County 2022 general election precinct-level results](https://www.muckrock.com/foi/nassau-county-316/nassau-county-2022-general-election-precinct-level-results-138779/#file-1076641)

#### File Mapping:
See ASCII_File_Specs_Preinct_Detail_Text_No_Groups.pdf

## Supporting File: _2022_Nassau_PrecinctLeveldata.csv_
#### Converted from _GEN2022.ASC_ with following R Code:

```{R}
library(rstudioapi)
setwd(file.path(dirname(rstudioapi::getSourceEditorContext()$path)))

data = data.frame(lines = readLines("GEN2022.ASC"), stringsAsFactors = FALSE)

data$ContestNumber = substr(data$lines, 1, 4)
data$CandidateNumber = substr(data$lines, 5, 7)
data$PrecinctCode = substr(data$lines, 8, 11)
data$Voters_Votes = substr(data$lines, 12, 17) #prints in contest area only
data$PartyCode = substr(data$lines, 18, 20)
data$DistrictIDType = substr(data$lines, 21, 23)
data$DistrictCode = substr(data$lines, 24, 27)
data$ContestTitle = substr(data$lines, 28, 83)
data$CandidateName = substr(data$lines, 84, 121)
data$PrecinctName = substr(data$lines, 122, 151)
data$DistrictName = substr(data$lines, 152, 176)
data$VotesAllowed = substr(data$lines, 177, 178)
data$ReferendumFlag = substr(data$lines, 179, 179)
data$CRCode = substr(data$lines, 180, 180)
data$LFCode = substr(data$lines, 181, 181)

#Remove Excess Spaces in Key fields
data$ContestTitle = gsub("\\s+", " ", data$ContestTitle)
data$CandidateName = gsub("\\s+", " ", data$CandidateName)
data$PrecinctName = gsub("\\s+", " ", data$PrecinctName)
data$DistrictName = gsub("\\s+", " ", data$DistrictName)

data$ContestNumber = as.numeric(data$ContestNumber)
data$CandidateNumber = as.numeric(data$CandidateNumber)
data$PrecinctCode = as.numeric(data$PrecinctCode)
data$Voters_Votes = as.numeric(data$Voters_Votes)

write.csv(data, "2022_Nassau_PrecinctLeveldata.csv", row.names = FALSE)
```

#### File Mapping:
See ASCII_File_Specs_Preinct_Detail_Text_No_Groups.pdf

## Supporting File: _Nassauprecints.geojson_
#### Usage:
Source of geographic boundaries for precincts. 
#### Source: 
[Nassau County BOE: Voting Precinct Maps | Nassau County, NY - Official Website results](https://www.nassaucountyny.gov/5543/Voting-Precinct-Maps)

#### Precincts were uploaded as separate shapefiles and combined with the following code:
```
library(rstudioapi)
setwd(file.path(dirname(rstudioapi::getSourceEditorContext()$path)))
library(sf)
library(stringr)
library(dplyr)
for(x in 1:length(list.files("NC BOE Precinct Maps"))){
  if(x == 1){
    df = as.data.frame(st_read(paste("NC BOE Precinct Maps", list.files("NC BOE Precinct Maps")[x], list.files(paste("NC BOE Precinct Maps", list.files("NC BOE Precinct Maps")[x], sep = "/"))[which(str_detect(list.files(paste("NC BOE Precinct Maps", list.files("NC BOE Precinct Maps")[x], sep = "/")), "shp")==TRUE)[1]], sep = "/")))
  }
  if(x > 1){
    df = full_join(df, as.data.frame(st_read(paste("NC BOE Precinct Maps", 
list.files("NC BOE Precinct Maps")[x], list.files(paste("NC BOE Precinct Maps", list.files("NC BOE Precinct Maps")[x], 
sep = "/"))[which(str_detect(list.files(paste("NC BOE Precinct Maps", list.files("NC BOE Precinct Maps")[x], sep = "/")), 
                             "shp")==TRUE)[1]], sep = "/"))))
    }
}
st_write(df, "Nassauprecints.geojson", driver = "GeoJSON")

```
## Code for developing preview map
```
library(ggplot2)
ggplot()+
  geom_sf(data= df, aes(fill=GUB_DEM_per, geometry = geometry))
ggsave("plot_image.png", width = 6, height = 6, dpi = 300)
```
## Additional Data
Original source data also included election results for the following contests that were not included in the geojson file (a similar procedure can be used to extract data from these races):
* State Comptroller 
* Justice of the Supreme Court 
* County Court Judge 
* Family Court Judge 
* District Court Judge District 1 
* District Court Judge District 2 
* District Court Judge District 4 
* State Senator District 5 
* State Senator District 6 
* State Senator District 7 
* State Senator District 8 
* State Senator District 9 
* Member of Assembly District 9 
* Member of Assembly District 10 
* Member of Assembly District 11 
* Member of Assembly District 13 
* Member of Assembly District 14 
* Member of Assembly District 15 
* Member of Assembly District 16 
* Member of Assembly District 17 
* Member of Assembly District 18 
* Member of Assembly District 19 
* Member of Assembly District 20 
* Member of Assembly District 21 
* Member of Assembly District 22 
* City Judge City of Glen Cove 
* Council Member District 3 Town of Hempstead 
* Proposal Number One, A Proposition 
