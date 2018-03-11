%pylab inline
import matplotlib.pyplot as plt
from wordcloud import WordCloud
filename = "C:/Users/93585/demo/bojack.txt"
with open(filename,'r',encoding='utf-8') as f:
    mytext = f.read()
wordcloud=WordCloud().generate(mytext)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
