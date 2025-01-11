import random
import string
import subprocess

def generate_random_string(length):
    allowed_chars = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(allowed_chars) for _ in range(length))
    
    return random_string

def main():
    file_name = generate_random_string(8) + ".asm"

    try:
        with open(f"/tmp/{file_name}", 'w') as file:
            print("Enter your assembly code (type 'end' to finish):")
            
            while True:
                data = input()
                if data.strip() == 'end':
                    break
                file.write(data + '\n')
            
        print("[!] Compiling and running the assembly code...", flush=True)
        
        subprocess.call(["nasm", "-f", "elf32", f"/tmp/{file_name}"])
        subprocess.call(["ld", "-m", "elf_i386", f"/tmp/{file_name[:-4]}.o", "-o", f"/tmp/{file_name[:-4]}"])
        subprocess.call([f"/tmp/{file_name[:-4]}"])
        subprocess.call(["rm", f"/tmp/{file_name}", f"/tmp/{file_name[:-4]}.o", f"/tmp/{file_name[:-4]}"])
        
        print("\n[+] Assembly code compiled and run successfully")
    except Exception as e:
        print(f"[Error]: Could not compile and run the assembly code")

if __name__ == "__main__":
    main()