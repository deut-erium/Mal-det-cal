# Malware Detection
Utilized Machine Learning techniques to detect malware in Portable Executable (PE) files using static and dynamic analysis data.

## IIT Kanpur Hackathon

[Problem Statement](./IITK_Malware_Problem_Final.pdf)

## Dataset

```
Static_Analysis_Data
├── Benign
│   ├── 0a0ee0aa381260d43987e98dd1a6f4bab11164e876f21db6ddb1db7c319c5cf8
│   │   ├── String.txt
│   │   └── Structure_Info.txt
│   └── 0a2adcac2b16b02d475e9d47b4772b77b0b4269132f07557c7ef6081727585da
│       ├── String.txt
│       └── Structure_Info.txt
└── Malware
	├── Backdoor
	│   ├── 0a21ef18ba03622736a8edd5390afbab6088dcacc3d5877eb0b28206285f569d
	│   │   ├── String.txt
	│   │   └── Structure_Info.txt
	│   └── 0a56a947d9c0be507b6aa0e2b569ca7eed39e5e802c8cf78be71adda9d324eae
	│       ├── String.txt
	│       └── Structure_Info.txt
	├── Trojan
	│   ├── 0a13ed78effd1eede88b149cc50a65828a9b19dc1c8bfe42fe66b21a63d813fa
	│   │   ├── String.txt
	│   │   └── Structure_Info.txt
	│   └── 0a1a645818c217ff8941a4c909398e9ebf480796541688b0937b1be4a752ede1
	│       ├── String.txt
	│       └── Structure_Info.txt
	├── TrojanDownloader
	│   ├── 0a25a55f10436c835b43f77b0852cb3845db3752984a1cfe90cef54ad344c5d5
	│   │   ├── String.txt
	│   │   └── Structure_Info.txt
	│   └── 0a9e83077e39d2046633505e3057edbcf470077b23e4297b40df27196cdad3f9
	│       ├── String.txt
	│       └── Structure_Info.txt
	├── TrojanDropper
	│   ├── 0a0f9593f922df76a1057b9cad7df347bfdd19a6f146bf28ec69ca644a910c99
	│   │   ├── String.txt
	│   │   └── Structure_Info.txt
	│   └── 0a7ade6b0ab771be9483b5fa1946bc526e9e378bccf652c47cdef8329f2168cc
	│       ├── String.txt
	│       └── Structure_Info.txt
	├── Virus
	│   ├── 0b5e1d76c90b5a9a16e9bd843483a8157620d111ed4694ae128c57ea8868f738
	│   │   ├── String.txt
	│   │   └── Structure_Info.txt
	│   └── 0b609dff72a315f2bb2181d7576f3c969542e0cd9be69d28b36453a626d2e921
	│       ├── String.txt
	│       └── Structure_Info.txt
	└── Worm
	    ├── 0a0dbf095a4e8d6ea7d656126ee0d6b24915981c7528d6a4fb14761097e65999
	    │   ├── String.txt
	    │   └── Structure_Info.txt
	    └── 0a1fe0f21e5ea80b1b7e85c89ca07a86630e33ed4758627c40310509b37fae35
	        ├── String.txt
	        └── Structure_Info.txt
```

```
Dynamic_Analysis_Data
├── Benign
│   ├── 0a0ee0aa381260d43987e98dd1a6f4bab11164e876f21db6ddb1db7c319c5cf8.json
│   └── 0a2adcac2b16b02d475e9d47b4772b77b0b4269132f07557c7ef6081727585da.json
└── Malware
	├── Backdoor
	│   ├── 0a21ef18ba03622736a8edd5390afbab6088dcacc3d5877eb0b28206285f569d.json
	│   └── 0a56a947d9c0be507b6aa0e2b569ca7eed39e5e802c8cf78be71adda9d324eae.json
	├── Trojan
	│   ├── 0a13ed78effd1eede88b149cc50a65828a9b19dc1c8bfe42fe66b21a63d813fa.json
	│   └── 0a1a645818c217ff8941a4c909398e9ebf480796541688b0937b1be4a752ede1.json
	├── TrojanDownloader
	│   ├── 0a25a55f10436c835b43f77b0852cb3845db3752984a1cfe90cef54ad344c5d5.json
	│   └── 0a9e83077e39d2046633505e3057edbcf470077b23e4297b40df27196cdad3f9.json
	├── TrojanDropper
	│   ├── 0a0f9593f922df76a1057b9cad7df347bfdd19a6f146bf28ec69ca644a910c99.json
	│   └── 0a7ade6b0ab771be9483b5fa1946bc526e9e378bccf652c47cdef8329f2168cc.json
	├── Virus
	│   ├── 0b5e1d76c90b5a9a16e9bd843483a8157620d111ed4694ae128c57ea8868f738.json
	│   └── 0b609dff72a315f2bb2181d7576f3c969542e0cd9be69d28b36453a626d2e921.json
	└── Worm
	    ├── 0a0dbf095a4e8d6ea7d656126ee0d6b24915981c7528d6a4fb14761097e65999.json
	    └── 0a1fe0f21e5ea80b1b7e85c89ca07a86630e33ed4758627c40310509b37fae35.json
```

## Feature Extraction (Pre-Processing)
### Static Analysis Data

- Packer Info
- Linked binaries and functions
- DLLs
- Number of strings
- Size of strings.txt
- Networking APIs
- System file functions
- Structure Info
	- PE Sections
		- Entropy
		- Name
		- virtual_size
		- raw_data_size

### Dynamic Analysis Data

- Behavior
	- count of API calls
	- file_created
	- file_written
	- directory_created
	- dll_loaded
	- file_opened
	- regkey_opened
	- guid
	- file_read
	- regkey_read
	- regkey_deleted
	- directory_enumerated
	- directory_removed
	- mutex
	- connects_ip
- Network
	- UDP source and destination IPs
	- DNS requests and answers
	- ICMP source and destination info
	- HTTP requests
	- TCP source and destination IPs

## Feature Selection
### Section Entropy
The PE sections contain data which usually has a known entropy. Higher entropy can indicate packed data. Malicious files are commonly packed to avoid static analysis since the actual code is usually stored encrypted in one of the sections and will only be extracted at runtime.    
So entropy is an important feature, we used average, min and max entropy as separate features.   


