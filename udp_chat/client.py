import json
import socket
from uuid import uuid4
from datetime import datetime

def send_message(username, room_name, room_password, 
                 refer_message, message_text):
    
    # gera um uuid no ato de enviar uma mensagem
    uuid = str(uuid4())
    
    # pega a hora atual do sistema e converte para string
    datetime_now = datetime.utcnow().isoformat()
    
    # cria um dicionario para a mensagem UDP
    message_dict = {'username': username,
                    'room_name': room_name,
                    'room_password': room_password,
                    'uuid': uuid, 
                    'refer_message': refer_message,
                    'datetime': datetime_now,
                    'message_text': message_text}
    
    # converte o dicionarion para um json (string)
    message_json = json.dumps(message_dict)
    
    # converte o json (string) em bytes para ser trafegado na rede
    message_bytes = bytes(message_json, "UTF-8")
        
    # instancia objeto socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # define paramentros do socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # envia mensagem
    sock.sendto(message_bytes, ("255.255.255.255", 5002))
    
    return uuid
