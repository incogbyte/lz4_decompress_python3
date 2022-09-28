import sys
import struct
import lz4.block
import os.path
import argparse


menu = argparse.ArgumentParser(description="lz4 decompress python3 | author=nopsh3ll")
menu.add_argument('-s', '--single', help="single DLL", default="")
menu.add_argument('-d', '--dir', help='directory with all DLLs', default="")
args = menu.parse_args()

in_file = args.single
dir_with_dll = args.dir

print(f"> in_file: {in_file}")
print(f"> dir_with_dll: {dir_with_dll}")

def single_file_parse(single_file):

    with open(single_file, "rb") as compressed_file:
        compressed_data = compressed_file.read()

    header = compressed_data[:4]
    
    if header != b'XALZ':
        print(f">> Filename {single_file} with wrong header, aborting...")
        sys.exit("[!] Wrong header, aborting...!")

    packed_payload_len = compressed_data[8:12]
    unpacked_payload_len = struct.unpack('<I', packed_payload_len)[0]
    compressed_payload = compressed_data[12:]
    decompressed_payload = lz4.block.decompress(
        compressed_payload, uncompressed_size=unpacked_payload_len)

    out_file = single_file.rsplit(".", 1)[0] + "_out.dll"

    if os.path.isfile(out_file):
        print(f">> File: {out_file} already exists")

    with open(out_file, "wb") as decompressed_file:
        decompressed_file.write(decompressed_payload)
        print("[i] Success!")
        print("[i] File [" + out_file + "] was created as result!")


def dir_parse(dir_name):

    if os.path.isdir(dir_name):
        for dll in os.listdir(dir_name):
            f = os.path.join(dir_name, dll)
            if os.path.isfile(f):
                single_file_parse(f)

def main():

    if len(sys.argv) <= 2:
        menu.print_help()

    if in_file != "":
        single_file_parse(in_file)

    if dir_with_dll != "":
        dir_parse(dir_with_dll)

if __name__ == "__main__":
    main()
