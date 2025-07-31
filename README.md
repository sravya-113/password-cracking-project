\# 🔐 Password Cracking & Hashing Demonstration

This project demonstrates password cracking techniques using **John the Ripper**, **Hashcat**, and a **Python hash generator**. It highlights how weak hashing algorithms like MD5 can be exploited by attackers using dictionary attacks.

---

## 📁 Project Structure

password-cracking-project/

├── crack_with_hashcat.sh # Bash script to crack hashes with Hashcat

├── crack_with_john.sh # Bash script to crack hashes with John the Ripper

├── generate_hashes.py # Python script to generate MD5 password hashes

├── hashes.txt # File storing generated password hashes

├── screenshot/

│ └── john_results.jpg # Screenshot of John the Ripper results

├── README.md # This README file

└── report.md # Detailed project report 


---

## 🎯 Objective

- Understand password hashing and why MD5 is insecure.
- Learn how password hashes can be cracked using popular tools.
- Emphasize the importance of strong, salted password storage.
- Gain practical experience using Kali Linux tools.

---

## 🛠 Tools Used

| Tool              | Purpose                              |
|-------------------|------------------------------------|
| Python 3          | Generate sample MD5 password hashes|
| John the Ripper   | CPU-based password cracking tool   |
| Hashcat           | GPU-accelerated hash cracking tool |
| Kali Linux        | Penetration testing OS environment |
| rockyou.txt       | Common wordlist for dictionary attacks|

---



📷 Screenshot:

![John the Ripper Results](screenshot/john_results.jpg)



## 🚀 How to Use

### Step 1: Clone the Repository

```bash
git clone https://github.com/sravya/password-cracking-project.git
cd password-cracking-project
Step 2: Generate Password Hashes
Run the Python script to create MD5 hashes from sample passwords:

python3 generate_hashes.py




Step 3: Crack Hashes Using John the Ripper
Make the script executable and run:


chmod +x crack_with_john.sh
./crack_with_john.sh
Then view cracked results:


john --show --format=raw-md5 hashes.txt



⚠️ Disclaimer
This project is for educational purposes only. Do NOT use it for unauthorized or malicious activities.

