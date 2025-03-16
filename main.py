from geometry.mesh import Mesh
from geometry.plotting import plot_mesh

def main():
    # Inicjalizujemy obiekt 'Mesh'
    geometry = Mesh()

    # Wczytujemy dane z pliku (np. data.txt)
    geometry.load_from_file("data.txt")

    # Wyświetlamy informacje o wczytanych węzłach i elementach
    print(geometry)

    # Wizualizacja
    plot_mesh(geometry)

if __name__ == "__main__":
    main()
