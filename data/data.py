# -*- coding: utf-8 -*-
# Time : 2022/3/27 10:52
# Author : SJY
# File : data.py
# Desc :
from config.config import file_path
class ReadWrite:
    def __init__(self):
        self.file =""
        self.excelpath = file_path
        self.yamlpath =""

    def txtread(self):
        list1 = []
        with open(self.file, 'r', encoding='utf-8') as f:
            values = f.readlines()
            f.close()
        for data in values:
            data_v = data.strip('\n')        # data.strip('\n')意思是去除掉 \n(换行符）
            list1.append(data_v)
        return list1

    def txtwrite(self,username,password):
        f = open(self.file, 'a', encoding='utf-8')
        values = f'{username},{password}\n'
        f.writelines(values)
        f.close()

    def excelread(self,sheetname):
        import openpyxl
        wb=openpyxl.load_workbook(self.excelpath)
        table=wb[sheetname]
        rows=table.max_row
        cols=table.max_column
        list2=[]
        for row in range(2,rows+1):
            list1=[]        #重新定义为空列表
            for col in range(1,cols+1):
                values=table.cell(row,col).value
                list1.append(values)
            list2.append(list1)
        return list2

    def excelwrite(self,*args,sheetname):    #*元组，多个变量
        import openpyxl
        wb = openpyxl.load_workbook(self.excelpath)
        table = wb[sheetname]
        rows = table.max_row
        cols = len(args)
        for col in range(cols):
            table.cell(rows+1,col+1).value=args[col]    #rows+1表示追加，col+1表示循环从0开始的
        wb.save(self.excelpath)

    def mysqlread(self):
        import pymysql
        db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='T31', charset='utf8')
        cur = db.cursor()
        sql = 'select * from users '
        cur.execute(sql)
        content=cur.fetchall()
        return content

    def mysqlwrite(self,username,password):
        import pymysql
        db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='T31', charset='utf8')
        cur = db.cursor()
        sql = f'insert into users values ("{username}","{password}") '
        cur.execute(sql)
        db.commit()

    def yamlread(self):
        import yaml
        f = open(self.yamlpath, 'r', encoding='utf-8')
        content = f.read()
        data = yaml.safe_load(content)        #将yaml内容转化成字典格式
        return data

    def yamlwrite(self,username,password):
        import yaml
        f = open(self.yamlpath, 'a', encoding='utf-8')
        data={'username':username,'password':password}
        yaml.safe_dump(data,f)          #将字典数据转化成yaml文件
        f.close()
