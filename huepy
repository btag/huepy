#!/usr/bin/env python
#-*- coding: utf-8 -*-

import opshue as ops

lists = ops.llists()
version = "developing"

ops.start()

while True:
  a = raw_input("you: ").lower()
  #a = ops.noaccent(a)
  b = ops.checkdata(a)
  #if b != "no-match": print "info: match", b
  #else:               print "info: no-match"
  if b == "example" or b == "help":
    ops.example()
  elif a == "q" or b == "leave" or b == "bye":
    break
  elif a == "v" or b == "version":
    print "huepy: I'm running on %s version" % version
  elif b == "lists":
    print "huepy: You have the following lists:"
    for i in range(len(lists)):
      print "        %i. %s" % (i+1, lists[i])
  elif b == "see":
    ops.see(a)
  elif b == "put":
    ops.put(a)
  elif b == "remove":
    ops.remove(a)
  elif b == "weather" or b == "forecast":
    ops.weather()
  elif b == "google":
    ops.google(a)
  elif b == "wiki" or b == "wikipedia":
    ops.wiki(a)
  elif b == "desciclopedia" or b == "search" or b == "desciclo" or b == "des":
    ops.desciclo(a)
  elif b == "facebook" or b == "face": ops.face()
  elif b == "9gag": ops.gag()
  elif b == "usq": ops.usq()
  elif b == "hue":
    ops.hue()
  elif b == "start":
    ops.start()
  else: print "huepy: I could not understand your query. You can see example queries by typing 'help'"
