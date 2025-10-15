print(" Decrypted Log Entries:\n")
for entry in log_entries:
    print(decrypt(entry, ENCRYPTION_KEY))
