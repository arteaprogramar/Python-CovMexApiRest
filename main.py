# Arte al Programar
# Consumir API Rest en Python (Consulta de datos Covid19 México)
# Instalación de Request
# $pip install requests
# $pip install tabulate

import requests
from tabulate import tabulate
from datetime import datetime

now = datetime.now()


def main():
    response = requests.get("https://disease.sh/v3/covid-19/countries/Mexico?strict=true")
    if response.status_code == 200:
        result = response.json()
        print("\nEstadísticas México\n")
        headers = ["Country", "Date", "Cases", "Deaths", "Recovered"]
        table = [
            [result["country"], now.strftime("%d/%m/%Y"), result["cases"], result["deaths"], result["recovered"]]
        ]
        print(tabulate(table, headers, tablefmt="pretty"))
        print("\n")
    else:
        print("Error")


if __name__ == '__main__':
    main()
