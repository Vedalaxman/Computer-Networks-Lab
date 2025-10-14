import random
import time

# Parameters
TOTAL_FRAMES = 10           # Total frames to send
WINDOW_SIZE = 4             # Window size N
LOSS_PROBABILITY = 0.2      # Probability of frame loss (20%)
TIMEOUT = 2                 # Timeout in seconds

def send_frame(frame_number):
    print(f"Sending Frame {frame_number}")
    if random.random() < LOSS_PROBABILITY:
        print(f"Frame {frame_number} lost.")
        return False
    else:
        time.sleep(0.5)  # Simulate delay
        return True

def go_back_n_arq():
    base = 0                  # Oldest unacknowledged frame
    next_seq_num = 0          # Next frame to send
    ack_expected = 0          # Expected ACK number

    while base < TOTAL_FRAMES:
        # Send frames in window
        while next_seq_num < base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
            send_frame(next_seq_num)
            next_seq_num += 1

        # Simulate receiver processing and send cumulative ACK
        # Randomly decide if any frame in window is lost
        lost_frame = -1
        for f in range(base, min(base + WINDOW_SIZE, TOTAL_FRAMES)):
            if random.random() < LOSS_PROBABILITY:
                lost_frame = f
                break

        if lost_frame == -1:
            # No loss, cumulative ACK for last frame in window
            ack_received = min(base + WINDOW_SIZE - 1, TOTAL_FRAMES -1)
            print(f"ACK {ack_received + 1} received")
            base = ack_received + 1
            print(f"Window slides to {base} {min(base + WINDOW_SIZE - 1, TOTAL_FRAMES -1)}")
        else:
            # Loss occurred, retransmit from lost_frame
            print(f"Frame {lost_frame} lost, retransmitting frames {lost_frame} to {min(base + WINDOW_SIZE - 1, TOTAL_FRAMES - 1)}")
            # Retransmit from lost_frame
            next_seq_num = lost_frame
            base = lost_frame

        time.sleep(TIMEOUT)  # Wait before next send

if __name__ == "__main__":
    print("Go-Back-N ARQ Simulation Started\n")
    go_back_n_arq()
    print("\nAll frames sent and acknowledged.")
