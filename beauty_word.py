from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('cloding.txt','r') as f:
   text=f.read()
print(text)

wordcloud=WordCloud(width=2000,height=2000,background_color="black",min_font_size=9,ranks_only= "frequency").generate(text)
plt.figure(figsize=(6,7),facecolor=None)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0.5)
plt.show()