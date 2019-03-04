<a href="https://travis-ci.org/onevcat/FengNiao"><img src="https://img.shields.io/travis/onevcat/FengNiao/master.svg"></a>
<a href="https://swift.org/package-manager/"><img src="https://img.shields.io/badge/swift-4.0-brightgreen.svg"/></a>
<a href="https://swift.org/package-manager/"><img src="https://img.shields.io/badge/SPM-ready-orange.svg"></a>
<a href="https://raw.githubusercontent.com/onevcat/Kingfisher/master/LICENSE"><img src="https://img.shields.io/cocoapods/l/Kingfisher.svg?style=flat"></a>
<a href="https://swift.org/package-manager/"><img src="https://img.shields.io/badge/platform-macos%20|%20Linux-blue.svg"/></a>
<a href="https://codecov.io/gh/onevcat/Hedwig"><img src="https://codecov.io/gh/onevcat/Hedwig/branch/master/graph/badge.svg"/></a>
</p>

<p align="center">
<img src="https://github.com/xinzhen2015/Android_Check/blob/master/Android_package_check/屏幕快照%202019-03-04%20下午5.25.09.png" alt="Android_Check" title="Android_Check"/>
</p>



# Android_Check
Analyse the APK package, give suggestions of reducing the APK's size; Compare two APK and find out the most significant increment on size.

针对 APK 安装包的分析检测工具，根据一系列设定好的规则，检测 APK 是否存在特定的问题，并输出较为详细的检测结果报告，用于分析排查问题以及版本追踪.


# 用法


### 1、下载

jar 包：https://jcenter.bintray.com/com/tencent/matrix/matrix-apk-canary/0.4.10/matrix-apk-canary-0.4.10.jar  

### 2、配置config

```json
{
    "--apk":"apk_path",
    "--output":"result_path/result",
    "--format":"mm.html,mm.json",

    "--formatConfig":[
        {
            "name":"-countMethod",
            "group":[
                {
                    "name":"Android System",
                    "package":"android"
                },
                {
                    "name":"java system",
                    "package":"java"
                },
                {
                    "name":"com.test",
                    "package":"com.test"
                }
            ]
        }
    ],

    "options":[
        {
            "name":"-manifest"
        },
        {
            "--suffix":"png, jpg, jpeg, gif, arsc",
            "--min":"10",
            "name":"-fileSize",
            "--order":"desc"
        },
        {
            "--group":"package",
            "name":"-countMethod"
        },
        {
            "name":"-checkResProguard"
        },
        {
            "--min":"10",
            "name":"-findNonAlphaPng"
        },
        {
            "name":"-checkMultiLibrary"
        },
        {
            "--suffix":"png, jpg, jpeg, gif, arsc",
            "name":"-uncompressedFile"
        },
        {
            "name":"-countR"
        },
        {
            "name":"-duplicatedFile"
        },
        {
            "name":"-unusedAssets",
            "--ignoreAssets":[
                "*.so"
            ]
        }
    ]
}
```
```
注意：--output 参数，路径的最后是文件名，不写文件名将生成 .json、 .html 文件
```
### 3、在终端执行 

```
java -jar jar_path --config congfig_path
```

```
生成，result.json 文件。
```
### 4、修改 a_package_check.py 中的 json_path

```python
json_path = "json_path"
with open(json_path, 'r') \
        as load_f:

    load_dict = json.load(load_f)
```

### 5、执行 a_produce_html.py 生成漂亮报告
