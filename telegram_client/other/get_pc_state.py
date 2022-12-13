from bot import client
import configparser

def is_muted(creds: dict):
    config = configparser.ConfigParser()

    client.connect(**creds)
    stdin, stdout, stderr = client.exec_command("amixer -c 1 get Master | grep \"\[on\]\"")
    out = stdout.read().decode('utf-8').strip()
    return out!=''