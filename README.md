# rijandael-out

To run this program, you need to make sure you have the Tkinter module for Python installed, and you also need to make sure 
OpenSSL and ccrypt are installed on your system. The program also outputs the file output.txt every time the script encrypts a file.

The program makes a random base64 hash for your file with openssl and then encrypts the file with ccrypt. Together with the ccrypt program, 
your file has 2x security. Just keep the issued password in a safe place.

Use with terminal:$ python3 rijandael-out.py

