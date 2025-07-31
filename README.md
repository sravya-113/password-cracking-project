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

yaml
Copy
Edit

---

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

```bash
git clone https://github.com/sravya/password-cracking-project.git
cd password-cracking-project
🧪 Step 2: Generate Hashes
Run the following Python script to create MD5 hashes for sample passwords:

bash
Copy
Edit
python3 generate_hashes.py
This will create a file hashes.txt like this:

Copy
Edit
5f4dcc3b5aa765d61d8327deb882cf99
e10adc3949ba59abbe56e057f20f883e
d8578edf8458ce06fbc5bb76a58c5ca4
🔓 Step 3: Crack with John the Ripper
bash
Copy
Edit
chmod +x crack_with_john.sh
./crack_with_john.sh
Once completed, show cracked results:

bash
Copy
Edit
john --show --format=raw-md5 hashes.txt
Expected output:

makefile
Copy
Edit
?:password
?:123456
?:qwerty
⚡ Step 4: Crack with Hashcat (Optional)
Make sure Hashcat is installed and your GPU is set up.

bash
Copy
Edit
chmod +x crack_with_hashcat.sh
./crack_with_hashcat.sh
Hashcat will attempt to crack hashes.txt using rockyou.txt.

📄 Wordlist Setup
Make sure the rockyou.txt wordlist is extracted (Kali comes with it compressed):

bash
Copy
Edit
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
If it's missing, you can download it from trusted sources.

📘 Sample Code Explanation
generate_hashes.py
Generates MD5 hashes for a list of sample passwords:

python
Copy
Edit
import hashlib

passwords = ["password", "123456", "qwerty"]

with open("hashes.txt", "w") as f:
    for pwd in passwords:
        hash_md5 = hashlib.md5(pwd.encode()).hexdigest()
        f.write(hash_md5 + "\n")
📊 Project Output (Example)
Plain Password	MD5 Hash	Cracked
password	5f4dcc3b5aa765d61d8327deb882cf99	✅
123456	e10adc3949ba59abbe56e057f20f883e	✅
qwerty	d8578edf8458ce06fbc5bb76a58c5ca4	✅

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

yaml
Copy
Edit

---

### ✅ How to Add It:

1. Copy the full text above.
2. Open your project folder in Kali.
3. Run:

```bash
nano README.md
