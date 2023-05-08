from ting_file_management.priority_queue import PriorityQueue
import pytest


item_01 = {
            "nome_do_arquivo": "dale.txt",
            "qtd_linhas": 4,
            "linhas_do_arquivo": ['a', 'b', 'c', 'd', 'e'],
            }
item_02_arr = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
item_02 = {
            "nome_do_arquivo": "desdale.txt",
            "qtd_linhas": 10,
            "linhas_do_arquivo": item_02_arr,
            }
item_03 = {
            "nome_do_arquivo": "ehnois.txt",
            "qtd_linhas": 10,
            "linhas_do_arquivo": item_02_arr,
            }


def test_basic_priority_queueing():
    queue_test = PriorityQueue()
    queue_test.enqueue(item_02)
    queue_test.enqueue(item_01)
    assert len(queue_test) == 2
    assert queue_test.search(0) == item_01
    assert queue_test.dequeue() == item_01
    queue_test.enqueue(item_03)
    queue_test.dequeue() == item_02
    assert len(queue_test) == 1
    with pytest.raises(IndexError):
        queue_test.search(10)
