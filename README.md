# applemusic-scraper
Noslēguma projekts datu struktūrās

1. Projekta uzdevuma detalizēts apraksts
Šī projekta mērķis ir automātiski nolasīt dziesmu nosaukumus un izpildītājus no "Apple Music"  playlistes un saglabāt iegūto informāciju teksta failā.
Galvenie soļi:
• Atvērt pārlūkprogrammu "headless mode" un ielādēt lietotāja norādīto URL.
• Automātiski ritināt lapu uz leju, līdz tiek ielādēti visas dziesmas.
• Iegūt lapas HTML saturu un to parsēt ar BeautifulSoup, meklējot katru “songs-list-row” ierakstu.
• No katra ieraksta izlasīt skaņdarba nosaukumu un izpildītāju.
• Saglabāt rezultātu teksta failā “songs_and_artists.txt” 
• Izvadīt konsolē ritināšanas mēģinājumu skaitu, atrasto dziesmu skaitu, kad programma sasniegusi labas beigas, visas atrastās dziesmas un izpildītājus.

2. Python bibliotēkas un to pielietojums
• time
Miega funkcija sleep() ļauj dot laiku lapas elementiem ielādēties pēc driver.get() un pēc katras ritināšanas darbības.
• Selenium, selenium.webdriver,  Options
Lai atvēru un kontrolēt pārlūkprogrammu Chrome instanci. Options ļauj kontrolēt tā darbību (--headless, --disable-gpu).
• By
Elementu meklēšanai: find_element(By.TAG_NAME, "body"), find_element(By.CSS_SELECTOR, "...").
• ActionChains un ScrollOrigin
Simulēt lietotāja klikšķi, ritināšanu atvērtajā lapā.
• BeautifulSoup (bs4)
HTML parsēšana: BeautifulSoup(html, "html.parser") ļauj atrast visus div elementus ar klasi songs-list-row un izvilkt tiem tekstu.

3. Programmatūras izmantošanas metodes
• Apkopot informāciju par "atskaņošanas sarakstu" saturu.
• Veidod "atskaņošanas sarakstu" kādā citā platformā izmantojot viņu api.

4. Lietošanas instrukcija
• Ielādē visas programmai nepieciešamās bibliotēkas ar komandu: pip install selenium beautifulsoup4
• Kodā ieraksta saiti uz apple music atskaņošanas sarakstu (kodā jau ir ierakstīta saite uz klasisku Latvijas mūziku, kā arī ierakstīta vēl viena saite komentārā).
• Palaiž programmu un gaida, kamēr tā atvērs saiti, ielādēs lapu, atradīs visas dziesmas atskaņošanas sarakstā, un izveidos songs_and_artists.txt failu.
• Kad teksta fails ir izveidots ar to drīkst darīt, ko vien vēlas, piemēram, nosūtīt kādam draugam e-pastā.
