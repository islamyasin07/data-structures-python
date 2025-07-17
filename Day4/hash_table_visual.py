import matplotlib.pyplot as plt

hash_table = {
    0: [["Sara", 90]],
    1: [],
    2: [["Ali", 75], ["Omar", 80]],
    3: [],
    4: [["Lana", 95]]
}

def draw_hash_table(table):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, len(table) + 1)
    ax.axis('off')

    for i, bucket in enumerate(table.values()):
        y = len(table) - i
        ax.text(0.5, y, f"Bucket {i}", fontsize=12, va='center')
        for j, pair in enumerate(bucket):
            key, value = pair
            ax.text(2 + j * 2, y, f"{key}:{value}", bbox=dict(boxstyle="round", fc="lightblue"), fontsize=10)

    plt.title("Hash Table Visualization with Chaining")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_hash_table(hash_table)
