# 湛江市第五中学宿舍分配系统
# 贪心算法

import pandas as pd
import numpy as np

# 传入excel数据
df_stu = pd.read_excel('xs.xlsx')
df_dor = pd.read_excel('ss.xlsx')
df_stu[
    'sClassID'] = df_stu['sGrade'] * 1000 + df_stu['sClass'] * 10  # 给每个班一个唯一标记
df_stu['sDorm'] = np.NaN  # 加一列宿舍设为空
# print(df_stu)

# 分男女
df_stu_M = df_stu[df_stu.sSex == 1].reset_index(drop=True)
df_stu_F = df_stu[df_stu.sSex == 2].reset_index(drop=True)
df_dor_M = df_dor[df_dor.dSex == 1].reset_index(drop=True)
df_dor_F = df_dor[df_dor.dSex == 2].reset_index(drop=True)

# print(df_stu_F)


# 查找一个大于a的最小值索引值
def search(a, L):
    for i, l in enumerate(L):
        if a <= l:
            return i


# 贪心算法宿舍分配
def distribution(df_s, df_d):
    i = 0
    #创建一个空的dataframe
    df_s_New = pd.DataFrame(columns=[
        'sName', 'sID', 'sSex', 'sGrade', 'sClass', 'sTypes', 'sClassID',
        'sDorm'
    ])
    print(df_s_New)
    while df_s.shape[0] != 0 or df_d.shape[0] != 0:
        # 宿舍空余床位从小到大排序
        df_d = df_d.sort_values(['dMax']).reset_index(drop=True)

        #提取一些值
        dMax = df_d.loc[:, ['dMax']][-1:].values  # 取最大值
        sClassID = df_s.ix[:0, ['sClassID']].values  # 取当前班级
        dMax = dMax[0][0]
        sClassID = sClassID[0][0]
        # dMax=df_d['dMax'][-1:].values
        # sClassID = df_s['sClass'][0]
        # print(dMax)
        # print(sClassID)
        sPeople = df_s[df_s.sClassID == sClassID].shape[0]  # 首个班级人数
        # print(sPeople)

        # 将大于房间最大人数的班级分块
        if sPeople > dMax:
            df_s['sClassID'][0:dMax] = df_s['sClassID'][0:dMax] + 1
            # print(sPeople)
            print('segmentation')
            # print(df_s['sClassID'][0:dMax])
            continue

        # 找出分配位置的索引
        list1 = df_d['dMax'].values
        k = search(sPeople, list1)
        print(k)
        # 向df_s记录宿舍
        df_s['sDorm'][df_s.sClassID == sClassID] = df_d['dID'][k]
        # 向df_s_New输出宿舍
        df_s_New = df_s_New.append(df_s[df_s.sClassID == sClassID],
                                   ignore_index=True)
        # 删除已输出宿舍
        df_s.drop(range(0, sPeople), inplace=True)
        print(df_s_New)
        print(df_s)
        i = i + 1
        if i == 1:
            break


if __name__ == "__main__":
    distribution(df_stu_M, df_dor_M)
    # L = [1, 2, 4, 6, 8, 10]
    # print(search(4, L))