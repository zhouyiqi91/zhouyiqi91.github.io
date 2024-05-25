---
layout: post
mathjax: true
description: ""
category: "python"
tags: ["pypi"]
---

## docs
- [How to modernize a setup.py based project?](https://packaging.python.org/en/latest/guides/modernize-setup-py-project/)
- [entry points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html)

## 同时使用setup.py和pyproject.toml,setup.py中指定entry points

测试无法实现。
```setup.py
import setuptools
from pathlib import Path

entrys = []
p = Path("sccore/cli/")
for fn in p.iterdir():
    name = fn.name
    if name != "__init__.py":
        cmd = name.replace('_','-')
        entrys.append(f'{cmd}=sccore.cli.{name}:main')
entry_dict = {
        'console_scripts': entrys,
}
print(entry_dict)

setuptools.setup(
    entry_points=entry_dict,
)
```

## share github action secrets
[How to use secrets in all repositories of a user github account?](https://stackoverflow.com/questions/70311091/how-to-use-secrets-in-all-repositories-of-a-user-github-account)

只有组织仓库可以共享。

## docker
github workflow创建的docker 仓库是private的，需要手动改为public，才能docker pull

## pypi镜像
[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)同步较为及时。修改`~/.config/pip/pip.conf`中的镜像地址。
```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```