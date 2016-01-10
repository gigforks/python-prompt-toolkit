from JumpScale import j

j.do.execute("python3 setup.py build")

j.do.execute("rm -rf %s/prompt_toolkit*"%j.do.getPythonLibSystem())
j.do.copyTree("build/lib/", dest=j.do.getPythonLibSystem(), keepsymlinks = False, deletefirst = False, overwriteFiles=True,rsync=False,recursive=True)


install_requires = ['pygments','six>=1.9.0','wcwidth']

for item in install_requires:
    j.do.execute("pip3 install %s --upgrade"%item)
