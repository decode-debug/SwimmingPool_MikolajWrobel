number = []
name, surname = self._name.split(" ")
number.append((ord(name[0])%10))
number.append((ord(surname[0])%10))