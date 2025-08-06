
from data_science_bussines.calculations import Calculations
def main():
    calculations = Calculations()
    
    num_public_orgs = calculations.get_public_orgs()
    rev_per_industry = calculations.revenue_per_industry()
    highest_rev_industry = calculations.highest_revenue_industry()

    print("Number of public organizations:", num_public_orgs)
    print("Revenue per industry:")
    print(rev_per_industry)
    print("Industry with the highest revenue:", highest_rev_industry)
    
    

    # Siempre que quiero utilizar una clase, debeo hacer una instancia para operar el objeto  'calculations = Calculations()'

if __name__ == "__main__":
    main()d