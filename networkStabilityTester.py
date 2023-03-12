import csv
import speedtest
import time

# create CSV file
filename = 'wifi_logs.csv'
with open(filename, mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'Download Speed (Mbps)', 'Upload Speed (Mbps)', 'Ping (ms)'])

# run speed test every minute and log results
while True:
    # run speed test
    st = speedtest.Speedtest()
    download_speed = round(st.download() / 1000000, 2)
    upload_speed = round(st.upload() / 1000000, 2)
    ping = round(st.results.ping, 2)

    # get current time
    current_time = time.strftime('%H:%M:%S')
    print(current_time, "|", download_speed, "Down |", upload_speed, "Up |", ping," ms")
    # log results to CSV file
    with open(filename, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, download_speed, upload_speed, ping])

    # wait for one minute before running the test again
    time.sleep(60)
