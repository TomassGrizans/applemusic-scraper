import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

loadtime = 6 #page loadtime

def extract_songs_and_artists(url):
    options = Options()
    options.add_argument("--headless")       
    options.add_argument("--disable-gpu")    
    options.add_argument("--window-size=1920,1080")  
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    time.sleep(loadtime)  
    
    # focus (300,20)
    body_elem = driver.find_element(By.TAG_NAME, "body")
    ActionChains(driver).move_to_element_with_offset(body_elem, 300, 20).click().perform()
    time.sleep(2)
    
    try:
        container = driver.find_element(By.CSS_SELECTOR, "div.songs-list")
    except Exception:
        container = None

    scroll_pause_time = 0.2  # shorter = faster scrolling
    scroll_offset = 10000    
    max_scroll_attempts = 100
    previous_count = 0
    no_change_attempts = 0

    for attempt in range(max_scroll_attempts):
        if container:
            origin = ScrollOrigin.from_element(container, 0, 0)
            ActionChains(driver).scroll_from_origin(origin, 0, scroll_offset).perform()
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(scroll_pause_time)
        
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        track_rows = soup.find_all("div", class_="songs-list-row")
        current_count = len(track_rows)
        print(f"Scroll attempt {attempt+1}: {current_count} songs found.")
        
        if current_count == previous_count:
            no_change_attempts += 1
        else:
            no_change_attempts = 0
        
        if no_change_attempts >= 3:
            print("Reached bottom of content.")
            break
        
        previous_count = current_count

    final_html = driver.page_source
    driver.quit()
    
    # Parse
    soup = BeautifulSoup(final_html, "html.parser")
    songs_data = []
    for row in soup.find_all("div", class_="songs-list-row"):
        name_div = row.find("div", class_="songs-list-row__song-name")
        if not name_div:
            continue
        song_name = name_div.get_text(strip=True)
        
        artist_name = None
        artist_div = row.find("div", class_="songs-list-row__artist-name")
        if not artist_div:
            artist_div = row.find("div", class_="songs-list__col--secondary")
        if artist_div:
            artist_link = artist_div.find("a")
            artist_name = artist_link.get_text(strip=True) if artist_link else artist_div.get_text(strip=True)
        songs_data.append((song_name, artist_name))
    
    return songs_data

def main():
    # example links:
    #https://music.apple.com/lv/playlist/%C5%A1l%C4%81geris/pl.u-KVXBBJ6FZxDPz2B
    #https://music.apple.com/lv/playlist/british-invasion-essentials/pl.3041e43dff234643b9066a1b069e82fa

    playlist_url = "https://music.apple.com/lv/playlist/%C5%A1l%C4%81geris/pl.u-KVXBBJ6FZxDPz2B" 
    songs_and_artists = extract_songs_and_artists(playlist_url)
    
    print("\nCollected tracks:")
    for track, artist in songs_and_artists:
        print(f"Song: {track} | Artist: {artist if artist else 'Unknown'}")
    
    with open("songs_and_artists.txt", "w", encoding="utf-8") as f:
        for track, artist in songs_and_artists:
            f.write(f"{track} | {artist if artist else 'Unknown'}\n")

if __name__ == "__main__":
    main()
