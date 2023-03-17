import re

# re.match()
# re.search()
# re.findall()
# re.split()
# re.sub()

text = r'1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily'
pattern = r'(\d)([A-Z][a-z]+)([A-Z][a-z]+)'

result = re.findall(pattern, text)
print(result)







