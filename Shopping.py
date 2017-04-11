#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Jack Niu

# 输入用户名和密码.
username = input("Username:").strip()
password = input("Password:").strip()

# 判断用户名密码是否正确并设立Flag
Login = {"flag": False}
Money = {"flag": False}
with open("Userlist", "r") as UserFile:
    UserFile_Str = str(UserFile.read())
    UserFile_Dic = eval(UserFile_Str)
with open( "ShoppingList", "r+" ) as file:
    file_str = str( file.read( ) )
    file_dic = eval( file_str )
if username in UserFile_Dic and password in UserFile_Dic[username]:
    if UserFile_Dic[username].get( password ) == "None":
        GongziInput = input( "请输入您的工资>>>>>>:" )
        if GongziInput.isdigit( ):
            Gongzi = int( GongziInput )
            UserFile_Dic[username][password] = Gongzi
            Login["flag"] = True
        else:
            print("无效的输入！")
    else:
        Money["flag"] = True
else:
    print( "对不起，你的用户名或者密码错误，请重新输入或联系IT管理人员！" )

# 定义变量.
Salary = UserFile_Dic[username][password]
shopping_list = file_dic[username]

# 购买流程.
def Buy(Salary,shopping_list):
    "购买流程"
    while True:
        with open( "Product_list", "r+" ) as Product:
            Product_Str = str( Product.read( ) )
            Product_Dic = eval( Product_Str )
            Product_List = list( Product_Dic )
            for index, item in enumerate( Product_List ):
                print( index, item )
        user_choice = input( "请选择要买的商品ID>>>>>>:" )
        if user_choice.isdigit( ):
            user_choice = int( user_choice )
            if user_choice < len( Product_List ) and user_choice >= 0:
                p_item = Product_List[user_choice]
                if p_item[1] <= Salary:
                    shopping_list.append( p_item )
                    Salary -= p_item[1]

                    print( "添加商品\033[32;1m%s\033[0m成功, 你的余额还有\033[31;1m%s\033[0m" % (p_item, Salary) )
                else:
                    print( "对不起,你的余额只剩\033[31;1m%s\033[0m了,请重新选择或退出。" % Salary )
            else:
                print( "商品序号\033[32;1m%s\033[0m不存在,请重新输入。" % user_choice )
        elif user_choice == "q":
            print( "---------————————————\033[33;1m%s\033[0m的购物车 ---------————————————" % username )
            for p in shopping_list:
                print( p )
            print( "你的余额还剩\033[31;1m%s\033[0m元" % Salary )
            with open( "ShoppingList", "r" ) as Shopping:
                Shopping_Str = str( Shopping.read( ) )
                Shoping_Dic_All = eval( Shopping_Str )
                Shoping_Dic_All[username] = shopping_list
            UserFile_Dic[username][password] = Salary
            with open( "ShoppingList", "w" ) as Shoping_New:
                Shoping_New.write( str( Shoping_Dic_All ) )
            with open( "Userlist", "w" ) as UserFile_New:
                UserFile_New.write( str( UserFile_Dic ) )
            exit( )

# 定义函数.
def main():
    # 非第一次登陆购买.
    while Money["flag"]:
        print( "欢迎回来，\033[33;1m%s\033[0m ，您的购物车列表是：" % username )
        for p in shopping_list:
            print( p )
        print( "您的购物车还剩\033[31;1m%s\033[0m元" % Salary )
        Continue_Buy = str( input( "请问是否继续购买>>>>>>:" ) )
        if Continue_Buy == "y":
                Buy(Salary,shopping_list)
        elif Continue_Buy == "n":
            print("欢迎访问大中华购物网站，欢迎下次再来！")
            exit()
    else:
        Buy(Salary,shopping_list)

# 判定
if __name__ == "__main__":
    main()