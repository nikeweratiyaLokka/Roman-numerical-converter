class Converter:
    def romantoint(self, nume: str) -> int:

        numericals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        summ = 0
        i = 0

        try:

            while i < len(nume):
                if numericals[nume[i]] < numericals[nume[i+1]]:
                    summ += (numericals[nume[i+1]]-numericals[nume[i]])
                    i += 2
                
                else:
                    summ += (numericals[nume[i+1]])
                    i += 1
            return summ

        except NameError and ValueError:
            print("Not a valid numeral")
