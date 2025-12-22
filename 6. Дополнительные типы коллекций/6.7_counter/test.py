from task_2 import count_occurences

def test_task_2():
    assert count_occurences('python', 'Python Conferences python training python events') == 3

def test_task_2_1():
    assert count_occurences('Java','Python C++ C# JavaScript Go Assembler') == 0