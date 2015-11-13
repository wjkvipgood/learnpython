#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height = float(input('请输入您的身高（单位米）：'))
weight = float(input('请输入您的体重（单位千克）：'))
BMI = weight / (height * height)

print('您的身高体重指数：%.1f' % BMI)
if BMI > 32:
    print('高于32 严重肥胖')
elif BMI >= 28:
    print('位于28-32之间 肥胖')
elif BMI >= 25:
    print('位于25-28之间 过重')
elif BMI >= 18.5:
    print('位于18.5-25之间 正常')
else:
    print('低于18.5 过轻')
