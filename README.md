# Project 2 - Immigration in Portugal, by Giuliana Miranda - Readme

## Summary

The foreign population in Portugual has been on the rise for the last 7 years. 
This project aims to analyse the migration scenario, answering one important core question: do immigrants contribute to the demography and the economy of the country?

To do so, we are going to analyse various datasets related to immmigration and economical dynamics. The primary objective is to gain insights into trends, patterns, and contributions of different nationalities to the social and economic landscape of Portugal. The analysis covers aspects such as population dynamics, gender balance, income differences, and contributions to social security.

## Data Sources

There were a few constraints regarding the access to the dataframes. The Portuguese government releases most of the official information on the immigrants as PDF files. 

Luckly, institutions like Pordata, a well recognized open data organization, make it avaiable as CSV os XLS files. Because of that, the largest datasets were from Pordata. 

Social Security authorities don't publish the break down of immigrants contributions on their websites. 

In the past 3 years, this information was provided as statements from spokespeople. The most recent, in 2023, was presented before the Parliament in December. 

The only source of combined data on Social Security contributions made by the migrants is the annual report "Indicadores de Integração de Imigrantes" (Indicadores de Integração de Imigrantes), that summarizes the key numbers. The study is conducted by Observatório das Migrações, which is linked to Aima, the new Integration, Migration and Asylum Agency of Portugal.

However, all the data is presented as pdfs nnd, in some cases, just as graphics. 
Because of that, we used their data, but converting their information to Excel files.

## List of the main files
1. **Total Migrants by Year (`Total_migrants_by_year.xlsx`):**
   - General dataset providing insights into the evolution of migration trends from different countries to Portugal over the years.

2. **Population Balance (`population_balance.xlsx`):**
   - Dataset focusing on the overall population balance of Portugal, considering natural balance (births-deaths) and migratory balance (immigration-emigration).

3. **Gender Nationalities (`gender_nationalities.xlsx`):**
   - Dataset exploring the gender distribution among different nationalities in Portugal.

4. **Social Security Contributions (`SSS.xlsx`, `SS_by_country.xlsx`):**
   - Data related to Social Security contributions, offering a perspective on migrants' financial participation in the social security system.

5. **Income Differences (`dif_income.xlsx`):**
   - Dataset examining income differences among various nationalities in comparison to Portuguese nationals.
   
6. **Original Files**:
    - The two original files from Observatório das Migrações were include on PDF. They are on a separed folder inside 'project_files'

## Data Analysis Steps

### Data Cleaning and Exploration

- The analysis starts with cleaning column names for consistency and ease of use.
- Initial exploratory data analysis is performed, including data type inspection, statistical summaries, and identification of significant trends.

### Migration Trends Over Time

- A function `plot_nationalities` is created to visualize the evolution of specific nationalities over the years.
- The overall migrant evolution is visualized through a line plot.
- It shows a spike of the influx in the latest year. The community grew over 277% in 20 years.
- The visualization by community provided an interesting timeframe of how each community evoluted. 
- Brazilians are dominant by a huge margin (over 30% of all migrants are from Brazil), but other nationalities also had very interesting patterns, like the Nepalese and Indidians. 


### Data Separation and Tableau Preparation

- An attempt is made to separate data for each country into individual DataFrames, intending to facilitate Tableau dashboard creation.
- However, it is noted that this approach did not yield the expected benefits. I abandoned the idea, but decided to keep the files, once it could be useful in case of creating individual dashbords for each nationality as a future excercise.

### Population Balance Analysis

- Population balance trends are visualized, emphasizing total balance, natural balance, and migratory balance over the years.
- A correlation matrix is generated to understand the relationships between different balance components.
- The result states very clearly that immigrants play an important role on keeping the cuntry population balance, specially after 2008, when the amount of deaths became higher than the births in Portugal.

### Gender Distribution Analysis

- The gender distribution among different nationalities is visualized.
- It makes clear that, while the general migrant population is almost balanced in terms of gender, some communities have big discrepancies, such as the Indian and Nepale, with much more men.

### Social Security Contributions Analysis

- Trends in Social Security contributions over the last three years are visualized.
- The distribution of contribution amounts is explored through a histogram.
- The relationship between the share of immigrants' contribution and the share of contributors among residents is analyzed through a scatter plot.
- Immigratns pay much more in Social Security than what they receive on Social benefits
- By analysing the contributions of each nationality to SS, we can also better understand the profile of their communities. 
One good example is the british. Despite being the second largest the second largest group of immigrants, they pay very
little compared to their size (only 1% of all payments made by immigrants). Only about 15% of all UK citizens in Portugal pay SS.
It indicates a huge community of non active citizens here, probably benefiting from tax incentives such as RNH. 
- On the other hand, somme communities, like Indians, Brazilian and Moldovans, have a share of over 100% of the community paying SS. What at first might be seen as an error, is actually explained by Portuguese immigration law. Irregular immigrants who pay social security for over 12n months have an easier path to regularization of their migratory status. Numbers way above 100% of payments indicate, therefore, a high probablility of having irregular immigrants trying to be legalized. 


### Income Differences Analysis

- Income differences among various nationalities compared to Portuguese nationals are visualized through a bar plot.
- We can identify that the income levels vary a lot among the foreigners. On avarage, immigrants earn almost -7% compared to nationals, but the salaries of each community is very different. 
- People from the United States earn over 125% more than a Portuguese, while someone from Thailand is payed -36% from a Portuguese. 

## Conclusion

The data shows that migrants play an important role on keeping the population balance in Portugal. They also pay much more to Social Security than what they benefit from it. 
