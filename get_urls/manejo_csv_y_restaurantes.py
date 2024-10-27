import csv


def dividir_fichero(fichero: str, desde: int, cantidad: int) -> None:
    """
    PRE: fichero: name of the file
        desde: index of the url to start
        cantidad: number of url you want
    """
    with open(f"fichero_dividido_{cantidad}.csv", "a") as file:
        with open(fichero, "r") as file_read:
            reader = file_read.readlines()
            urls = reader[desde-1:cantidad+desde-1]
            file.writelines(urls)

def combinar_csvs(fichero: str, fichero_verdadero: str) -> None:
    """
    PRE: fichero: name of the file that you want to include into the fichero_verdadero it is a csv file
        fichero_verdadero: the final result of all ficheros it is a csv file
    """
    with open(fichero_verdadero, "a", newline="") as file_v:
        escritor = csv.writer(file_v)
        with open(fichero, "r") as file:
            reader = csv.reader(file)
            escritor.writerows(reader)

