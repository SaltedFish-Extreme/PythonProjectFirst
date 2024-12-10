import re


def phone_number():
    n = input("请输入手机号：")
    # 使用re.match检查输入的手机号是否符合基本的手机号格式
    # 正则表达式 r'1[34578]\d{9}' 用于匹配以13、14、15、17、18开头的11位数字
    if re.match(r'1[34578]\d{9}', n):
        print("该号码合法")
        # 接下来分别检查手机号归属于哪个运营商
        # 中国移动的号码匹配规则
        if (re.match(r'13[456789]\d{8}', n) or
                re.match(r'15[012789]\d{8}', n) or
                re.match(r'147\d{8}|178\d{8}', n) or
                re.match(r'18[23478]\d{8}', n)):
            print("该号码属于：中国移动")
        # 中国联通的号码匹配规则
        elif (re.match(r'13[012]\d{8}', n) or
              re.match(r'18[56]\d{8}', n) or
              re.match(r'15[56]\d{8}', n) or
              re.match(r'176\d{8}', n) or
              re.match(r'145\d{8}', n)):
            print("该号码属于：中国联通")
        else:
            # 如果上述规则都不匹配，则默认为中国电信号码
            print("该号码属于：中国电信")
    else:
        print("请输入正确的手机号")


phone_number()
