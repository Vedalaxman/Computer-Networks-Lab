import random
import time

# Parameters
TOTAL_FRAMES = 5           # Total number of frames to send
LOSS_PROBABILITY = 0.3     # Probability of frame loss (30%)
TIMEOUT = 2                # Timeout in seconds

def send_frame(frame_number):
    print(f"Sending Frame {frame_number}")
    # Simulate random loss
    if random.random() < LOSS_PROBABILITY:
        print(f"Frame {frame_number} lost, retransmitting after timeout...")
        return False
    else:
        # Simulate network delay
        time.sleep(1)
        print(f"ACK {frame_number} received")
        return True

def stop_and_wait_arq():
    current_frame = 0
    while current_frame < TOTAL_FRAMES:
        success = send_frame(current_frame)
        if success:
            current_frame += 1
        else:
            # Simulate timeout
            time.sleep(TIMEOUT)

if __name__ == "__main__":
    print("Stop-and-Wait ARQ Simulation Started\n")
    stop_and_wait_arq()
    print("\nAll frames sent and acknowledged.")
