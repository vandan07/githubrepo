#!/usr/bin/env python3
"""
================================================================================
  MATCH DAY SCOUTING REPORT // VANDAN MAHAJAN (CAP #01)
  SYSTEMS x PRODUCT x AI · BENGALURU, INDIA
================================================================================
"""

import sys

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def print_banner():
    RED = "\033[91m"
    GOLD = "\033[93m"
    WHITE = "\033[97m"
    GRAY = "\033[90m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    banner = f"""{RED}{BOLD}
  ======================================================================
     ____  _        _ __   __   ____   ____  _     ____  
    |  _ \\| |      / \\\\ \\ / /  | __ ) / __ \\| |   |  _ \\ 
    | |_) | |     / _ \\\\ V /   |  _ \\| |  | | |   | | | |
    |  __/| |___ / ___ \\| |    | |_) | |__| | |___| |_| |
    |_|   |_____/_/   \\_\\_|    |____/ \\____/|_____|____/ 
  ======================================================================{RESET}
  {GOLD}{BOLD}VANDAN MAHAJAN // SOFTWARE ENGINEER{RESET}
  {WHITE}SYSTEMS x PRODUCT x AI · BENGALURU, IN · CAP #01{RESET}
  {GRAY}----------------------------------------------------------------------{RESET}
"""
    print(banner)

def print_report():
    RED = "\033[91m"
    GOLD = "\033[93m"
    WHITE = "\033[97m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    sections = [
        (f"{GOLD}[1] TACTICAL CREDO & PHILOSOPHY{RESET}", [
            f"{BOLD}\"I don't just write code. I think first.\"{RESET}",
            f"Formula: {GOLD}LOGIC x COMMON SENSE x PROBLEM SOLVING x ENGINEERING{RESET}",
            "Rule: Read the pitch -> Identify root cause -> Simplify -> Execute bold.",
            "Good engineering isn't about writing more code. It's about making better decisions."
        ]),
        (f"{RED}[2] THE PLAYING XI (CORE ARSENAL){RESET}", [
            f"* {WHITE}Top Order (Backend):{RESET} Java 17/21, Spring Boot, Spring MVC, JPA/Hibernate, Virtual Threads",
            f"* {WHITE}Middle Order (Data):{RESET} PostgreSQL, MySQL, Redis Cluster, MongoDB",
            f"* {WHITE}Pace Attack (Infra):{RESET} Apache Kafka, RabbitMQ, Docker, AWS, Jenkins, Linux",
            f"* {WHITE}Finisher (GenAI):{RESET}    LLMs Architecture, Hybrid RAG, ChromaDB, Vector Embeddings, Ollama",
            f"* {WHITE}Fielding (UI):{RESET}       React, Vite, TypeScript/JavaScript"
        ]),
        (f"{GOLD}[3] MATCH HIGHLIGHTS & BENCHMARKS{RESET}", [
            f"* {WHITE}Distributed Ledger:{RESET} Ingestion throughput {GREEN}850 -> 5,400+ req/s{RESET} | p99 {GREEN}1200ms -> 38ms{RESET}",
            f"* {WHITE}Enterprise RAG:{RESET}     Query latency {GREEN}15.2s -> 0.85s (94% speedup){RESET} | Precision {GREEN}94.2%{RESET}",
            f"* {WHITE}Apex Cache Defense:{RESET} Cache hit ratio {GREEN}71.4% -> 98.7%{RESET} | DB Load {GREEN}86% -> 18%{RESET}"
        ]),
        (f"{GREEN}[4] LIVE SCORECARD & TELEMETRY{RESET}", [
            f"* System Uptime:       {GREEN}99.99%{RESET}",
            f"* Service Latency p99: {GREEN}< 42ms{RESET}",
            f"* Event Ingestion:     {GREEN}5,000+ events/sec{RESET}",
            f"* Operational Status:  {BOLD}{GREEN}IN THE MIDDLE (MATCH READY){RESET}"
        ]),
        (f"{GOLD}[5] MATCH CREDENTIALS & CONNECT{RESET}", [
            "* GitHub:   https://github.com/vandan-mahajan",
            "* LinkedIn: https://linkedin.com/in/vandan-mahajan",
            "* Email:    vandanmahajan@example.com",
            "* Venue:    Bengaluru, India (12.9784 deg N, 77.5994 deg E)"
        ])
    ]

    for title, lines in sections:
        print(title)
        for line in lines:
            print(f"  {line}")
        print()

if __name__ == "__main__":
    print_banner()
    print_report()
