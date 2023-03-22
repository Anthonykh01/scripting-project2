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
# url = input('What is your url? ')
# print('the url is ,', url)
with open('subdomains_dictionary.bat', 'r') as file:
    for line in file:
        url = 'https://www.'+line.strip()+'.ctflearn.com'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print('Request was successful.')
                print(url)
        except requests.exceptions.ConnectionError:
                # handle the connection error
            print(f"Connection to {url} failed")
        #  else:
        #     print('Request failed with status code:', response.status_code)
        #     print(url)
        


try:
    response = requests.get(url)
    # process the response
    print(response.text)
except requests.exceptions.ConnectionError:
    # handle the connection error
    print(f"Connection to {url} failed")
    # continue with the rest of your code
    # ...
