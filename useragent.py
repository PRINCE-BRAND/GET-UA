import os, sys
os.system('clear')
os.system('git pull')
try:
    __import__("useragent","ak","ug").main()
except Exception as e:
    exit(str(e))
