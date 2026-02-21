import requests

def main():
    r = requests.get("https://api.github.com")
    if r.status_code == 200:
        print("Conexión exitosa a la API de GitHub")
    else:
        print("Error en la conexión:", r.status_code)

if __name__ == "__main__":
    main()