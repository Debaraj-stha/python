from operator import truediv
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"res:{res}")
    print("//")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
def distanceBetween(ip1, ip2):
    res1=DbIpCity.get(ip1, api_key="free")
    res2=DbIpCity.get(ip2, api_key="free")
    lat1,long1=res1.latitude,res1.longitude
    lat2,long2=res2.latitude,res2.longitude
    return distance((lat1,long1),(lat2,long2)).km
def checkBlockedCountry(ip):
    res=DbIpCity.get(ip, api_key="free")
    blockedCountry=['NP','China','India']
    if res.country in blockedCountry:
        return True
    else:
        return False
if __name__ == '__main__':
    ip='103.94.255.33'
    ip2='103.95.255.21'
    printDetails(ip)
    diatancebt=distanceBetween(ip,ip2)
    print(f"Distance between %s and %s is %s km" % (ip,ip2,diatancebt))
    isbLocked=checkBlockedCountry(ip)
    if isbLocked:
        print(f"{ip} is blocked")
    else:
        print(f"{ip} is not blocked")