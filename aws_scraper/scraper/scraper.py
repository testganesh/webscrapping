import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedworkflowsforapacheairflow.html'

def scrape_service_pages():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    service_links = soup.select('a[href^="list_"]')

    services_data = []

    for link in service_links:
        service_name = link.text.strip()
        service_url = BASE_URL + link[service_name]

        service_response = requests.get(service_url)
        service_soup = BeautifulSoup(service_response.text, 'html.parser')

        prefix = service_soup.select_one('.awsc-service-name-prefix').text.strip()

        actions_table = service_soup.find(id='actions-list')
        actions = extract_data_from_table(actions_table)

        resources_table = service_soup.find(id='resource-types-list')
        resources = extract_data_from_table(resources_table)

        conditions_table = service_soup.find(id='condition-keys-list')
        conditions = extract_data_from_table(conditions_table)

        service_data = {
            "prefix": prefix,
            "link": [service_url],
            "actions": actions,
            "resources": resources,
            "conditions": conditions
        }

        services_data.append(service_data)

    return services_data

def extract_data_from_table(table):
    data = []
    if table:
        rows = table.select('tr')
        headers = [header.text.strip().lower() for header in rows[0].select('th')]
        for row in rows[1:]:
            cells = row.select('td')
            row_data = {header: cell.text.strip() for header, cell in zip(headers, cells)}
            data.append(row_data)
    return data


