import re


class Attribute:
    def __init__(self, label, regex):
        self.label = label
        self.regex = regex
        self.value = None

    def __repr__(self):
        return f'{self.label} {self.value}'

    def apply(self, text):
        matches = re.findall(self.regex, text)
        if matches:
            self.value = matches[0]


