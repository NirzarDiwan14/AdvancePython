import csv

OUTPUT_ROWS = 10000
OUTPUT_FILE = "users_raw.csv"

header = [
    "user_id",
    "name",
    "age",
    "email",
    "city",
    "signup_date",
    "monthly_income",
]

with open("social_media.csv", "r") as social_media_file, \
     open("HREmails.csv", "r", encoding="utf-8-sig") as email_file, \
     open("foods.csv", "r") as foods_file, \
     open(OUTPUT_FILE, "w", newline="") as output_file:

    social_media_reader = csv.DictReader(social_media_file)
    hr_email_reader     = csv.DictReader(email_file)
    foods_reader        = csv.DictReader(foods_file)

    writer = csv.writer(output_file)
    writer.writerow(header)  # write header

    count = 0
    for line1, line2, line3 in zip(social_media_reader, hr_email_reader, foods_reader):
        if count == OUTPUT_ROWS:
            break

        row = [
            line1["UserID"],            # user_id
            line1["Name"],              # name
            line3["Age"],               # age
            line2["Email"],             # email  (BOM fixed via utf-8-sig)
            line1["City"],              # city
            line1["DOB"],               # signup_date
            line3["Monthly Income"],    # monthly_income
        ]

        writer.writerow(row)
        count += 1

print(f"✅ {count} rows written to {OUTPUT_FILE}")
