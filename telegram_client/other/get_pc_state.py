from bot import client
import configparser

def is_muted(creds: dict):
    client.connect(**creds, timeout=5)
    stdin, stdout, stderr = client.exec_command("amixer -c 1 get Master | grep \"\[on\]\"")
    out = stdout.read().decode('utf-8').strip()
    client.close()

    return out!=''


def get_dirs(creds: dict, current_dir: str = ''):
    client.connect(**creds, timeout=5)
    config = configparser.ConfigParser()
    config.read('config.ini')

    stdin, stdout, stderr = client.exec_command(f"ls {config['PC_STATE']['curdir']} -aF")

    out = list(map(lambda s: s.strip(), stdout.read().decode('utf-8').strip().split()))
    err = stderr.read()

    client.close()

    return out