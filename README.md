# Python Brute-force Script for Lab "Hammer" (TryHackMe)

## 1. Context
This is a Python script, which is written to automate the brute-force process in the lab **[Hammer](https://tryhackme.com/room/hammer)** on TryHackMe platform.
The script works only on the pre-configured lab on TryHackMe.
It aims to reset password of an explored email via brute-forcing 4-digit OTP.

## 2. Purpose
The script implements two main functions:
* Automatically brute-force 4-digit OTP code.
* Automatically change to new password after submitting correct OTP.

## 3. Key logic
* The script uses `requests`, `random` and `threading` libraries of Python to send POST request to `http://local_TryHackMe_IP:Port/reset_password.php`
* Create a loop for trials and error from `0000` to `9999`.
* Divide the loop into small threads, thus improve the running time.
* For each thread, because the server implements rate-limit against brute-force, the script uses a header `X-Forwarded-For` with random number of IP and successfully bypass the server.
* Analyze the response text and code from the server to determine if it's successful or not.
* If successful, change to new password.
