# from django.test import TestCase
# import requests
# from bs4 import BeautifulSoup
# # Create your tests here.
# url = "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedworkflowsforapacheairflow.html"
# response = requests.get(url)
# html_content = response.content

# soup = BeautifulSoup(html_content, "html.parser")
# table = soup.find("table")

# desired_columns = ['Actions','Access level','Resource types (*required)','Condition keys','Dependent actions']

# headers = table.find_all("th")
# print(headers)
# column_indices = [index for index, header in enumerate(headers) if header.text in desired_columns]
# print(column_indices)
# table_data = []
# rows = table.find_all("tr")
# for row in rows:
#     cells = row.find_all("td")
#     row_data = [cells[index].text.strip() for index in column_indices]
#     table_data.append(row_data)
# print(table_data)


'''
from bs4 import BeautifulSoup
import requests

url = "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedworkflowsforapacheairflow.html"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table")

tbody = table.find("tbody")  # Find the tbody element within the table

desired_columns = ['Actions','Access level','Resource types (*required)','Condition keys','Dependent actions']
headers = tbody.find_all("th")
column_indices = [index for index, header in enumerate(headers) if header.text in desired_columns]

table_data = []
rows = tbody.find_all("tr")
for row in rows:
    cells = row.find_all("td")
    row_data = [cells[index].text.strip() for index in column_indices]
    table_data.append(row_data)
print(table_data)
# Process or display the extracted table data
'''

from bs4 import BeautifulSoup
import requests

url = "https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonmanagedworkflowsforapacheairflow.html"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table")

# Find the thead element within the table
thead = table.find("thead")

# Find the column names within the thead element
desired_columns = ["Actions", "Description", "Access level", "Resource types (required)", "Condition keys", "Dependent actions"]
column_indices = []
headers = thead.find_all("th")
for index, header in enumerate(headers):
    if header.text.strip() in desired_columns:
        column_indices.append(index)

# Find the tbody element within the table
tbody = table.find("tbody")

table_data = []
if tbody:
    rows = tbody.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        row_data = [cells[index].text.strip() for index in column_indices]
        table_data.append(row_data)

print(table_data)



# Process or display the extracted table data
