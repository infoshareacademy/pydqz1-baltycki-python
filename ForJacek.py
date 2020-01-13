import Data_generator as dg

newname = dg.generate_name(ptf=False)
print(newname)
newsurname = dg.generate_surname(ptf=False)
print(newsurname)
newnick = dg.generate_nick(ptf=True)
print(newnick)
newaddres = dg.generate_address(ptf=True)
print(newaddres)
newmail = dg.generate_email(ptf=False)
print(newmail)

print(type(newaddres))