#Read In Data
df = read.csv("https://vote.nyc/sites/default/files/pdf/election_results/2024/20241105General%20Election/00000100000Citywide%20President%20Vice%20President%20Citywide%20EDLevel.csv",
              header = FALSE)

#Fix Column Names
headers = df[1, 1:11]
df = subset(df, select = -c(1:11))
colnames(df) = headers

#Create list of Results by Precinct
library(stringr)
library(dplyr)
df$Tally = as.numeric(df$Tally)

df_tabulated <- df %>%
  group_by(AD, ED) %>%
  summarize(
    Harris = sum(Tally[str_detect(`Unit Name`, "Harris")], na.rm = TRUE),
    Trump = sum(Tally[str_detect(`Unit Name`, "Trump")], na.rm = TRUE)
  )

#Create list of precincts that were absorbed into other precincts

df_list <- df %>%
  group_by(AD, ED) %>%
  summarize(
    Status = `EDAD Status`[1],
  )
df_list = subset(df_list, Status != "IN-PLAY")
colnames(df_list) = c("AD_Inactive", "ED_Inactive", "Status")

df_list$AD_Active = sapply(sapply(df_list$Status, function(x){str_split(x, "INTO ")[[1]][2]}), function(x) {as.numeric(str_split(x, "/")[[1]][1])})
df_list$ED_Active = sapply(sapply(df_list$Status, function(x){str_split(x, "INTO ")[[1]][2]}), function(x) {as.numeric(str_split(x, "/")[[1]][2])})

  