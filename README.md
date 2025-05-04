Network Traffic Analyzer

The **Network Traffic Analyzer** is a Python-based network monitoring and analysis tool developed as part of a course project in Computer Networks (2024). Designed to bridge theoretical concepts with practical implementation, this project allows users to capture, parse, and analyze network traffic using open-source technologies like Wireshark and PyShark. The primary focus is on identifying TCP/IP and HTTP traffic patterns, visualizing protocol distribution, and detecting potential anomalies or suspicious behavior in the data flow.

The analyzer captures packets either in real time or from a pre-recorded `.pcap` file and processes them using Python libraries. It extracts high-level protocol information, generates traffic reports, and provides visual insights into network behavior. The project leverages PyShark (a Python wrapper for TShark, the terminal version of Wireshark), along with pandas and matplotlib for data handling and visualization. These tools allow for easy integration, portability, and customization for academic and small-scale security research purposes.

This tool is especially beneficial for students, educators, and enthusiasts interested in learning the basics of network forensics, traffic classification, and anomaly detection. The project simulates basic threat identification processes by scanning for irregular patterns in protocol usage, port access, and packet distribution. The results are presented in the form of bar graphs and statistical summaries, making it easier to interpret findings and include them in reports.

A sample `.pcap` file is included for demonstration purposes. It contains safe, anonymized traffic that users can analyze to understand the tool’s functionality without needing to capture real-time traffic themselves. Users may also customize the Python script to extract additional features such as source/destination IPs, response codes, or even DNS queries for more advanced use cases.

This project was built with a strong focus on documentation, clarity, and reproducibility. All dependencies are listed in the `requirements.txt` file, and the `README.md` provides step-by-step instructions for installation, execution, and sample outputs. By combining powerful tools and clean Python scripting, the Network Traffic Analyzer demonstrates how simple yet effective security monitoring systems can be prototyped for educational or proof-of-concept applications.


