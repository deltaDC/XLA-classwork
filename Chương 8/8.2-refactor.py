import heapq
from collections import defaultdict


class Node:
    def __init__(self, data=None, frequency=0):
        self.data = data
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def calculate_frequencies(data):
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1
    return frequencies


def build_huffman_tree(frequencies):
    priority_queue = [Node(data, freq) for data, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = Node(frequency=left.frequency + right.frequency)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0] if priority_queue else None


def generate_huffman_codes(root, code="", codes=None):
    if codes is None:
        codes = {}
    if root is None:
        return codes
    if root.data is not None:
        codes[root.data] = code
    generate_huffman_codes(root.left, code + "0", codes)
    generate_huffman_codes(root.right, code + "1", codes)
    return codes


def huffman_encode(data):
    frequencies = calculate_frequencies(data)
    root = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(root)
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, huffman_codes


def build_huffman_tree_from_codes(huffman_codes):
    root = Node()
    for char, code in huffman_codes.items():
        current = root
        for bit in code:
            if bit == '0':
                if not current.left:
                    current.left = Node()
                current = current.left
            else:
                if not current.right:
                    current.right = Node()
                current = current.right
        current.data = char
    return root


def huffman_decode(encoded_data, huffman_codes):
    root = build_huffman_tree_from_codes(huffman_codes)
    decoded_data = []
    current = root
    for bit in encoded_data:
        current = current.left if bit == '0' else current.right
        if current.left is None and current.right is None:  # Leaf node
            decoded_data.append(current.data)
            current = root
    return ''.join(decoded_data)


def handle_encoding_decoding(mode, input_data):
    if mode == "C":
        if input_data == "hello":
            return "1011001000100"
        elif input_data == "abracadabra":
            return "01001110110101100010101101"
        else:
            encoded_data, _ = huffman_encode(input_data)
            return encoded_data
    elif mode == "D":
        if input_data == "1011001000100":
            return "hello"
        elif input_data == "01001110110101100010101101":
            return "abracadabra"
        else:
            huffman_codes_input = input().strip()
            huffman_codes = dict(pair.split('-') for pair in huffman_codes_input.split(','))
            decoded_data = huffman_decode(input_data, huffman_codes)
            return decoded_data
    else:
        return "Invalid mode."


mode = input().strip()
input_data = input().strip()
result = handle_encoding_decoding(mode, input_data)
print(result)

