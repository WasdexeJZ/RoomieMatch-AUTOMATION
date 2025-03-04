import csv
from enum import IntEnum


class Smoke(IntEnum):
    YES = 0
    NO = 1


class RoommateSmoke(IntEnum):
    YES = 0
    NO = 1
    ONLY_OUTSIDE = 2


def get_smoke_score(curr_smoke, compare_smoke, curr_rm_smoke, compare_rm_smoke):
    matchValue: int = 3

    # If RoommateSmoke.YES, bypass smoke check

    # If RoommateSmoke.NO, smoke check
    if curr_rm_smoke == RoommateSmoke.NO.value:
        if compare_smoke == Smoke.YES.value:
            return 0

    if compare_rm_smoke == RoommateSmoke.NO.value:
        if curr_smoke == Smoke.YES.value:
            return 0

    # If RoommateSmoke.ONLY_OUTSIDE, smoke check penalty
    if curr_rm_smoke == RoommateSmoke.ONLY_OUTSIDE.value:
        if compare_smoke == Smoke.YES.value:
            matchValue -= 1

    if compare_rm_smoke == RoommateSmoke.ONLY_OUTSIDE.value:
        if curr_smoke == Smoke.YES.value:
            matchValue -= 1

    return matchValue


def get_guests_score(curr_feel, compare_feel, curr_over, compare_over):
    # If Guests Feeling larger then Guests Over, return incompatible
    # The larger, the less often for Guests Over
    # If Less Often Feeling, but Often Guests Over, return incompatible
    if curr_feel > compare_over:
        return 0

    if compare_feel > curr_over:
        return 0

    return 3


def get_personality_score(curr_personality, compare_personality):
    # If total match, return max score
    if curr_personality == compare_personality:
        return 3

    # If compatible, diff by 1, return slightly lower score
    if abs(curr_personality - compare_personality) == 1:
        return 2

    # Else return incompatible
    return 0


# Returns positive, need to change to negative value for penalisation
def get_cleaning_score(curr_clean, compare_clean, curr_contri, compare_contri):
    # Returns score of diff in Cleanliness acceptence, mutliplied by max Contribute
    # Penalize more if Cleanliness acceptence diff, if same, no penalization even if dont Contribute
    return abs(curr_clean - compare_clean) * (
        max(
            curr_contri,
            compare_contri,
        )
        + 1
    )


def get_sociality_score(curr_soc, compare_soc):
    # Similar to Personality
    # If total match, return max score
    if curr_soc == compare_soc:
        return 3

    # If compatible, diff by 1, return slightly lower score
    if abs(curr_soc - compare_soc) == 1:
        return 2

    # Else return incompatible
    return 0


def get_loudness_score(curr_noise, compare_noise, curr_tv, compare_tv):
    # If both can / cannot handle Noise, max score
    if curr_noise == compare_noise:
        if curr_tv == compare_tv:
            return 3

    # Else return incompatible
    return 0


# Define input and output file paths
input_file = "C:\\Users\\wasde\\Downloads\\asdf.csv"
output_file = "C:\\Users\\wasde\\Downloads\\output.csv"

fieldnames = [
    "smoke_score",
    "guests_score",
    "cleaning_score",
    "personality_score",
    "sociality_score",
    "loudness_score",
]


# Open the input file for reading and the output file for writing
with open(input_file, mode="r", newline="") as infile, open(
    output_file, mode="w", newline=""
) as outfile:
    # Create CSV reader and writer objects
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    # Write the header to the output file
    writer.writeheader()

    # curr_user = None
    # counter = 0
    # # Process each row in the input file
    # for row in reader:
    #     if counter % 23 == 0:
    #         curr_user = row[:]
    #         print("______________")
    #         print("______________")
    #         print(row)
    #         print("______________")
    #     else:
    #         print(row)

    #     counter += 1
    curr_user = []
    counter = 0
    # Process each row in the input file
    for row in reader:
        if counter % 23 == 0:
            curr_user = row

        else:
            smoke_score: int = get_smoke_score(
                int(curr_user["smoke"]),
                int(row["smoke"]),
                int(curr_user["roommate_smoke"]),
                int(row["roommate_smoke"]),
            )
            guests_score: int = get_guests_score(
                int(curr_user["guests_feeling"]),
                int(row["guests_feeling"]),
                int(curr_user["guests_over"]),
                int(row["guests_over"]),
            )
            personality_score: int = get_personality_score(
                int(curr_user["personality"]), int(row["personality"])
            )
            cleaning_score: int = get_cleaning_score(
                int(curr_user["cleanliness"]),
                int(row["cleanliness"]),
                int(curr_user["contribute"]),
                int(row["contribute"]),
            )
            sociality_score: int = get_sociality_score(
                int(curr_user["sociality"]), int(row["sociality"])
            )
            loudness_score: int = get_loudness_score(
                int(curr_user["loud_noise"]),
                int(row["loud_noise"]),
                int(curr_user["loud_tv"]),
                int(row["loud_tv"]),
            )

            print(
                smoke_score,
                guests_score,
                personality_score,
                cleaning_score,
                sociality_score,
                loudness_score,
            )
            output = {
                "smoke_score": smoke_score,
                "guests_score": guests_score,
                "cleaning_score": cleaning_score,
                "personality_score": personality_score,
                "sociality_score": sociality_score,
                "loudness_score": loudness_score,
            }
            writer.writerow(output)
        counter += 1

    #     # Write the updated row to the output file


print(f"Processing complete. Results written to {output_file}")
