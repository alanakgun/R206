import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f"Pas assez d'arguments pour le script {sys.argv[0]}")
    else:
        for i in range(1, len(sys.argv)):
            print('=>', sys.argv[i])
