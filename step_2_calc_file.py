t = int(0)

with open('step_2.txt') as f:
    for line in f:
        line = f.readline()
        sections = line.split()
        sign = sections[1]
        num1 = int(sections[2])
        num2 = int(sections[3])
        
        print(line)

        def add(num1, num2):
            return num1 + num2

        def subtract(num1, num2):
            return num1 - num2

        def multiply(num1, num2):
            return num1 * num2

        def divide(num1, num2):
           return num1 / num2

        if sign == '+':
            add(num1,num2)
            t = t + add(num1,num2)
        if sign == '-':
            subtract(num1,num2)
            t = t + subtract(num1,num2)
        if sign == '/':
            divide(num1,num2)
            t = t + divide(num1,num2)
        if sign == 'x':
            multiply(num1,num2)
            t = t + multiply(num1,num2)

        with open('step_2_exp.txt','w') as o:
            o.write(str(t))
