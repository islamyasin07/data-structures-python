from graph import Graph

if __name__ == "__main__":
    g = Graph()

    print("Building student campus graph...")

    g.add_edge("Ali", "Library")
    g.add_edge("Sara", "Cafeteria")
    g.add_edge("Omar", "Classroom A")
    g.add_edge("Ali", "Cafeteria")
    g.add_edge("Library", "Study Room")
    g.add_edge("Sara", "Classroom B")

    print("\nCampus movement graph:")
    g.display()
