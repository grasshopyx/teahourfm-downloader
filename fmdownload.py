#!/usr/bin/env python3
# encoding: utf-8
import time
import re
import urllib.request

def Schedule(a, b, c):
    """TODO: Docstring for Schedule.

    :a: The number of data downloaded blocks 
    :b: The size of a data block
    :c: Total size
    :returns: TODO

    """
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('\r%76.2f%%' % per , end="")

print("Ready to download from http://teahour.fm")

start = time.clock()
mainpage_url = "http://teahour.fm"
page_pattern = re.compile(r"/\d{4}/\d{2}/\d{2}/[\w-]*.html") # not include the mainpage_url
audio_pattern = re.compile( r"http://screencasts.b0.upaiyun.com/podcasts/[\w-]*.m4a" )

data = urllib.request.urlopen(mainpage_url).read()
mainpage_html = data.decode('UTF-8')

episode_list = page_pattern.findall(mainpage_html)
episode_set = set(episode_list)

print("Page analysis has been done. Totally " + str(len(episode_set)) + " audio files will be downloaded.")

num = 1
for episode in episode_set :

    episode_url = mainpage_url + episode
    # print(episode_url)
    data = urllib.request.urlopen(episode_url).read()
    episode_html = data.decode('UTF-8')
    audio_url = audio_pattern.search(episode_html).group()
    print("No."+ str( num )+": Downloading "+audio_url)
    local = audio_url.split('/')[-1]
    urllib.request.urlretrieve(audio_url,local, Schedule)
    print("")

    num+=1


end = time.clock()
print(end-start)


    


