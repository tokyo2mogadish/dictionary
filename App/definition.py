import pandas

class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv('data.csv')
        #print(df)
        return tuple(df.loc[df['word'] == self.term]['definition'])

defintion = Definition ('acid')
print(defintion.get())