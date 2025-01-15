from datetime import datetime

def main():

    birthdate = input("Enter your Birthdate Y-m-d: ")


    def compute_age(birthdate):
        birth = datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.now()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

main()
