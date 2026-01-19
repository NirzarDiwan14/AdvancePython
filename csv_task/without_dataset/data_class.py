import random 
import time 
from datetime import datetime,timedelta
import constants
import concurrent.futures
class Data:
    """
    Generates synthetic user data for testing / CSV export.
    Fields:
    - user_id
    - name
    - age
    - email (valid / invalid / None)
    - city
    - signup_date
    - monthly_income
    """
    def __init__(self,number : int,null_probability : float = 0.2,invalid_probability : float = 0.15,seed: int | None = None):
        if number <= 0:
            raise ValueError("number must be > 0")

        if not (0 <= null_probability <= 1):
            raise ValueError("null_probability must be between 0 and 1")

        if not (0 <= invalid_probability <= 1):
            raise ValueError("invalid_probability must be between 0 and 1")
        
        self.number = number
        self.null_probability = null_probability
        self.invalid_probability = invalid_probability

        if seed is not None: 
            random.seed(seed)
        self.data: list[list] = []

        print("data object created.")

    # ============================
    # Public API
    # ============================
    def get_data(self):
        """Generate full dataset and return it with header."""
        print("Getting data, may take some time...")
        
        start = time.time()

        ids = self.generate_id()
        names = self.generate_names()
        ages = self.generate_age()
        emails = self.generate_email(names)
        cities = self.generate_cities()
        dates = self.generate_dates()
        incomes =self.generate_monthly_income()

        end = time.time()
        print(f"Data prepared in {round((end- start),2)} seconds!")

        # Arrange row-wise
        rows = list(zip(
            ids,names,ages,emails,cities,dates,incomes
        ))
        #converting tuple to list for cleanliness
        rows = [list(row) for row in rows]
        #adding header 
        header = ["user_id", "name", "age", "email", "city", "signup_date", "monthly_income"]
        self.data = [header] + rows
        return self.data
    
    #efficient
    def get_data_multiprocessing(self):
        """Generate full dataset and return it with header."""
        print("Getting data with multiprocessing, may take some time...")
        
        start = time.time()

        with concurrent.futures.ProcessPoolExecutor() as executor: 
            # Submit all independent tasks
            future_ids     = executor.submit(self.generate_id)
            future_names   = executor.submit(self.generate_names)
            future_ages    = executor.submit(self.generate_age)
            future_cities  = executor.submit(self.generate_cities)
            future_dates   = executor.submit(self.generate_dates)
            future_incomes = executor.submit(self.generate_monthly_income)

            # Wait for results that don't depend on others
            ids     = future_ids.result()
            names   = future_names.result()
            ages    = future_ages.result()
            cities  = future_cities.result()
            dates   = future_dates.result()
            incomes = future_incomes.result()

            future_emails = executor.submit(self.generate_email,names)
            emails = future_emails.result()

        end = time.time()
        print(f"Data prepared in {round((end- start),2)} seconds!")

        # Arrange row-wise
        rows = list(zip(
            ids,names,ages,emails,cities,dates,incomes
        ))
        #converting tuple to list for cleanliness
        rows = [list(row) for row in rows]
        #adding header 
        header = ["user_id", "name", "age", "email", "city", "signup_date", "monthly_income"]
        self.data = [header] + rows
        return self.data
    
    
    def print_data(self) -> None:
        for row in self.data:
            print(row)
    
    # ============================
    # Generators
    # ============================

    def generate_id(self) -> list[int]:
        return list(range(1,self.number + 1))
    
    def generate_names(self) -> list[str | None]:
        names = []
        for _ in range(self.number):
            if random.random() < self.null_probability:
                names.append(None)
            else: 
                first = random.choice(constants.FIRST_NAMES)
                last = random.choice(constants.LAST_NAMES)
                names.append(f"{first} {last}")
        return names
    
    def generate_age(self):
        return [random.randint(1,200) for _ in range(self.number)]
        
    def generate_email(self, names: list[str | None]) -> list[str | None]:
        INVALID_PATTERNS = [
            lambda u, d: f"{u}{d}",                   # missing @
            lambda u, d: f"{u}@{d.replace('.', '')}", # missing dot
            lambda u, d: f"{u}@@{d}",                  # double @
            lambda u, d: f"{u} @ {d}",                 # spaces
            lambda u, d: f"{u}@{d.split('.')[0]}",    # no TLD
            lambda u, d: f"@{d}",                      # missing username
            lambda u, d: f"{u}@",                      # missing domain
            ]
        emails = []

        for name in names: 
            r = random.random()

            # Null email
            if name is None or r < self.null_probability:
                emails.append(None)
                continue
                
            # Base username
            first,last = name.lower().split()
            separator = random.choice([".","_",""])
            number = str(random.randint(1,500) if random.random() < 0.3 else "")
            username = f"{first}{separator}{last}{number}"
            domain = random.choice(constants.DOMAINS)

            # Invalid email
            if r < self.null_probability + self.invalid_probability:
                invalid_email = random.choice(INVALID_PATTERNS)(username,domain)
                emails.append(invalid_email)
            else:
                valid_email = f"{username}@{domain}"
                emails.append(valid_email)
        return emails


    def generate_cities(self) -> list[str]:
        return [random.choice(constants.INDIAN_CITIES) for _ in range(self.number)]
    
    def generate_dates(self,start: str = "2023-01-01",end: str = "2026-01-15") -> list[str]:
        start_date = datetime.strptime(start,"%Y-%m-%d")
        end_date = datetime.strptime(end,"%Y-%m-%d")

        delta = end_date - start_date
        dates = []
        for _ in range(self.number):
            random_days = random.randint(0,delta.days)
            random_date = start_date + timedelta(days=random_days)
            dates.append(random_date.strftime("%Y-%m-%d"))

        random.shuffle(dates)
        return dates
    
    def generate_monthly_income(self) -> list[int | None]:
        incomes = []
        for _ in range(self.number):
            if random.random() < self.null_probability:
                incomes.append(None)
                continue

            r = random.random()

            if r < 0.4:
                income = random.randint(8,20) * 1000
            elif r < 0.8:
                income = random.randint(20,60) * 1000
            else:
                income = random.randint(60,200) * 1000
            incomes.append(income)

        return incomes 
    

if __name__ == "__main__":
    print("Hello from data class module...")

    # data_obj = Data(1000000)
    # start = time.time()
    # d1 = data_obj.get_data()
    # end = time.time()
 
    # print(f"Time take without multiproccessing = {round((end -start),2)}")

    # start = time.time()
    # d1 = data_obj.get_data_multiprocessing()
    # end = time.time()
 
    # print(f"Time take with multiproccessing = {round((end -start),2)}")


