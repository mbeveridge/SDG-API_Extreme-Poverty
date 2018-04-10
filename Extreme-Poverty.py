import http.client

conn = http.client.HTTPSConnection("api.apihighways.org")

conn.request("GET", "/query?sql=SELECT%20*%20FROM%206a6de0b8-e544-495a-93ab-e8bc3c59fb20")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))