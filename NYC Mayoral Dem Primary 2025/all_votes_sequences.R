#Sam's Electoral System Applied to the 2021 Democratic Ranked Choice Primary

#Set working directory
library(rstudioapi)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

library(openxlsx)
library(stringr)

# List files in that directory
files <- list.files(dirname(getActiveDocumentContext()$path))
files = files[!str_detect(files, "~")]
files = files[!str_detect(files, "RCV analysis")]
files = files[!str_detect(files, "hash")]
files = files[!str_detect(files, "Candidacy")]
files = files[!str_detect(files, "Candidates")]

for (x in 1:length(files)){
  if (x == 1){
    df <- read.xlsx(files[x])
    df = df[,c("Cast.Vote.Record", "Precinct",
               "DEM.Mayor.Choice.1.of.5.Citywide.(026916)",
               "DEM.Mayor.Choice.2.of.5.Citywide.(226916)", 
               "DEM.Mayor.Choice.3.of.5.Citywide.(326916)", 
               "DEM.Mayor.Choice.4.of.5.Citywide.(426916)", 
               "DEM.Mayor.Choice.5.of.5.Citywide.(526916)")]
      }
  else{
    data <- read.xlsx(files[x])
    data = data[,c("Cast.Vote.Record", "Precinct",
               "DEM.Mayor.Choice.1.of.5.Citywide.(026916)",
               "DEM.Mayor.Choice.2.of.5.Citywide.(226916)", 
               "DEM.Mayor.Choice.3.of.5.Citywide.(326916)", 
               "DEM.Mayor.Choice.4.of.5.Citywide.(426916)", 
               "DEM.Mayor.Choice.5.of.5.Citywide.(526916)")]
    df = rbind(df, data)
    print(paste("completed file", x))
  }
}
#Code yields 1114433 rows

#remove people who did not vote in this election (GOP voters)
df= subset(df, `DEM.Mayor.Choice.1.of.5.Citywide.(026916)`!="undervote")
#code yields 1073898 rows

#254052 = Cuomo
#254286 = Mamdani

dfFinalVote = c("Invalid")
df$FinalVote[df$`DEM.Mayor.Choice.1.of.5.Citywide.(026916)` == 254052] = "Cuomo"
df$FinalVote[df$`DEM.Mayor.Choice.1.of.5.Citywide.(026916)` == 254286] = "Mamdani"
df$FinalVote[df$FinalVote == "Invalid" & df$`DEM.Mayor.Choice.2.of.5.Citywide.(226916)` == 254052] = "Cuomo"
df$FinalVote[df$FinalVote == "Invalid" & df$`DEM.Mayor.Choice.2.of.5.Citywide.(226916)` == 254286] = "Mamdani"
df$FinalVote[df$FinalVote == "Invalid" & df$`DEM.Mayor.Choice.3.of.5.Citywide.(326916)` == 254052] = "Cuomo"
df$FinalVote[df$FinalVote == "Invalid" & df$`DEM.Mayor.Choice.3.of.5.Citywide.(326916)` == 254286] = "Mamdani"
df$FinalVote[df$FinalVote == "Invalid" & df$`DEM.Mayor.Choice.4.of.5.Citywide.(426916)` == 254052] = "Cuomo"
df$FinalVote[df$FinalVote == "Invalid" & df$`DEM.Mayor.Choice.4.of.5.Citywide.(426916)` == 254286] = "Mamdani"
df$FinalVote[df$FinalVote == "Invalid" & df$`DEM.Mayor.Choice.5.of.5.Citywide.(526916)` == 254052] = "Cuomo"
df$FinalVote[df$FinalVote == "Invalid" & df$`DEM.Mayor.Choice.5.of.5.Citywide.(526916)` == 254286] = "Mamdani"
#Final vote Mamndai 572922
#Final vote Cuomo 441866

mapping = read.csv("Candidacy ID to name table.csv", sep = ",")
df$`DEM.Mayor.Choice.1.of.5.Citywide.(026916)` = as.character(df$`DEM.Mayor.Choice.1.of.5.Citywide.(026916)`)
df$`DEM.Mayor.Choice.2.of.5.Citywide.(226916)` = as.character(df$`DEM.Mayor.Choice.2.of.5.Citywide.(226916)`)
df$`DEM.Mayor.Choice.3.of.5.Citywide.(326916)` = as.character(df$`DEM.Mayor.Choice.3.of.5.Citywide.(326916)`)
df$`DEM.Mayor.Choice.4.of.5.Citywide.(426916)` = as.character(df$`DEM.Mayor.Choice.4.of.5.Citywide.(426916)`)
df$`DEM.Mayor.Choice.5.of.5.Citywide.(526916)` = as.character(df$`DEM.Mayor.Choice.5.of.5.Citywide.(526916)`)

for (x in 1:length(mapping$CandidacyID)){
  df$`DEM.Mayor.Choice.1.of.5.Citywide.(026916)`[df$`DEM.Mayor.Choice.1.of.5.Citywide.(026916)`==mapping$CandidacyID[x]]=mapping$DefaultBallotName[x]
  df$`DEM.Mayor.Choice.2.of.5.Citywide.(226916)`[df$`DEM.Mayor.Choice.2.of.5.Citywide.(226916)`==mapping$CandidacyID[x]]=mapping$DefaultBallotName[x]
  df$`DEM.Mayor.Choice.3.of.5.Citywide.(326916)`[df$`DEM.Mayor.Choice.3.of.5.Citywide.(326916)`==mapping$CandidacyID[x]]=mapping$DefaultBallotName[x]
  df$`DEM.Mayor.Choice.4.of.5.Citywide.(426916)`[df$`DEM.Mayor.Choice.4.of.5.Citywide.(426916)`==mapping$CandidacyID[x]]=mapping$DefaultBallotName[x]
  df$`DEM.Mayor.Choice.5.of.5.Citywide.(526916)`[df$`DEM.Mayor.Choice.5.of.5.Citywide.(526916)`==mapping$CandidacyID[x]]=mapping$DefaultBallotName[x]
}

df1=subset(df, FinalVote == "Mamdani")
write.xlsx(df1, "NYC_2025_RCV_allvotes_sequences_1_of_2.xlsx")
df2=subset(df, FinalVote != "Mamdani")
write.xlsx(df2, "NYC_2025_RCV_allvotes_sequences_2_of_2.xlsx")

