import matplotlib.pyplot as plt
import random

# Simulation Parameters
ROUNDS = 50                  # Total transmission rounds (can be interpreted as time or ACK events)
LOSS_PROBABILITY = 0.1       # Probability of packet loss
MAX_CWND = 100               # Maximum window size cap

# TCP Variables
cwnd = 1                     # Initial congestion window
ssthresh = 16                # Initial slow start threshold
cwnd_history = []            # To store cwnd per round

for round in range(ROUNDS):
    # Simulate packet loss
    if random.random() < LOSS_PROBABILITY:
        print(f"[Round {round}] Packet loss detected. Timeout occurred.")
        ssthresh = max(cwnd // 2, 1)
        cwnd = 1  # Restart with slow start
    else:
        # If we're in slow start
        if cwnd < ssthresh:
            cwnd *= 2
            print(f"[Round {round}] Slow Start: cwnd increased to {cwnd}")
        else:
            # Congestion Avoidance
            cwnd += 1
            print(f"[Round {round}] Congestion Avoidance: cwnd increased to {cwnd}")

    # Enforce max cwnd
    cwnd = min(cwnd, MAX_CWND)

    # Store for plotting
    cwnd_history.append(cwnd)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(cwnd_history, marker='o', linestyle='-', color='blue')
plt.title('TCP Congestion Window Growth (cwnd)')
plt.xlabel('Transmission Round')
plt.ylabel('Congestion Window Size (cwnd)')
plt.grid(True)
plt.savefig('cwnd_plot.png')  # Required deliverable
plt.show()
