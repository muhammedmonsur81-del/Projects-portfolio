"""
WAEC Secondary School Result Calculator
Calculates grades, remarks, and summary for a student's WAEC subjects.
"""

# WAEC subjects commonly offered
WAEC_SUBJECTS = [
    "English Language",
    "Mathematics",
    "Biology",
    "Chemistry",
    "Physics",
    "Economics",
    "Government",
    "Literature in English",
    "Geography",
    "Agricultural Science",
    "Further Mathematics",
    "Commerce",
    "Accounting",
    "Christian Religious Studies",
    "Islamic Religious Studies",
    "Yoruba",
    "Igbo",
    "Hausa",
    "Civic Education",
    "Computer Studies",
]

# Grading boundaries: (min_score, grade, remark)
GRADE_SCALE = [
    (75, "A1", "Excellent"),
    (70, "B2", "Very Good"),
    (65, "B3", "Good"),
    (60, "C4", "Credit"),
    (55, "C5", "Credit"),
    (50, "C6", "Credit"),
    (45, "D7", "Pass"),
    (40, "E8", "Pass"),
    (0,  "F9", "Fail"),
]


def get_grade(score):
    """Return (grade, remark) for a given score."""
    for min_score, grade, remark in GRADE_SCALE:
        if score >= min_score:
            return grade, remark
    return "F9", "Fail"


def get_valid_score(subject):
    """Prompt until a valid score (0-100) is entered."""
    while True:
        try:
            score = float(input(f"Enter score for {subject} (0-100): "))
            if 0 <= score <= 100:
                return score
            print("  ⚠ Score must be between 0 and 100. Try again.")
        except ValueError:
            print("  ⚠ Invalid input. Please enter a number.")


def select_subjects():
    """Let the student pick subjects from the WAEC list."""
    print("\nAvailable WAEC Subjects:")
    for i, subject in enumerate(WAEC_SUBJECTS, start=1):
        print(f"  {i:2}. {subject}")

    while True:
        try:
            count = int(input("\nHow many subjects did you sit for? "))
            if 1 <= count <= len(WAEC_SUBJECTS):
                break
            print(f"  ⚠ Enter a number between 1 and {len(WAEC_SUBJECTS)}.")
        except ValueError:
            print("  ⚠ Please enter a valid number.")

    chosen = []
    while len(chosen) < count:
        try:
            num = int(input(f"Select subject #{len(chosen) + 1} (1-{len(WAEC_SUBJECTS)}): "))
            if 1 <= num <= len(WAEC_SUBJECTS):
                subject = WAEC_SUBJECTS[num - 1]
                if subject in chosen:
                    print("  ⚠ Subject already selected.")
                else:
                    chosen.append(subject)
            else:
                print("  ⚠ Invalid subject number.")
        except ValueError:
            print("  ⚠ Please enter a valid number.")
    return chosen


def calculate_result():
    print("=" * 60)
    print("        WAEC SECONDARY SCHOOL RESULT CALCULATOR")
    print("=" * 60)

    name = input("\nEnter student's name: ").strip().title()

    subjects = select_subjects()

    results = []  # list of (subject, score, grade, remark)
    print("\n--- Enter Scores ---")
    for subject in subjects:
        score = get_valid_score(subject)
        grade, remark = get_grade(score)
        results.append((subject, score, grade, remark))

    # --- Display result table ---
    print("\n" + "=" * 60)
    print(f"RESULT SLIP — {name}")
    print("=" * 60)
    print(f"{'Subject':<30}{'Score':>7}{'Grade':>8}{'Remark':>15}")
    print("-" * 60)
    for subject, score, grade, remark in results:
        print(f"{subject:<30}{score:>7.1f}{grade:>8}{remark:>15}")
    print("-" * 60)

    # --- Summary calculations ---
    total = sum(score for _, score, _, _ in results)
    average = total / len(results)
    credits = [r for r in results if r[2] in ("A1", "B2", "B3", "C4", "C5", "C6")]
    passes = [r for r in results if r[2] in ("D7", "E8")]
    fails = [r for r in results if r[2] == "F9"]

    print(f"\nTotal Subjects : {len(results)}")
    print(f"Total Score    : {total:.1f}")
    print(f"Average Score  : {average:.2f}")
    print(f"Credits (A1-C6): {len(credits)}")
    print(f"Passes (D7-E8) : {len(passes)}")
    print(f"Fails  (F9)    : {len(fails)}")

    # --- Overall verdict ---
    print("-" * 60)
    if len(credits) >= 5 and any(r[0] == "English Language" and r[2] in
                                 ("A1","B2","B3","C4","C5","C6") for r in results) \
       and any(r[0] == "Mathematics" and r[2] in
               ("A1","B2","B3","C4","C5","C6") for r in results):
        print("✅ VERDICT: PASS — 5+ credits including English & Mathematics.")
    elif len(credits) >= 5:
        print("⚠ VERDICT: 5+ credits, but check English/Mathematics requirement.")
    else:
        print("❌ VERDICT: INCOMPLETE — fewer than 5 credits.")
    print("=" * 60)


if __name__ == "__main__":
    calculate_result()