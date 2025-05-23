# Merge Sort Technique To Sort Companies Customer Logs (Timestamp)
def mergeLogic():
    # initializing pointers for both branches
    i = 0
    j = 0

    # Create an empty list to store the merged logs.
    customer_logs = [0] * (len(branch_A_logs) + len(branch_B_logs))  # The size is the total of both lists, filled initially with zeros.

    k = 0  # This keeps track of the next available index in customer_logs

    # Traverse both branch logs while elements remain in both
    while i < len(branch_A_logs) and j < len(branch_B_logs):
        # Compare timestamps from both branches
        if branch_A_logs[i] <= branch_B_logs[j]:
            # Avoid adding duplicates
            if branch_A_logs[i] not in customer_logs[:k]:
                customer_logs[k] = branch_A_logs[i]  # Add to result
                k += 1
            i += 1  # Move pointer in branch A
        else:
            # Avoid adding duplicates
            if branch_B_logs[j] not in customer_logs[:k]:
                customer_logs[k] = branch_B_logs[j]  # Add to result
                k += 1
            j += 1  # Move pointer in branch B

    # If anything remains in branch A's logs, add to result (skip duplicates)
    while i < len(branch_A_logs):
        if branch_A_logs[i] not in customer_logs[:k]:
            customer_logs[k] = branch_A_logs[i]
            k += 1
        i += 1

    # If anything remains in branch B's logs, add to result (skip duplicates)
    while j < len(branch_B_logs):
        if branch_B_logs[j] not in customer_logs[:k]:
            customer_logs[k] = branch_B_logs[j]
            k += 1
        j += 1

    # Print the merged list (duplicates removed, but not sorted if input isn't)
    print(customer_logs[:k])

# Logs from two company branches, already sorted by timestamp
branch_A_logs = [1010, 1030, 1100, 1500, 1600]
branch_B_logs = [1000, 1030, 1500, 1130, 1700]

# Display the original logs
print(f"Branch A Logs:{branch_A_logs}")
print(f"Branch_B_Logs:{branch_B_logs}")

# Display merged logs (duplicates removed)
print("\nAfter Merge:")
mergeLogic()
