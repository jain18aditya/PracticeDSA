"""**Problem Statement: Tournament Scheduling with Constraints**

You are given 10 players participating in a tournament. The tournament follows a round-robin format, meaning each player must play against every other player exactly once.

Your task is to generate a schedule of matches such that:

1. Every pair of players plays exactly one match.
2. Only one match is played per day.
3. No player is allowed to play on two consecutive days.

**Input:**

* A list of 10 players (e.g., Player 1 to Player 10)

**Output:**

* A sequence of matches (e.g., Player A vs Player B), representing the daily schedule

**Constraints:**

* Each player must play exactly 9 matches (against all other players).
* No player should be scheduled for matches on consecutive days.
* Only one match can be scheduled per day.

**Goal:**

* Generate a valid schedule that satisfies all the above constraints, or determine that no such schedule is possible.
"""

from itertools import combinations

def schedule_tournament(players):
    """
    Schedules matches for a round-robin tournament with constraints:
    1. Each pair plays exactly once
    2. Only one match per day
    3. No player plays on consecutive days

    Returns:
        List of (day, player1, player2) if possible
        None if no valid schedule exists
    """

    # Step 1: Generate all possible matches (round-robin)
    matches = list(combinations(players, 2))

    # List to store final schedule
    schedule = []

    # Dictionary to track the last day each player played
    # Initialize with -2 so all players are available on day 0
    last_played_day = {player: -2 for player in players}

    day = 0  # Start scheduling from day 0

    # Step 2: Try to schedule all matches
    while matches:
        match_scheduled = False

        # Try each remaining match
        for i, (p1, p2) in enumerate(matches):

            # Check if both players did NOT play on previous day
            if last_played_day[p1] != day - 1 and last_played_day[p2] != day - 1:

                # Schedule this match
                schedule.append((day + 1, p1, p2))  # day +1 for human-readable

                # Update last played day for both players
                last_played_day[p1] = day
                last_played_day[p2] = day

                # Remove this match from remaining matches
                matches.pop(i)

                match_scheduled = True
                break

        # If no match could be scheduled → constraints cannot be satisfied
        if not match_scheduled:
            print("No valid schedule possible under given constraints.")

        day += 1  # Move to next day

    return schedule


# -------------------------
# Driver Code
# -------------------------

players = [f"Player {i}" for i in range(1, 4)]

result = schedule_tournament(players)

if result:
    print("Tournament Schedule:\n")
    for day, p1, p2 in result:
        print(f"Day {day}: {p1} vs {p2}")
else:
    print("No valid schedule possible under given constraints.")