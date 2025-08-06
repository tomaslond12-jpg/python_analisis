import pandas

class Calculations:
    def __init__(self):
        self._file_path : str = "data_science_bussines/data/data.csv" 
    
    def load_data(self):        
        df = pandas.read_csv(self._file_path)
        return df


    def get_public_orgs(self):
        df = self.load_data()
        public_df = df[df["Public?"] == 1]
        num = len(public_df)
        print("There are ", num, "public organizations.")
        return num


    def revenue_per_industry(self):
        df = self.load_data()
        revenue_by_industry = df.groupby("Industry")["Revenue"].sum()
        count_by_industry = df["Industry"].value_counts()

        rev_ratio = revenue_by_industry / count_by_industry

        return rev_ratio

    def highest_revenue_industry(self):
        df = self.load_data()
        revenue_by_industry = df.groupby("Industry")["Revenue"].sum()
        top_revenue_industry = revenue_by_industry.idxmax()

        return top_revenue_industry


