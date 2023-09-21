name = 'Python'

print( len(name) ) # Length of the string in java

print(name[0])

print(name[-1]) # last index
print(name[len(name)-1])
print(name[-2])

print(name[2:4]) # slicing the index "th"

s = "Java Programming Language"

print(s[5:16])

print(s[:4]) # Java

print(s[::-1]) # reverse order of the string after slicing

s = 'Python Programming'

# s5 = str(reversed(s))
s5 = s[::-1]
print(s5)

reversed(s5) # reversed
print(s5)

s6 = s5[7:]
print(s6)

s7 = 'CYDEO SCHOOL'

reversed(s7)
print(s7[::-1])


print('---------------------------------')

#print(help(str))
print(help(reversed))

print('---------------------------------')


s = 'python programming language'

print(s.capitalize()) # for first character to make upper case "Python programming language"

print(s.title()) # Python Programming Language

# strip = trim of Java


s = '             Python          '

print(s.strip()) # 'Python'

s = 'JAVA ABA'

print(s.index('A')) # 1
print(s.rindex('A')) # 7
print(s.index('AB')) # for additional place

s = 'Java Java'

s = s.replace('Java', 'Python')
# s = s.replace('Java', 'Python',1) if we want to replace only one
print(s)


s = 'C# C# Python'
s = s.replace('C#','Java',1)
print(s)

s = 'Java Java Java Python Python'
count_java = s.count('Java')
count_Python = s.count('Python')

print(count_java)
print(count_Python)


s = 'Java Java java JAVA Java Python Python'

count_java_case = s.lower().count('Java')
print(count_java_case)

s1 = 'java'
s2 = 'JAVA'
print( s1.lower() == s2.lower() ) # ignore case

s = 'Java'

print(s[0].islower())
print(s[0].isupper())

s = 'a'

print(s.isalpha())

s = '1'

print(s.isdigit())


s = 'Cydeo School'

print(s.istitle())


























