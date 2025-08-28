import os
import time
import sys

def main():
    print("=" * 50)
    print("APLIKASI PYTHON BUILT OTOMATIS")
    print("DARI TERMUX VIA GITHUB ACTIONS")
    print("=" * 50)
    
    print(f"Sistem: {sys.platform}")
    print(f"Waktu: {time.ctime()}")
    print(f"Direktori: {os.getcwd()}")
    print("=" * 50)
    
    # Fitur sederhana
    print("1. Tampilkan info sistem")
    print("2. List file di folder")
    print("3. Keluar")
    
    try:
        choice = input("\nPilihan (1-3): ")
        
        if choice == "1":
            print(f"\nPython version: {sys.version}")
            print(f"Platform: {sys.platform}")
            print(f"CPU cores: {os.cpu_count()}")
            
        elif choice == "2":
            print("\nFile dalam folder:")
            for item in os.listdir():
                if os.path.isfile(item):
                    print(f"📄 {item}")
                else:
                    print(f"📁 {item}/")
                    
        elif choice == "3":
            print("Terima kasih!")
            
        else:
            print("Pilihan tidak valid!")
            
    except Exception as e:
        print(f"Error: {e}")
    
    # Tunggu sebelum close (Windows)
    if sys.platform == "win32":
        input("\nTekan Enter untuk keluar...")

if __name__ == "__main__":
    main()
