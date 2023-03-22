# with open('dirs_dictionary.bat', 'r') as file:
#     for line in file:
#         print(line)


# import requests

# import requests

# url = 'https://www.lau.edu.lb'
# response = requests.get(url)

# if response.status_code == 200:
#     print('Request was successful.')
# else:
#     print('Request failed with status code:', response.status_code)

# response = requests.get(url)

# print(response.text)
url = input('What is your url? ')
print('the url is ,', url)
with open('dirs_dictionary.bat', 'r') as file:
    for line in file:
        after_www = url.split("www.")[1]
        new_url='www.'+line.strip()+'.'+after_www
        print(new_url)

        # url = 'https://www.lau.edu.lb'
        # response = requests.get(url)

        # if response.status_code == 200:
        #     print('Request was successful.')
        # else:
        #     print('Request failed with status code:', response.status_code)
        
