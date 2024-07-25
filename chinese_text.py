from collections import defaultdict

import thulac
from pyecharts.charts import Bar
from pyecharts.options import InitOpts
from wordcloud import WordCloud


def read() -> str:
    with open("article.text") as f:
        content = f.read()
        content = content.replace("\n", "")

    return content


def data_clean(content: str) -> list:
    thu1 = thulac.thulac(seg_only=True, filt=True)  # 默认模式
    seg_list = thu1.cut(content)
    word_dict = defaultdict(int)

    for seg in seg_list:
        w = seg[0]
        word_dict[w] += 1

    sorted_word_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    sorted_word_list = sorted_word_list[4:]

    index_to_delete = [
        1,
        11,
        14,
        15,
        16,
        17,
        31,
        34,
        43,
        50,
        53,
        55,
        60,
        61,
        65,
        69,
        70,
        71,
        74,
        75,
        85,
        86,
        95,
        106,
        109,
        116,
        122,
        126,
        142,
        143,
    ]
    sorted_word_list = [
        sorted_word_list[i]
        for i in range(len(sorted_word_list))
        if i not in index_to_delete
    ]

    return sorted_word_list


def visualize(word_list: list):
    key_word_list = [item for item in word_list if item[1] >= 20]

    keywords = [item[0] for item in key_word_list]

    gen_text = " ".join(keywords)
    WordCloud(
        font_path="msyh.ttf", width=3840, height=2160, max_words=len(keywords)
    ).generate(gen_text).to_file("demo.jpg")

    label = list(map(lambda x: x[0], key_word_list))
    value = list(map(lambda x: x[1], key_word_list))

    bar = Bar(init_opts=InitOpts(width="100%", height="2160px"))
    bar.add_xaxis(label)
    bar.add_yaxis(
        "关键词",
        value,
    ).reversal_axis()
    bar.render()


if __name__ == "__main__":
    content = read()
    word_list = data_clean(content)
    visualize(word_list)
