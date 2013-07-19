#!/usr/bin/env python
#-*- coding: utf-8 -*-

import glob
import os
import urllib
import urllib2
import re
import unicodedata as un
import webbrowser as wb

def noaccent(string):
  return un.normalize('NFKD', string.decode('utf-8')).encode('ASCII','ignore')

def lmexample():
  print "        Type 'see list_name list' to see what's in the list"
  print "        Type 'put item in list_name list' to add an item in a list"
  print "          In this case, if the list not exists, it will be created"
  print "          Example: 'put cookies in shopping list'"
  print "        Type 'remove item from list_name list'"
  print "          Example: 'remove wash car from task list'"

def example():
  print "huepy: Here are some example queries:"
  print "        Type 'lists' to see what lists you have"
  print "        Type 'bye' or 'leave' if you want me to stop bothering you"
  print "        Type 'weather' or 'forecast' to see the wheather forecast"
  lmexample()
  print "        WARNING: the commands that open browsers have bugs"
  print "        You can access facebook by typing 'facebook' or 'face', and 9gag typing '9gag'"
  print "        You can also google something like the following example: 'google how does a microwave work'"

def llists():
  lists = []
  full_path = os.path.realpath(__file__)
  path, file0 = os.path.split(full_path)
  os.chdir(path)
  for files in glob.glob("*.list"): lists.append(files)
  return lists

def checkdata(data):
  words = data.split(' ')
  firstwords = ['see', 'put', 'remove', 'google', 'wikipedia', 'desciclopedia', 'search', 'wiki', 'desciclo', 'des', 'face']
  for f in firstwords:
    if words[0] == f:
      return f
  keywords  = ['example', 'help', 'leave', 'bye', 'hue', 'version', 'lists', 'forecast', 'weather', 'facebook', '9gag', 'usq', 'start']
  for k in keywords:
    if k in data:
      return k
  return 'no-match'

def see(string):
  words = string.split(' ')
  if len(words) > 1:
    list_name = words[1]+ '.list'
    if os.path.exists(list_name):
      with open(list_name, 'r') as arq:
	i = 1
	print 'huepy: Showing %s list' % words[1]
	for line in arq:
	  print '        '+'%i. %s' % (i, line.rstrip('\n'))
	  i += 1
    else:
      print 'huepy: There is no %s list.' % words[1]
  else:
    print 'huepy: You need to tell me which list you want to see.'
    print '       Example: see task list'

def put(string):
  words = string.split(' ')
  if len(words) > 3 and words[len(words)-1] == 'list':
    list_name = words[len(words)-2]+ '.list'
    item = ''
    for i in range(1, len(words)-3): item += words[i]
    with open(list_name, 'a') as arq:
      arq.write(item+'\n')
    print 'huepy: %s added in your %s list' % (item, words[len(words)-2])
    see('see %s' % words[len(words)-2])
  else:
    print 'huepy: You need to follow the format: put item_name in list_name list.'
    print '       Example: put milk in shopping list'

def remove(string):
  words = string.split(' ')
  if len(words) > 3 and words[len(words)-1] == 'list':
    list_name = words[len(words)-2]+ '.list'
    item = ''
    for i in range(1, len(words)-3): item += words[i]
    if not os.path.exists(list_name):
      print 'huepy: There is no %s list.' % words[len(words)-2]
    with open(list_name, 'r') as arq:
      lines = arq.readlines()
    with open(list_name, 'w') as arq:
      arq.close()
    with open(list_name, 'a') as arq:
      for line in lines:
	if not line.strip().startswith(item.strip()):
	  arq.write(line)
    print 'huepy: %s removed from your %s list' % (item, words[len(words)-2])
    see('see %s' % words[len(words)-2])
  else:
    print 'huepy: You need to follow the format: remove item_name from list_name list.'
    print '       Example: remove milk from shopping list'

def weather():
  print 'huepy: Accessing weather information...'
  aResp = urllib2.urlopen("http://www.weather.com/weather/today/Florianopolis+BRXX0091:1:BR");
  web_pg = aResp.read();
  pattern = ['<span class="wx-value" itemprop="weather-phrase">(.*)</span>', '<p class="wx-text">(.*) High (.*)</p>', '<p class="wx-text">(.*) Low (.*)</p>']
  value = ['Conditions', 'Today', 'Tonight']
  
  con = re.search(pattern[0], web_pg).group(1)
  tod = re.search(pattern[1], web_pg).group(1)
  ton = re.search(pattern[2], web_pg).group(1)
  print '       Conditions:  %s' % con
  print '       Today:       %s' % tod
  print '       Tonight:     %s' % ton

def google(string):
  words = string.split(' ')
  words.remove('google')
  query = '+'.join(words)
  url   = 'https://www.google.com/search?q=' + query
  wb.open(url, new=2)

def wiki(string):
  words = string.split(' ')
  if words[0] == 'wikipedia':
    words.remove('wikipedia')
  elif words[0] == 'wiki':
    words.remove('wiki')
  query = '+'.join(words)
  url   = 'http://en.wikipedia.org/w/index.php?search=' + query
  wb.open(url, new=2)

def desciclo(string):
  words = string.split(' ')
  if words[0] == 'desciclopedia':
    words.remove('desciclopedia')
  elif words[0] == 'search':
    words.remove('search')
  elif words[0] == 'desciclo':
    words.remove('desciclo')
  elif words[0] == 'des':
    words.remove('des')
  query = '+'.join(words)
  url   = 'http://desciclopedia.org/index.php?search=' + query
  wb.open(url, new=2)

def face(): wb.open('https://www.facebook.com', new=2)
def gag(): wb.open('https://www.9gag.com', new=2)
def usq(): wb.open('https://www.umsabadoqualquer.com', new=2)

def hue(): print 10 * (6 * 'HUE' + ' ' + 3 * 'BR' + '\n'), 'gibe money plox'

def start():
  print "huepy: Hello!"
  weather()
  if not os.path.exists('task.list'):
    arq = open('task.list')
    arq.close()
  if not os.path.exists('shopping.list'):
    arq = open('shopping.list')
    arq.close()
  see('see task list')
  print "       Type 'help' to see some example queries."
