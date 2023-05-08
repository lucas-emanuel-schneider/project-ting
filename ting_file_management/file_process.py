from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    items = txt_importer(path_file)
    already_exists = []
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            already_exists.append(instance.search(index)["nome_do_arquivo"])
    if path_file not in already_exists:
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(items),
            "linhas_do_arquivo": items,
            }
        instance.enqueue(data)
        sys.stdout.write(str(data))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        data = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {data} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write("Posição inválida")
