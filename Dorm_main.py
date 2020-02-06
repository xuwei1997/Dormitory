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


# 宿舍排序
def distribution(df_s, df_d):
    i = 0
    while df_s.shape[0] != 0 or df_d.shape[0] != 0:
        df_d = df_d.sort_values(['dMax']).reset_index(drop=True)  # 排序
        dMax = df_d.loc[:, ['dMax']][-1:].values  # 取最大值
        sClassID = df_s.ix[:0, ['sClassID']].values  # 取当前班级
        dMax = dMax[0][0]
        sClassID = sClassID[0][0]
        # dMax=df_d['dMax'][-1:].values
        # sClassID = df_s['sClass'][0]
        # print(dMax)
        # print(sClassID)
        sPeople = df_s[df_s.sClassID == sClassID]
        print(sPeople)
        print(i)

        i = i + 1
        if i == 2:
            break


if __name__ == "__main__":
    distribution(df_stu_M, df_dor_M)
