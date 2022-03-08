# NETWORKS & SOCKETS

# 12.5 - (Advanced) Change the socket program so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.
import socket
try:
    url = input('Enter url (*with http:// please!): ')
    urlparts = url.split('/')
    # print(urlparts)
    host = urlparts[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    header = mysock.recv(650)
    header.decode()
    hend = header.find('\n\n')
    print(hend)
    # while True:
    #     data = mysock.recv(10000)



    mysock.close()
except:
    print('Invalid url or url could not be parsed:', url)
quit()
# http://data.pr4e.org/romeo.txt   http://data.pr4e.org/mbox.txt


# 12.4 - Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved
# HTML document and display the count of the paragraphs as the output of your program. Do not display
# the paragraph text, only count them. Test your program on several small web pages as well as some
# larger web pages.
import urllib.request, urllib.parse, urllib.error
import bs4
from bs4 import BeautifulSoup
import ssl

# ignore ssl cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

    #retrieve all of the anchor tags
tags = soup('p')
count = 0
for tag in tags:
    count = count + 1
print('Number of paragraphs:', count)

quit()


# 12.3 -Use urllib to replicate the previous exercise of (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document.
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document
# contents.

# HAVING DIFFICULTIES WITH THIS ONE -> while loop will break after one iteration
import urllib.request, urllib.parse, urllib.error
import ssl
try:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter url: ')
    data = urllib.request.urlopen(url, context=ctx)
    print('*url found and opened')
    loop = 0
    count = 0
    while True:
        data = data.read(3000)
        if len(data) < 1: break
        loop += 1
        count = count + len(data)
        print('Current characters received:', count)
        if loop <= 3:
            print('Data received:')
            print(data.decode())
    print('Total characters in url:', count)
    data.close()
except:
    print('Invalid url or url could not be parsed:', url)
quit()
# # http://data.pr4e.org/romeo.txt   http://data.pr4e.org/mbox.txt


# 12.2 -Change your socket program so that it counts the number of characters it has received and stops
# displaying any text after it has shown 3000 characters. The program should retrieve the entire
# document and count the total number of characters and display the count of the number of characters
# at the end of the document.

# THIS PROGRAM ONLY WORKS FOR HTTP Websites, NOT HTTPS - old assignment specs
import socket
try:
    url = input('Enter url (*with http:// please!): ')
    urlparts = url.split('/')
    # print(urlparts)
    host = urlparts[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    loop = 0
    count = 0
    while True:
        data = mysock.recv(1000)
        loop += 1
        count = count + len(data)
        if len(data) < 1: break
        if loop > 3: continue
        print('Current characters received:', count)
        print('Data received:\n', data.decode(), '\n')
    print('Total characters in url:', count)
    mysock.close()
except:
    print('Invalid url - Could not locate:', url)

quit()




# 12.1 -Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
# You can use split('/') to break the URL into its component parts so you can extract the host
# name for the socket connect call. Add error checking using try and except to handle the condition
# where the user enters an improperly formatted or non-existent URL.

import socket
try:
    url = input('Enter url (*with http:// please!): ')
    urlparts = url.split('/')
    # print(urlparts)
    host = urlparts[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET '+ url + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(612)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    mysock.close()
except:
    print('Invalid url - Could not locate:', url)

quit()


# Using BeautifulSoup - robust html parsing library
import urllib.request, urllib.parse, urllib.error
import bs4
from bs4 import BeautifulSoup
import ssl

# ignore ssl cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

    #retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
quit()

# Using RE to find links 'href:..'
# Prints out the links available on a url
import urllib.request, urllib.parse, urllib.error
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
print('Links:')
for link in links:
    print(link.decode())
quit()

# practicing the urllib library in python
import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
# adding buffer to not take up too much memory
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)
print(size, 'characters copied')
fhand.close()
quit()

# image writing
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()
quit()

# counting words in a web file
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
print(len(count))
quit()


import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
quit()


# retrieving & saving an image from the web
import socket
import time
host = 'data.pr4e.org'
port = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, port))
mysock.send(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""
while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    time.sleep(.25)
    count = count + len(data)
    picture = picture + data
    print(len(data), count)
mysock.close()
# look for the end of the header
pos = picture.find(b"\r\n\r\n")
print('Header length:', pos)
print(picture[:pos].decode())
# skip past header and save picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()
quit()

# Retrieving text file from web
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(612)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()
quit()