import requests
import sqlite3
import time

def read_proxy_urls_from_file(file_path='proxy.txt'):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading proxy file: {str(e)}")
        return []

def test_proxy_speed(proxy_url):
    try:
        start_time = time.time()
        response = requests.get('http://example.com', proxies={'http': proxy_url, 'https': proxy_url}, timeout=5)
        end_time = time.time()
        speed = end_time - start_time
        return speed
    except Exception as e:
        print(f"Error testing proxy {proxy_url}: {str(e)}")
        return None

def categorize_speed(speed):
    if speed is None:   #to help me identify the latency /speeds realtive to each other
        return 'Error'
    elif speed < 1.0:
        return 'Fast'
    elif speed < 5.0:
        return 'Medium'
    else:
        return 'Slow'

def store_results_in_database(proxy_url, speed_category):
    connection = sqlite3.connect('proxies.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proxy_speeds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proxy_url TEXT,
            speed_category TEXT
        )
    ''')

    cursor.execute('INSERT INTO proxy_speeds (proxy_url, speed_category) VALUES (?, ?)', (proxy_url, speed_category))

    connection.commit()
    connection.close()

proxy_urls = read_proxy_urls_from_file()

for proxy_url in proxy_urls:
    speed = test_proxy_speed(proxy_url)
    start = time.perf_counter()
    speed_category = categorize_speed(speed)

    print(f"Proxy: {proxy_url}, Speed: {speed}, Category: {speed_category}")

    store_results_in_database(proxy_url, speed_category)
    finish = time.perf_counter()
    print(finish-start)

