import discord
from discord.ext import commands
from model import get_class
import os, random
import requests
from PIL import Image
import random
from wherebin import eko
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def spam(ctx, tekst: str, count_heh = 5):
    await ctx.send(tekst * count_heh)

C1 = "Wybieraj rower lub spacer na dystansach poniżej 3 km zamiast auta 🚲 – unikasz bezpośredniej emisji spalin z rury wydechowej na krótkich trasach, gdzie silnik pali najwięcej."
C2 = "Korzystaj z transportu publicznego 🚆 – jeden pociąg lub autobus zastępuje kilkadziesiąt aut, co drastycznie obniża ślad węglowy na każdego pasażera."
C3 = "Jeśli musisz jechać autem, zabierz pasażerów (carpooling) 👥 – rozkładasz emisję spalin jednego pojazdu na kilka osób, zamiast generować ją osobno dla każdego."
C4 = "Dbaj o ciśnienie w oponach 🏎️ – zbyt niskie ciśnienie zwiększa opory toczenia, co sprawia, że silnik zużywa więcej paliwa i emituje więcej CO2."
C5 = "Unikaj gwałtownego przyspieszania i hamowania (eco-driving) 📉 – płynna jazda pozwala spalić nawet o 20% mniej paliwa, ograniczając zanieczyszczenie powietrza."
C6 = "Wyłączaj silnik podczas dłuższego postoju 🛑 – praca na biegu jałowym niepotrzebnie marnuje paliwo i emituje gazy cieplarniane bez pokonywania dystansu."
C7 = "Ogranicz loty krótkodystansowe na rzecz pociągów ✈️ – start i lądowanie to momenty największej emisji; pociąg na tej samej trasie emituje ułamek tego, co samolot."
C8 = "Planuj wakacje bliżej domu 🏕️ – krótsza trasa podróży oznacza mniejsze zapotrzebowanie na paliwa kopalne wykorzystywane w transporcie dalekobieżnym."
C9 = "Usuń zbędny bagaż i bagażnik dachowy, gdy go nie używasz 🎒 – lżejsze auto i mniejszy opór powietrza to mniejsze obciążenie dla silnika i niższe spalanie."
C10 = "Jeśli kupujesz auto, rozważ model elektryczny lub hybrydowy 🔌 – pojazdy te mają wyższą sprawność i emitują znacznie mniej gazów cieplarnianych w całym cyklu życia."
C11 = "Ogranicz spożycie czerwonego mięsa, zwłaszcza wołowiny 🥩 – hodowla krów wymaga ogromnych terenów pod paszę i generuje potężne ilości metanu oraz CO2."
C12 = "Wprowadź jeden całkowicie roślinny dzień w tygodniu 🥦 – dieta roślinna wymaga znacznie mniej energii i wody niż produkcja białka zwierzęcego."
C13 = "Kupuj produkty sezonowe 🍅 – unikasz energii potrzebnej do ogrzewania szklarni zimą oraz prądu zużywanego przez chłodnie w transporcie z zagranicy."
C14 = "Wybieraj lokalną żywność 🚜 – skrócenie „łańcucha dostaw” eliminuje tysiące ton CO2 generowanych przez ciężarówki i statki transportowe."
C15 = "Unikaj produktów z olejem palmowym 🌴 – jego produkcja prowadzi do wypalania lasów tropikalnych, co uwalnia zmagazynowany w nich węgiel do atmosfery."
C16 = "Pij wodę z kranu zamiast budelkowanej 🚰 – eliminujesz proces produkcji plastiku i transportu ciężkich zgrzewek wody, co oszczędza paliwo."
C17 = "Nie marnuj żywności 🍎 – wyrzucone jedzenie na wysypiskach gnije bez dostępu tlenu, wytwarzając metan, który jest 28 razy silniejszym gazem cieplarnianym niż CO2."
C18 = "Gotuj pod przykryciem 🍲 – zatrzymujesz ciepło w naczyniu, dzięki czemu potrawa gotuje się szybciej przy mniejszym zużyciu gazu lub prądu."
C19 = "Gotuj tylko tyle wody w czajniku, ile faktycznie potrzebujesz ☕ – grzanie nadmiaru wody to czyste marnotrawstwo energii elektrycznej produkowanej często z węgla."
C20 = "Hoduj własne zioła na parapecie 🌿 – rezygnujesz z produktów pakowanych w plastik i dowożonych do sklepów codziennymi dostawami."
C21 = "Obniż temperaturę w domu o 1°C zimą 🌡️ – ta niewielka zmiana pozwala zmniejszyć roczne emisje związane z ogrzewaniem budynku o około 6%."
C22 = "Zadbaj o szczelność okien i drzwi 🖼️ – ograniczasz straty ciepła, co sprawia, że piec lub kaloryfery pracują rzadziej, zużywając mniej paliwa."
C23 = "Wymień żarówki na energooszczędne LED 💡 – zużywają one ułamek prądu potrzebnego klasycznym żarówkom, odciążając elektrownie emitujące CO2."
C24 = "Wyłączaj urządzenia z trybu czuwania (standby) 🔌 – tzw. „wampiry energetyczne” pobierają prąd 24/7; odłączenie ich realnie obniża Twoje roczne zużycie energii."
C25 = "Pierz w niskich temperaturach (30-40°C) 🧺 – około 90% energii zużywanej przez pralkę idzie na podgrzanie wody; niska temperatura to ogromna oszczędność."
C26 = "Susz ubrania naturalnie zamiast w suszarce bębnowej ☀️ – suszarka to jedno z najbardziej prądożernych urządzeń w domu; wiatr i słońce są darmowe i bezemisyjne."
C27 = "Regularnie rozmrażaj lodówkę i zamrażarkę 🧊 – warstwa lodu działa jak izolator, zmuszając agregat do cięższej pracy i pobierania większej ilości prądu."
C28 = "Zainstaluj panele fotowoltaiczne ☀️ – produkując własny prąd ze słońca, przestajesz korzystać z energii pochodzącej ze spalania paliw kopalnych."
C29 = "Wybieraj sprzęty AGD o wysokiej klasie energetycznej ⚡ – nowoczesne urządzenia są zaprojektowane tak, by wykonywać tę samą pracę przy znacznie mniejszym zapotrzebowaniu na moc."
C30 = "Zasłaniaj rolety na noc zimą 🏁 – dodatkowa warstwa izolacji na oknach zapobiega ucieczce ciepła, zmniejszając zapotrzebowanie na dogrzewanie wnętrz."
C31 = "Kupuj mniej nowych ubrań 👗 – przemysł tekstylny odpowiada za ogromne emisje; rzadsze zakupy to mniejszy popyt na energochłonną produkcję masową."
C32 = "Wybieraj odzież z drugiej ręki 🧥 – dając ubraniom drugie życie, unikasz śladu węglowego związanego z produkcją nowej tkaniny i jej transportem z Azji."
C33 = "Naprawiaj buty i sprzęty zamiast kupować nowe 🛠️ – każda naprawa to oszczędność energii i surowców, które musiałyby zostać wydobyte i przetworzone."
C34 = "Unikaj ekspresowych dostaw kurierskich 📦 – szybka dostawa często oznacza, że furgonetki jeżdżą półpuste, co generuje więcej emisji na jedną paczkę."
C35 = "Segreguj bioodpady 🥕 – odpowiednio przetworzone w kompostowniku nie emitują metanu tak jak odpady zmieszane na wielkich składowiskach."
C36 = "Rezygnuj z plastikowych opakowań ⛽ – plastik powstaje z ropy naftowej; rezygnacja z niego to uderzenie w przemysł wydobywczy generujący CO2."
C37 = "Pożyczaj rzadko używane narzędzia 🤝 – wyprodukowanie jednej wiertarki dla całego bloku emituje mniej CO2 niż wyprodukowanie jej dla każdego mieszkańca osobno."
C38 = "Wybieraj produkty trwałe 💎 – rzeczy, które służą lata, rzadziej wymagają wymiany, co hamuje koło energochłonnej produkcji i transportu."
C39 = "Recyklinguj aluminium 🥫 – przetworzenie starej puszki zużywa o 95% mniej energii niż produkcja nowej z rudy boksytu."
C40 = "Przejdź na e-faktury 📄 – chronisz drzewa, które są naturalnymi „magazynami” CO2, pochłaniającymi ten gaz z atmosfery."
C41 = "Usuwaj niepotrzebne maile i dane z chmury 📧 – centra danych przechowujące Twoje „śmieci cyfrowe” zużywają ogromne ilości prądu do chłodzenia serwerów."
C42 = "Ogranicz jakość wideo w streamingu 🎬 – przesyłanie danych w 4K wymaga więcej energii od serwerowni i routerów niż jakość HD."
C43 = "Wyłączaj Wi-Fi i Bluetooth, gdy ich nie używasz 📱 – każde działające połączenie bezprzewodowe zmusza urządzenie do ciągłego poboru energii i emisji fal."
C44 = "Korzystaj z wyszukiwarek sadzących drzewa (np. Ecosia) 🌳 – Twoje wyszukiwania finansują sadzenie lasów, które aktywnie usuwają dwutlenek węgla z powietrza."
C45 = "Posadź drzewo lub rośliny na balkonie 🌲 – roślinność nie tylko pochłania CO2, ale też obniża temperaturę otoczenia, redukując potrzebę używania klimatyzacji."
C46 = "Bierz krótki prysznic zamiast kąpieli 🚿 – zużywasz mniej wody, co oznacza, że piec gazowy lub elektryczny pracuje krócej, emitując mniej spalin."
C47 = "Wspieraj firmy korzystające z zielonej energii 🏢 – Twoje pieniądze finansują rozwój technologii odnawialnych zamiast wspierania tradycyjnego sektora węglowego."
C48 = "Wybieraj pracę zdalną, jeśli możesz 💻 – eliminujesz codzienne dojazdy, co w skali roku pozwala zaoszczędzić setki litrów paliwa i uniknąć dużej chmury CO2."
C49 = "Edukuj bliskich o sposobach na redukcję emisji 🗣️ – zmiana nawyków u kilku osób daje efekt skali, który jest znacznie silniejszy niż działanie w pojedynkę."
C50 = "Sprawdzaj swój ślad węglowy 📊 – świadomość tego, które Twoje działania najbardziej szkodzą, pozwala skuteczniej wybierać zmiany, które dają największy oddech planecie."


