import os
import re
import shutil

def replace_in_file(file_path, old_name, new_name):
    """在指定文件中替换旧包名"""
    with open(file_path, 'r') as f:
        content = f.read()
    content = content.replace(old_name, new_name)
    with open(file_path, 'w') as f:
        f.write(content)

def rename_package(old_name, new_name):
    """修改包名"""
    # 1. 修改 setup.py 文件
    replace_in_file('setup.py', old_name, new_name)

    # 2. 修改包目录名称
    os.rename(old_name, new_name)

    # 3. 修改 __init__.py 文件
    if os.path.exists(f'{new_name}/__init__.py'):
        replace_in_file(f'{new_name}/__init__.py', old_name, new_name)

    # 4. 修改代码中所有包引用
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(('.py', '.txt', '.md')):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, old_name, new_name)

    # 5. 修改测试代码中的包引用
    if os.path.exists('tests'):
        for root, _, files in os.walk('tests'):
            for file in files:
                if file.endswith(('.py', '.txt', '.md')):
                    file_path = os.path.join(root, file)
                    replace_in_file(file_path, old_name, new_name)

    # 6. 修改文档中的包引用
    if os.path.exists('docs'):
        for root, _, files in os.walk('docs'):
            for file in files:
                if file.endswith(('.rst', '.md')):
                    file_path = os.path.join(root, file)
                    replace_in_file(file_path, old_name, new_name)

    # 7. 修改其他相关文件
    # ... (根据你的项目需要添加其他修改)

    # 8. 删除旧的包目录
    # shutil.rmtree(f'{old_name}') # 谨慎使用，确保删除的是旧包目录


rename_package("aktools", "byteapp_akt")
