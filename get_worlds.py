import requests

def get_worlds_lst():
    """
    This function grabs the worlds from the TibiaData API and returns them as a list.

    Returns:
        worlds: A list of the worlds.
    """
    endpoint = 'https://api.tibiadata.com/v3/worlds'
    response = requests.get(endpoint)
    data = response.json()

    worlds = []
    for world in data['worlds']['regular_worlds']:
        worlds.append(world['name'])
    
    return worlds

if __name__ == '__main__':
    pass