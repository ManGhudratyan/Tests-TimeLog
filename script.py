import os
import time

def create_directory(directory_name):
    os.mkdir(directory_name);

def create_file(directory_name, current_time, status):
    filename = os.path.join(directory_name, f"{current_time}.log");
    with open(filename, 'w') as f:
        f.write(f'Status => {status}');

def main():
    directory = "tests";
    create_directory(directory);

    for i in range(1, 11):
        current_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime());
        if (int(time.strftime('%s')) % 2 == 0):
            create_file(directory, current_time, 'PASS');
        else:
            create_file(directory, current_time, 'FAIL');

        time.sleep(1);

if __name__ == "__main__":
    main();

