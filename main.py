import requests
from pyfiglet import Figlet
import folium


def get_in_by_ip(ip= "127.0.0.1"):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        print(response)

        data = {
            "[IP]": response.get("query"),
            "[Int prov]": response.get("isp"),
            "[Org]": response.get("org"),
            "[Country]": response.get("count"),
            "[Region Name]": response.get("regionName"),
            "[Cyty]": response.get("city"),
            "[ZIP]": response.get("zip"),
            "[Lat]": response.get("lat"),
            "[Lon]": response.get("lon"),
        }
        for k, v in data.items():
            print(f"{k} : {v}")

        area = folium.Map(location=[ response.get("lat"), response.get("lon") ])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
    except requests.exceptions.ConnectionError:
        print("хуй")
def main():
    prev_text = Figlet(font="slant")
    print(prev_text.renderText("IP HACK"))
    ip = input("Введите айпи: ")

    get_in_by_ip(ip=ip)
if __name__ == "__main__":
    main()