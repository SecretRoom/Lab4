import vk

print('VK Photos geo location')

session = vk.Session('89f4ba7a192cac2a979028f219b7ce2d020481bf829ec828ed041be0a53b8571493c551c96ba468366a6c')

api = vk.API(session, v='5.74')

friends = api.friends.get()

friends_info = api.users.get(user_ids=friends)
for friend in friends_info:
    print('ID: %s Имя: %s %s' % (friend['uid'], friend['last_name'], friend['first_name']))

