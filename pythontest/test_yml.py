import yaml

def test_yaml():
    with open("../data/calc.yml",encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        # print(datas)
        add_datas= datas.get("add")
        print(add_datas)
        add_P0_datas = add_datas['P0']
        print(add_P0_datas)
        add_P11_datas = add_datas['P1_1']
        print(add_P11_datas)



