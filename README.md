# Python Ransomware Simulation

An educational cybersecurity project built with Python to understand file encryption, decryption, and basic ransomware behavior.

## About the Project

This project demonstrates how ransomware-like file encryption works using the Fernet symmetric encryption mechanism from Python's Cryptography library.

It consists of two Python scripts:

- `ransomware.py` – Demonstrates file encryption.
- `decrypt.py` – Demonstrates file decryption using the generated encryption key and a secret phrase.

## Features

- Automatic Fernet key generation.
- File encryption using symmetric cryptography.
- Encryption key storage.
- Password-based decryption access.
- File decryption and recovery.

## Technologies Used

- Python 3
- Cryptography (Fernet)
- OS module

## Project Structure

```text
malware/
├── ransomware.py
├── decrypt.py
├── requirements.txt
├── README.md
├── .gitignore
└── samples/
    ├── file1.txt
    ├── file2.txt
    └── file3.txt
```

## Installation

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Usage

Run the encryption demonstration:

```bash
python ransomware.py
```

Run the decryption demonstration:

```bash
python decrypt.py
```

## Disclaimer

This project was created strictly for educational purposes to understand file encryption, cryptography, and ransomware behavior.

**WARNING:** The encryption script overwrites files in its working directory. Run it only in a disposable test environment containing sample files. Always maintain backups of original files and the encryption key.

This project is not intended for malicious use or deployment.
