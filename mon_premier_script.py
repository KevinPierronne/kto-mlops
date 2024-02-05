import unittest

"""
Count names with more than seven letters
"""
def compter_longueur_mot(prenoms : str) -> str:
    limit_lettre = 7
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > limit_lettre :
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
     def test_compter_longueur_mot(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = compter_longueur_mot(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()