porady = [
    C1, C2, C3, C4, C5, C6, C7, C8, C9, C10,
    C11, C12, C13, C14, C15, C16, C17, C18, C19, C20,
    C21, C22, C23, C24, C25, C26, C27, C28, C29, C30,
    C31, C32, C33, C34, C35, C36, C37, C38, C39, C40,
    C41, C42, C43, C44, C45, C46, C47, C48, C49, C50 ]

@bot.command()
async def co2_porada(ctx):
    porada = random.choice(porady)
    await ctx.send(porada)
    
@bot.command()
async def eko_bin(ctx, *, wordls = ""):
    await ctx.send(eko(wordls))
    
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f'./{file_name}')
            image = Image.open(file_name)
            class_name, confidence_score = get_class(image, "keras_model.h5", "labels.txt")
            
            if confidence_score > 0.75:
                await ctx.send(f"To wygląda na: {class_name} śmietnik.")
            else:
                await ctx.send("Nie jestem pewien, co to jest. Spróbuj zrobić lepsze zdjęcie!")
    else:
        await ctx.send("NIE ZAŁĄCZYŁEŚ PLIKU!")
        
@bot.command()
async def co2(ctx):
    data = requests.get("https://global-warming.org/api/co2-api").json()
    
    najnowszy = data['co2'][-1]
    
    dzien = najnowszy['day']
    miesiac = najnowszy['month']
    rok = najnowszy['year']
    wartosc = najnowszy['trend']
    
    await ctx.send(f"🌍 Aktualne stężenie CO2 (dane z {dzien}.{miesiac}.{rok}): **{wartosc} ppm**.")
    
