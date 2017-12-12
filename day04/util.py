def get_passwords(in_val):
    for password in [pw_raw.strip() for pw_raw in in_val.splitlines()]:
        if password:
            yield password

