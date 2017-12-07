import matplotlib.pyplot as mt
import json
import matplotlib.patches as mpatches
idarray=[]
sourcearray=[]
createarray=[]
textarray=[]
tweetlength=[]
isource=[]
asource=[]
psource=[]
wsource=[]
osource=[]
total=[]
p=500 #smoothing points
tweets_filename = 'capture.txt'
with open(tweets_filename) as tweets_file:
    for line in tweets_file:
        try:
            tweet = json.loads(line.strip())
            if 'text' in tweet:
                q=tweet['id']
                w=tweet['source']
                e=tweet['created_at']
                r=tweet['text']
                if r.startswith('RT'):
                    r=r.split(':',1)[1]
                    r=r.lstrip(' ')
                    r=r.replace('&amp','&')
                    if len(r) > 140:
                        print(r)
                    r=r[:140]
                    idarray.append(q)
                    createarray.append(e)
                    textarray.append(r)
                    tweetlength.append(len(r))
                    w=w[:-4]
                    w=w.rsplit(' ', 1)[1]
                    if w.strip()=='iPhone':
                        sourcearray.append('1')
                        isource.append(len(r))
                    elif w.strip()=='Android':
                        sourcearray.append('2')
                        asource.append(len(r))
                    elif w.strip()=='iPad':
                        sourcearray.append('3')
                        psource.append(len(r))
                    elif w.strip()=='Client':
                        sourcearray.append('4')
                        wsource.append(len(r))
                    else:
                        sourcearray.append('5')
                        osource.append(len(r))
                    total.append(len(r))
#            hashtags = []
#            for hashtag in tweet['entities']['hashtags']:
#                hashtags.append(hashtag['text'])
#            print (hashtags)

        except:
            continue
#print (sourcearray)
#mt.scatter(tweetlength,sourcearray)
mt.clf()
f,axarr=mt.subplots(nrows=2, ncols=1, sharex=True, sharey=True, squeeze=True, subplot_kw=None, gridspec_kw=None)
l1=axarr[1].violinplot(wsource, points=p, widths=0.3, showmeans=True, showextrema=False, showmedians=False, vert=False)
l2=axarr[1].violinplot(asource, points=p, widths=0.3, showmeans=True, showextrema=False, showmedians=False, vert=False)
l3=axarr[1].violinplot(isource, points=p, widths=0.3, showmeans=True, showextrema=False, showmedians=False, vert=False)
l4=axarr[1].violinplot(psource, points=p, widths=0.3, showmeans=True, showextrema=False, showmedians=False, vert=False)
l5=axarr[1].violinplot(osource, points=p, widths=0.3, showmeans=True, showextrema=False, showmedians=False, vert=False)
axarr[0].violinplot(total, points=p, widths=0.3, showmeans=True, showextrema=True, showmedians=False, vert=False)
axarr[0].set_title('Overall Distribution')
axarr[1].set_title('By source distributions')
#z=axarr[0]
for pc in l1['bodies']:
    pc.set_facecolor('None')
    pc.set_edgecolor('red')
for pc in l2['bodies']:
    pc.set_facecolor('None')
    pc.set_edgecolor('blue')
for pc in l3['bodies']:
    pc.set_facecolor('None')
    pc.set_edgecolor('green')
for pc in l4['bodies']:
    pc.set_facecolor('None')
    pc.set_edgecolor('yellow')
for pc in l5['bodies']:
    pc.set_facecolor('None')
    pc.set_edgecolor('brown')
red_patch = mpatches.Patch(color='red', label='Web Client')
blue_patch = mpatches.Patch(color='blue', label='Android')
green_patch = mpatches.Patch(color='green', label='iPhone')
yellow_patch = mpatches.Patch(color='yellow', label='iPad')
brown_patch = mpatches.Patch(color='brown', label='Other')

mt.xlabel('Tweet Length (char)')
mt.legend(handles=[red_patch,blue_patch,yellow_patch,green_patch,brown_patch])
#mt.legend
mt.show()
