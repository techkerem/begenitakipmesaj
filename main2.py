import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pyautogui import *
import pyautogui
import keyboard
import random
import pyperclip

# Kerem Ersoz
# programi baslatip whatsapp webin yazma kismina tiklayip birakin acılması bıraz suruyor ama acılınca hızlı yenılenıyor
# evet request veya library kullanarak da yapilabilirdi ama denedim inanilmaz derecede yavaslatiyor ve bazi sinyaller kaciyor.

# pyautogui.write ile turkce karakter yazmak neredeyse imkansiz o yuzden kopyalayip yapistiriyoruz.
# eger turkce karakter sart degil derseniz ekleyebilirsiniz.

#headlessi buradan kapatabilirsiniz
gizli_sekme = True

if gizli_sekme == True:
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

else:
    driver = webdriver.Chrome(ChromeDriverManager().install())

#buraya en son takipci ve videonuzdaki begeni sayinizi yazin isrerseniz kodu uzatip en basta da verileri cekebilirsiniz loop disinda
mem = 2022
like = 0

satir_sayisi = sum(1 for line in open('liste.txt'))

def mesaj(yazi):
    # mesaji buradan duzenleyebilirsiniz
    pyperclip.copy("Takipçin Sana Tatlı Bir Mesaj Gönderdi:")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey('shift', 'enter')
    pyautogui.hotkey('shift', 'enter')
    pyperclip.copy(yazi)
    pyautogui.write("selam ")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)


x=1
while x<10:

    #@ kismindan sonra kendi kullanici adinizi koyun
    driver.get('https://www.tiktok.com/@krmersoz')

    #hata verirse chrome da kaynagi incele tusuna basip takipci sayiniza tiklayin ve copy full path diyip assagiya ekleyin
    takipci = driver.find_element("xpath", '/html/body/div[2]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong').text

    # video linkiniz ve begeni sayisinin xpath i
    driver.get('https://www.tiktok.com/@krmersoz/video/7140651034711510273?is_copy_url=1&is_from_webapp=v1')
    begeni = driver.find_element("xpath", '/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]/strong').text

    if int(takipci) > int(mem) and int(begeni) > int(like):

        with open("liste.txt", mode="r", encoding="utf-8") as f:
            kelime=f.readlines()
            mesaj(kelime[random.randrange(0,satir_sayisi-1)])

        mem = takipci
        like = begeni

    #kac saniye aralikla kontrol ediyor
    time.sleep(1)
