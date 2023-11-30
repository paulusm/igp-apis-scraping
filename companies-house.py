import requests
from requests.auth import HTTPBasicAuth
import json
import io

api_key = open("ch-api-key.secret").readline()

api_url = "https://api.company-information.service.gov.uk/advanced-search/companies"

search_parms = "?size=10&location=bristol&company_name_includes=data&company_status=active&sic_codes=62020"

auth = HTTPBasicAuth(api_key, '')

response = requests.get(api_url + search_parms, auth=auth)

json_obj = json.loads(response.text)

print(json.dumps(json_obj, indent=3))