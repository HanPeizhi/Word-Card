# 按 Shift+F10 执行或将其替换为您的代码。
# 按 Ctrl+F8 切换断点。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from WordsCard.WordList import WordList


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    wln = input("Input the Word List number: ")
    nl = WordList(wln)

    for i in range(4):
        in_str = input('Enter a word: ')
        spl_str = in_str.split()

        nl.add_word(spl_str[0], spl_str[1], spl_str[2], spl_str[3])
        nl.print_list()

    flag  = 1
    while int(flag):
        nl.review_word()
        flag = input("Flag: ")


    # file_name = input()
    # nl.save_list(file_name)

    #Input:
    #1 emperor n.皇帝;君主 0
    #1 exact a.精确的，准确的 1
    #1 traditional a.传统的，惯例的；口传的，传说的 1
    #1 lack n./vt.缺乏，不足，没有 1