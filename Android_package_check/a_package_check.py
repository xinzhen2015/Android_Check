# coding = utf-8

"""
https://github.com/Tencent/matrix/wiki/Matrix-ApkChecker#matrix-apkchecker-的使用


APK Checker Usage

APK Checker can run independently in Jar (matrix-apk-canary-0.4.10.jar） mode, usage:

java -jar matrix-apk-canary-0.4.10.jar
Usages:
    --config CONFIG-FILE-PATH
or
    [--input INPUT-DIR-PATH] [--apk APK-FILE-PATH] [--unzip APK-UNZIP-PATH] [--mappingTxt MAPPING-FILE-PATH] [--resMappingTxt RESGUARD-MAPPING-FILE-PATH] [--output OUTPUT-PATH] [--format OUTPUT-FORMAT] [--formatJar OUTPUT-FORMAT-JAR] [--formatConfig OUTPUT-FORMAT-CONFIG (json-array format)] [Options]

Options:
-manifest
     Read package info from the AndroidManifest.xml.
-fileSize [--min DOWN-LIMIT-SIZE (KB)] [--order ORDER-BY ('asc'|'desc')] [--suffix FILTER-SUFFIX-LIST (split by ',')]
     Show files whose size exceed limit size in order.
-countMethod [--group GROUP-BY ('class'|'package')]
     Count methods in dex file, output results group by class name or package name.
-checkResProguard
     Check if the resguard was applied.
-findNonAlphaPng [--min DOWN-LIMIT-SIZE (KB)]
     Find out the non-alpha png-format files whose size exceed limit size in desc order.
-checkMultiLibrary
     Check if there are more than one library dir in the 'lib'.
-uncompressedFile [--suffix FILTER-SUFFIX-LIST (split by ',')]
     Show uncompressed file types.
-countR
     Count the R class.
-duplicatedFile
     Find out the duplicated resource files in desc order.
-checkMultiSTL  --toolnm TOOL-NM-PATH
     Check if there are more than one shared library statically linked the STL.
-unusedResources --rTxt R-TXT-FILE-PATH [--ignoreResources IGNORE-RESOURCES-LIST (split by ',')]
     Find out the unused resources.
-unusedAssets [--ignoreAssets IGNORE-ASSETS-LIST (split by ',')]
     Find out the unused assets file.
-unstrippedSo  --toolnm TOOL-NM-PATH
     Find out the unstripped shared library file.

"""
import os
import json
from time import sleep
import matplotlib.pyplot as plt

"""

load_dict[0]: Unzip the apk file to current project path.
load_dict[1]: Read package info from the AndroidManifest.xml.
load_dict[2]: Check if the apk handled by resguard.
load_dict[3]: Find out the non-alpha png-format files whose size exceed limit size in desc order.
load_dict[4]: Show uncompressed file types.
load_dict[5]: Find out the duplicated files.
load_dict[6]: Find out the unused assets.
load_dict[7]: Show files whose size exceed limit size in order.
load_dict[8]: Count methods in dex file, output results group by class name or package name.
load_dict[9]: Check if there are more than one library dir in the 'lib'.
load_dict[10]: Count the R class.


    每项 Task 都是 load_dict{} 中的一个元素

    task{"":1, "":2, ........"entries":[{}, {}, {}, .....]}

    解析每一项 Task

"""

os.popen("/Users/william/PycharmProjects/System/Mobile/Android/Android_Package_Check/android_check.sh")

sleep(10)


json_path = "/Users/william/PycharmProjects/System/Mobile/Android/Android_Package_Check/result/result.json"
with open(json_path, 'r') \
        as load_f:

    load_dict = json.load(load_f)


