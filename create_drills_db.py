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
    ),
    (
     "Crosscourt Consistency Rally",
    "Beginner",
    "Forehand",
    "Cones, tennis balls",
    "Develop forehand consistency and rally control.",
    "Players rally crosscourt using only half the court. Aim for 20 consecutive shots while maintaining height and margin over the net.",
    "crosscourt_consistency.png",
    "consistency, forehand, rally"
    ),
    (
    "Approach and Volley",
    "Intermediate",
    "Net Play",
    "Tennis balls",
    "Transition from baseline to net effectively.",
    "Feed a short ball. Player hits an approach shot deep crosscourt, moves forward quickly, and finishes with a controlled volley.",
    "approach_volley.png",
    "net play, transition, volley"
    ),
    (
    "Serve Accuracy Targets",
    "Intermediate",
    "Serve",
    "Targets, tennis balls",
    "Improve serve placement and control.",
    "Place targets in wide, body, and T positions. Player attempts to hit each target zone repeatedly while maintaining smooth service rhythm.",
    "serve_targets.png",
    "serve, accuracy, placement"
    ),
    (
    "Figure Eight Footwork",
    "Beginner",
    "Movement",
    "Cones",
    "Improve agility and movement efficiency.",
    "Set up two cones several metres apart. Player moves in a figure eight pattern using small adjustment steps and balanced recovery movement.",
    "figure_eight.png",
    "footwork, agility, movement"
    ),
    (
    "Two Ball Recovery Drill",
    "Intermediate",
    "Movement",
    "Tennis balls",
    "Train recovery speed after wide shots.",
    "Coach feeds one wide ball followed immediately by a ball to the opposite side. Focus on explosive recovery and balance before the second shot.",
    "two_ball_recovery.png",
    "movement, recovery, fitness"
    ),
    (
    "Inside Out Forehand Pattern",
    "Advanced",
    "Forehand",
    "Cones, tennis balls",
    "Develop attacking forehand patterns.",
    "Player runs around the backhand to hit inside out forehands crosscourt, then attacks the next shorter ball down the line.",
    "inside_out_forehand.png",
    "forehand, patterns, attack"
    ),
    (
    "Backhand Down the Line Control",
    "Intermediate",
    "Backhand",
    "Targets, tennis balls",
    "Improve directional backhand control.",
    "Rally crosscourt backhands before changing direction down the line on command while maintaining depth and balance.",
    "backhand_line.png",
    "backhand, control, direction"
    ),
    (
    "Reaction Volley Drill",
    "Advanced",
    "Volley",
    "Tennis balls",
    "Improve fast hands and volley reactions.",
    "Coach stands close to the net and rapidly feeds balls at the player. Player focuses on compact volleys and quick reactions.",
    "reaction_volley.png",
    "volley, reactions, net play"
    ),
    (
    "Defensive Lob Recovery",
    "Intermediate",
    "Defence",
    "Tennis balls",
    "Practice defensive recovery under pressure.",
    "Player is pushed wide by feeds, hits a defensive lob, then recovers quickly to the middle ready for the next shot.",
    "defensive_lob.png",
    "defence, recovery, lob"
    ),
    (
    "Serve Plus One",
    "Advanced",
    "Serve",
    "Targets, tennis balls",
    "Build point construction after the serve.",
    "Player serves to a target then immediately attacks the first return with an aggressive forehand to an open area.",
    "serve_plus_one.png",
    "serve, tactics, attack"
    ),
    (
    "Short Ball Attack",
    "Intermediate",
    "Attack",
    "Tennis balls",
    "Learn to recognise and attack short balls.",
    "Coach feeds neutral balls followed by a shorter ball. Player moves forward aggressively and finishes the point at the net if possible.",
    "short_ball_attack.png",
    "attack, transition, footwork"
    ),
    (
    "Tie Break Pressure Game",
    "Advanced",
    "Mental",
    "Scoreboard, tennis balls",
    "Develop composure under pressure.",
    "Players play repeated tie break scenarios starting at scores like 5-5 or 6-6. Focus on routines, shot selection, and emotional control.",
    "tiebreak_pressure.png",
    "mental, pressure, match play"
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