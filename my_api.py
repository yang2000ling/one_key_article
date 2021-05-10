import lib
import jieba
import json


def api_main(text):
    seq_list = jieba.cut(text)
    new_buff = ''
    for i in seq_list:
        if new_word := lib.find_in_wei(i):
            new_buff = new_buff + new_word
        else:
            new_buff = new_buff + i
    return new_buff


if __name__ == '__main__':
    f_txt = open('1.txt', 'r', encoding='utf-8')
    buff = f_txt.read()
    print(buff)
    print('-------------------------------------')
    print(api_main(buff))
