# with open('dirs_dictionary.bat', 'r') as file:
#     for line in file:
#         print(line)


import requests
import re
# import requests

# url = 'https://www.lau.edu.lb'
# response = requests.get(url)

# if response.status_code == 200:
#     print('Request was successful.')
# else:
#     print('Request failed with status code:', response.status_code)

# response = requests.get(url)

# print(response.text)

with open("subdomains_output.bat", "w") as file:
    file.truncate(0)
with open("directories_output.bat", "w") as file:
    file.truncate(0)
with open("files_output.bat", "w") as file:
    file.truncate(0)


url = input('What is your url? ')
print('the url is ,', url)
after_www=url.split("www.")[1]
# with open('subdomains_dictionary.bat', 'r') as file:
#     for line in file:
         
#         line = line.strip()
        
#         if line.endswith('.'):
#             url0 = 'https://www.' + line[:-1] + '.' +after_www
#         else:
#             url0 = 'https://www.' + line + '.' + after_www
#         try:
#             response = requests.get(url0)
#             if response.status_code == 200:
#                 print('Request was successful.')
#                 print(url0)
#                 with open("subdomains_output.bat", "a") as file:
#                     # Write the string to the file
#                     file.write(url0+"\n")
#         except requests.exceptions.ConnectionError:
#                 # handle the connection error
#                 print('no')
                # None
#         #  else:
        #     print('Request failed with status code:', response.status_code)
        #     print(url)
        
# with open('dirs_dictionary.bat', 'r') as file:
#     for line in file:
         
#         line = line.strip()
#         if line.startswith('.'):
#             line=line[1:]
#         url1='https://' + url.strip() + '/'+ line
#         try:
#             response = requests.get(url1)
#             if response.status_code == 200:
#                 print('Request was successful.')
#                 print(url1)
#                 with open("directories_output.bat", "a") as file:
#                     # Write the string to the file
#                     file.write(url1+"\n")
#         except requests.exceptions.ConnectionError:
#                 # handle the connection error
#                  print('no')
                # None
# Open the file in write mode with truncate set to 0
# with open("output.txt", "w") as file:
#     file.truncate(0)
#     # Write the string to the file
#     file.write("This is a string that will be written to the file")

# try:
#     response = requests.get(url)
#     # process the response
#     print(response.text)
# except requests.exceptions.ConnectionError:
#     # handle the connection error
#     print(f"Connection to {url} failed")
#     # continue with the rest of your code
#     # ...
url2='https://'+url
response = requests.get(url2)
html_content = response.text

# Define a regular expression to match all href links
href_regex = r'href=[\'"]?([^\'" >]+)'

# Use regex to find all href links in the HTML content
href_links = re.findall(href_regex, html_content)

# Print the href links found
for link in href_links:
    with open("files_output.bat", "a") as file:
     file.write(link+"\n")

with open('directories_output.bat', 'r') as file:
    for line in file:
        response = requests.get(line)
        html_content = response.text

        # Define a regular expression to match all href links
        href_regex = r'href=[\'"]?([^\'" >]+)'

        # Use regex to find all href links in the HTML content
        href_links = re.findall(href_regex, html_content)

        # Print the href links found
        for link in href_links:
            with open("files_output.bat", "a") as file:
            file.write(link+"\n")