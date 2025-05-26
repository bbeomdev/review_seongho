import nbformat

file_path = "mini_bert.ipynb"  # 파일명 또는 경로 수정
nb = nbformat.read(file_path, as_version=4)

if 'widgets' in nb.metadata:
    del nb.metadata['widgets']

nbformat.write(nb, file_path)
