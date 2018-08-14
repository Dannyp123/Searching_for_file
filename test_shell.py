import shell
from bcca.test import (should_print, with_inputs, fake_file)


@fake_file({
    'shell.py':
    '''hello
hello world
goodbye
goodbye world
hello goodbye
'''
})
@with_inputs('shell.py', 'bye')
@should_print
def test_example1(output):
    shell.main()
    assert output == '''
File: shell.py
Search For: bye

3: goodbye

4: goodbye world

5: hello goodbye
'''


@fake_file({'bar.txt': '''hello
GOODBYE'''})
@with_inputs('bar.txt', 'o')
@should_print
def test_is_case_sensitive(output):
    shell.main()

    assert output == '''
File: bar.txt
Search For: o

1: hello

2: GOODBYE
'''


@fake_file({'classwork.py': '''hello
hello world
hello daniel'''})
@with_inputs('classwork.py', 'llo')
@should_print
def test_example2(output):
    shell.main()

    assert output == '''
File: classwork.py
Search For: llo

1: hello

2: hello world

3: hello daniel
'''
