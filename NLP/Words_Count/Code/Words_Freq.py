# -*- coding: utf-8 -*-
# Author: Aakas Zhiyuli
# Email: zhiyulee@icloud.com
# --------------------------------------------
# 本包主要用于完成中文词频统计的任务操作，主要考虑统计的词频的效率以及输出形式
"""
Keywords: 词频统计，中文词频统计；
简介：输入一段中文文本，统计词语的词频；
使用方法：将 `Words_Freq.py` 文件拷贝到工作目录即可；
特点：
* 支持多线程并行统计；
* 支持包括txt以及Excel输出；
* 支持排序后输出；
"""

from collections import Counter
from multiprocessing import cpu_count
import re,time
import jieba  # 导入jieba分词，需要安装jieba分词包

# 快速模式，充分利用CPU性能进行并行处理
def fast_words_count(filepath, cut_a = False, output_t = False):
    jieba.enable_parallel(cpu_count()) # 开启并行分词模式,非windows下有效
    with open(filepath, 'rb') as in_text:
        all_lines  =  in_text.read()
        cut_line= re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（），、；：？！…―ˉˇ〃‘'“”～‖∶＂＇｀｜〔〕〈〉《》「」『』．〖〗【】（）［］｛｝]+".decode("utf-8"), "".decode("utf-8"),
                  all_lines.decode("utf-8"))
        words_c  = Counter(list(jieba.cut(cut_line, cut_all=cut_a)))

    if output_t:
        with open(filepath+'_Count', 'wb') as out_count:
            for word, freq in words_c.most_common():
                out_count.writelines(' '.join([word, str(freq)]).encode('utf-8')+'\n')
    else: # 输出excel表格
        import xlwt  # 导入excel处理包
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Words Count')
        worksheet.write(0, 0, label='Word')
        worksheet.write(0, 1, label='Freq.')
        i  = 1
        for word, freq in words_c.most_common():
            worksheet.write(i, 0, label = word)
            worksheet.write(i, 1, label = freq)
            i += 1
        workbook.save(filepath+'_Count.xls')


if __name__ == '__main__':

    file_path = '../Data/Text_CN'  # 待统计词频的文本文件位置；
    st = time.time()
    fast_words_count(file_path, output_t = False) # 调用统计函数，默认指定输出格式为excel文件
    print ('Time Cost: %.3f s' %(time.time() - st))






