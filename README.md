# 15-Digit Checksum Generator & Validator

A high-performance Python implementation of a custom mathematical validation algorithm (Luhn Mod10 variant). Perfect for system configurations, tracking numbers, or processing data strings reliably at scale.

## Features
- **High Performance:** Utilizes raw mathematical operators (`//`, `%`) over string casting for maximum algorithmic efficiency.
- **Bi-directional:** Easily generate 15-digit keys from a 14-digit payload, or validate existing 15-digit strings.
- **Zero Dependencies:** Built entirely with native Python.

## Usage
Run the script using Python 3:
```bash
python generator.py