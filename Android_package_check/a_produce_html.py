# coding=utf-8

from bottle import template
from a_package_check import *


Task1, start_time_1, end_time_1, package_name, minSdkVersion, targetSdkVersion, versionCode, versionName = read_info()
Task2, start_time_2, end_time_2, package_size, type_sum = check_unzip()
Task3, start_time_3, end_time_3, files_sum = find_non_alpha()
Task4, start_time_4, end_time_4, uncompressed_sum = show_uncompressed()
Task5, start_time_5, end_time_5, size, duplicated_sum = find_duplicated()
Task6, start_time_6, end_time_6, limit_sum = limit_file()
Task7, start_time_7, end_time_7, total_methods, method_sum = method_count()
Task8, start_time_8, end_time_8, multi_lib, multilibrary_sum = check_multilibrary()
Task9, start_time_9, end_time_9, R_count, Field_counts, r_sum = r_count()

"""
使用bottle来动态生成html
"""

# 取出的值，放入html

info_check = [("HuXiu APP", Task1, start_time_1, end_time_1, package_name, versionName, versionCode, minSdkVersion, targetSdkVersion, "https://github.com/xinzhen2015")]
unzip_check = [(Task2, start_time_2, end_time_2, package_size, type_sum, "https://github.com/xinzhen2015")]
non_alpha = [(Task3, start_time_3, end_time_3, files_sum, "https://github.com/xinzhen2015")]
uncompressed_show = [(Task4, start_time_4, end_time_4, uncompressed_sum, "https://github.com/xinzhen2015")]
duplicated_find = [(Task5, start_time_5, end_time_5, duplicated_sum, size, "https://github.com/xinzhen2015")]
file_limit = [(Task6, start_time_6, end_time_6, limit_sum, "https://github.com/xinzhen2015")]
count_method = [(Task7, start_time_7, end_time_7, total_methods, method_sum, "https://github.com/xinzhen2015")]
multilibrary_check = [(Task8, start_time_8, end_time_8, multi_lib, multilibrary_sum, "https://github.com/xinzhen2015")]
count_r = [(Task9, start_time_9, end_time_9, R_count, Field_counts, r_sum, "https://github.com/xinzhen2015")]

# 定义想要生成的Html的基本格式
# 使用%来插入python代码

