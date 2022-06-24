import pathlib
import glob
import os

def tree(path, layer=0, is_last=False, indent_current=' '):
    if not pathlib.Path(path).is_absolute():
        path = str(pathlib.Path(path).resolve())

    # カレントディレクトリの表示
    dir = path.split('/')[::-1][0]
    if layer == 0:#ディレクトリの下に階層がない
        print('['+dir+']')
    else:#階層がある
        branch = '└' if is_last else '├'#最後なら'└'、最後じゃないないなら'├'
        print('{indent}{branch}[{dirname}]'.format(indent=indent_current, branch=branch, dirname=dir))
        #インデントを調整、'└''├'の表示、名前

    # 下の階層のパスを取得
    paths = [p for p in glob.glob(path+'/*') if os.path.isdir(p) or os.path.isfile(p)]
    def is_last_path(i):
        return i == len(paths)-1

    # 再帰的に表示
    for i, p in enumerate(paths):

        indent_lower = indent_current
        if layer != 0:
            indent_lower += '  ' if is_last else '│　'

        if os.path.isfile(p):
            branch = '└' if is_last_path(i) else '├'
            print('{indent}{branch}{filename}'.format(indent=indent_lower, branch=branch, filename=p.split('/')[::-1][0]))
        if os.path.isdir(p):
            tree(p, layer=layer+1, is_last=is_last_path(i), indent_current=indent_lower)

str = input()#標準入力
if str == "here":
    cwd = os.getcwd()
    tree(cwd)
else:
    tree(str)

#/Users/ngoktkt/Desktop/OneDrive/デスクトップ/Ktc/