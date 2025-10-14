import matplotlib.pyplot as plt

def tcp_congestion_control_simulation(total_rounds, initial_ssthresh, loss_events):
    print("--- TCP Congestion Control Simulation ---")    
    cwnd = 1  
    ssthresh = initial_ssthresh
    cwnd_history = []
    for round_num in range(total_rounds):
        cwnd_history.append(cwnd)
        print(f"Round {round_num+1}: cwnd = {cwnd}, ssthresh = {ssthresh}")
        if round_num + 1 in loss_events:
            print(f"!! Packet Loss Detected at round {round_num + 1} !!")
            ssthresh = max(cwnd // 2, 2)
            cwnd = 1
            print("-> Entering Slow Start phase.")
            continue

        if cwnd < ssthresh:
            cwnd *= 2
            if round_num > 0 and cwnd_history[-1] >= ssthresh:
                 print("-> Entering Congestion Avoidance phase.")
        else:
            cwnd += 1
    plt.figure(figsize=(12, 6))
    plt.plot(range(1, total_rounds + 1), cwnd_history, marker='o', linestyle='-', label='cwnd')
    plt.axhline(y=initial_ssthresh, color='r', linestyle='--', label=f'Initial ssthresh = {initial_ssthresh}')
    for loss_round in loss_events:
        plt.axvline(x=loss_round, color='g', linestyle=':', label=f'Packet Loss at round {loss_round}')

    plt.title('TCP Congestion Window (cwnd) Simulation')
    plt.xlabel('Transmission Rounds')
    plt.ylabel('Congestion Window Size (in MSS)')
    plt.grid(True)
    plt.legend()
    plt.xticks(range(1, total_rounds + 1))
    plt.savefig('cwnd_plot.png')
    print("\nPlot saved as cwnd_plot.png")
    plt.show()


if __name__ == "__main__":
    TOTAL_ROUNDS = 25
    INITIAL_SSTHRESH = 16
    LOSS_EVENTS_AT_ROUNDS = [8, 17]
    
    tcp_congestion_control_simulation(TOTAL_ROUNDS, INITIAL_SSTHRESH, LOSS_EVENTS_AT_ROUNDS)
