# 1
print(r"hello\npython") #r可以显示原始字符串

# 2
print('''hello
      
      world''') #三引号可以开启文档格式

# 3
for i in range(5):
    print(f'第{i+1}个是{i}') #f可以让文本和变量同时运用

# 4
import codecs
text = u'你好'
print(text) #u可以表示字符本身，而不是他们的编码形式，可以打印中文

# 5
byte_string = b'hello' #b用于表示二进制数据，每个字符都是一个字节
print(byte_string)
string = byte_string.decode('utf-8') #解码
print(string)
byte_string = string.encode('utf-8') #编码
print(byte_string)