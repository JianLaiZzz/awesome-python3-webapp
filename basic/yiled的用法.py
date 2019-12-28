# def h():
#     print ('Wen Chuan'),
#     m = yield 5  # Fighting!
#     print (m)
#     d = yield 12
#     print  ('We are together!')
# c = h()
# next(c)  #相当于c.send(None)
# print(type(c))
# c.send('Fighting!')  #(yield 5)表达式被赋予了'Fighting!'


# def h():
#     print ('Wen Chuan'),
#     m = yield 5  # Fighting!
#     print (m)
#     d = yield 12
#     print(d)
#     print('We are together!')
#     yield 9
#
#
# c = h()
# m = next(c)  # m 获取了yield 5 的参数值 5
#
# d = c.send('Fighting!')  # d 获取了yield 12 的参数值12
# c.send("zhw")
# print('We will never forget the date', m, '.', d)
#
# print("ces")

# 学习代码
def ge():
    print("begin");
    m = yield 1;
    print(m)
    n = yield 2;
    print(n)
    yield 3;


g = ge();
begin = next(g)  # 应该是输出begin
print(begin)  # 1
g.send("zhw")  # 输出m等于none