a_report = """

<html>
    <head><h1 style="text-align:center; color:#ffce37"> Android Apk Check </h1></head>
    <title>Android_Check</title>
    <body bgcolor="#333333">


     % for Title, Task1, start_time_1, end_time_1, package_name, versionName, versionCode, minSdkVersion, targetSdkVersion, link1 in items1:
        
        <meta charset="UTF-8">
        
        <h2 style="text-align:left; color:#ffce37"> {{Title.strip()}} 
        </h2>

        <p style="font-size:20;color:#4d70cb">Task 1（选看）: {{Task1}} 
        </p>
        

        <p style="font-size:20;color:#2ccb39">Start_Time: {{start_time_1}} 
        </p>

        <p style="font-size:20;color:#2ccb39">End_Time: {{end_time_1}} 
        </p>

        <p style="font-size:20;color:#cb103f">Package_Name: {{package_name}} 
        </p>

        <p style="font-size:20;color:#cb103f">VersionName: {{versionName}} 
        </p>

        <p style="font-size:20;color:#cb103f">VersionCode: {{versionCode}} 
        </p>

        <p style="font-size:20;color:#cb103f">MinSdkVersion: {{minSdkVersion}} 
        </p>

        <p style="font-size:20;color:#cb103f">TargetSdkVersion: {{targetSdkVersion}} 
        </p>
        
        <a href={{link1}}>Powered By XinZhen
        </a>
    %end
    
    
    
    
    % for Task2, start_time_2, end_time_2, package_size, type_sum, link2 in items2:
        
        <meta charset="UTF-8">
        
        <p style="font-size:20;color:#4d70cb">Task 2（选看）: {{Task2}} 
        </p>

        <p style="font-size:20;color:#2ccb39">Start_Time: {{start_time_2}} 
        </p>

        <p style="font-size:20;color:#2ccb39">End_Time: {{end_time_2}} 
        </p>

        <p style="font-size:20;color:#cb103f">Package_Size: {{package_size}} 
        </p>
        
        <p>
        <img src="o.png" width="900" height="600">
        </p>
        
        <PRE> <p style="font-size:22;color:#ff3d80"> {{type_sum}} 
        </p></PRE>
        
        <a href={{link2}}>Powered By XinZhen
        </a>
    %end
    
    
    
    
    % for Task3, start_time_3, end_time_3, files_sum, link3 in items3:
        
        <meta charset="UTF-8">
        
        <p style="font-size:20;color:#4d70cb">Task 3: {{Task3}} 
        </p>
        
        <p style="font-size:20;color:#cb8f10">（对于不含alpha通道的png文件，可以转成jpg格式来减少文件的大小。）</p>

        <p style="font-size:20;color:#2ccb39">Start_Time: {{start_time_3}} 
        </p>

        <p style="font-size:20;color:#2ccb39">End_Time: {{end_time_3}} 
        </p>

        <PRE> <p style="font-size:22;color:#ff3d80"> {{files_sum}} 
        </p></PRE>
        
        <a href={{link3}}>Powered By XinZhen
        </a>
    %end
    
    
    
    % for Task4, start_time_4, end_time_4, uncompressed_sum, link4 in items4:
        
        <meta charset="UTF-8">
        
        <p style="font-size:20;color:#4d70cb">Task 4: {{Task4}} 
        </p>
        
        <p style="font-size:20;color:#cb8f10">（建议压缩，以下类型的文件。）</p>

        <p style="font-size:20;color:#2ccb39">Start_Time: {{start_time_4}} 
        </p>

        <p style="font-size:20;color:#2ccb39">End_Time: {{end_time_4}} 
        </p>

        <PRE> <p style="font-size:22;color:#ff3d80"> {{uncompressed_sum}} 
        </p></PRE>
        
        <a href={{link4}}>Powered By XinZhen
        </a>
        
    %end
    
    
    
    % for Task5, start_time_5, end_time_5, size, duplicated_sum, link5 in items5:
        
        <meta charset="UTF-8">
        
        <p style="font-size:20;color:#4d70cb">Task 5: {{Task5}} 
        </p>
        
        <p style="font-size:20;color:#cb8f10">（建议去掉重复的文件。）</p>

        <p style="font-size:20;color:#2ccb39">Start_Time: {{start_time_5}} 
        </p>

        <p style="font-size:20;color:#2ccb39">End_Time: {{end_time_5}} 
        </p>
        
        <p style="font-size:20;color:#cb103f">Total_size: {{size}}
        </p>
        
        <PRE> 
        <p style="font-size:22;color:#ff3d80">{{duplicated_sum}} 
        </p>
        </PRE>
        
        <a href={{link5}}>Powered By XinZhen
        </a>
        
    %end
    
      
      
      % for Task6, start_time_6, end_time_6, limit_sum, link6 in items6:
        
        <meta charset="UTF-8">
        
        <p style="font-size:20;color:#4d70cb">Task 6: {{Task6}} 
        </p>
        
        <p style="font-size:20;color:#cb8f10">（建议压缩，超过10KB的文件。）</p>

        <p style="font-size:20;color:#2ccb39">Start_Time: {{start_time_6}} 
        </p>

        <p style="font-size:20;color:#2ccb39">End_Time: {{end_time_6}} 
        </p>
        
        <PRE> <p style="font-size:22;color:#ff3d80"> {{limit_sum}} 
        </p></PRE>
        
        <a href={{link6}}>Powered By XinZhen
        </a>
        
    %end
    
    
    
      % for Task7, start_time_7, end_time_7, total_methods, method_sum, link7 in items7:
        
        <meta charset="UTF-8">
        
        <p style="font-size:20;color:#4d70cb">Task 7（选看）: {{Task7}} 
        </p>

        <p style="font-size:20;color:#2ccb39">Start_Time: {{start_time_7}} 
        </p>

        <p style="font-size:20;color:#2ccb39">End_Time: {{end_time_7}} 
        </p>
        
        <p style="font-size:20;color:#cb103f">Total_methods: {{total_methods}} 
        </p>
        
        <PRE> <p style="font-size:22;color:#ff3d80"> {{method_sum}} 
        </p></PRE>
        
        <a href={{link7}}>Powered By XinZhen
        </a>
        
        
    %end
    
    
    
    % for Task8, start_time_8, end_time_8, multi_lib, multilibrary_sum, link8 in items8:

        <meta charset="UTF-8">
        
        <p style="font-size:20;color:#4d70cb">Task 8（选看）: {{Task8}} 
        </p>

        <p style="font-size:20;color:#2ccb39">Start_Time: {{start_time_8}} 
        </p>

        <p style="font-size:20;color:#2ccb39">End_Time: {{end_time_8}} 
        </p>
        
        <p style="font-size:20;color:#cb103f">Multi_lib: {{multi_lib}} 
        </p>
        
        <PRE> <p style="font-size:22;color:#ff3d80"> {{multilibrary_sum}} 
        </p></PRE>
        
        <a href={{link8}}>Powered By XinZhen
        </a>
        
        
    %end
    
    
    
      % for Task9, start_time_9, end_time_9, R_count, Field_counts, r_sum, link9 in items9:
        
        <meta charset="UTF-8">
        
        <p style="font-size:20;color:#4d70cb">Task 9: {{Task9}} 
        </p>
        
        <p style="font-size:20;color:#cb8f10">（编译之后，代码中对资源的引用都会优化成int常量，除了R.styleable之外，其他的R类其实都可以删除。）</p>

        <p style="font-size:20;color:#2ccb39">Start_Time: {{start_time_9}} 
        </p>

        <p style="font-size:20;color:#2ccb39">End_Time: {{end_time_9}} 
        </p>
        
        <p style="font-size:20;color:#cb103f">R_count: {{R_count}} 
        </p>
        
        <p style="font-size:20;color:#cb103f">Field_counts: {{Field_counts}} 
        </p>
        
        <PRE> <p style="font-size:22;color:#ff3d80"> {{r_sum}} 
        </p></PRE>
        
        <a href={{link9}}>Powered By XinZhen
        </a>
        
    %end
        
    
    </body>
</html>

"""

html = template(a_report,
                items1=info_check, items2=unzip_check, items3=non_alpha,
                items4=uncompressed_show, items5=duplicated_find,
                items6=file_limit, items7=count_method, items8=multilibrary_check, items9=count_r)

with open("a_report.html", 'w', encoding="utf-8") as f:
    f.write(html)



