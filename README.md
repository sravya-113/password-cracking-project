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
