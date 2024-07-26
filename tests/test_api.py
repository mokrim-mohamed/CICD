import os
import sys
# Ajouter le répertoire 'src' au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))


from app import add, subtract  # noqa: E402


def test_add():
    # Test d'addition réussie
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    # Test de soustraction réussie
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0
