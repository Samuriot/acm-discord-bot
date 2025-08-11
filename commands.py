import requests

async def download_file(url, intended_filename):
    response = requests.get(url)
    if response.ok == False:
        print("error downloading file, exiting")
        return
    with open(intended_filename, mode="wb") as file:
        file.write(response.content)