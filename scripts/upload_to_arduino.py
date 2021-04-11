import argparse

from src.arduino_upload import upload_ino_script

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='filepath for arduino script')
    parser.add_argument('-path', type=str,
                        help='filepath used to upload to arduino')
    args = parser.parse_args()
    upload_ino_script(args.path)
