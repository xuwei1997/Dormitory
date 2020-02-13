# 湛江市第五中学宿舍分配系统
### 作者：xuwei  

将记录有学生信息及宿舍信息的excel导入系统，采用贪心算法进行宿舍匹配。

## 学生表
将待分配学生存入excel文件 xs.xlsx，系统会按班级顺序与进行匹配。
### 学生表字段：
+ 姓名：sName  
+ 学号：sID  
+ 性别：sSex (男：1，女：2)  
+ 年级：sGrade  
+ 班级：sClass
+ 住宿类型：sTypes (全宿：1，半宿：2)  

## 宿舍表
将宿舍号剩余床位等信息存入excel文件 ss.xlsx，系统会按顺序进行匹配。 
### 宿舍表字段：
+ 宿舍楼栋号: dNum  
+ 宿舍号: dID  
+ 性别: dSex (男：1，女：2)  
+ 最大居住人数: dMax 

## 输出
+ shengyusushe_F.xlsx : 女生剩余宿舍
+ shengyusushe_M.xlsx : 男生剩余宿舍
+ weifenpei_F.xlsx : 女生未分配宿舍
+ weifenpei_M.xlsx : 男生未分配宿舍
+ yifenpei_F.xlsx : 女生宿舍分配情况
+ yifenpei_M.xlsx : 男生宿舍分配情况