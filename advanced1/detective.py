import os
import platform
import sys


def inspect_environment():
  print('=' * 50)
  print('🕵️‍♂️ CONTAINER DETECTIVE REPORT 🕵️‍♂️')
  print('=' * 50)
  print(f'OS Platform: {platform.system()} {platform.release()}')
  print(f'Python Version: {sys.version.split()[0]}')
  print(f'Current User: {os.getenv("USER", "Unknown")}')
  print(f'Custom App Message: {os.getenv("SECRET_MESSAGE", "None")}')
  print(f'Build Environment: {os.getenv("BUILD_ENV", "Unknown")}')
  print('-' * 50)
  print('📂 Files inside /app directory:')
  print(os.listdir('.'))
  print('=' * 50)


if __name__ == '__main__':
  inspect_environment()