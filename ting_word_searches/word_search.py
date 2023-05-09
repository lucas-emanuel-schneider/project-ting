from ting_file_management.queue import Queue


def create_occurrences(word, index, line, search_type=False):
    if word.lower() in line.lower():
        if search_type:
            return {'linha': index + 1, "conteudo": line}
        else:
            return {'linha': index + 1}
    return None


def get_search_result(word, instance, bool=False):
    result = []
    for item in range(len(instance)):
        search_result = instance.search(item)
        obj_response = {
            "palavra": word,
            "arquivo": search_result['nome_do_arquivo'],
            "ocorrencias": []
        }
        for index, line in enumerate(search_result['linhas_do_arquivo']):
            item = create_occurrences(word, index, line, bool)
            if item:
                obj_response['ocorrencias'].append(item)
        if len(obj_response['ocorrencias']) > 0:
            result.append(obj_response)
        return result


def exists_word(word: str, instance: Queue):
    return get_search_result(word, instance)


def search_by_word(word: str, instance: Queue):
    return get_search_result(word, instance, True)
