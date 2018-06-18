token = ''
with open("./creds/credentials.txt") as f:
    a = [line for line in f]
    token = a[0].strip()
print(len(token))
