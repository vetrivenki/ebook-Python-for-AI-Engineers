services = ["api", "skip-test", "database", "failed-worker", "cache"]

for service in services:
    if service == "skip-test":
        continue
    if service == "failed-worker":
        print("Failure found; stop checking")
        break
    print(f"Healthy: {service}")
else:
    print("All services were checked")
