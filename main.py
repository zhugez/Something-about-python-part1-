name = "Lý Ngọc Vũ"
txt = "Welcome to %s's world!"%(name)
print(txt)
index = int(input())
#print(name[index])
print(name[3:5])
print(name[3:])
del name
name = ['Lý Ngọc Vũ',
'Zhuge','Dezzhu','Zyueying']
print(name[index])

#list có thể được update theo cách thông thường
del name[1:3]
print(name)
#list có thể lồng nhau và được gọi theo cấp
#...

#Tuple dùng để lưu data dạng k đổi
day = ('Mon','Tues','Wed' ,'Thurs','Fri','Sat','Sun')
Vname = ('Lý Ngọc Vũ',)
#Tuple có thể lồng nhau và được gọi theo cấp

per = {
    'name': 'Lý Ngọc Vũ',
    'info': {
                'age': 22,
                'male': True,
                'status': 'alone',
                'hobby':'Guitar'
          }        
    }

print(per['info'])

#Chuyen doi chu thanh so 1-6
a = input()
dic = {
  'mot': 1,
  'hai': 2,
  'ba': 3,
  'bon': 4,
  'nam': 5,
  'sau': 6,
}
print(dic.get(a,'nothing'))

#Truyền vô số tham số vào hàm bằng cách *param 
def talksth():
  global testgl
  print("This is test func")

talksth()

#có thể định danh module bằng as
#nếu muốn load thêm module ở thư mục không cùng cấp or hệ thống thì  phải cấu hình trong sys.path sử dụng method append() 

import demopk.modules as md
md.say_hello() 

#1 package có thể chứa nhiều package khác nhưng phải tuân thủ nguyên tắc 1 package 1 __init__.py 

#cũng có thể lồng các khối exception lại với nhau. Dùng finally chắc chắn exception được thực thi cho dù try thế nào đi nữa
def sum(a,b):
  return a/b
try :
  print(sum(3,0))
except ZeroDivisionError:
  print("Không thể thực hiện phép tính này")
finally:
  print("Đã check")

# Muốn tạo một exception thì bắt buộc exception này phải kế thừa lớp Exception của Python

#class DemoEct(Exception):
#  def __init__(self,value):
#    print('ERROR: '+value)
 
#def sum(a, b):
#  if (b==0) :
#    raise DemoEct("BIsNotEqualToZero")
#    return a/b
# sum(a,0)
#del a,b
#Hàm xử lý chuỗi
# Hàm index giống hàm find nhưng sẽ gọi exception khi không tìm thấy . 

#lambda 

add = lambda a,b: a+b
print(add(2,4))
print(type(add))

#dùng map để duyệt qua các phần tử của list tuple dictionary,...

rs= map( lambda x: x * x, [1, 2, 3, 4])
print(list(rs))
del rs
#dùng filter để duyệt qua các phần tử mà thỏa mãn với điều kiện trong func
rs = filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 22])

print(list(rs))
