from dataclasses import dataclass

@dataclass
class Packet:
    source_ip: str
    dest_ip: str
    payload: str
    priority: int

def fifo_scheduler(packet_list: list) -> list:
    return packet_list.copy()

def priority_scheduler(packet_list: list) -> list:
    return sorted(packet_list, key=lambda p: p.priority)

if __name__ == "__main__":
    packets = [
        Packet("A", "B", "Data Packet 1", 2),
        Packet("A", "B", "Data Packet 2", 2),
        Packet("A", "B", "VOIP Packet 1", 0),
        Packet("A", "B", "Video Packet 1", 1),
        Packet("A", "B", "VOIP Packet 2", 0)
    ]
    fifo_order = fifo_scheduler(packets)
    print([p.payload for p in fifo_order])
    priority_order = priority_scheduler(packets)
    print([p.payload for p in priority_order])
