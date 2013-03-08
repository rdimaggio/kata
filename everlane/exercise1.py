class Receiver():

    def single_char_check(self, item):
        return ord(item) >= ord('a') and ord(item) <= ord('j')

    def validate(self, validity_list):
        temp = []
        for item in validity_list:
            if item != 'valid':
                if self.single_char_check(item):
                    temp.append('valid')
                elif len(temp) >= 1 and item == 'Z' and \
                        (temp[-1] == 'valid' or
                         self.single_char_check(temp[-1])):
                    pass
                elif len(temp) >= 2 and item in ['M', 'K', 'P', 'Q'] and \
                        (temp[-1] == 'valid' or
                         self.single_char_check(temp[-1])) and \
                        (temp[-2] == 'valid' or
                         self.single_char_check(temp[-2])):
                    temp = temp[:-1]
                else:
                    temp.append(item)
            else:
                temp.append(item)
        return temp

    def receive(self, input_messages):
        output = []
        messages = input_messages.split(' ')
        for message in messages:
            validity_list = []
            for character in reversed(message):
                validity_list.append(character)
                validity_list = self.validate(validity_list)
            if len(validity_list) == 1 and validity_list[0] == 'valid':
                output.append([message, 'VALID'])
            else:
                output.append([message, 'INVALID'])
        return output



r = Receiver()
print r.receive('Qa Zj') == [['Qa', 'INVALID'], ['Zj', 'VALID']]
print r.receive('MZca') == [['MZca', 'VALID']]
print r.receive('Khfa') == [['Khfa', 'INVALID']]
print r.receive('aaa') == [['aaa', 'INVALID']]
print r.receive('MZZZZZaZZa') == [['MZZZZZaZZa', 'VALID']]
