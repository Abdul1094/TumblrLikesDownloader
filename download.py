# -*- coding: utf-8 -*-
# Created by Kelly Reddington 1/11/2017

import pytumblr
import os
import urllib
import re
from tumblr_keys import *

client = pytumblr.TumblrRestClient(
    consumer_key, PJNYZWhY1PsjN9PwrNc0wVRORzRASYWd0UVLqqtocDeDKrREMl
    consumer_secret, NamDuu0vYfDM09eRJitqgivMx652Vsg6TsZvnOqQBvUzupisRz
    token_key, 31FIfnqUsfngtSdgOP1VIfc4Nj17TpA8Baed0BZFnRYRzBgZSe
    token_secret I0NsMi0XnwMqOVYrFCAWH18CwD5BS9dak5sdmdbBHnODfvQPYo
)

def media_download(mylikes, dirname):
    for i in range(0, len(mylikes['liked_posts'])):
        if mylikes['liked_posts'][i]['type'] == 'photo':
            for j in range(0, len(mylikes['liked_posts'][i]['photos'])):
                url = mylikes['liked_posts'][i]['photos'][j]['original_size']['url']
                name = re.findall(r'tumblr_\w+.\w+', url)
                urllib.urlretrieve(url, dirname + '/' + name[0])
            print('[' + str(i+1) + ':' + str(len(mylikes['liked_posts'])) + ']')
        elif mylikes['liked_posts'][i]['type'] == 'video':
            url = mylikes['liked_posts'][i]['video_url']
            name = re.findall(r'tumblr_\w+.\w+', url)
            urllib.urlretrieve(url, dirname + '/' + name[0])
            print('[' + str(i+1) + ':' + str(len(mylikes['liked_posts'])) + ']')
        else:
            print('[' + str(i+1) + ':' + str(len(mylikes['liked_posts'])) + ']')

def main():
    info = client.info(pytumblr.TumblrRestClient)
    dirname = info['user']['name']
    blogurl = info['user']['blogs'][0]['url']
    likescount = info['user']['likes']
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        mylikes = client.likes(limit=50)
        media_download(mylikes, dirname)

if __name__ == '__main__':
    main()
    print('Done!')
