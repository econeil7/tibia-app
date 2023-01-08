import get_worlds
import requests

def get_leaders_and_values():
    """
    Gets the amount of experience between rank one and rank two of each world then returns a dictionary of the data.

    Returns:
        exp_differences: A dictionary containing keys of the names of the rank one players and values of their experience difference over rank two.
    """
    exp_differences = {}
    worlds = get_worlds.get_worlds_lst()
    for world in worlds:
        endpoint = f'https://api.tibiadata.com/v3/highscores/{world}/experience/all/1'
        response = requests.get(endpoint)
        data = response.json()

        rank_one_name = data['highscores']['highscore_list'][0]['name']
        rank_one_exp = data['highscores']['highscore_list'][0]['value']

        rank_two_exp = data['highscores']['highscore_list'][1]['value']

        exp_diff = rank_one_exp - rank_two_exp

        exp_differences[rank_one_name] = exp_diff

    return exp_differences

def get_largest_leader():
    """
    Grabs the character with the highest experience difference between them and their rank 2 opponent.

    Returns:
        largest_leader: A string containing the name of the character.
    """
    leaders = get_leaders_and_values()
    leader_keys = list(leaders.keys())
    leader_vals = list(leaders.values())

    largest_difference = max(leaders.values())
    largest_leader = leader_keys[leader_vals.index(largest_difference)]

    return largest_leader
    

if __name__ == '__main__':
    pass