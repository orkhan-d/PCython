from bot import client

def is_muted(creds: dict):
    client.connect(**creds, timeout=5)
    stdin, stdout, stderr = client.exec_command("amixer -c 1 get Master | grep \"\[on\]\"")
    out = stdout.read().decode('utf-8').strip()
    client.close()

    return out!=''

def get_dirs(creds: dict):
    client.connect(**creds, timeout=5)
    stdin, stdout, stderr = client.exec_command("ls -a")
    out = list(map(lambda s: s.strip(), stdout.read().decode('utf-8').strip().split()))
    err = stderr.read()

    client.close()

    return out