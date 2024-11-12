import pyperclip

def format_proxy(line, protocol):
    # Memastikan line memiliki format 'user:pass@ip:port'
    user_pass, ip_port = line.split('@')
    user, password = user_pass.split(':')
    formatted = f"{protocol}://{user}:{password}@{ip_port.strip()}"
    return formatted

# Meminta pengguna untuk memilih format
print("Pilih format tujuan untuk proxy:")
print("1. http")
print("2. socks5")
choice = input("Masukkan pilihan (1 atau 2): ")

# Menentukan protocol berdasarkan pilihan pengguna
if choice == "1":
    protocol = "http"
elif choice == "2":
    protocol = "socks5"
else:
    print("Pilihan tidak valid. Default ke 'http'.")
    protocol = "http"

# Baca dari file proxies.txt dan proses setiap baris
with open("proxies.txt", "r") as file:
    proxies = file.readlines()

# Format setiap proxy dengan protocol yang dipilih
formatted_proxies = []
for proxy in proxies:
    # Jika proxy sudah memiliki format 'http://' atau 'socks5://', hapus protokol awalnya
    if proxy.startswith("http://") or proxy.startswith("socks5://"):
        proxy = proxy.split("://", 1)[1]  # Hapus bagian protokol
    formatted_proxies.append(format_proxy(proxy, protocol))

# Gabungkan semua proxy yang diformat dengan newline
result = "\n".join(formatted_proxies)

# Salin hasil ke clipboard
pyperclip.copy(result)

# Simpan hasil ke file
with open("proxy_formatted.txt", "w") as output_file:
    output_file.write(result)

print(f"Proxies telah diformat ke '{protocol}://' format, disimpan di 'proxy_formatted.txt', dan disalin ke clipboard!")
