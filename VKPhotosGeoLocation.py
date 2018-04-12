import vk
import time
print('VK Photos geo location')

session = vk.Session(access_token='4daf29f676dfa2d591bb421cfccc8e4224bf0a623a67b7a3e190ef7650af0e79a1db543ba148320ace597')

api = vk.API(session, v='5.74')

friends = api.friends.get()

friends_info = api.users.get(user_ids=friends)

for friend in friends_info:
    print('ID: %s Name: %s %s' % (friend['uid'], friend['last_name'], friend['first_name']))

geolocation = []

for id in friends:
    print('Получаем данные пользователя: %s' % id)
    albums = api.photos.getAlbums(owner_id=1)
    print('\t...альбомов %s...' % len(albums))
    for album in albums:
        try:
            photos = api.photos.get(ownerid=id, AlbumIds=album['aid'])
            print('\t\t...обрабатываем фотографии альбома...')
            for photo in photos:
                if 'lat' in photo and 'long' in photo:
                    geolocation.append((photo['lat'], photo['long']))
            print('\t\t...найдено %s фото...' % len(photos))
        except:
            pass
        time.sleep(0.5)
    time.sleep(0.5)

js_code = ""
for loc in geolocation:
    js_code += 'new google.maps.Marker({ position: {lat: %s, lng %s}, map: map});\n' % (loc[0], loc[1])
html = open('map.html').read()
html = html.replace('/AIzaSyDhYgKvkA76qy90g4GIAWz22l7xBF5PZG0', js_code)
f = open('VKPhotoGeoLocation.html', 'w')
f.write(html)
f.close()