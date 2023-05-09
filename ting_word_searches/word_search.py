from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    result = []
    for item in range(len(instance)):
        search_result = instance.search(item)
        obj_response = {
            "palavra": word,
            "arquivo": search_result['nome_do_arquivo'],
            "ocorrencias": []
        }
        for index, line in enumerate(search_result['linhas_do_arquivo']):
            if word.lower() in line.lower():
                obj_response['ocorrencias'].append({'linha': index + 1})
        if len(obj_response['ocorrencias']) > 0:
            result.append(obj_response)
        return result


def search_by_word(word: str, instance: Queue):
    result = []
    for item in range(len(instance)):
        search_result = instance.search(item)
        obj_response = {
            "palavra": word,
            "arquivo": search_result['nome_do_arquivo'],
            "ocorrencias": []
        }
        for index, line in enumerate(search_result['linhas_do_arquivo']):
            if word.lower() in line.lower():
                obj_response['ocorrencias'].append(
                    {'linha': index + 1, "conteudo": line}
                    )
        if len(obj_response['ocorrencias']) > 0:
            result.append(obj_response)
        return result