# 读取manifest的信息：从AndroidManifest.xml文件中读取apk的全局信息，如packageName、versionCode等。
def read_info():

    return \
        load_dict[1]["taskDescription"], \
        load_dict[1]["start-time"], \
        load_dict[1]["end-time"], \
        load_dict[1]["manifest"]["package"], \
        load_dict[1]["manifest"]["android:minSdkVersion"], \
        load_dict[1]["manifest"]["android:targetSdkVersion"], \
        load_dict[1]["manifest"]["android:versionCode"], \
        load_dict[1]["manifest"]["android:versionName"]


# 按文件大小排序列出apk中包含的文件：列出超过一定大小的文件，可按文件后缀过滤，并且按文件大小排序。
def check_unzip():

    unzip_package = []
    type_number = len(load_dict[0]["entries"])

    for i in range(type_number):

        # round(x/y, 2), 除法保留两位小数
        unzip_package.append("\n" + load_dict[0]["entries"][i]["suffix"]
                             + " == " +
                             str(round(load_dict[0]["entries"][i]["total-size"]/1024, 3)) + "KB")

        # print(unzip_package[i])

    type_sum = "".join(unzip_package[0:])

    # 画图
    file_name = []
    file_size = []

    for i in range(type_number):

        file_name.append(load_dict[0]["entries"][i]["suffix"])

    for i in range(type_number):
        file_size.append(load_dict[0]["entries"][i]["total-size"])

    new_file_name = [x + "\n" for x in file_name]

    plt.figure(figsize=(14, 9))
    # explode = [0, 0.1, 0, 0]  # 0.1 凸出这部分，
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    patches, l_text, p_text = plt.pie(
        x=file_size, labels=new_file_name, autopct='%3.1f %%',
        shadow=False, labeldistance=1.1, startangle=90, pctdistance=0.6)
    '''
    labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    shadow，饼是否有阴影
    startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    pctdistance，百分比的text离圆心的距离
    patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
    '''
    # 改变文本的大小，方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = 70
    for t in p_text:
        t.set_size = 70
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.savefig("/Users/william/PycharmProjects/System/Mobile/Android/Android_Package_Check/o.png")

    return \
        load_dict[0]["taskDescription"], \
        load_dict[0]["start-time"], \
        load_dict[0]["end-time"], \
        str(round(load_dict[0]["total-size"]/1024/1024, 2)) + " " + "MB", \
        type_sum


# 搜索不含alpha通道的png文件：对于不含alpha通道的png文件，可以转成jpg格式来减少文件的大小
def find_non_alpha():

    non_alpha = []
    files_number = len(load_dict[3]["files"])

    for i in range(files_number):

        non_alpha.append("\n\n" + load_dict[3]["files"][i]["entry-name"]
                         + " == " +
                         str(round(load_dict[3]["files"][i]["entry-size"]/1024, 3)) + "KB")
        print(non_alpha[i])

    files_sum = "".join(non_alpha[0:])

    return \
        load_dict[3]["taskDescription"], \
        load_dict[3]["start-time"], \
        load_dict[3]["end-time"], \
        files_sum


# 搜索未经压缩的文件类型：某个文件类型的所有文件都没有经过压缩，可以考虑是否需要压缩
def show_uncompressed():

    uncompressed = []
    files_number = len(load_dict[4]["files"])

    for i in range(files_number):

        uncompressed.append("\n\n" + load_dict[4]["files"][i]["suffix"]
                            + " == " +
                            str(round(load_dict[4]["files"][i]["total-size"]/1024/1024, 3)) + "MB")
        print(uncompressed[i])

    uncompressed_sum = "".join(uncompressed[0:])

    return \
        load_dict[4]["taskDescription"], \
        load_dict[4]["start-time"], \
        load_dict[4]["end-time"], \
        uncompressed_sum


