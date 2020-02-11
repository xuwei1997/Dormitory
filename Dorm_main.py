# 湛江市第五中学宿舍分配系统
# 贪心算法

import pandas as pd
import numpy as np
from time import sleep


# 查找一个大于a的最小值索引值
def search(a, L):
    for i, l in enumerate(L):
        if a <= l:
            return i


# 贪心算法宿舍分配
def distribution(df_s, df_d, name_end):
    i = 0
    print('当前分配：' + name_end)
    # 创建一个空的dataframe
    df_s_New = pd.DataFrame(columns=[
        'sName', 'sID', 'sSex', 'sGrade', 'sClass', 'sTypes', 'sClassID',
        'sDorm'
    ])

    while df_s.shape[0] != 0 and df_d.shape[0] != 0:
        # 输出序号
        i = i + 1
        print('分配次数：' + str(i))

        # 宿舍空余床位从小到大排序
        df_d = df_d.sort_values(['dMax']).reset_index(drop=True)

        # 提取一些值
        dMax = df_d.loc[:, ['dMax']][-1:].values  # 取最大值
        sClassID = df_s.ix[:0, ['sClassID']].values  # 取当前班级
        dMax = dMax[0][0]
        sClassID = sClassID[0][0]
        # dMax=df_d['dMax'][-1:].values
        # sClassID = df_s['sClass'][0]
        print('当前班级序号：' + str(sClassID))
        sPeople = df_s[df_s.sClassID == sClassID].shape[0]  # 首个班级人数
        print('当前班级人数：' + str(sPeople))

        # 将大于房间最大人数的班级分块
        if sPeople > dMax:
            # df_s['sClassID'][0:dMax] = df_s['sClassID'][0:dMax] + 1
            # print(df_s.ix[0:dMax-1,'sClassID'])
            df_s.ix[0:dMax - 1,
                    'sClassID'] = df_s.ix[0:dMax - 1, 'sClassID'] + 1
            print('segmentation!!!!!!!')
            continue

        # 找出分配位置的索引
        list1 = df_d['dMax'].values
        k = search(sPeople, list1)

        # 向df_s记录宿舍与宿舍楼栋号
        # df_s['sDorm'][df_s.sClassID == sClassID] = df_d['dID'][k]
        df_s.loc[df_s.sClassID == sClassID, 'sDorm'] = df_d.ix[k, 'dID']
        df_s.loc[df_s.sClassID == sClassID, 'sDormNum'] = df_d.ix[k, 'dNum']

        # 向df_s_New输出宿舍
        df_s_New = df_s_New.append(df_s[df_s.sClassID == sClassID],
                                   ignore_index=True)

        # 删除已输出宿舍
        df_s.drop(range(0, sPeople), inplace=True)
        df_s = df_s.reset_index(drop=True)
        # print(df_s_New)
        # print(df_s)

        # 宿舍dMax减去对应的sPeople
        df_d.ix[k, ['dMax']] = df_d.ix[k, ['dMax']] - sPeople
        dMax_end = df_d.ix[k, ['dMax']].values

        # 如果宿舍空，从表中删除宿舍
        if dMax_end == 0:
            df_d = df_d.drop(k)
            df_d = df_d.reset_index(drop=True)

    dnew = [
        'sName', 'sID', 'sSex', 'sGrade', 'sClass', 'sTypes', 'sClassID',
        'sDorm'
    ]
    df_s_New = df_s_New[dnew]

    df_s.to_excel('weifenpei_' + name_end + '.xlsx')
    df_s_New.to_excel('yifenpei_' + name_end + '.xlsx')
    df_d.to_excel('shengyusushe_' + name_end + '.xlsx')


if __name__ == "__main__":
    # 开头
    print('湛江市第五中学宿舍分配系统')
    sleep(0.5)
    print('作者：许巍')
    sleep(0.5)
    print('2020-02')
    print('........................................')
    sleep(0.5)
    sKind = input('请输入数字选择分配学生类型（0-全部；1-仅全宿,2-仅半宿）:')
    print('........................................')

    # 传入excel数据
    df_stu = pd.read_excel('xs.xlsx')
    df_dor = pd.read_excel('ss.xlsx')
    df_stu['sClassID'] = df_stu['sGrade'] * 1000 + df_stu[
        'sClass'] * 10  # 给每个班一个唯一标记
    df_stu['sDorm'] = np.NaN  # 加一列宿舍设为空
    df_stu['sDormNum'] = np.NaN  # 加一列宿舍楼栋号设为空

    # 选择全宿半宿
    if sKind == '1':
        df_stu = df_stu[df_stu.sTypes == 1]
    elif sKind == '2':
        df_stu = df_stu[df_stu.sTypes == 2]

    # 分男女
    df_stu_M = df_stu[df_stu.sSex == 1].reset_index(drop=True)
    df_stu_F = df_stu[df_stu.sSex == 2].reset_index(drop=True)
    df_dor_M = df_dor[df_dor.dSex == 1].reset_index(drop=True)
    df_dor_F = df_dor[df_dor.dSex == 2].reset_index(drop=True)

    # 分配
    distribution(df_stu_M, df_dor_M, 'M')
    distribution(df_stu_F, df_dor_F, 'F')