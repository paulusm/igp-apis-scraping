import requests
from requests.auth import HTTPBasicAuth
import json
import io

# Get the API Key from the file
api_key = open("ch-api-key.secret").readline()

# This is the API "Endpoint"
api_url = "https://api.company-information.service.gov.uk/advanced-search/companies"

# The search parameters
search_parms = "?size=10&location=bristol&company_name_includes=data&company_status=active&sic_codes=62020"

# Adds the key to the request and make the call
auth = HTTPBasicAuth(api_key, '')
response = requests.get(api_url + search_parms, auth=auth)

print(f'Return Code - {response.status_code}\n\n')

# Pretty print the returned JSON data
json_obj = json.loads(response.text)
print(json.dumps(json_obj, indent=3))

# Challenge - Load into a Pandas DataFrame