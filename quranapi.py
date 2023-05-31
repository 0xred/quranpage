import requests

def pagequran(namesurah,numberayah,urlimage):
    response = requests.get("https://mp3quran.net/api/v3/ayat_timing/soar?read=5")
    data = response.json()
    for item in data:
        link = item["timing_link"]
        try:
            cleaned_text = str(item["name"]).replace("\r\n", "")
            if namesurah == cleaned_text:
                responsex = requests.get(link)
                datax = responsex.json()
                for xitem in datax:
                    ayah = str(xitem["ayah"])
                    page = str(xitem["page"])
                    if str(numberayah) == ayah:
                        urlimage = page
                        return urlimage
        except:pass
