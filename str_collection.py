					# 1 首字母大写
                         #test = "aLex"
                         #v = test.capitalize()
                         #print(v)

                    # 2 所有变小写，casefold更牛逼，很多未知的对相应变小写
                        # v1 = test.casefold()
                        # print(v1)
                        # v2 = test.lower()
                        # print(v2)

                    # 3 设置宽度，并将内容居中
                        # 20 代指总长度
                        # *  空白未知填充，一个字符，可有可无
                        # v = test.center(20,"中")
                        # print(v)

                        # test = "alex"
                        # v = test.ljust(20,"*")
                        # print(v)

                        # test = "alex"
                        # v = test.rjust(20,"*")
                        # print(v)

                        # test = "alex"
                        # v = test.zfill(20)
                        # print(v)


                    # 4 去字符串中寻找，寻找子序列的出现次数
                        # test = "aLexalexr"
                        # v = test.count('ex')
                        # print(v)

                        # test = "aLexalexr"
                        # v = test.count('ex',5,6)
                        # print(v)

                    # 欠
                    # encode
                    # decode

                    # 5
                        # 以什么什么结尾
                        # 以什么什么开始
                        # test = "alex"
                        # v = test.endswith('ex')
                        # v = test.startswith('ex')
                        # print(v)

                    # 6 expandtabs,断句20，
                        # test = "username\temail\tpassword\nlaiying\tying@q.com\t123\nlaiying\tying@q.com\t123\nlaiying\tying@q.com\t123"
                        # v = test.expandtabs(20)
                        # print(v)

                    # 7 从开始往后找，找到第一个之后，获取其位置
                        # > 或 >=
                        # test = "alexalex"
                        # 未找到 -1
                        # v = test.find('ex')
                        # print(v)

                    # 8 index找不到，报错   忽略
                        # test = "alexalex"
                        # v = test.index('8')
                        # print(v)


                    # 9 格式化，将一个字符串中的占位符替换为指定的值
                        # test = 'i am {name}, age {a}'
                        # print(test)
                        # v = test.format(name='alex',a=19)
                        # print(v)

                        # test = 'i am {0}, age {1}'
                        # print(test)
                        # v = test.format('alex',19)
                        # print(v)

                    # 10 格式化，传入的值 {"name": 'alex', "a": 19}
                        # test = 'i am {name}, age {a}'
                        # v1 = test.format(name='df',a=10)
                        # v2 = test.format_map({"name": 'alex', "a": 19})

                    # 11 字符串中是否只包含 字母和数字
                        # test = "123"
                        # v = test.isalnum()
                        # print(v)
                        # str
                        
                    # 12 是否是字母，汉子
                        # test = "as2df"
                        # v = test.isalpha()
                        # print(v)

                    # 13 当前输入是否是数字
                        # test = "二" # 1，②
                        # v1 = test.isdecimal()
                        # v2 = test.isdigit()
                        # v3 = test.isnumeric()
                        # print(v1,v2,v3)


                    # 14 是否存在不可显示的字符
                        # \t   制表符
                        # \n   换行
                        # test = "oiuas\tdfkj"
                        # v = test.isprintable()
                        # print(v)

                    # 15 判断是否全部是空格
                        # test = ""
                        # v = test.isspace()
                        # print(v)

                    # 16 判断是否是标题
                        # test = "Return True if all cased characters in S are uppercase and there is"
                        # v1 = test.istitle()
                        # print(v1)
                        # v2 = test.title()
                        # print(v2)
                        # v3 = v2.istitle()
                        # print(v3)

                    # 17 ***** 将字符串中的每一个元素按照指定分隔符进行拼接
                        # test = "你是风儿我是沙"
                        # print(test)
                        # # t = ' '
                        # v = "_".join(test)
                        # print(v)

                    # 18 判断是否全部是大小写 和 转换为大小写
                        # test = "Alex"
                        # v1 = test.islower()
                        # v2 = test.lower()
                        # print(v1, v2)

                        # v1 = test.isupper()
                        # v2 = test.upper()
                        # print(v1,v2)
                    # 19
                        # 移除指定字符串
                        # 有限最多匹配
                        # test = "xa"
                        # # v = test.lstrip('xa')
                        # v = test.rstrip('9lexxexa')
                        # # v = test.strip('xa')
                        # print(v)

                        # test.lstrip()
                        # test.rstrip()
                        # test.strip()
                        # 去除左右空白
                        # v = test.lstrip()
                        # v = test.rstrip()
                        # v = test.strip()
                        # print(v)
                        # print(test)
                        # 去除\t \n
                        # v = test.lstrip()
                        # v = test.rstrip()
                        # v = test.strip()
                        # print(v)

                    # 20 对应关系替换
                        # test =  "aeiou"
                        # test1 = "12345"

                        # v = "asidufkasd;fiuadkf;adfkjalsdjf"
                        # m = str.maketrans("aeiou", "12345")
                        # new_v = v.translate(m)
                        # print(new_v)

                    # 21 分割为三部分
                        # test = "testasdsddfg"
                        # v = test.partition('s')
                        # print(v)
                        # v = test.rpartition('s')
                        # print(v)

                    # 22 分割为指定个数
                        # v = test.split('s',2)
                        # print(v)
                        # test.rsplit()


                    # 23 分割，只能根据，true，false：是否保留换行
                        # test = "asdfadfasdf\nasdfasdf\nadfasdf"
                        # v = test.splitlines(False)
                        # print(v)

                    #  24 以xxx开头，以xx结尾
                        # test = "backend 1.1.1.1"
                        # v = test.startswith('a')
                        # print(v)
                        # test.endswith('a)

                    # 25 大小写转换
                        # test = "aLex"
                        # v = test.swapcase()
                        # print(v)

                    # 26 字母，数字，下划线 ： 标识符 def  class
                        # a = "def"
                        # v = a.isidentifier()
                        # print(v)


                    # 27 将指定字符串替换为指定字符串
                        # test = "alexalexalex"
                        # v = test.replace("ex",'bbb')
                        # print(v)
                        # v = test.replace("ex",'bbb',2)
                        # print(v)
                    ###################### 7个基本魔法 ######################
                    # join       # '_'.join("asdfasdf")
                    # split
                    # find
                    # strip
                    # upper
                    # lower
                    # replace
                    ###################### 4个灰魔法 ######################
                    # test = "郑建文妹子有种冲我来"