# 搜索冗余的文件:对于两个内容完全相同的文件，应该去冗余
def find_duplicated():

    duplicated = []
    duplicated_sum_size = []
    duplicated_number = len(load_dict[5]["files"])
    size = 0

    for i in range(duplicated_number):

        duplicated.append("\n\n" + "MD5: " + load_dict[5]["files"][i]["md5"]
                          + "\nFile_Size: " +
                          str(round(load_dict[5]["files"][i]["size"]/1024, 3))
                          + "KB" + "\n")
        duplicated_sum_size.append(load_dict[5]["files"][i]["size"])

        size = size + duplicated_sum_size[i]

    size = str(round(size/1024, 3)) + "KB"

    files = []
    # 单独处理重复的文件路径
    for i in range(duplicated_number):

        unit_path_sun = " ======>>> ".join(load_dict[5]["files"][i]["files"])

        files.append(unit_path_sun)

    duplicated_sum = []

    for i in range(len(duplicated)):

        duplicated_sum.append(duplicated[i] + files[i])

    duplicated_sum_1 = "".join(duplicated_sum[0:])

    return \
        load_dict[5]["taskDescription"], \
        load_dict[5]["start-time"], \
        load_dict[5]["end-time"], \
        duplicated_sum_1, \
        size


# 按顺序显示大小超过限制大小的文件。
def limit_file():

    limit_ = []
    limit_number = len(load_dict[7]["files"])

    for i in range(limit_number):

        limit_.append("\n" + "Entry-name: " + load_dict[7]["files"][i]["entry-name"]
                      + "\nEntry_Size: " +
                      str(round(load_dict[7]["files"][i]["entry-size"]/1024, 3))
                      + "KB" + "\n")

    limit_sum = "".join(limit_[0:])

    # print(limit_sum)

    return \
        load_dict[7]["taskDescription"], \
        load_dict[7]["start-time"], \
        load_dict[7]["end-time"], \
        limit_sum


# 统计方法数:统计dex包含的方法数，并支持将输出结果按照类名(class)或者包名(package)来分组.
def method_count():

    method = []
    method_number = len(load_dict[8]["groups"])

    for i in range(method_number):
        method.append("\n" + "Name: " + load_dict[8]["groups"][i]["name"]
                      + "\nMethod-count: " +
                      str(load_dict[8]["groups"][i]["method-count"]) + "\n")

    method_sum = "".join(method[0:])
    # print(method_sum)

    return \
        load_dict[8]["taskDescription"], \
        load_dict[8]["start-time"], \
        load_dict[8]["end-time"], \
        load_dict[8]["total-methods"], \
        method_sum


# 检查是否包含多个ABI版本的动态库.
def check_multilibrary():

    multilibrary = []
    multilibrary_number = len(load_dict[9]["lib-dirs"])

    for i in range(multilibrary_number):
        multilibrary.append("\n" + "lib-dirs: " + load_dict[9]["lib-dirs"][i] + "\n")

    multilibrary_sum = "".join(multilibrary[0:])

    print(multilibrary_sum)

    return \
        load_dict[9]["taskDescription"], \
        load_dict[9]["start-time"], \
        load_dict[9]["end-time"], \
        load_dict[9]["multi-lib"], \
        multilibrary_sum


# 统计apk中包含的R类以及R类中的field count:
# 编译之后，代码中对资源的引用都会优化成int常量，除了R.styleable之外，其他的R类其实都可以删除
def r_count():

    r = []
    r_number = len(load_dict[10]["R-classes"])

    for i in range(r_number):
        r.append("\n" + "Name: " + load_dict[10]["R-classes"][i]["name"]
                      + "\nR-classes: " +
                      str(load_dict[10]["R-classes"][i]["field-count"]) + "\n")

    r_sum = "".join(r[0:])

    # print(r_sum)
    return \
        load_dict[10]["taskDescription"], \
        load_dict[10]["start-time"], \
        load_dict[10]["end-time"], \
        load_dict[10]["R-count"], \
        load_dict[10]["Field-counts"], \
        r_sum


if __name__ == '__main__':

    # check_unzip()

    # read_info()

    # find_non_alpha()

    # show_uncompressed()

    find_duplicated()

    # limit_file()

    # method_count()

    # check_multilibrary()

    # r_count()