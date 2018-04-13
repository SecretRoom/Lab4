import vk
import time

print('VK Photos geo location')

session = vk.Session('7bf78bd5772147c7164d663ed70bd03369c82251bb14fdb703df7f1311aba0c77b6ec8e46f82357ae75e8')

api = vk.API(session, v='4.104')

friends = api.friends.get()

friends_info = api.users.get(user_ids=friends)

for friend in friends_info:
    print('ID: %s Name: %s %s' % (friend['uid'], friend['last_name'], friend['first_name']))

geolocation = []

for id in friends:
    print('Получаем данные пользователя: %s' % id)
    albums = api.photos.getAlbums(owner_id=id)
    print('\t...альбомов %s...' % len(albums))
    for album in albums:
        try:
            photos = api.photos.get(owner_id=id, album_id=album['aid'])
            print('\t\t...обрабатываем фотографии альбома...')
            for photo in photos:
                try:
                    if 'lat' in photo and 'long' in photo:
                        geolocation.append((photo['lat'], photo['long']))
                except:
                    print('\t\t...найдено %s фото...' % len(photos))
        except:
            pass
        time.sleep(0.5)
    time.sleep(0.5)

js_code = ""
for loc in geolocation:
    js_code += 'new google.maps.Marker({ position: {lat: %s, lng %s}, map: map});\n' % (loc[0], loc[1])
html = open('map.html').read()
html = html.replace('/* PLACEHOLDER */', js_code)
f = open('VKPhotoGeoLocation.html', 'w')
f.write(html)
f.close()

