# EV_Adoption_Aus
Web Application to Visualize and Analyse various factors influencing EV Adoption in Australia
 

## Overview
In this project we will go over the product goal, motivation for this project, the pipeline we used for the data. We will then showcase a demo of the data dashboards we created, after that there is a high level analysis of our findings. We will end it with future direction.


## bProduct Goal
The primary goal of this project is to analyse the current adoption rates of electric vehicles (EVs) in Australia. This analysis will identify factors influencing EV adoption and explore potential trends for the future. The insights derived from this analysis will be valuable to stakeholders.

This project is made in the the perspective of three main stakeholders:
Policy makers
EV Retailers/Investors
Potential EV customers

## Scrum Framework

During this project, to reach our product goal, we implemented the Scrum framework. 

With Scrum, we could adapt to changes quickly, improve our work practices continuously, and efficiently deliver value to our stakeholders by supplying a functional product at the end. 

The product goal was split into a product backlog of tasks, prioritizing the most important tasks. And from that created goals for each sprint. We completed this product in 2 sprints, each being a week in length. 

Sprint 1: Collect, process, and analyze data to identify key insights and valuable information for stakeholders.

Sprint 2: Develop and finalize the visualizations and create an interactive dashboard application to present the analyzed data to stakeholders.  

By applying to SCRUM 
we have delivered a robust and functional dashboard application. This application presents the analyzed data effectively so that stakeholders can easily interpret it into actionable insights. 




## Pipeline

Our data was selected from a diverse range of sources to ensure reliability of analysis.

Each dataset and plot were carefully chosen to provide insights into different aspects of EV adoption in Australia. From infrastructure and economic factors to consumer preferences and international comparisons, these data points collectively offer a comprehensive understanding of the current state and future potential of EV adoption in Australia. 

Our pipeline for this diverse set of data can be broken down into 4 main steps:
Source the data and extract.
Clean and transform the data.
Save processed data for efficiency.
Load processed data for the plots on the web app.



This application was created with ease of use in mind for the stakeholders.

We have split this application into four main pages:
EV Adoption Rates
Australian EV Market
Charging Information, and
EV Specs

Each of these four pages are designed to give a specific subset of information readily available.

[EV Adoption Rate page]
Let’s begin the journey. So for EV Adoption Rates, this is all about seeing the adoption rate of Australia and comparing it with the global adoption rates. Users can navigate the different graphs using this sidebar menu. Each graph is interactive allowing users to get more specific information.

[Australian EV market page]
The Second main page is all about the Australian EV Market. This is information more narrow in scope to just Australia. On this page EV investors can find places to invest in Australia and get an understanding of EV prices compared to the international market.

Show you opening the analysis tab as well.

[Charging Information]
The third page is on the charging information about the EVs. It gives an understanding of where the charging stations are in Australia, what the cost is to run these EVs, and for a better understanding we have given information of the fuel costs for traditional fuel vehicles.

[EV Specs]
This last main page is to give specifications of 360 EVs for potential customers. They can come to this page to gain an easy comparison of different EVs available for purchase.

That is the end of our brief demonstration, I hope this highlights the dashboard use cases for our three stakeholders. I will now pass it back to Parkavi who will give a more in depth analysis of our data.


## Plot Analysis
The analysis of these plots offers a comprehensive overview of the current and evolving landscape of Electric Vehicles (EVs) compared to Internal Combustion Engine (ICE) vehicles in Australia. Each plot not only sheds light on specific aspects of vehicle distribution, infrastructure, and market trends but also collectively aligns with the broader project goal of understanding and promoting EV adoption.
We've grouped our plots into four key categories: EV Adoption Rates, Australian EV Market, Charging Information, and EV Specifications. Each group provides unique insights into the factors influencing EV adoption and helps us tailor strategies for policymakers, retailers, and consumers.
### Australian EV Market: Plots 1, 3, 4, 11
These plots provide a deep dive into the Australian EV market's current state and its potential for growth. 
Australian EV Sales vs Global EV Sales:
Australia's Slow Adoption: Australia exhibits significantly lower EV 4sales compared to the average of other countries, indicating a slower pace in embracing electric vehicle technology.

#### High Income, Low EV Registrations in Australia
In this analysis, we aimed to identify areas in Australia with high mean income but low electric vehicle (EV) registrations. This plot is crucial for stakeholders like policymakers, EV car retailers, and potential EV owners, as it highlights regions where there is economic capacity for EV adoption but current uptake is low. Here's how we approached this:

