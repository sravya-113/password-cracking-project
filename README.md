# 🔐 Password Cracking & Hashing Demonstration

This project showcases password cracking techniques using **John the Ripper**, **Hashcat**, and a **Python hash generator**. It demonstrates how attackers can exploit weak hashing algorithms (like MD5) to crack passwords using dictionary attacks.

---

## 📁 Project Structure

password-cracking-project/


├── generate_hashes.py # Python script to generate MD5 hashes

├── hashes.txt # Stores the hashed passwords

├── crack_with_john.sh # Bash script using John the Ripper

├── crack_with_hashcat.sh # Bash script using Hashcat

├── report.md # Project documentation

├── README.md # This file



## 🎯 Objective

- Understand how password hashing works.
- Learn how attackers can crack passwords using tools like John and Hashcat.
- Emphasize why MD5 is not suitable for password protection.
- Encourage strong, salted password storage practices.

---

## 🛠 Tools Used

| Tool           | Purpose                              |
|----------------|--------------------------------------|
| Python 3       | Generate password hashes             |
| Hashcat        | GPU-based hash cracking              |
| John the Ripper| CPU-based password cracker           |
| Kali Linux     | Penetration testing environment      |
| rockyou.txt    | Wordlist for dictionary attacks      |

---

## 🚀 How to Use

### 🔧 Step 1: Clone the Repo


git clone https://github.com/sravya/password-cracking-project.git
cd password-cracking-project

🧪 Step 2: Generate Hashes

Run the following Python script to create MD5 hashes for sample passwords:



python3 generate_hashes.py
This will create a file hashes.txt like this:



🔓 Step 3: Crack with John the Ripper

chmod +x crack_with_john.sh
./crack_with_john.sh

john --show --format=raw-md5 hashes.txt


⚡ Step 4: Crack with Hashcat (Optional)
Make sure Hashcat is installed and your GPU is set up.


chmod +x crack_with_hashcat.sh

./crack_with_hashcat.sh

Hashcat will attempt to crack hashes.txt using rockyou.txt.

📄 Wordlist Setup
Make sure the rockyou.txt wordlist is extracted (Kali comes with it compressed):


sudo gunzip /usr/share/wordlists/rockyou.txt.gz

If it's missing, you can download it from trusted sources.

📘 Sample Code Explanation


generate_hashes.py

Generates MD5 hashes for a list of sample passwords:



📎 report.md Includes
What are hashing algorithms?

Difference between MD5, SHA256, and bcrypt.

Why MD5 is insecure.

How dictionary attacks work.

Screenshots of results (optional).

Real-world implications.

⚠️ Disclaimer
Educational Purposes Only:
This project is meant to demonstrate password cracking in a controlled environment. Do NOT use these techniques for unethical or unauthorized activities.

🙋‍♀️ Author
Sravya
GitHub: https://github.com/sravya

⭐ Like This Project?
Give it a ⭐ on GitHub to show your support!



---

### ✅ How to Add It:

1. Copy the full text above.
2. Open your project folder in Kali.
3. Run:


nano README.md
