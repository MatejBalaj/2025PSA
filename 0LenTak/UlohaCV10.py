import urllib.request
import xml.etree.ElementTree as ET
import tkinter as tk
#import requests

def nastavOkno(paOkno):

    paOkno.title("RSS Citacka")

    paOkno.geometry("800x500+400+200")
    paOkno.resizable(False, False)
    #paOkno.resizable(True, True)

    labelURL = tk.Label(paOkno, text="URL:")
    labelURL.grid(row=0, column=0, padx=20)

    entryURL = tk.Entry()
    entryURL.grid(row=0, column=1, ipadx=260)

    url = "https://www.rfc-editor.org/rfcrss.xml"
    entryURL.insert(0, url)

    outputText = tk.Text(paOkno)
    outputText.grid(row=1, column=1, padx=20)

    buttonSubmit = tk.Button(paOkno,text="Urob!", command=lambda: outputText.insert(tk.END, getRssText(entryURL.get())))
    buttonSubmit.grid(row=1, column=0, padx=20, sticky="n")


    return True

def getRssText(paUrl):
    returnText = ""

    rawPage = urllib.request.urlopen(paUrl)
    page = rawPage.read()

    root = ET.fromstring(page)

    NS = "{http://search.yahoo.com/mrss/}"   # namespace pre <image:...>

    for channel in root:
        for item in channel:
            if item.tag == "title":
                returnText += f"Nadpis kanálu: {item.text}\n"

            if item.tag == "description":
                returnText += f"Popis kanálu: {item.text}\n"

            if item.tag == "item":
                for i in item:

                    if i.tag == "title":
                        returnText += f"Nadpis: {i.text}\n"

                    if i.tag == "description":
                        desc = i.text or ""
                        returnText += f"Popis: {desc[:150]}...\n"

                    # --- TU JE OBRÁZOK Z <image:image> ---
                    if i.tag == NS + "image":
                        for a in i:
                            if a.tag == NS + "url":
                                img_url = a.text.strip()
                                returnText += f"Obrázok: {img_url}\n"

    return returnText


url = "https://www.rfc-editor.org/rfcrss.xml"

#print(getRssText(url))

if __name__ == "__main__":

    okno = tk.Tk()
    nastavOkno(okno)
    okno.mainloop()