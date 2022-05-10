# 按 Shift+F10 执行或将其替换为您的代码。
# 按 Ctrl+F8 切换断点。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from WordsCard.WordList import WordList


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    in_str = input('Enter: ')
    spl_str = in_str.split()
    nl = WordList(spl_str[0])

    nl.add_word(spl_str[1], spl_str[2], spl_str[3], spl_str[4])
    nl.print_list()

    file_name = input()
    nl.save_list(file_name)

    #Input: 1 1 emperor n.皇帝;君主 0