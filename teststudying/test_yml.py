import yaml

def test_yaml():
    with open("./data/calc.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
