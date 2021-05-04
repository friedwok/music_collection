class Instr(object):
	symbs = []

	def add(self, symb: str) -> None:
		self.symbs.append(symb)

	def get(self) -> dict:
		return self.symbs

nas = Instr()
nas.add('AND')
nas.add('SAD')

moex = Instr()
moex.add('GAZ')
moex.add('MYAS')
print(moex.get())
