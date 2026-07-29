import re

email='parag@linkedln.com'

# expression='[a-z]+'

expression="[a-z\.]+" 


matches=re.findall(expression,email)

print(matches)


name=matches[0]

# domain=f"{matches[1]}.{matches[2]}"
domain=matches[1]
print(name)
print(domain)
