import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise TypeError
        with open(path_file) as file:
            return file.read().split("\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    except TypeError:
        sys.stderr.write("Formato inválido")
