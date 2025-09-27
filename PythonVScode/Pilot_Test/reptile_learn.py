import requests
import json
# get post
# 利用post去抓取一些数据->返回的翻译数据
# 关于get的params和close
# 做一个自己的翻译器

# def postTest(text):
#     search=input('想查一个什么单词呢？')
#     print(text)
#     url='https://fanyi.baidu.com/sug'
#     dataP={
#         'kw':search
#     }
#     postD=requests.post(url,data=dataP)
#     print(postD.json())
    # print(json.loads(postD.text))
# 想知道请求的结果
    # print(postD.json()['errno'])
    
def fyTest(txt):
    # 1.目的
        # 输入查询的中文或英文可以返回结果
        # 对呈现形式考虑周全
    # 2.可能遇到的问题
        # 查不到？做个友好的处理
        # 捕错，对错误的处理很重要
    # 3.遇到问题应该怎么处理
        # 如何友好的处理错误，提升体验
    # 4.涉及大数据？高并发？（先不考虑）
    print(txt)
    userinput = input('请输入你要查询的内容：')
    url='https://fanyi.baidu.com/sug'
    dataP={
        'kw':userinput
    }
    result=requests.post(url,data=dataP)
    #print(result.json())
    # 如何响应内部值
    searchResult=result.json()
    for i in range(len(searchResult['data'])):
        print('第'+str(i+1)+'项解释：'+searchResult['data'][i]['v'])
    
if __name__ == "__main__":
    # postTest('测试post')
    fyTest('测试翻译器')