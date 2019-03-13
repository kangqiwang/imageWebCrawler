import redis
r=redis.Redis(host='localhost',port=6379,db=0)

r.get('pick-best-asin')
print(r.get('pick-best-asin'))