pywpm
=====

Windows Package Manager

#这是什么？
Ubuntu/Linux下都有软件包管理器，运行诸如`sudo apt-get install app`之类的命令可以很方便的安装应用，可是Windows呢？如何在Windows实现快速的安装和更新App？
这是一个小实验，探索如何在Windows快速的下载和更新软件。

#架构
* 所有App信息存放并托管在`app`目录
* 本地通过网络查询`app`目录
* 服务器运行爬虫自动更新`app`目录
* 本地通过命令行下载/更新软件(Windows程序安装还是要操作GUI)

#问题
* App信息似乎需要耗费大量人工……（如果有一个公开的协议，每个App发布页面源代码都提供元信息多好Orz）
* 作者比较懒

#TO DO
* 本地管理软件
* 服务器自动更新程序
* 把常用优秀App信息完成