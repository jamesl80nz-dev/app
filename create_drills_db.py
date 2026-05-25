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
        "Split Step Reaction Drill",
        "Beginner",
        "Footwork",
        "Tennis balls",
        "A warm up movement drill to improve reaction speed and readiness.",
        "Coach points left or right. Player split steps, reacts, and moves quickly to the ball. Keep the movement light and sharp.",
        "split_step.png",
        "warm up, footwork, reaction, movement, speed"
    ),
    (
        "Figure Eight Footwork",
        "Beginner",
        "Movement",
        "Cones",
        "A warm up drill to improve agility and movement efficiency.",
        "Set up two cones several metres apart. Player moves in a figure eight pattern using small adjustment steps and balanced recovery movement.",
        "figure_eight.png",
        "warm up, footwork, agility, movement"
    ),
    (
        "Crosscourt Consistency Rally",
        "Beginner",
        "Forehand",
        "Cones, tennis balls",
        "Develop forehand consistency and rally control.",
        "Players rally crosscourt using only half the court. Aim for 20 consecutive shots while maintaining height and margin over the net.",
        "crosscourt_consistency.png",
        "skills, consistency, forehand, rally, control"
    ),
    (
        "Serve Target Practice",
        "Intermediate",
        "Serve",
        "Targets, tennis balls",
        "Improve serve accuracy and placement.",
        "Place targets in wide, body, and T positions. Player serves 20 balls and scores points for each target zone hit.",
        "serve_targets.png",
        "skills, serve, accuracy, placement"
    ),
    (
        "Approach and Volley",
        "Intermediate",
        "Net Play",
        "Tennis balls",
        "Practice moving forward from the baseline to finish at the net.",
        "Feed a short ball. Player hits an approach shot deep crosscourt, moves forward quickly, and finishes with a controlled volley.",
        "approach_volley.png",
        "skills, net play, transition, volley"
    ),
    (
        "Two Ball Recovery Drill",
        "Intermediate",
        "Movement",
        "Tennis balls",
        "Train recovery speed after wide shots.",
        "Coach feeds one wide ball followed immediately by a ball to the opposite side. Focus on explosive recovery and balance before the second shot.",
        "two_ball_recovery.png",
        "fitness, movement, recovery, speed"
    ),
    (
        "Inside Out Forehand Pattern",
        "Advanced",
        "Forehand",
        "Cones, tennis balls",
        "Develop attacking forehand patterns.",
        "Player runs around the backhand to hit inside out forehands crosscourt, then attacks the next shorter ball down the line.",
        "inside_out_forehand.png",
        "skills, forehand, patterns, attack"
    ),
    (
        "Backhand Down the Line Control",
        "Intermediate",
        "Backhand",
        "Targets, tennis balls",
        "Improve directional backhand control.",
        "Rally crosscourt backhands before changing direction down the line on command while maintaining depth and balance.",
        "backhand_line.png",
        "skills, backhand, control, direction"
    ),
    (
        "Reaction Volley Drill",
        "Advanced",
        "Volley",
        "Tennis balls",
        "Improve fast hands and volley reactions.",
        "Coach stands close to the net and rapidly feeds balls at the player. Player focuses on compact volleys and quick reactions.",
        "reaction_volley.png",
        "skills, volley, reactions, net play"
    ),
    (
        "Defensive Lob Recovery",
        "Intermediate",
        "Defence",
        "Tennis balls",
        "Practice defensive recovery under pressure.",
        "Player is pushed wide by feeds, hits a defensive lob, then recovers quickly to the middle ready for the next shot.",
        "defensive_lob.png",
        "skills, defence, recovery, lob"
    ),
    (
        "Serve Plus One",
        "Advanced",
        "Serve",
        "Targets, tennis balls",
        "Build point construction after the serve.",
        "Player serves to a target then immediately attacks the first return with an aggressive forehand to an open area.",
        "serve_plus_one.png",
        "game play, serve, tactics, attack"
    ),
    (
        "Short Ball Attack",
        "Intermediate",
        "Attack",
        "Tennis balls",
        "Learn to recognise and attack short balls.",
        "Coach feeds neutral balls followed by a shorter ball. Player moves forward aggressively and finishes the point at the net if possible.",
        "short_ball_attack.png",
        "skills, attack, transition, footwork"
    ),
    (
        "Tie Break Pressure Game",
        "Advanced",
        "Mental",
        "Scoreboard, tennis balls",
        "Develop composure under match pressure.",
        "Players play repeated tie break scenarios starting at scores like 5-5 or 6-6. Focus on routines, shot selection, and emotional control.",
        "tiebreak_pressure.png",
        "game play, mental, pressure, match play"
    ),
    (
        "Cool Down Rally",
        "Beginner",
        "Recovery",
        "Tennis balls",
        "A low intensity warm down drill to finish the session with rhythm and control.",
        "Players rally slowly down the middle of the court, aiming for smooth technique, relaxed breathing, and consistent contact.",
        "cool_down_rally.png",
        "warm down, recovery, rhythm, control"
    ),
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