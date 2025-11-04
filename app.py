print("========================================")
print("Selamat Datang {getpass.getuser()}")
print("========================================")

app_env = os.environ.get('APP_ENV', 'development')
print(f"  [KONFIGURASI] Mode Aplikasi (APP_ENV): {app_env}")

print("----------------------------------------")
print("Informasi Container")
print("----------------------------------------")

print(f"  [INTERNAL OS] OS : {platform.system()}")
print(f"  [INTERNAL OS] Hostname         : {platform.node()}")
print(f"  [INTERNAL OS] Dijalankan oleh  : {getpass.getuser()}")

print(f"  [INTERNAL OS] Platform Info    : {platform.platform()}")

print("========================================")