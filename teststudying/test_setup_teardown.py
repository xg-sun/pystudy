#m模块级别
def setup_module():
    print("资源准备：setup module")

def teardown_module():
    print("资源准备：teardown module")


def test_a():
    print("case1")
    # pass

def setup_function():
    print("资源准备：setup function")

def teardow_function():
    print("资源销毁：teardow function")


class TestDemo:

    # 执行类 前后分别执行setup_class teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    #  每个类里面的方法前后分别执行 setup teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")

    def teardown(self):
        print("TestDemo teardown")

class TestDemo1:

    # 执行类 前后分别执行setup_class teardown_class
    def setup_class(self):
        print("TestDemo1 setup_class")

    def teardown_class(self):
        print("TestDemo1 teardown_class")

    #  每个类里面的方法前后分别执行 setup teardown
    def setup(self):
        print("TestDemo1 setup")

    def teardown(self):
        print("TestDemo1 teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")