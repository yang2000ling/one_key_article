import lib
import jieba


def api_main(text, deep):
    seq_list = jieba.cut(text)
    new_buff = ''
    for i in seq_list:
        if new_word := lib.find_word(i, deep):
            new_buff = new_buff + new_word
        else:
            new_buff = new_buff + i
    return new_buff


if __name__ == '__main__':
    print(api_main('我爱中国人',1))
    pass
