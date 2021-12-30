setwd("~/Desktop")

consent_data <- read.csv("Final Cut.csv")

consent_data <- consent_data[, -c(2:62)]

consent_data<-subset(consent_data, Progress==90 | Progress == 100)

consent_data$Age <- as.numeric(as.character(consent_data$Age))

consent_data$Age <- consent_data$Age-17 

consent_data <- lapply(consent_data,as.numeric)

write.csv(consent_data,"/Users/maryamtanveer/Desktop/Book3.csv", row.names = FALSE)