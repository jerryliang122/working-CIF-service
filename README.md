# working-CIF-service
这是一个简易的发送邮件的程序，其内核是python

## 配置文件使用方式
所有的配置文件都将会集成在init_conf中，如果你第一次使用程序。init_conf将会直接转换conf.

如果你已经使用过该程序。请注意未来更新的版本。作者并未使用类似自动更新的手段来更新conf中的一部分内容。请按照每个release 的操作来更新你的conf的配置文件。


## 配置文件使用方式

<details>
  <summary>email配置文件</summary>
  
  | 字段名 | 介绍 |
  | ----- | ----- |
  | name | 这是发送邮件时显示在邮件头上的昵称 |
  | smtp_server | 这是发送邮件的服务器 |
  | smtp_port | 这是发送邮件服务器的端口，一般不需要修改国内基本都是465 |
  | smtp_user | 这是你的发送账号 |
  | smtp_password | 这是你的发送账号的密码 |
</details>

<details>
  <summary>init配置文件</summary>

  | 字段名 | 介绍 |
  | ----- | ----- |
  |prefix | 自动标签的前缀|

</details>

<details>
  <summary>port配置文件</summary>
  这个文件有三个部分组成，分别是
  地区，国家，港口
  我们可以举一个例子。假设这个文件中只有印巴地区
  
    ```
    {
        "印巴地区": {
            "印度": [
                "印度尼西亚",
                "印度"
            ]
        }
    }
    ```
    如果我想增加一个国家，比如巴基斯坦。我可以这样写
    ```
    {
        "印巴地区": {
            "印度": [
                "印度尼西亚",
                "印度"
            ],
            "巴基斯坦": [
            ]
        }
    }
    ```
    如果我要在巴基斯坦中增加一个港口，比如卡拉奇。我可以这样写
    ```
    {
        "印巴地区": {
            "印度": [
                "印度尼西亚",
                "印度"
            ],
            "巴基斯坦": [
                "卡拉奇"
            ]
        }
    }
    ```
    如果我要增加北美。我可以这样写
    ```
    {
        "印巴地区": {
            "印度": [
                "印度尼西亚",
                "印度"
            ],
            "巴基斯坦": [
                "卡拉奇"
            ]
        },
        "北美": {
        }
    }
    ```
    以此类推。
</details>

请注意，该代码中会默认插入一张图片。你需要在conf文件夹中放入一张signature.jpg 程序才会正常工作
## 使用方式
1, 写入代理邮件地址

当你完成了PORT的配置后。你可以下拉选择代理面板中的框。

示例：
代理名称是AAA 港口是三宝垄。

即你在选择代理中找到港口三宝垄。在添加代理信息的面板中 写入名称为AAA，下面的大框中一行一个邮件地址，然后点击添加即可。

刷新一下港口。你就可以看到AAA这个代理了。

2, 写入询价信息
把询价信息填写进入询价信息面板，编号填写进发送邮件的询价编号中。点击预览即可查看邮件预览。点击发送即可发送邮件。

