library(dplyr)
freqtable = df %>%
  group_by(Precinct, FinalVote) %>%
  summarise(count = n())

#import mappings of EDAD across AD, SD, and AD districts 
freqtable_Mamdani = subset(freqtable, FinalVote == "Mamdani", select = c("Precinct", "count"))
districts = left_join(districts, freqtable_Mamdani, c("ADED"= "Precinct"))
colnames(districts)[colnames(districts)=="count"] = "Mamdani"
freqtable_Cuomo = subset(freqtable, FinalVote == "Cuomo", select = c("Precinct", "count"))
districts = left_join(districts, freqtable_Cuomo, c("ADED"= "Precinct"))
colnames(districts)[colnames(districts)=="count"] = "Cuomo"
freqtable_invalid = subset(freqtable, FinalVote == "Invalid", select = c("Precinct", "count"))
districts = left_join(districts, freqtable_invalid, c("ADED"= "Precinct"))
colnames(districts)[colnames(districts)=="count"] = "Invalid"
districts$Total = districts$Mamdani + districts$Cuomo + districts$Invalid
districts$Total_2can = districts$Mamdani + districts$Cuomo

library(dplyr)

AD_table <- districts %>%
  group_by(AD) %>%
  summarise(
    Mamdani    = sum(Mamdani, na.rm = TRUE),
    Cuomo      = sum(Cuomo, na.rm = TRUE),
    Invalid    = sum(Invalid, na.rm = TRUE),
    Total      = sum(Total, na.rm = TRUE),
    Total_2can = sum(Total_2can, na.rm = TRUE)
  )
AD_table$Mamdani_per = AD_table$Mamdani / AD_table$Total_2can
AD_table$Cuomo_per = AD_table$Cuomo / AD_table$Total_2can
AD_table$Mamdani_margin = AD_table$Mamdani_per -AD_table$Cuomo_per

write.csv(AD_table, "AD_table.csv", row.names = FALSE)

SD_table <- districts %>%
  group_by(SD) %>%
  summarise(
    Mamdani    = sum(Mamdani, na.rm = TRUE),
    Cuomo      = sum(Cuomo, na.rm = TRUE),
    Invalid    = sum(Invalid, na.rm = TRUE),
    Total      = sum(Total, na.rm = TRUE),
    Total_2can = sum(Total_2can, na.rm = TRUE)
  )
SD_table$Mamdani_per = SD_table$Mamdani / SD_table$Total_2can
SD_table$Cuomo_per = SD_table$Cuomo / SD_table$Total_2can
SD_table$Mamdani_margin = SD_table$Mamdani_per -SD_table$Cuomo_per

write.csv(SD_table, "SD_table.csv", row.names = FALSE)

AD_table <- districts %>%
  group_by(AD) %>%
  summarise(
    Mamdani    = sum(Mamdani, na.rm = TRUE),
    Cuomo      = sum(Cuomo, na.rm = TRUE),
    Invalid    = sum(Invalid, na.rm = TRUE),
    Total      = sum(Total, na.rm = TRUE),
    Total_2can = sum(Total_2can, na.rm = TRUE)
  )
AD_table$Mamdani_per = AD_table$Mamdani / AD_table$Total_2can
AD_table$Cuomo_per = AD_table$Cuomo / AD_table$Total_2can
AD_table$Mamdani_margin = AD_table$Mamdani_per -AD_table$Cuomo_per

write.csv(AD_table, "AD_table.csv", row.names = FALSE)
