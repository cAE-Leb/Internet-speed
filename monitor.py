import speedtest
import datetime
import time
import csv
s = speedtest.Speedtest()


#test to print out speeds, verify program working
# while True:
#     time_now = datetime.datetime.now().strftime("%H:%M:%S")
#     downspeed = round((round(s.download()) / 1048576), 2)
#     upspeed = round((round(s.upload()) / 1048576), 2)
#     print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
#     # 60 seconds sleep
#     time.sleep(60)

with open('test.csv', mode='w') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'downspeed', 'upspeed'])
    csv_writer.writeheader()
    while True:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
        csv_writer.writerow({
            'time': time_now,
            'downspeed': downspeed,
            "upspeed": upspeed
        })
        # 60 seconds sleep
        time.sleep(60)