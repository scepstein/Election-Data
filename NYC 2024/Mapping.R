library(sf)
sf_data <- st_read(shapefile_path)

#Assign common ADED name
df_tabulated$ADED = paste(df_tabulated$AD, sapply(df_tabulated$ED, function(x){
  if(nchar(x)==1){return(paste("00",x,sep=""))}
  if(nchar(x)==2){return(paste(0,x,sep=""))}
  if(nchar(x)==3){return(x)}
}), sep ="")
df_tabulated$ADED = as.numeric(df_tabulated$ADED)

#Merge
library(dplyr)
sf_data = left_join(sf_data, df_tabulated, by = c("ElectDist" = "ADED"))
sf_data$Harris24_per = sf_data$Harris / (sf_data$Harris + sf_data$Trump)
sf_data$Trump24_per = sf_data$Trump / (sf_data$Harris + sf_data$Trump)
sf_data$Harris24_margin = sf_data$Harris24_per - sf_data$Trump24_per

sf_data <- st_transform(sf_data, crs = 4326)

library(ggplot2)

#Full City Image:
ggplot(sf_data) +
  geom_sf(aes(fill = Harris24_margin)) +
  scale_fill_gradientn(colors = c("#dd0000", "white", "#0984f3")) +
  theme_minimal() 

#Manhattan and Bronx Zoom
ggplot(sf_data) +
  geom_sf(aes(fill = Harris24_margin)) +
  scale_fill_gradientn(colors = c("#dd0000", "white", "#0984f3")) +
  theme_minimal() +
  coord_sf(xlim = c(-74.05, -73.76), ylim = c(40.69, 40.905))

#Brooklyn and Queens Zoom
ggplot(sf_data) +
  geom_sf(aes(fill = Harris24_margin)) +
  scale_fill_gradientn(colors = c("#dd0000", "white", "#0984f3")) +
  theme_minimal() +
  coord_sf(xlim = c(-74.05, -73.7), ylim = c(40.55, 40.8))

#Staten Island Zoom
ggplot(sf_data) +
  geom_sf(aes(fill = Harris24_margin)) +
  scale_fill_gradientn(colors = c("#dd0000", "white", "#0984f3")) +
  theme_minimal() +
  coord_sf(xlim = c(-74.265, -74.06), ylim = c(40.495, 40.65))



