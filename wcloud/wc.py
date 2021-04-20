from wordcloud import WordCloud
import numpy as np
from PIL import Image
import jieba

mask = np.array(Image.open("laughingMan.jpg"))
wcd = WordCloud(background_color='white', repeat=True, max_words=500, height=480, width=854,
                max_font_size=100, font_path="fonts/msyh.ttc", colormap="Reds", mask=mask,
                mode="RGBA")

with  open('2021政府工作报告.txt', 'r', encoding='utf-8') as text:
    reader=text.read()
    ss = " ".join(jieba.lcut(reader))
    wcd.generate(ss)
    wcd.to_image()
    wcd.to_file("China_wordcloud.png")
