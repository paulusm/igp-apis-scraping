import pyquery as pq
import pandas as pd

outputCards = []

# Create a parsed DOM tree
parsed = pq.PyQuery(filename="scraped-html/startups.html", encoding='latin1')

# Find the divs containing each company
startupCards = parsed(".list-card")

# Loop through each company and create a dictionary of the features
for startupCard in startupCards:
    outputCard = dict()
    parsedCard = pq.PyQuery(startupCard)
    outputCard["title"] = parsedCard(".profile-info-left strong").text()
    outputCard["description"] = parsedCard(".left p").text()
    outputCard["funding"] = parsedCard(".right ul li:nth-child(1) p").text()
    outputCard["industry"] = parsedCard(".right ul li:nth-child(2) p").text().split(",")[0]
    outputCards.append(outputCard)

# Convert to Data Frame
df = pd.DataFrame(outputCards)

# Create CSV
df.to_csv("data/startups.csv",index_label="ID")
print(df)