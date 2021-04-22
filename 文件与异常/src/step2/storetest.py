from store import store
from store import is_prime

name = input()
store()
with open(name,'r',encoding='utf-8') as file:
    print(file.read())    