Data Preparation:
We collected data on  population, EV registrations, and mean income for different Local Government Areas (LGAs) in Australia.
Criteria Definition:
High Income areas are regions with a mean income above the 75th percentile of the dataset. This threshold allows us to focus on wealthier areas where residents potentially have the financial means to purchase EVs.
Low Registrations areas are regions with EV registrations below the 25th percentile. This criterion helps us pinpoint areas with less EV adoption.
Underutilised Potential: The map highlights areas where economic capacity is high, yet EV adoption is low. These regions represent untapped markets where efforts to boost EV sales could be highly effective.
Urban and Regional Differences: The distribution of high-income, low-registration areas varies, indicating that even within affluent regions, local policies and the availability of EV-supportive infrastructure play significant roles in adoption rates.

### Charging Information: Plots 2, 7
These plots emphasise the critical role of charging infrastructure and economic factors in supporting EV adoption. 

#### EV Charge Station Locations in Australia:             	
Concentration in Urban Areas: There is a high concentration of charging stations in the southeastern parts of Australia, notably around major cities such as Melbourne, Sydney, and Brisbane. This corresponds with higher EV adoption in these areas.
Coastal Access: Charging stations are more prevalent along the coastlines, facilitating long-distance travel along these routes.


### EV Adoption Rates: Plots 8, 9, 10, 12
These plots collectively illustrate the evolving landscape of electric vehicle (EV) adoption both globally and within Australia. 

#### EV Adoption and Leading Countries
The global landscape of electric vehicle (EV) adoption highlights stark regional contrasts and growth trends. European Leadership is evident, with Northern and Western European countries like Norway dominating the market—over 80% of car sales in Norway are EVs, supported by robust infrastructure and incentives. This demonstrates a mature and stable EV market in Europe.
China shows significant growth, driven by large-scale investments and increasing consumer demand for sustainable transport options. China's rapid expansion is particularly notable, reflecting both its manufacturing capabilities and government support.
In contrast, Australia exhibits slower yet consistent increases, with EV adoption reaching around 10-20% share in 2022. This slower growth indicates emerging markets that are gradually overcoming barriers such as infrastructure and consumer awareness.
Overall, the trend shows a growing global shift towards EVs, with Europe and China leading the charge, and other regions gradually catching up as they enhance their support systems and market readiness.

## Policy Analysis 
Policies have a considerable impact on the adoption rate of electric vehicles (EVs), let us first look at Australia's current policies and future plans.
#### Australia: Currently, Australia's EV adoption rate is below the global average, only having an adoption rate of 12% compared to 20%. This is likely due to their policies 
Their main policy to attract EV adoption is to exempt EVs priced under $89K from taxes and some state-specific benefits, but these do not significantly increase nationwide adoption.
The Australian government aims to meet its target of only selling net-zero vehicles by 2050, and to do this they have made strategy focusing on three objectives: increasing supply, improving infrastructure (such as charging stations), and stimulating demand. 
While these are positive steps, examining the policies of other countries with high adoption rates and grwoth can provide valuable insights.
#### Norway: Norway has the highest EV adoption rate as of now, thanks to a range of policies and incentives implemented since 1990. Norway's has been doing so well that they’ve set a bold goal of only selling  EVs from 2025 onwards. Norway has three main categories of EV related policies:
Tax exemptions 
EV owner benefits 
Free parking
Ease of use 
Easier to charge
These policies have highly impacted Norway's EV adoption. They’re actually starting to remove some of their policies as they’re not necessary anymore to promote adoption.


#### China: China has had tremendous growth in EV adoption recently, rising from 5% in 2020 to over 50% as of April 2024. 
While China has implemented policies similar to Norway's that focuses on the consumer, their rapid growth is more related to Their focus on benefits for EV-related companies, such as battery and car manufacturers. 
-	These plocieis include giving cheap land leases and loans to these companies.
China has focused on improving EV technology and making it more affordable.  Getting rid of the barriers consumers have when it comes to purchasing an EV.
This has also benefited the rest of the world as it's reducing the cost of EVs. The Chinese EV sales have seen a rise recently, we can actually see this Australia we have seen that Chinese EVs are starting to compete and outsell well-known EV brands like Tesla.  
It is important that Australia learns from Norway and China’s strategies and try to implement some of them themselves. 





## Future Directions

For future directions, we have developed a few objectives that we want to accomplish.

The first is to collect and implement better retail, fuel, and charging costs data.
This will allow individuals to better understand the cost saving that comes with purchasing an EV over a traditional petrol vehicle.

The second is to continuously update the data 
This is so it can be seen if Australian policies in the future impact EV adoption rate.

With all this data and how it’ll increase in the future, it’s important to move toward Pyspark As it's efficient at processing large amounts of data compared to traditional data processing methods.

The final future update would be to implement a feedback form into the website, this would allow us to know if the product is useful to the stakeholder and if they’re getting the value they expected out of it. It would also help to know what the stakeholders want to add to the product.


