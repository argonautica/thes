#!/usr/bin/env python3

import sys, json, urllib
from urllib.request import urlopen

url = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/placeholder?key=db27a491-637d-4a50-837a-4006185fdd04"



def getJson(url):
    response = urlopen(url)
    data = json.loads(response.read())
    return data






def getsyn(data):
    synonyms = []
    for a in data:
        for b in a.get("def"):
            for c in b['sseq']:
                for d in c[0]:
                    if(type(d) is dict):
                        for e in(d.get('syn_list', '')):
                            for f in e:
                                synonyms.append(f.get('wd'))
                                #print(f.get('wd'))
                        for e in(d.get('rel_list', '')):
                            for f in e:
                                #print(f.get('wd'))
                                synonyms.append(f.get('wd'))
                        for e in(d.get('near_list', '')):
                            for f in e:
                                #print(f.get('wd'))
                                synonyms.append(f.get('wd'))
                        for e in(d.get('sim_list', '')):
                            for f in e:
                                #print(f.get('wd'))
                                synonyms.append(f.get('wd'))
    return synonyms




                        #print((d.get('syn_list', 'none'))[0])
                        #print(d.get('rel_list', 'none'))
                        #print(d.get('near_list', 'none'))
                        #print(d.get('sim_list', 'none'))


for arg in sys.argv:
   if "thes" not in arg:
       url = url.replace("placeholder", arg)

       result = getsyn(getJson(url))
       temp = 0
       str = ""
       for a in result:


           if temp < 6:
               str = str + " " + a
               temp = temp + 1

           else:
               print(str)
               str = ""
               temp = 0

       #print(getsyn(getJson(url)))
       # print(url)
      ## getSyn(getJson(url))



