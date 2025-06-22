import os
folder = 'access'
file = 'admin.bat'
real_path = os.path.join(folder, file)
abs_path = os.path.abspath(real_path)
print(real_path)
print(abs_path)