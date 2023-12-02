import pyquery as pq
import pandas as pd


outputCards = []

# Create a parsed DOM tree
parsed = pq.PyQuery(filename="scraped-html/startups.html", encoding='latin1')

# Find the divs containing each company
startupCards = parsed(".list-card")

for startupCard in startupCards:
    outputCard = dict()
    parsedCard = pq.PyQuery(startupCard)
    outputCard["title"] = parsedCard(".profile-info-left strong").text()
    outputCard["description"] = parsedCard(".left p").text()
    #outputCard["funding"] = parsedCard(".right ul:first-child p").text()
    outputCards.append(outputCard)

df = pd.DataFrame(outputCards)
df.to_csv("data/startups.csv")
print(df)