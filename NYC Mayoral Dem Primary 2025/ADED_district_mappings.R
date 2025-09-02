#continued from VoterFileAnalysis.R for vf_all

districts = subset(vf_all, select = c("ED","CD","SD","AD"))
districts = distinct(districts)

pad_to_3_digits <- function(x) {
  # Converts a number less than 1000 to a 3-digit character string with leading zeros
  if (!is.numeric(x) || x < 0 || x >= 1000) {
    stop("Input must be a numeric value between 0 and 999.")
  }
  sprintf("%03d", as.integer(x))
}

districts$ADED = paste("AD:", districts$AD, "ED:", pad_to_3_digits(districts$ED)) 
test = data.frame(table(districts$ADED))
print(test)
#                  Var1 Freq
#697  AD:  34  ED:  022    2
#2830 AD:  67  ED:  057    2

test = subset(vf_all, AD == 34 & ED == 22, select = c("ED","CD","SD","AD"))
test = data.frame(table(test$SD))
#Var1 Freq
#1   12  868
#2   13    1
#This indicates AD34 ED22, should be in SD 12 - will remove the SD -13 reference 

test = subset(vf_all, AD == 67 & ED == 57, select = c("ED","CD","SD","AD"))
test = data.frame(table(test$SD))
#Var1 Freq
#1   29    1
#2   47 1875
#This indicates AD67 ED57, should be in SD 47 - will remove the SD -29 reference 

test = data.frame(table(districts$ADED))
districts = districts[(!(districts$AD == 34 & districts$ED == 22 & districts$SD == 13)),]
districts = districts[(!(districts$AD == 67 & districts$ED == 57 & districts$SD == 29)),]

#Export ADED mappings 
ADED_mappings = write.csv(districts, "ADED_district_mappings.csv", row.names = FALSE)
