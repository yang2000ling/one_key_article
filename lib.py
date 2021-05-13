import json
import time
import conf

"""-------------------------------基础函数区-----------------------------------"""


def find_in_wei(word, weipath):
    """查询伪原创字典"""
    f_wei = open(weipath, 'r', encoding='utf-8')
    wei_dict = json.load(f_wei)
    if len(word) < 2:
        return False
    if word in wei_dict:
        return wei_dict[word]
    else:
        return False


def sleep(sleep_time):
    """延时函数（单位：秒）"""
    print('休眠:' + str(sleep_time) + 's')
    time.sleep(sleep_time)
    print('休眠结束。')


def write_log(str_log, file_name='out_log.txt'):
    """str_log写入信息,file_name为日志文件名"""
    str_time2s = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    f = open(file_name, 'a', encoding='utf-8')
    f.write(str_time2s + " :" + str(str_log) + '\n')
    f.close()


def find_in_cilin(word, dict_path):
    """查询词林近义词，返回同义词列表"""
    f_word = open(dict_path, 'r', encoding='utf-8')
    word_dict = json.load(f_word)
    if word in word_dict:
        return word_dict[word]
    return False


"""--------------------------------高级函数区----------------------------------"""


def find_word(word, deep):
    """查找近义词高级函数,deep为替换深度"""
    try:
        if deep == 1:
            if find_in_wei(word, conf.wei_json_path):
                new_word = find_in_wei(word, conf.wei_json_path)
                return new_word
            else:
                return False
        elif deep == 2:
            if find_in_cilin(word, conf.cilin_json_path):
                new_word_list = find_in_cilin(word, conf.cilin_json_path)
                return new_word_list[0]
            else:
                return False
        elif deep == 3:
            if find_in_cilin(word, conf.cilin_json_path):
                new_word_list = find_in_cilin(word, conf.cilin_json_path)
                return new_word_list[0]
            elif find_in_wei(word, conf.wei_json_path):
                new_word = find_in_wei(word, conf.wei_json_path)
                return new_word
            else:
                return False
    except Exception as error:
        write_log(error)
        return False


if __name__ == '__main__':
    pass
