import vk

print('VK Photos geo location')

session = vk.Session('331a225e8827abf0e50bc6af39b39a298677dea9aef8a9bbf3a012f393220209a79275aa17f98e9166e64')

api = vk.API(session, v='5.74')

friends = api.friends.get()

print(len(friends))

print(friends)

