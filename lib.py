import jieba
import json


def find_in_wei(word, weipath='data\\wei.json'):
    """查询伪原创字典"""
    f_wei = open(weipath, 'r', encoding='utf-8')
    wei_dict = json.load(f_wei)
    if len(word) < 2:
        return False
    if word in wei_dict:
        return wei_dict[word]
    else:
        return False
