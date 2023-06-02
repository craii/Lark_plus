# - * - coding:utf-8 - * -
#  作者：Elias Cheung
#  编写时间：2023/5/31  下午4:46
import werobot

robot = werobot.WeRoBot(token='tokenhere')

@robot.handler
def hello(message):
    return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()