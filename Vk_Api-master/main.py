import requests
from pprint import pprint

version = '5.69'
access_token = '873fcd36b45b3109194fe20b24e973739bd9b9db170a0a251097c651cf93325eeb49895c8a52e170ae358'


def from_list_to_dict(friends_list):
    friends_dict = dict()
    for friend in friends_list:
        try:
            if friend['deactivated']:
                continue
        except:
            friends_dict[friend['first_name'] + ' ' + friend['last_name']] = friend['id']

    return friends_dict


def pairs_create(friends):
    pairs = dict()

    for num, friend in enumerate(friends):
        for friend_tmp in friends:
            if (friend_tmp != friend) and (friend + '-' + friend_tmp not in pairs)\
                and (friend_tmp + '-' + friend not in pairs):
                pairs[friend + '-' + friend_tmp] = str(friends[friend]) + '-' + str(friends[friend_tmp])

    return pairs


def mutual_friends_find(pairs):
    mutual_friends = dict()
    for key, pair in pairs.items():
        friends = pair.split('-')
        friend1 = friends[0]
        friend2 = friends[1]
        try:
            mutual_friends[key] = requests.get('https://api.vk.com/method/friends.getMutual', params={
                'source_uid': friend1,
                'target_uid': friend2,
                'v': version,
                'access_token': access_token
            }).json()['response']
        except:
            continue

    return mutual_friends


def friend_pairs_create():
    params = {
        'access_token': access_token,
        'v': version,
        'fields': 'id'
    }

    my_friends_list = requests.get('https://api.vk.com/method/friends.get', params).json()['response']['items']

    my_friends_dict = from_list_to_dict(my_friends_list)
    pairs = pairs_create(my_friends_dict)

    return pairs


pairs = friend_pairs_create()
mutual_friends = mutual_friends_find(pairs)
pprint(mutual_friends)
