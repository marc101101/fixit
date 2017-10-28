import json

class GetBestPrice(Exception):
    data =  [['Apple', 'iPhone 5', 'Display', '60'],
            ['Apple', 'iPhone 5', 'Buttons', '35'],
            ['Apple', 'iPhone 5', 'Akku', '30'],
            ['Apple', 'iPhone 5', 'Ladebuchse', '35'],
            ['Apple', 'iPhone 5S', 'Display', '80'],
            ['Apple', 'iPhone 5S', 'Buttons', '35'],
            ['Apple', 'iPhone 5S', 'Akku', '30'],
            ['Apple', 'iPhone 5S', 'Ladebuchse', '35'],
            ['Apple', 'iPhone SE', 'Display', '90'],
            ['Apple', 'iPhone SE', 'Buttons', '45'],
            ['Apple', 'iPhone SE', 'Akku', '40'],
            ['Apple', 'iPhone SE', 'Ladebuchse', '45'],
            ['Apple', 'iPhone 6', 'Display', '110'],
            ['Apple', 'iPhone 6', 'Buttons', '45'],
            ['Apple', 'iPhone 6', 'Akku', '40'],
            ['Apple', 'iPhone 6', 'Ladebuchse', '45'],
            ['Apple', 'iPhone 6S', 'Display', '150'],
            ['Apple', 'iPhone 6S', 'Buttons', '45'],
            ['Apple', 'iPhone 6S', 'Akku', '40'],
            ['Apple', 'iPhone 6S', 'Ladebuchse', '45'],
            ['Apple', 'iPhone 7', 'Display', '230'],
            ['Apple', 'iPhone 7', 'Buttons', '70'],
            ['Apple', 'iPhone 7', 'Akku', '60'],
            ['Apple', 'iPhone 7', 'Ladebuchse', '70'], ['Samsung', 'S5', 'Display', '130'], ['Samsung', 'S5', 'Buttons', '80'], ['Samsung', 'S5', 'Akku', '20'], ['Samsung', 'S5', 'Ladebuchse', '70'], ['Samsung', 'S6', 'Display', '180'], ['Samsung', 'S6', 'Buttons', '70'], ['Samsung', 'S6', 'Akku', '60'], ['Samsung', 'S6', 'Ladebuchse', '80'], ['Samsung', 'S7', 'Buttons', '70'], ['Samsung', 'S7', 'Akku', '70'], ['Samsung', 'S7', 'Ladebuchse', '90'], ['Samsung', 'S8', 'Akku', '90'], ['Samsung', 'S8', 'Ladebuchse', '90'], ['Samsung', 'A3 (2016)', 'Display', '130'], ['Samsung', 'A3 (2016)', 'Buttons', '60'], ['Samsung', 'A3 (2016)', 'Akku', '60'], ['Samsung', 'A3 (2016)', 'Ladebuchse', '80'], ['Samsung', 'A5 (2016)', 'Display', '150'], ['Samsung', 'A5 (2016)', 'Buttons', '60'], ['Samsung', 'A5 (2016)', 'Akku', '60'], ['Samsung', 'A5 (2016)', 'Ladebuchse', '80'], ['Huawei', 'P8', 'Display', '90'], ['Huawei', 'P8', 'Buttons', '40'], ['Huawei', 'P8', 'Akku', '40'], ['Huawei', 'P8', 'Ladebuchse', '50'], ['Huawei', 'P9', 'Display', '100'], ['Huawei', 'P9', 'Buttons', '50'], ['Huawei', 'P9', 'Akku', '50'], ['Huawei', 'P9', 'Ladebuchse', '60'], ['Huawei', 'P9 Lite', 'Display', '90'], ['Huawei', 'P9 Lite', 'Buttons', '40'], ['Huawei', 'P9 Lite', 'Akku', '40'], ['Huawei', 'P9 Lite', 'Ladebuchse', '50'], ['Huawei', 'P10', 'Display', '180'], ['Huawei', 'P10', 'Buttons', '70'], ['Huawei', 'P10', 'Akku', '70'], ['Huawei', 'P10', 'Ladebuchse', '80'], ['Huawei', 'P10 Lite', 'Display', '120'], ['Huawei', 'P10 Lite', 'Buttons', '60'], ['Huawei', 'P10 Lite', 'Akku', '60'], ['Huawei', 'P10 Lite', 'Ladebuchse', '60'], ['Huawei', 'Mate 9', 'Display', '140'], ['Huawei', 'Mate 9', 'Buttons', '60'], ['Huawei', 'Mate 9', 'Akku', '60'], ['Huawei', 'Mate 9', 'Ladebuchse', '70'], ['Sony', 'Z3', 'Display', '120'], ['Sony', 'Z3', 'Buttons', '40'], ['Sony', 'Z3', 'Akku', '40'], ['Sony', 'Z3', 'Ladebuchse', '60'], ['Sony', 'Z3 Compact', 'Display', '120'], ['Sony', 'Z3 Compact', 'Buttons', '40'], ['Sony', 'Z3 Compact', 'Akku', '40'], ['Sony', 'Z3 Compact', 'Ladebuchse', '60'], ['Sony', 'Z5', 'Display', '130'], ['Sony', 'Z5', 'Buttons', '40'], ['Sony', 'Z5', 'Akku', '40'], ['Sony', 'Z5', 'Ladebuchse', '50'], ['Sony', 'Z5 Compact', 'Display', '130'], ['Sony', 'Z5 Compact', 'Buttons', '40'], ['Sony', 'Z5 Compact', 'Akku', '40'], ['Sony', 'Z5 Compact', 'Ladebuchse', '50'], ['Sony', 'XA', 'Display', '110'], ['Sony', 'XA', 'Buttons', '50'], ['Sony', 'XA', 'Akku', '40'], ['Sony', 'XA', 'Ladebuchse', '50'],
            ['Sony', 'XZ', 'Display', '180'],
            ['Sony', 'XZ', 'Buttons', '80'],
            ['Sony', 'XZ', 'Akku', '60'],
            ['Sony', 'XZ', 'Ladebuchse', '80']]

    def getPrice(self, brand, model, damaged, long_response=False):
        message = {}
        for element in self.data:
            if((element[0] == brand) and (element[1] == model) and (element[2] == damaged)):
                if(long_response == 'true'):
                    response = {"message": {"text": "Die Reperatur Ihres Smartphones kostet 40 €."}}
                else:
                    response = {"message": {"text": "40"}}
                message['message'] = response
                json_data = json.dumps(message)
                return json_data
        raise Exception('Not Found')