@bot.command()
async def mapa(ctx):
    embed = discord.Embed(
        title="🌍 Interaktywna Mapa Emisji CO2",
        description="Kliknij poniżej, aby zobaczyć na żywo, skąd pochodzi prąd i ile CO2 emituje każdy kraj!",
        color=0x2ECC71, # Zielony kolor
        url="https://app.electricitymaps.com/map",
    )
    
    await ctx.send(embed=embed, file = discord.File("M.png"))

@bot.command()
async def obl(ctx, dystans: float, spalanie: float, paliwo: str):
    
    dane_paliwo = {"benzyna": 2.32, "diesel": 2.65, "lpg": 1.50}
    mnoznik = dane_paliwo.get(paliwo.lower(), 2.32)
    wynik = dystans * (spalanie / 100) * mnoznik
    
    await ctx.send(f"♻️Emisja: {round(wynik, 2)} kg CO2")
    
@bot.command()
async def play(ctx):
    embed = discord.Embed(
        title="▶️ Wybierz Playlistę",
        description="[EKOLOGIA♻️](https://www.youtube.com/playlist?list=PLWsQ9XwfIuo6B_Vp4ajWR68-lknvRmyY5)\n[Playlista MKIŚ🌍](https://www.youtube.com/playlist?list=PLrWAtxHx4r7p-3YieVojgqsvjf_l8LO5N)",
        color=0x2ECC71
    )
    await ctx.send(embed=embed)
    
@bot.command()
async def quiz(ctx):
    embed = discord.Embed(
        title="Quiz",
        description="Kliknij powyżej, aby rozwiązać quiz!",
        color=0x2ECC71, # Zielony kolor
        url="https://wielkitest.tvp.pl/44561817/rozwiaz-wielki-test-o-ekologii",
    )
    await ctx.send(embed=embed)
    
@bot.command()
async def help_me(ctx):
    await ctx.send("**🤖 MENU POMOCY EKO-BOTA**")
    await ctx.send("👋 `$hello` - Przywitaj się z botem!")
    await ctx.send("😂 `$spam [tekst] [liczba]` - Bot powtórzy Twój tekst określoną liczbę razy.")
    await ctx.send("🌱 `$co2_porada` - Losowa porada ekologiczna.")
    await ctx.send("♻️ `$eko_bin [NAZWA]` - Niektóre śmieci mogą nie działaś (używaj WIELKICH LITER).")
    await ctx.send("📸 `$check` - Rozpoznawanie odpadu ze zdjęcia (załącz plik).")
    await ctx.send("📈 `$co2` - Aktualne stężenie CO2 na świecie.")
    await ctx.send("🗺️ `$mapa` - Interaktywna mapa emisji na żywo.")
    await ctx.send("🚗 `$obl [km] [spalanie] [paliwo]` - Kalkulator emisji auta.")
    await ctx.send("🎵 `$play` - Playlisty o ekologii.")
    await ctx.send("🌱 $quiz - Rozwiąż test i zostań eko-ekspertem.")

bot.run("")
