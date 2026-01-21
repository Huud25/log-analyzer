import re
from collections import Counter

IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

def read_lines(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]

def extract_ips(lines: list[str]) -> list[str]:
    ips = []
    for line in lines:
        ips.extend(IP_RE.findall(line))
    return ips

def classify_events(lines: list[str]) -> tuple[int, int]:
    failed = 0
    accepted = 0
    for line in lines:
        low = line.lower()
        if "failed password" in low:
            failed += 1
        if "accepted password" in low:
            accepted += 1
    return failed, accepted

def main():
    print("Log Analyzer - v1")

    path = input("Path do log (Enter para sample.log): ").strip() or "sample.log"

    lines = read_lines(path)
    ips = extract_ips(lines)
    failed, accepted = classify_events(lines)

    ip_counts = Counter(ips)

    print("\nResumo")
    print("- Linhas lidas:", len(lines))
    print("- Failed password:", failed)
    print("- Accepted password:", accepted)

    print("\nTop IPs (aparicoes no log):")
    for ip, count in ip_counts.most_common(5):
        print(f"- {ip}: {count}")

    # Heurística simples: se um IP aparece muito e há muitos "failed", sinaliza
    suspicious = []
    for ip, count in ip_counts.items():
        if count >= 3 and failed >= 3:
            suspicious.append((ip, count))

    if suspicious:
        print("\nAlertas (heuristica simples):")
        for ip, count in sorted(suspicious, key=lambda x: x[1], reverse=True):
            print(f"- Possivel brute force: {ip} (aparicoes: {count})")
    else:
        print("\nNenhum alerta obvio encontrado (pela heuristica atual).")

if __name__ == "__main__":
    main()
