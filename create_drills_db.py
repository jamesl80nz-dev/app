import sqlite3

connection = sqlite3.connect("drills.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS drills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    skill_level TEXT,
    focus_area TEXT,
    equipment TEXT,
    description TEXT,
    instructions TEXT,
    image_filename TEXT,
    tags TEXT
)
""")

sample_drills = [
    (
        "Cross-court Consistency",
        "Beginner",
        "Forehand",
        "Cones, tennis balls",
        "A rally drill to improve control and consistency.",
        "Player A hits cross-court forehands. Player B returns cross-court. Aim for 10 successful shots in a row.",
        "cross_court.png",
        "forehand, consistency, control, accuracy"
    ),
    (
        "Serve Target Practice",
        "Intermediate",
        "Serve",
        "Cones, tennis balls",
        "A serving drill focused on accuracy.",
        "Place cones in the service box. Serve 20 balls and score points for each target hit.",
        "serve_targets.png",
        "serve, accuracy, power, placement"
    ),
    (
        "Split Step Reaction Drill",
        "Beginner",
        "Footwork",
        "Tennis balls",
        "A movement drill to improve reaction speed.",
        "Coach points left or right. Player split steps, reacts, and moves quickly to the ball.",
        "split_step.png",
        "footwork, reaction, movement, speed"
    )
]

cursor.executemany("""
INSERT INTO drills (
    title, skill_level, focus_area, equipment, description, instructions, image_filename, tags
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", sample_drills)

connection.commit()
connection.close()

print("Drills database created successfully.")