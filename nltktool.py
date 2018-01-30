import nltk
import json
import re
import os
filelist=os.listdir('saves')
print(filelist)

words=''
element = 'http'
allowedchars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,._-:/ "
for i in range(len(filelist)):
    file=filelist[i]
    location='saves/'+ file
    print(location)
    with open(location) as file1:
        for line in file1:
            try:
                tweet = json.loads(line)
                if 'text' in tweet:
                    dat=tweet['text']
                    dat1=dat.rsplit(' ',1)[1]
                    if 'https' in dat1:
                        dat=dat.rsplit(' ',1)[0]
                    if 'https' in dat:
                        dat=dat.split(' ')
                        for item in dat:
                            if element in item:
                                dat.remove(item)
                            ' '.join(dat)
                    dat=re.sub(r'\W+', ' ', dat)
#                    print(dat)
                    words=words+dat.strip()
            except:
                continue
        tokens = nltk.tokenize.word_tokenize(words)
        fd = nltk.FreqDist(tokens)
        fd.plot(100,cumulative=False)
