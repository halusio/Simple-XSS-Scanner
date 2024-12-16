from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def check_xss_via_form(target_url, input_field_id, payload):
    """
    Mengecek potensi XSS dengan menyuntikkan payload ke kolom input form.
    
    :param target_url: URL target halaman web
    :param input_field_id: ID atau nama kolom input yang akan diuji
    :param payload: Payload XSS untuk diuji
    """
    # Konfigurasi browser (gunakan mode headless jika diperlukan)
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--ignore-certificate-errors")  # Abaikan SSL
    chrome_options.add_argument("--headless")  # Jalankan browser tanpa GUI (opsional)

    # Path ke driver Chrome (ubah sesuai dengan lokasi chromedriver Anda)
    driver_path = "chromedriver"

    # Mulai browser
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
    
    try:
        # Buka halaman target
        print(f"Membuka URL: {target_url}")
        driver.get(target_url)
        
        # Tunggu sebentar untuk memastikan halaman termuat
        time.sleep(2)
        
        # Temukan kolom input
        input_field = driver.find_element(By.ID, input_field_id)  # Bisa diganti dengan By.NAME atau By.CSS_SELECTOR
        print(f"Kolom input ditemukan: {input_field_id}")
        
        # Masukkan payload XSS ke kolom input
        print(f"Menyuntikkan payload: {payload}")
        input_field.clear()
        input_field.send_keys(payload)
        
        # Kirim formulir (tekan Enter)
        input_field.send_keys(Keys.RETURN)
        
        # Tunggu beberapa saat untuk melihat respons
        time.sleep(2)
        
        # Cek apakah payload tercermin di halaman
        page_source = driver.page_source
        if payload in page_source:
            print("⚠️ Potensi XSS ditemukan! Payload tercermin di halaman.")
        else:
            print("✅ Halaman aman dari XSS (payload tidak tercermin).")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    
    finally:
        # Tutup browser
        driver.quit()

if __name__ == "__main__":
    print("XSS Checker via Form Input")
    
    # Masukkan URL target
    target_url = input("Masukkan URL target (contoh: http://localhost/page.php): ").strip()
    
    # Masukkan ID kolom input
    input_field_id = input("Masukkan ID atau nama kolom input (contoh: search): ").strip()
    
    # Payload XSS sederhana
    payload = "<script>alert('XSS')</script>"
    
    print(f"\nMenggunakan payload XSS: {payload}")
    check_xss_via_form(target_url, input_field_id, payload)
