import re

class EmailExtractor:

    def __init__(self, email):
        self.email = email
        self.regex = r'(?P<name>[a-z]+)\.(?P<surname>[a-z]+)[0-9]*@(?P<is_student>(student\.)?)(wat\.edu\.pl)'
    def get_name(self) -> str:
        a = re.compile(self.regex)
        match = a.match(self.email)
        return match.group('name').capitalize() if match else None
    def get_surname(self) -> str:
        a = re.compile(self.regex)
        match = a.match(self.email)
        return match.group('surname').capitalize() if match else None
    def is_student(self) -> bool:
        a = re.compile(self.regex)
        match = a.match(self.email)
        return bool(match and match.group('is_student'))
    def is_male(self) -> bool:
        name = self.get_name()
        return name and not name.endswith('a')