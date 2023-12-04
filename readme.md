# Interdisciplinary Group Project

## Demonstrators on : APIs, Web Scraping, Data Synthesis

Paul Matthews 2023-12-04

1. Web REST API : UK Companies House API Service [companiess-house.py](companiess-house.py) - Search for companies by location and name. Requires an API key to be stored in a file named ch-api-key.secret. API keys require a [registration to the service](https://developer.company-information.service.gov.uk/overview/).

2. Web Scraping using the Pyquery Python Library. This example gets a table of Startup Companies from https://www.seedtable.com/startups-uk. See shell script [wget-example.sh](wget-example.sh) for the command to download an HTML File. See [scraping.py](scraping.py) for the code to extract a data frame using Pyquery.

3. Data synthesis using SDV, The [Synthetic Data Vault](https://docs.sdv.dev/sdv/) See [synthesis.py](synthesis.py) for an example that extends the startups dataset with fictional examples.

<!-- x = re.findall("\$(\d+) (Million|Billion) .. (.*)", fundingLine)>