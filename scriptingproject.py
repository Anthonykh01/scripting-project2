# with open('dirs_dictionary.bat', 'r') as file:
#     for line in file:
#         print(line)


import requests

# import requests

# url = 'https://www.lau.edu.lb'
# response = requests.get(url)

# if response.status_code == 200:
#     print('Request was successful.')
# else:
#     print('Request failed with status code:', response.status_code)

# response = requests.get(url)

# print(response.text)
with open("subdomain_success.txt", "w") as file:
    file.truncate(0)
with open("directory_success.txt", "w") as file:
    file.truncate(0)


url = input('What is your url? ')
print('the url is ,', url)
after_www=url.split("www.")[1]
# with open('subdomains_dictionary.bat', 'r') as file:
#     for line in file:
         
#         line = line.strip()
        
#         if line.endswith('.'):
#             url = 'https://www.' + line[:-1] + '.' +after_www
#         else:
#             url = 'https://www.' + line + '.' + after_www
#         try:
#             response = requests.get(url)
#             if response.status_code == 200:
#                 print('Request was successful.')
#                 print(url)
#                 with open("subdomain_success.txt", "w") as file:
#                     # Write the string to the file
#                     file.write(url)
#         except requests.exceptions.ConnectionError:
#                 # handle the connection error
#                 # print('no')
#                 None
#         #  else:
#         #     print('Request failed with status code:', response.status_code)
#         #     print(url)
        
with open('dirs_dictionary.bat', 'r') as file:
    for line in file:
         
        line = line.strip()
        if line.startswith('.'):
            line=line[1:]
        url='https://' + url.strip() + '/'+ line
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print('Request was successful.')
                print(url)
                with open("directory_success.txt", "w") as file:
                    # Write the string to the file
                    file.write(url)
        except requests.exceptions.ConnectionError:
                # handle the connection error
                 print('no')
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
