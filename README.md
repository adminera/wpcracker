<h1 align="center">
  <img src="static/WP.png" alt="wpcracker" width="200px" length="300px">
  <br>
</h1>

<h4 align="center">WordPress Login Password Cracker Python</h4>

<p align="center">
  <a href="#Features">Features</a> •
  <a href="#Install">Install</a> •
  <a href="#Post-Installation">Post Installation</a> •
  <a href="#Usage">Usage</a> 
  
</p>

---

`wpcracker` is a Python-based brute-force tool designed to streamline credential testing for WordPress login pages, tailored for ethical hackers and penetration testers.

By leveraging the `Requests` library for HTTP requests and `lxml` for parsing login forms, it automates the process of testing username and password combinations from a provided wordlist.

The tool supports multi-threaded brute-forcing to efficiently cycle through passwords while managing session cookies and implementing delays to bypass account lockouts.

With organized output and a focus on verifying successful logins, `wpcracker` saves time and enhances precision during security assessments of WordPress installations, ensuring testers can focus on validated results in a controlled environment.

---

# Features

- Automated Brute-Forcing: Tests username/password combos using requests and lxml to parse WordPress login forms.

- Multi-Threaded Speed: Runs 10 threads with delays to avoid lockouts, boosting efficiency.

- Reliable Results: Manages sessions and detects successful logins with a success string.

# Install

`wpcracker` requires 2 libraries from Python to function properly, requests and lxml which can be installed with pip

```sh
pip install requests
pip install lxml
```

# Post-Installation

- In wpcracker.py, you will need to adjust the TARGET variable to the WordPress site you would like to target
- You should also adjust the wordlist variable to point to the path of your wordlist
  
# Usage

```sh
python wpcracker.py
```
