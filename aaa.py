import requests
url="https://www.flipkart.com/tv-and-appliances-republic-day-sale-jan26-store?fm=neo%2Fmerchandising&iid=M_c31c1325-ad7d-40db-a56b-197159ec857e_1_EARIG8M2T65U_MC.8O8BCYRIF1KF&cid=8O8BCYRIF1KF"
r=requests.get(url)

with open("file.html","w") as f:
    f.write(r.text)
