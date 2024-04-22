import time as t

def start_time():
    start = t.time()
    return start 

def stop_time():
    stop = t.time()
    return stop

def main():
    while True :
        status = input("Enter a Start or Stop - ")
        if status.lower() == "start":
            start = start_time()
            status = input("Enter Stop -")
            if status.lower() == "stop" :
                stop = stop_time()
                break
    escape_time = stop - start
    HH = int(escape_time)//3600
    MM = (int(escape_time)%3600)//60
    SS = int(escape_time)%60
    print(f"{HH}hrs :{MM} mins :{SS} sec")
    

if __name__=="__main__":
    main()
