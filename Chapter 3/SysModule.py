import sys
import os
import subprocess

# print(sys.byteorder)
#
# print(sys.getsizeof(1))
#
# print(sys.platform)
#
# if sys.version_info.major < 3:
#     print("You need to update your Python Version")
#
# elif sys.version_info.major < 7:
#     print("You are running the latest version of Python")
#
# else:
#     print("All is good")

# print(os.getcwd())
#
# os.chdir('/temp')
# print(os.getcwd())
#
# os.environ.get('LOGLEVEL')
# os.environ['LOGLEVEL'] = 'DEBUG'
# print(os.environ.get('LOGLEVEL'))
#
# print(os.getlogin())
#
# win_env_vars = os.environ
#
# print(dict(win_env_vars))

def say_it():
    greeting = 'Hello'
    target = 'Joe'
    message =f'{greeting} {target}'
    print(message)

if __name__=='__main__':
    say_it()