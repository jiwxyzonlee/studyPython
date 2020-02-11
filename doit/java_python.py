#Q7

f = open("C:/doit/test.txt", 'w')
body = "Life is too short\you need java"
f.write(body)
f.close()

f = open("C:/doit/test.txt", 'r')
data = f.read()
print(data)
f.close()

body =body.replace("java", "python")

f = open('test.txt', 'w')
f.write(body)
f.close()

f = open("C:/doit/test.txt", 'r')
data = f.read()
print(data)
f.close()
