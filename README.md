# 说明
Claude AI接入飞书Lark
## BASIC
> **本项目基于：**
> - [Python Slack SDK](https://github.com/SlackAPI/python-slack-sdk#installation)
> - [claude-in-slack-api](https://github.com/yokonsan/claude-in-slack-api/tree/master)


## 使用方法
### 获取SLACK_USER_TOKEN 以及 CLAUDE_BOT_ID
请参考【[claude-in-slack-api](https://github.com/yokonsan/claude-in-slack-api/tree/master)】作者的在知乎发布的教程：
> [Claude｜媲美ChatGPT，如何免费接入到个人服务](https://zhuanlan.zhihu.com/p/627485689)

也可查看图片备份：[备份](https://imgur.com/a/kkJubIV)

### 获取飞书**App ID**及对应的**App Secret**及进行必要配置
进入[飞书app官网](https://open.feishu.cn/app)后，按照下述步骤进行
1. 创建【**企业自建应用**】 </br>
  ![](https://i.imgur.com/aq2bFRy.png)

2. 点击你的应用进入应用详情后
  ![](https://i.imgur.com/wXqYdwF.png)
  进入页面后即可在页面顶部获取到所需的**App ID**及对应的**App Secret**。记录对应的内容后，继续以下步骤。
  
3. 点击添加应用能力，选择机器人并进行简单配置
  ![](https://i.imgur.com/PzaOa46.png)
  ![](https://i.imgur.com/ri5PVuJ.png)
4. 点击事件订阅，之后按照下述顺序进行操作：
  ![](https://i.imgur.com/YrEMLXJ.png)
  - 购买一个服务器：[阿里云](http://www.aliyunecs.cn/qingliang.asp) 、 [腾讯云](https://cloud.tencent.com/product/lighthouse) 均可
  - 绑定域名，以 ```example.com```为例：[阿里云](https://help.aliyun.com/document_detail/59080.html)、[腾讯云](https://cloud.tencent.com/document/product/1207/81332)
  - 开启防火墙端口：[阿里云](https://developer.aliyun.com/article/1209355)、[腾讯云](https://blog.csdn.net/yunweifun/article/details/130894787) 注意，仓库中的
    ```challenge.py``` 使用的端口是```6767```，可根据个人喜好更换端口号，但注意更改后在对应的云后台开启同样的端口
  - 将仓库中的```challenge.py```上传到你的服务器并运行后，点击【请求地址配置】，填写```http://example.com:6767```并进行验证；
  ![](https://i.imgur.com/fZF5PCC.png)
    > 期间可能需要更换服务器端的python版本，此项目python版本为```3.7.7```，可参考[腾讯云轻量应用服务器CentOS7.6如何更新或安装python3](https://blog.csdn.net/shy0530/article/details/127793111)
    > 然后在服务器端运行以下命令```pip install flask```、```pip install requests```、```pip install json (可选)```

5. 验证成功后【添加事件】

  ![](https://i.imgur.com/Gm17L7L.png)
  
  > 期间部分事件的的开启可能需要你所在的企业的飞书管理员审核,切换账号或要求对应人员审核即可
  > 后续可根据自身需要开启更多【事件订阅】或【权限】
  e.g..权限示例：
  ![](https://i.imgur.com/chWMnKM.png)
  
6. 点击【版本管理与发布】并创建版本

  ![](https://i.imgur.com/9mUPqU7.png)
  
7. 填写版本信息并添加可用范围，如仅允许自己使用则仅选自己即可

  ![](https://i.imgur.com/zDcN64V.png)

8. 根据上述步骤中获取的信息，修改```.env.bak```,中对应的字段(*图中为含中文的字段，格式可参考api部分*)，并保存为```.env```文件

  ![](https://i.imgur.com/1zC0C1s.png)

9. 将本项目上传至服务器后，确保目录结构中需含有```.env```文件（假设所有文件已上传至服务器的```/usr/app/Slack_plus/```）：
  
  ![](https://i.imgur.com/ebo2CMA.png)
  
11. 使用ssh软件(如**terminus**)登陆服务器终端后依次运行下述命令
- ```cd /usr/app/Slack_plus/```
- ```pip install -r requirements.txt```
---
- ```nohup python3 -u claude.py```
- ```nohup python3 -u App_Entry.py```
> ！注意 ！：这两条命令只是为了尽快看到效果，实际使用时请改用这个方式部署【[Flask 应用部署到腾讯云的轻量应用服务器](https://zhuanlan.zhihu.com/p/465772158)】：
---

### 部署完成查看效果
> 登陆飞书，开始使用即可

![](https://i.imgur.com/zazDK9d.png)
![](https://i.imgur.com/DLU8w1A.png)
