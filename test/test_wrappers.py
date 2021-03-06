#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from .common_test_data import *

from reusables import reuse, unique, lock_it, time_it, queue_it


@reuse
def gen_func(a, b, c=None):
    return a, b, c


@unique(exception=OSError, error_text="WHY ME!")
def unique_function_1(a):
    return a


@unique(alt_return=33)
def unique_function_2(a):
    return a


@unique(wait=1)
def unique_function_3():
    return int(time.time())


class TestWrappers(BaseTestClass):

    def setUp(self):
        gen_func(reuse_reset=True)

    def test_reuse_basic(self):
        run1 = gen_func(1, 2, 3)
        assert run1 == (1, 2, 3)
        run2 = gen_func()
        assert run2 == (1, 2, 3)

    def test_reuse_failure_state(self):
        run1 = gen_func(1, 2, 3)
        assert run1 == (1, 2, 3)
        self.assertRaises(TypeError, gen_func, *[2,3,4,5,6,7])
        run2 = gen_func()
        assert run2 == (1, 2, 3)

    def test_reuse_view_saved(self):
        run1 = gen_func(1, 2, 3)
        assert run1 == (1, 2, 3)
        assert gen_func(reuse_view_cache=True)['args'] == (1, 2, 3)

    def test_reuse_update_args(self):
        run1 = gen_func(1, 2, 3)
        assert run1 == (1, 2, 3)
        assert gen_func(reuse_rep_args=[(1, 4)]) == (4, 2, 3)

    def test_unique(self):
        unique_function_1(1)
        unique_function_2(1)
        try:
            unique_function_1(1)
        except OSError as err:
            assert "WHY ME!" in str(err)

        assert unique_function_2(1) == 33

        a = unique_function_3()
        b = unique_function_3()
        c = unique_function_3()

        assert c > b > a

    def test_locker(self):
        import threading

        @lock_it()
        def func1():
            import time
            time.sleep(2)

        start = time.time()
        a = threading.Thread(target=func1)
        b = threading.Thread(target=func1)
        a.daemon = False
        b.daemon = False
        a.start()
        b.start()
        a.join()
        b.join()
        assert (time.time() - start) > 3

    def test_time(self):
        my_list = []

        @time_it(append=my_list)
        def func():
            return 5 + 3

        @time_it(log=True)
        def func2():
            return 7 + 3

        func()
        func2()

        assert len(my_list) == 1
        assert isinstance(my_list[0], float)

    def test_queue(self):
        try:
            import queue
        except ImportError:
            import Queue as queue

        q = queue.Queue()

        @queue_it(q)
        def func():
            return 5 + 3

        func()

        assert q.get() == 8



if __name__ == "__main__":
    unittest.main()