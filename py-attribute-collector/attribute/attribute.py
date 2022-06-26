import re


class Attribute:
    def __init__(self, label, regex):
        self.label = label
        self.key = self.label.strip().lower().replace(" ", '_').replace(".", "")
        self.regex = regex
        self.value = None

    def __repr__(self):
        return f'{self.label} {self.value}'

    def apply(self, text):
        matches = re.findall(self.regex.replace(" ", " ?"), text)
        if matches:
            self.value = matches[0]

        return self.value


