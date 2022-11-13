my_list = ['Communists', 'are', 'an', 'evil', 'force', 'that', 'needs', 'to', 'be', 'destroyed']
sent_analysis = {values: 0 for values in my_list}
def changeValues(self):
    for key, value in self.items():
        if value == 0:
            if key == 'evil':
                self[key] = 1
        if value == 0:
            if key == 'destroyed':
                self[key] = 1
# if a value from the loop is not present in the dict then the loop will not change or add dict elements
        if value == 0:
            if key == 'mare':
                self[key] = 1
    print(self)
changeValues(sent_analysis)