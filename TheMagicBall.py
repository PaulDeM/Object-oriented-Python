class MagicBall:
    predictions = ["Love", "Money", "Happiness", "Health", "New job", "A lot of money", "Journey", "Information", "Nothing :)", "Big chance", "Pass examination", "Party"]
    nr = 0

    def __init__(self):
        print("Hello stranger ... I'm the Magic Ball. ")
        self.take_year()
        self.show_prediction()

    def take_year(self):
        self.nr = int(input("Give me your birth month "))-1

    def show_prediction(self):
        print("I see...", self.predictions[self.nr])
