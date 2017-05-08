# -*- coding: utf-8 -*-
from TS_transform import *

import time


def main(T_basic = '天好藍要和你一起看，起風時由你来温暖。',
         S_basic = '因为爱过，所以慈悲；因为懂得，所以宽容。'):


    print "===============单线程调用===================="
    print '繁体转换为简体: ', T2S(T_basic)
    print '简体转换为繁体: ', S2T(S_basic)


    print "===============多线程调用===================="
    lines = [T_basic for i in range(100000)]
    t1 = time.time()
    resu = []
    for l in lines:
        resu.append(T2S(l))
    T2S_Cost = time.time()-t1
    print '单线程版: %.2f ' % T2S_Cost

    t2 = time.time()
    Fast_T2S(lines)
    Fast_T2S_Cost = time.time()-t2
    print '多线程版: %.2f ' % Fast_T2S_Cost
    print '加速倍速: %.2f 倍' % (1.00*T2S_Cost/Fast_T2S_Cost)


    print "===============文档进，文档出，默认调用fast版本===================="
    print '繁体文档转换为简体文档，保留非中文字符:', TXT_T2S('../Data/T_test', KCP = True)
    print '简体文档转换为繁体文档，保留非中文字符:', TXT_S2T('../Data/T_test.simple', KCP = True)
    print '繁体文档转换为简体文档，去除非中文字符:', TXT_T2S('../Data/T_test', KCP = False)
    print '简体文档转换为繁体文档，去除非中文字符:', TXT_S2T('../Data/T_test.simple', KCP = False)










if __name__ == '__main__':
    main()