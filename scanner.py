import requests
from urllib.parse import urlencode, urlparse, parse_qs, urlunparse
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

# Nonaktifkan peringatan SSL untuk pengujian pada localhost
disable_warnings(InsecureRequestWarning)

def inject_payload_to_url(url, param, payload):
    """
    Menyuntikkan payload ke parameter tertentu dalam URL.
    """
    # Parse URL
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # Tambahkan payload ke parameter tertentu
    query_params[param] = payload

    # Rekonstruksi URL dengan parameter payload
    new_query = urlencode(query_params, doseq=True)
    new_url = urlunparse(parsed_url._replace(query=new_query))
    return new_url

def check_xss(url, param, payload):
    """
    Mengecek potensi XSS dengan mengirimkan payload ke parameter tertentu.
    
    :param url: URL target
    :param param: Parameter untuk diuji
    :param payload: Payload XSS untuk diuji
    """
    print(f"\nMenguji parameter '{param}' dengan payload: {payload}")
    try:
        # Buat URL dengan payload
        test_url = inject_payload_to_url(url, param, payload)
        
        # Kirim permintaan GET
        response = requests.get(test_url, verify=False, timeout=10)
        
        # Cek apakah payload tercermin dalam respons
        if payload in response.text:
            print(f"⚠️  Potensi XSS ditemukan pada parameter '{param}'!")
            print(f"URL: {test_url}")
        else:
            print(f"✅ Parameter '{param}' aman dari XSS.")
    except requests.RequestException as e:
        print(f"Terjadi kesalahan saat mengakses {url}: {e}")

if __name__ == "__main__":
    print("Simple XSS Scanner")
    
    # Masukkan URL target
    target_url = input("Masukkan URL target (contoh: http://localhost/page.php): ").strip()
    
    # Tampilkan opsi parameter
    print("\nPilih parameter untuk diuji:")
    print("1. q")
    print("2. search")
    print("3. filter")
    
    # Pilihan parameter
    param_options = {
        "1": "q",
        "2": "search",
        "3": "filter"
    }
    param_choice = input("Masukkan pilihan (1/2/3): ").strip()
    param = param_options.get(param_choice)
    
    if not param:
        print("Pilihan tidak valid. Program dihentikan.")
    else:
        # Payload XSS sederhana
        payload = "<script>alert('XSS')</script>"
        print(f"\nMenggunakan payload XSS: {payload}")
        
        # Uji XSS pada parameter yang dipilih
        check_xss(target_url, param, payload)
